#创建一个字符串变量，保存一段招标文本。
#把文本写入 sample_tender.txt。
#再从 sample_tender.txt 读取内容。
#输出读取到的内容和字符数量。
#全部使用 with open(...)。

with open("tenderguard\learning\day03\sample_tender.txt","w",encoding="utf-8") as fw:
    fw.write("某单位现对办公设备采购项目进行公开招标。\n投标截止时间为2026年7月30日。\n符合条件的供应商均可参加投标")
    fw.flush()
    print("成功写入文件")
with open("tenderguard\learning\day03\sample_tender.txt","r",encoding="utf-8") as fr:
    content = fr.read().strip()
#读取内容
print(f"读取到的内容为：\n{content}")
#读取字符数量
print("字符数量为:",len(content))

#修改 file_practice.py：
#文件存在时正常读取。
#文件不存在时，捕获 FileNotFoundError。
#显示友好提示，不要让程序直接出现一整屏红色报错。

try:
    f = open("missing.txt","r",encoding="utf-8") 
except FileNotFoundError as e: #捕获到FileNotFoundError这个异常时输出内容
    print("读取失败：没有找到 missing.txt,异常为：",e)
else:#没有捕获到异常时输出内容
    print("读取成功！")
finally:#不管有没有异常都要执行
    print("不管有没有异常都要执行")
