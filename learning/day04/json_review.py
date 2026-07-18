'''
load_rules() 使用 json.load()。
捕获 FileNotFoundError 和 json.JSONDecodeError。
加载失败返回空列表。
save_report() 使用 json.dump()。
必须设置 ensure_ascii=False 和 indent=2。
保存后重新读取报告并打印。
'''
import json
def load_rules(file_path):  
    try:
        with open(file_path,'r',encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError) as e:
        return []

def save_report(file_path, report):
    with open(file_path,'w',encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    with open(file_path,'r',encoding='utf-8') as f:
        saved_report = json.load(f)
        print(saved_report)