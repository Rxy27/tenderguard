'''
使用 with open()。
编码使用 UTF-8。
保存成功后返回 True。
读取成功后返回文本。
文件不存在时捕获 FileNotFoundError,返回空字符串。
分别测试存在和不存在的文件。
'''

def save_tender_text(file_path, content):
    with open(file_path,'w',encoding='utf-8') as f:
        try:
            f.write(content)
            return True
        except Exception as e:
            return False

def read_tender_text(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError as e:
        return ""
