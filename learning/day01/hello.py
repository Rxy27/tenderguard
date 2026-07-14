#询问姓名
name = input("what is your name?\n").strip().title() 
#.strip()表示删除多余的空格 .title()表示将每个单词的首字母转换为大写，其余所有字母转换为小写
                                             
#询问专业                                            
profession = input("what is your profession?\n").strip()
#格式化输出
print(f"hello,{name}! Your profession is {profession}! ")
