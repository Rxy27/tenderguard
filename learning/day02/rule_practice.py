#用字典表示一条风险规则。
#字典包含 keyword、level、reason。
#将至少三条规则放进列表。
#使用 for 循环逐条输出。
#关键词使用“最低价中标”“无限责任”“不接受联合体”。

#以字典形式定义第一条规则
risk_rule1 = {
    "keyword":"最低价中标",
    "level":1,
    "reason":"可能导致供应商过度压价，影响项目质量"
}
#以字典形式定义第二条规则
risk_rule2 = {
    "keyword":"无限责任",
    "level":2,
    "reason":"责任范围没有上限，可能带来较大的赔偿风险"
}
#以字典形式定义第三条规则
risk_rule3 = {
    "keyword":"不接受联合体",
    "level":3,
    "reason":"限制联合投标，可能降低参与项目的灵活性"
}
#将三条规则放入列表
risk_list=[risk_rule1,risk_rule2,risk_rule3]
#for循环逐条输出
for risk_rule in risk_list:
    print(risk_rule,type(risk_rule))
