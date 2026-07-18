'''
读取 sample_tender.txt。
加载 rules.json。
遍历风险规则。
检测关键词并保存命中详情。
累加风险分数。
调用函数确定风险等级。
在终端打印结果。
生成 risk_report.json。

至少拆成以下函数：
load_text()
load_rules()
check_risks()
get_risk_level()
save_report()
main()
'''
import json
#读取 sample_tender.txt。
def load_text(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        return f.read().strip()
#加载 rules.json。
def load_rules(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        return json.load(f)
#遍历风险规则。检测关键词并保存命中详情。
def check_risks(text,rules):
    matched_rules = []
    total_score = 0 
    for rule in rules:
        if rule["keyword"] in text:
            matched_rules.append()
            total_score += rule["score"]
    return matched_rules,total_score
#调用函数确定风险等级。
def get_risk_level(score):
    if score < 30:
        return "低风险"
    elif score < 60:
        return "中风险"
    else:
        return "高风险"

#在终端打印结果。生成 risk_report.json。
def save_report(report,file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

def main():
    text = load_text("sample_tender.txt")
    rules = load_rules("rules.json")

    matched_rules, total_score = check_risks(text, rules)
    risk_level = get_risk_level(total_score)

    report = {
        "matched_rules": matched_rules,
        "total_score": total_score,
        "risk_level": risk_level
    }

    print("风险检测结果：")
    print("命中规则：", matched_rules)
    print("风险总分：", total_score)
    print("风险等级：", risk_level)

    save_report(report, "risk_report.json")

if __name__ == "__main__":
    main()






