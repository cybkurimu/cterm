import requests
from bs4 import BeautifulSoup

# Get all the child pages within the portswigger document

proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}

# 发送 HTTP 请求并获取页面内容
url = "https://portswigger.net/burp/documentation/contents"
response = requests.get(url, proxies=proxies)
html_content = response.text

# 解析 HTML 内容并查找目标元素
soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table", class_="is-nonresponsive-table")
links = table.find_all("a")

# 提取链接地址并保存到文件
with open("links.txt", "w") as file:
    for link in links:
        href = link.get("href")
        file.write("https://portswigger.net" + href + "\n")
