import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 设置请求头和代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}

# 发送请求
# url = 'https://portswigger.net/burp/documentation/contents'

def craw(url):
    response = requests.get(url, headers=headers, proxies=proxies)

    # 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取英文单词
    words = []
    for string in soup.stripped_strings:
        for word in string.split():
            if word.isalpha():
                words.append(word.lower())

    # 保存结果
    now = datetime.now()
    filename = f"output/{now.strftime('craw_%Y%m%d%H%M%S')}.txt"
    with open(filename, 'w') as f:
        for word in words:
            f.write(word + '\n')