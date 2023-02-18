import os

def merged():
    # 遍历 output 目录下的所有 craw_*.txt 文件路径
    dir_path = 'output'
    file_paths = [os.path.join(dir_path, file) for file in os.listdir(dir_path) if file.startswith('craw_') and file.endswith('.txt')]

    # 合并所有文件的内容
    content = ''
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            content += f.read()

    # 将合并后的内容写入新文件
    output_file = 'merged.txt'
    with open(output_file, 'w') as f:
        f.write(content)
