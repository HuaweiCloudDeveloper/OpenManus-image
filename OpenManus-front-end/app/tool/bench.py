import aiohttp
import asyncio
import time
from tqdm import tqdm
import random
import argparse
                                                                                                                                                       
                                                                                                                                                       
questions = [
    "Why is the sky blue?", "Why do we dream?", "Why is the ocean salty?", "Why do leaves change color?",
    "Why do birds sing?", "Why do we have seasons?", "Why do stars twinkle?", "Why do we yawn?",
    "Why is the sun hot?", "Why do cats purr?", "Why do dogs bark?", "Why do fish swim?",
"中国传统文化有哪些独特魅力？",
"如何提高中文写作能力？",
"现代科技对生活影响有多大？",
"历史上的英雄人物如何定义？",
"中国美食的地域特色是什么？",
"怎样学习古诗词更有效？",
"社交网络改变了人际交往吗？",
"汉字的演变历程是怎样的？",
"传统文化如何传承创新？",
"人工智能的发展趋势是什么？",
"中国民俗文化包含哪些内容？",
"阅读经典文学有什么好处？",
"城市发展带来哪些环境问题？",
"如何培养良好的阅读习惯？",
"中国古代建筑有何艺术价值？",
"怎样保持积极乐观的心态？",
"家庭教育对孩子有多重要？",
"中国戏曲的特色与魅力在哪？",
"运动对健康的重要性有哪些？",
"如何提升自己的审美水平？",
"网络文学发展现状如何？",
"中国哲学思想的核心是什么？",
"语言学习的关键要素是什么？",
"怎样才能更好地保护环境？",
"中国书法艺术的精髓是什么？",
"旅游对文化交流的作用？",
"如何克服拖延的毛病？",
"中国民间艺术有哪些种类？",
"科技创新如何改善教育？",
"怎样理解现代艺术？",
"中国历史上的盛世有哪些？",
"如何做好时间管理？",
"中国茶文化的内涵是什么？",
"情绪管理的有效方法？",
"互联网对商业的变革影响？",
"如何传承家族文化？",
"中国绘画的风格特点？",
"健康饮食的基本原则？",
"如何在工作中提升效率？",
"中国传统节日的意义？",
"怎样提高自己的逻辑思维？",
"新媒体对舆论的影响？",
"中国武术的文化底蕴？",
"如何选择适合自己的书籍？",
"城市规划与文化保护？",
"怎样进行有效的沟通？",
"中国古代文学的辉煌之处？",
"如何平衡工作与生活？",
"传统文化元素在现代设计？",
"学习新知识的最佳途径？"
]                                                                                                                                                      
                                                                                                                                                       
                                                                                                                                                       
async def fetch(session, url, model_path):
    start_time = time.time()
                                                                                                                                                       
    # 随机选择一个问题
    question = random.choice(questions)
    # 固定问题
    # question = questions
                                                                                                                                                       
    json_payload = {
        "model": model_path,
        "messages": [{"role": "user", "content": question}],
        "stream": False,
   "max_tokens": 200,
        "temperature": 0.7
    }
    async with session.post(url, json=json_payload) as response:
        response_json = await response.json()
        end_time = time.time()
        request_time = end_time - start_time
        completion_tokens = response_json['usage']['completion_tokens']
        return completion_tokens, request_time
                                                                                                                                                       
                                                                                                                                                       
async def bound_fetch(sem, session, url, pbar, model_path):
    async with sem:
        result = await fetch(session, url, model_path)
        pbar.update(1)
        return result
                                                                                                                                                       
                                                                                                                                                       
async def run(load_url, max_concurrent_requests, total_requests, model_path):
    sem = asyncio.Semaphore(max_concurrent_requests)
    async with aiohttp.ClientSession() as session:
        tasks = []
        with tqdm(total=total_requests) as pbar:
            for _ in range(total_requests):
                task = asyncio.ensure_future(bound_fetch(sem, session, load_url, pbar, model_path))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
        completion_tokens = sum(result[0] for result in results)  # Extract completion_tokens from each tuple
        response_times = [result[1] for result in results]
        return completion_tokens, response_times
                                                                                                                                                       
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Benchmark script')
    parser.add_argument('--model_path', type=str, required=True, help='Path to the model')
    parser.add_argument('C', type=int, help='Max concurrent requests')
    parser.add_argument('N', type=int, help='Total requests')
    args = parser.parse_args()
                                                                                                                                                       
    url = 'http://localhost:11561/v1/chat/completions'
                                                                                                                                                       
    start_time = time.time()
    completion_tokens, response_times = asyncio.run(run(url, args.C, args.N, args.model_path))
    end_time = time.time()
                                                                                                                                                       
    total_time = end_time - start_time
    avg_time_per_request = sum(response_times) / len(response_times)
    tokens_per_second = completion_tokens / total_time
                                                                                                                                                       
    print(f'Performance Results:')
    print(f'  Total requests            : {args.N}')
    print(f'  Max concurrent requests   : {args.C}')
    print(f'  Total time                : {total_time:.2f} seconds')
    print(f'  Average time per request  : {avg_time_per_request:.2f} seconds')
    print(f'  Tokens per second         : {tokens_per_second:.2f}')
