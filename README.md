# cterm

```

# 1. Use url to get words
# urlcraw("https://www.baidu.com")
# filecraw("links.txt")

# 2. Merge all txt in the "output" directory
# merged()

# 3. Count the number of words
# count('merged.txt')

```

`urlcraw` 获取指定链接内所有单词

`filecraw` 获取 links.txt 文件内所有链接内的单词

`merged` 合并 output 中所有结果, 并保存至 merged.txt

`count` 统计单词出现数量, 从大到小排序, 输出 {单词}-{数量}

vim 正则删除 -{数量} `:%s/-.*//`