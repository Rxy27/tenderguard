#接收项目预算和费率，返回服务费。
def calculate_service_fee(x,y):
    price = x * y
    print("----------------")
    print("预算:",x)
    print("费率:",y)
    print(f"服务费为:{price}元")

budget = float(input("请输入项目预算:").strip())
rate = float(input("请输入费率:").strip())
calculate_service_fee(budget,rate)
print("----------------")
'''
0~29:低风险
30~59:中风险
60~100:高风险
其他：无效分数
'''
def get_risk_level(x):
    if x>=0 and x<=29:
        print("低风险")
    elif x>=30 and x<=59:
        print("中风险")
    elif x>=60 and x<=100:
        print("高风险")
    else:
        print("无效分数")

score = int(input("请输入分数:").strip())
get_risk_level(score)
print("----------------")