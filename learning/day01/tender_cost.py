#输入项目名称
project_name = input("请输入项目名称：").strip().title()
#输入文档页数
pages = int(input("请输入文档总页数：").strip())
#输入每页分析价格
price_per_page = float(input("请输入每页分析的价格：").strip())
#编写 calculate_cost(pages, price_per_page) 函数
#如果文档页数超过100页就打九折
def calculate_cost(x,y):
    if(x>100):
        return x*y*0.9
    else:
        return x*y
#函数返回总价格
sum_price = calculate_cost(pages, price_per_page)
#输出项目名称、文档页数和预计费用
print("\n")
print(f"项目名称：{project_name}\n文档页数:{pages}\n预计分析费用:{sum_price}")