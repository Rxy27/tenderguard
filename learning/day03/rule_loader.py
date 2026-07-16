#使用 json.load()。
#文件不存在时捕获 FileNotFoundError。
#JSON 格式错误时捕获 json.JSONDecodeError。
#成功后返回规则列表。
#失败时返回空列表 []。

import json

def load_rules(file_path):
        return_list = []
        try:
            #打开的是file_path这个变量，不是具体的某个文件
            with open(file_path,"r",encoding ="utf-8") as f:
                rules = json.load(f)
        except FileNotFoundError as e:
            print("文件不存在，异常为:",e)
            print(return_list)
        except json.JSONDecodeError as e2:
            print("JSON 格式错误,异常为:",e2)
            print(return_list)
        else:
            print(rules)  

load_rules("E:\VScode_Project\\tenderguard\learning\day03\\rules.json")
