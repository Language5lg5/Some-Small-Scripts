import os

def remove_hex_prefix_in_place(file_path):
    with open(file_path, 'r+b') as file:
        # 移动文件指针到文件开头
        file.seek(1)

        # 读取剩余内容
        content = file.read()

        # 将文件指针移动到文件开头
        file.seek(0)

        # 写入修改后的内容
        file.write(content)

        # 截断文件，以确保删除剩余的内容
        file.truncate()
current = os.path.dirname(__file__)

files = os.listdir(current)

for file in files :
    if os.path.abspath(file) == __file__:
        continue

    if os.path.isfile(file):
        remove_hex_prefix_in_place(file)