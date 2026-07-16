'''
从 sample_tender.txt 读取招标文本。
从 rules.json 加载风险规则。
遍历规则，判断关键词是否出现在文本中。
记录所有命中的规则。
累加风险分数。
根据总分计算风险等级。
在终端输出检测结果。
把结果保存到 risk_report.json。

0~29:低风险
30~59:中风险
60 分及以上：高风险

生成的报告结构建议：
{
  "total_score": 80,
  "risk_level": "高风险",
  "hit_count": 2,
  "hits": [
    {
      "keyword": "最低价中标",
      "score": 30,
      "reason": "可能存在过度价格竞争风险"
    }
  ]
}

必须完成的三个测试:
测试一：没有关键词。
本项目采用综合评分方式确定中标单位。
预期：低风险，命中 0 条。
测试二：命中一条。
本项目采用最低价中标方式。
预期：中风险，命中 1 条。
测试三：命中多条。
本项目采用最低价中标，投标方承担无限责任。
预期：高风险，命中 2 条。
每次测试后都打开 risk_report.json,确认结果随程序运行而更新。
'''
'''
初始错误代码:
import json
fr = open("E:\VScode_Project\\tenderguard\learning\day03\sample_tender.txt","r",encoding = "utf-8")
rules = json.load("E:\VScode_Project\\tenderguard\learning\day03\\rules.json")
matched_rules = []
for rule in rules:
    if rule["keyword"] in fr:
        matched_rules.append(rule)
sum =0
for score in matched_rules:
    sum +=score["score"]

def score_check(x):
    if x>=0 and x<=29:
        print("低风险")
    elif x>=30 and x<=59:
        print("中风险")
    else:
        print("中风险")

score_check(sum)
print(f"命中{len(matched_rules)}条风险：")
fw = open("E:\VScode_Project\\tenderguard\learning\day03\\risk_report.json","w",encoding = "utf-8")
fw.write(score_check(sum),print(f"命中{len(matched_rules)}条风险："))
json.dump(
    fw,
    ensure_ascii=False,
    indent=2
)
fr.close()
fw.close()
'''

import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent

with (base_dir / "sample_tender.txt").open(
    "r", encoding="utf-8"
) as file:
    tender_text = file.read()

with (base_dir / "rules.json").open(
    "r", encoding="utf-8"
) as file:
    rules = json.load(file)

matched_rules = []

for rule in rules:
    if rule["keyword"] in tender_text:
        matched_rules.append(rule)

total_score = sum(rule["score"] for rule in matched_rules)


def get_risk_level(score):
    if score < 30:
        return "低风险"
    elif score < 60:
        return "中风险"
    else:
        return "高风险"


risk_level = get_risk_level(total_score)

report = {
    "total_score": total_score,
    "risk_level": risk_level,
    "hit_count": len(matched_rules),
    "hits": matched_rules,
}

print(f"风险等级：{risk_level}")
print(f"风险总分：{total_score}")
print(f"命中 {len(matched_rules)} 条风险：")

for rule in matched_rules:
    print(
        f"- {rule['keyword']}:"
        f"{rule['score']} 分，{rule['reason']}"
    )

with (base_dir / "risk_report.json").open(
    "w", encoding="utf-8"
) as file:
    json.dump(report, file, ensure_ascii=False, indent=2)

