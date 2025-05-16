"""
练习: 文件处理

描述：
本练习帮助您学习如何在Python中进行文件的读取和写入操作。

请补全下面的函数，实现文件的读取和写入功能。
"""

def read_file(file_path):
    try:
        with open(file_path,"r",encoding="utf-8") as f:
            content=f.read()
            return content
    except FileNotFoundError:
        print("文件未找到")
        return None

def write_file(file_path, content):
    """
    写入内容到文本文件
    
    参数:
    - file_path: 文件路径
    - content: 要写入的内容
    
    返回:
    - 是否写入成功的布尔值
    """
    # 请在下方编写代码
    # 使用with语句和open()函数写入内容到文件
    pass 
    try:
        with open(file_path,"w",encoding="utf-8") as f:
            f.write(content)                   
        return True
    except Exception as e:
        print("写入文件时发生错误:", e)
        return False


    
