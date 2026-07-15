#用户输入项目名称和招标条款。
# 定义 check_tender_risks(text, rules)。
# 循环检查条款中是否包含规则关键词。
# 使用列表保存命中的规则。
# 输出命中数量、等级和原因。
# 没有命中时输出“暂未发现已知风险”。
#测试：本项目采用最低价中标方式，供应商需要承担无限责任。输出：预期命中两条风险。
#测试：本项目采用综合评分法确定供应商。输出：预期没有命中已知风险。

#以上为要求和测试内容，以下为代码:
risk_list = [
    {
        "keyword": "最低价中标",
        "level": 1,
        "reason": "可能导致供应商过度压价，影响项目质量",
    },
    {
        "keyword": "无限责任",
        "level": 2,
        "reason": "责任范围没有上限，可能带来较大的赔偿风险",
    },
    {
        "keyword": "不接受联合体",
        "level": 3,
        "reason": "限制联合投标，可能降低参与项目的灵活性",
    },
]

#定义check_tender_risks函数
def check_tender_risks(text, rules):
    #创建一个空列表，用来保存命中的风险规则
    matched_rules = []
    #循环遍历 rules 中的每一条风险规则
    for rule in rules:
        #取出当前规则中的关键词，检查它是否包含在招标条款 text 中
        if rule["keyword"] in text:
            #如果关键词出现在招标条款中，就使用 append() 把当前整条规则添加到 matched_rules 列表中
            matched_rules.append(rule)
    #判断 matched_rules 是否为空，相当于判断len(matched_rules) == 0
    if not matched_rules:
        #如果列表为空，说明没有任何风险规则被命中
        print("暂未发现已知风险")
        #立即结束函数，不再继续执行后面的代码
        #这里使用 return 是为了避免在没有风险时，继续输出“命中0条风险”等内容
        return
    #输出命中规则的数量
    print(f"命中{len(matched_rules)}条风险：")
    #循环遍历所有已经命中的规则
    for rule in matched_rules:
        #取出当前命中规则的 keyword，输出风险关键词
        print(f"关键词：{rule['keyword']}")
        #取出当前命中规则的 level，输出风险等级
        print(f"等级：{rule['level']}")
        #取出当前命中规则的 reason，输出风险原因
        print(f"原因：{rule['reason']}")
#输入项目名称
project_name = input("请输入项目名称：").strip()
#输入招标条款
tender_text = input("请输入招标条款：").strip()
print(f"\n项目名称:{project_name}")
#调用函数
check_tender_risks(tender_text, risk_list)


