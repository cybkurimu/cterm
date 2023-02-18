from collections import Counter

def count(file):
    # 读取文本文件并统计单词数量
    with open(f'{file}', 'r') as f:
        text = f.read()
        word_count = Counter(text.split())

    # 按数量从大到小排序，并输出每个单词及其对应的数量
    for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}-{count}")
