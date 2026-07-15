#条件判断练习：
#根据输入分数输出：
#0～39：低风险
#40～69：中风险
#70～100：高风险
#其他数字：分数无效
#必须测试：-1、0、39、40、69、70、100、101

score = int(input("请输入你的分数:").strip())
if (score>=70 and score<=100):
    print("高风险")
elif(score>=40 and score<=69):
    print("中风险")
elif(score>=0 and score<=39):
    print("低风险")
else:
    print("分数无效！")