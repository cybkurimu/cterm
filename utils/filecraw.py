import requests
from bs4 import BeautifulSoup
from datetime import datetime
from queue import Queue
import threading

# 设置请求头和代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}

def craw(url_queue, html_queue):
    while True:
        # 从队列中获取 URL
        url = url_queue.get()

        # 发送请求
        response = requests.get(url, headers=headers, proxies=proxies)

        # 将 HTML 内容放入队列中
        html_queue.put(response.text)

        # 标记 URL 任务完成
        url_queue.task_done()

def parse_html(html_queue):
    while True:
        # 从队列中获取 HTML 内容
        html = html_queue.get()

        # 解析 HTML
        soup = BeautifulSoup(html, 'html.parser')

        # 提取英文单词
        words = []
        for string in soup.stripped_strings:
            for word in string.split():
                if word.isalpha():
                    words.append(word.lower())

        # 保存结果
        now = datetime.now()
        filename = f"{now.strftime('craw_%Y%m%d%H%M%S')}.txt"
        with open("output/" + filename, 'w') as f:
            for word in words:
                f.write(word + '\n')

        # 标记 HTML 任务完成
        html_queue.task_done()

def main(file):
    # 创建队列
    url_queue = Queue()
    html_queue = Queue()

    # 启动线程
    for i in range(5):
        t = threading.Thread(target=craw, args=(url_queue, html_queue), daemon=True)
        t.start()

    t = threading.Thread(target=parse_html, args=(html_queue,), daemon=True)
    t.start()

    # 添加 URL 到队列中
    with open(f'{file}', 'r') as f:
        lines = f.readlines()
        for line in lines:
            url = line.strip()
            url_queue.put(url)

    # 等待队列中的所有任务完成
    url_queue.join()
    html_queue.join()

if __name__ == '__main__':
    main()