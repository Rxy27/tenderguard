#练习要求：
#创建 project_name、budget、risk_count 三个变量。
project_name = input("请输入项目名称:").strip().title()
budget = input("请输入预算:").strip()
risk_count = input("请输入风险数量:").strip()
#分别使用字符串拼接和 f-string 输出项目摘要。
print("项目名称:"+ project_name + "\n" + "预算:" + budget + "\n" + "风险数量:" + risk_count)
print("-------------------------")
print(f"项目名称:{project_name}\n预算:{budget}\n风险数量:{risk_count}")
print("-------------------------")
#定义 format_project_summary() 函数。
def format_project_summary(x,y,z):
    return "项目名称:" + x + "\n" + "预算:" + y + "\n" + "风险数量:" + z
#让函数返回摘要字符串，再在函数外使用 print() 输出。
print(format_project_summary(project_name,budget,risk_count))
#将函数调用放在函数定义之后。
format_project_summary(project_name,budget,risk_count)
#重点观察：字符串拼接遇到数字时为什么麻烦，而 f-string 为什么更方便。

