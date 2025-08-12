OpenManus ARM架构在Ubuntu部署指南

# 一、环境准备

## 1.构建python anaconda

```markdown
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-aarch64.sh

bash Miniconda3-latest-Linux-aarch64.sh
```

## 2.创建新的虚拟环境

```markdown
# 创建虚拟环境
conda create -n open_manus python=3.12 -y

# 激活虚拟环境
conda activate open_manus
```



# 二、源码下载

```
# 进入目录
cd /opt

# 克隆远程 带有前端代码分支仓库
git clone -b front-end  https://github.com/mannaandpoem/OpenManus.git
cd OpenManus

# 下载源码上传
unzip  OpenManus-front-end

# 
cd OpenManus-front-end
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install baidusearch

```

### 浏览器自动化工具（可选）

```
playwright install
```





# 三、配置与部署

## 1. 目录中创建一个`config.toml`文件`config`

```
# 进入到项目目录
cd OpenManus-front-end

cp config/config.example.toml config/config.toml
```

## 2.编辑配置添加您的 API 密钥并自定义设置：

## 2.1 修改模型配置

```markdown
# 配置自己大模型地址 国内优选deepseek
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


# Server configuration 支持所有ip访问
[server]
host = "0.0.0.0" 
port = 5172
```

## 2.2 修改 webserach 工具

```markdown
# 在OpenManus-front-end/app/tool创建百度搜索文件
vi baidu_search.py

# 添加下边内容
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
# 注销谷歌搜索 国内无法访问谷歌
# from app.tool.google_search import GoogleSearch
from app.tool.python_execute import PythonExecute
# 导入百度搜索工具
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







# 四、服务管理

### **1. 创建 systemd 服务文件**

```
sudo vi /etc/systemd/system/openmanus.service
```

文件中写入以下内容

```markdown
# 部署的时候移除所有注释
[Unit]
Description=OpenManus Service
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/OpenManus-front-end  # 替换为你的 app.py 所在目录
ExecStart=/root/miniconda3/envs/open_manus/bin/python app.py
Restart=on-failure   # 崩溃时自动重启
RestartSec=5s        # 重启间隔
StandardOutput=file:/var/log/openmanus.log  # 日志重定向
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





### **2. **赋予权限并启用服务**

```
sudo chmod 644 /etc/systemd/system/openmanus.service  # 设置权限
sudo systemctl daemon-reload     # 重新加载 systemd
sudo systemctl enable openmanus  # 开机自启
sudo systemctl start openmanus   # 立即启动
```

### **3. 检查服务状态**

```
sudo systemctl status openmanus       # 查看运行状态
journalctl -u openmanus -f            # 查看实时日志
```



## 4.验证服务

```
# 浏览器打开-ip地址换成自己的
http://localhost:5172
```



