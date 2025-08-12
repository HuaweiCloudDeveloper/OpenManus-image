# 1、Environmental preparation

## 1.Build python anaconda

```markdown
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-aarch64.sh

bash Miniconda3-latest-Linux-aarch64.sh
```

## 2.Create a new virtual environment

```markdown
#Creating a virtual environment
conda create -n open_manus python=3.12 -y

# Activate virtual environment
conda activate open_manus
```



# 2、Source code download

```
# Enter directory
cd /opt

# Clone remote repository with front-end code branch
git clone -b front-end  https://github.com/mannaandpoem/OpenManus.git
cd OpenManus

# Download source code and upload
unzip  OpenManus-front-end

# 
cd OpenManus-front-end
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install baidusearch

```

### Browser automation tool (optional)

```
playwright install
```





# 3、Configuration and Deployment

## 1. Create a ` config. toml ` file ` config ` in the directory`

```
# Enter the project directory
cd OpenManus-front-end

cp config/config.example.toml config/config.toml
```

## 2.Edit configuration, add your API key, and customize settings:

## 2.1 Modify model configuration

```markdown
# Configure your own large model address
[llm]
model = "deepseek-chat"
base_url = "https://api.deepseek.com/v1"
api_key = "sk---"  # Replace with your actual API key
max_tokens = 8192
temperature = 0.0

# Optional configuration for specific LLM models
[llm.vision]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # Replace with your actual API key


# Server configuration Support all IP access
[server]
host = "0.0.0.0" 
port = 5172
```

## 2.2 Modify the webserach tool

```markdown
# OpenManus-front-end/app/tool Create Baidu search file
vi baidu_search.py

# Add the following content
import asyncio
from typing import List

from baidusearch.baidusearch import search 
from app.tool.base import BaseTool


class BaiduSearch(BaseTool):
    name: str = "baidu_search"
    description: str = """Perform a Baidu search and return a list of relevant links.
Use this tool when you need to find information on the web, get up-to-date data, or research specific topics.
The tool returns a list of URLs that match the search query.
"""
    parameters: dict = {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "(required) The search query to submit to Baidu.",
            },
            "num_results": {
                "type": "integer",
                "description": "(optional) The number of search results to return. Default is 10.",
                "default": 10,
            },
        },
        "required": ["query"],
    }

    async def execute(self, query: str, num_results: int = 10) -> List[str]:
        """
        Execute a Baidu search and return a list of URLs.

        Args:
            query (str): The search query to submit to Baidu.
            num_results (int, optional): The number of search results to return. Default is 10.

        Returns:
            List[str]: A list of URLs matching the search query.
        """
        # Run the search in a thread pool to prevent blocking
        loop = asyncio.get_event_loop()
        links = await loop.run_in_executor(
            None, lambda: [result['url'] for result in search(query, num_results=num_results)]
        )

        return links
```



```markdown
# 修改 OpenManus-front-end/app/agent/manus.py

from pydantic import Field
from app.agent.toolcall import ToolCallAgent
from app.prompt.manus import NEXT_STEP_PROMPT, SYSTEM_PROMPT
from app.tool import Terminate, ToolCollection
from app.tool.browser_use_tool import BrowserUseTool
from app.tool.file_saver import FileSaver
# Cancel Google search, unable to access Google in China
# from app.tool.google_search import GoogleSearch
from app.tool.python_execute import PythonExecute

# Import Baidu search tool
from app.tool.baidu_search import BaiduSearch

class Manus(ToolCallAgent):
    """
    A versatile general-purpose agent that uses planning to solve various tasks.

    This agent extends PlanningAgent with a comprehensive set of tools and capabilities,
    including Python execution, web browsing, file operations, and information retrieval
    to handle a wide range of user requests.
    """

    name: str = "Manus"
    description: str = (
        "A versatile agent that can solve various tasks using multiple tools"
    )

    system_prompt: str = SYSTEM_PROMPT
    next_step_prompt: str = NEXT_STEP_PROMPT

    max_observe: int = 2000
    max_steps: int = 20

    # Add general-purpose tools to the tool collection
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            PythonExecute(), BaiduSearch(), BrowserUseTool(), FileSaver(), Terminate()
        )
    )

```







# 4、Service Management

### **1. Create a systemd service file**

```
sudo vi /etc/systemd/system/openmanus.service
```

Write the following content in the file

```markdown
# Remove all comments during deployment

[Unit]
Description=OpenManus Service
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/OpenManus-front-end   
app.py  
ExecStart=/root/miniconda3/envs/open_manus/bin/python app.py
Restart=on-failure   
RestartSec=5s        
StandardOutput=file:/var/log/openmanus.log   
StandardError=file:/var/log/openmanus_error.log

[Install]
WantedBy=multi-user.target
```

```
[Unit]
Description=OpenManus Service
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/OpenManus-front-end
ExecStart=/root/miniconda3/envs/open_manus/bin/python app.py
Restart=on-failure
RestartSec=5s    
StandardOutput=file:/var/log/openmanus.log
StandardError=file:/var/log/openmanus_error.log

[Install]
WantedBy=multi-user.target
```





### **2. **Granting permissions and enabling services

```
sudo chmod 644 /etc/systemd/system/openmanus.service  # 设置权限
sudo systemctl daemon-reload     # reload systemd
sudo systemctl enable openmanus  # PowerBoot
sudo systemctl start openmanus   # restart now
```

### **3. Check service status**

```
sudo systemctl status openmanus       # View operational status
journalctl -u openmanus -f            # View real-time logs
```



## 4.Verification Services

```
# Open the browser and change the IP address to your own
http://localhost:5172
```



