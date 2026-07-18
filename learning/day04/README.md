1.f-string 解决了什么问题？
解决了字符串拼接麻烦的问题

2.函数相比重复写代码有什么好处？
简化了代码，一次定义函数可以多次调用函数，只需要传入对应的参数即可

3.参数和返回值分别是什么？
参数是自己定义的属性                  修改:参数不是“属性”，更准确地说：参数是函数接收外部数据的变量
返回值是最后可以输出的具体结果         返回值是函数执行后通过 return 交还给调用者的结果，不一定是“输出”。

4.列表和字典有什么区别？
表达形式不同,列表list用[]来表示，字典dict用{}来表示,字典中的每个元素包括key和value，列表直接传入单个元素内容即可
补充：列表靠位置索引取值，比如 list[0]；字典靠key取值，比如 dict["name"]。

5.为什么文件读写推荐使用 with open()？
with open() 最后自动关闭打开的文件 防止因遗忘用.close()而导致修改后的文件未被加载保存
小修正：不是“未被加载保存”，更准确是避免文件没关闭导致资源占用、数据没有及时写入磁盘等问题

6.try / except 解决什么问题？
try是尝试执行可能会报错的代码
except是捕获异常

7.JSON 和 Python 字典是不是同一个东西？
不是。JSON 是一种文本数据格式，Python 字典是 Python 里的数据类型。

8.json.load() 和 json.dump() 分别做什么？
json.load()是把json文件转换成python文件
json.dump()是把python文件转换成json文件

修改：
更准确地说：
json.load()：从 JSON 文件读取内容，转换成 Python 对象，比如字典/列表。
json.dump()：把 Python 对象写入 JSON 文件。

以上问题是用自己的理解来回答，修改补充的地方是基于原本回答基础上的表述优化。

| 函数 | 方向 | 处理对象 | 作用 |
|---|---|---|---|
| `json.load(fp)` | JSON -> Python | 文件对象 | 从文件读取 JSON，转成 Python 对象 |
| `json.loads(s)` | JSON -> Python | 字符串 | 从 JSON 字符串解析成 Python 对象 |
| `json.dump(obj, fp)` | Python -> JSON | 文件对象 | 把 Python 对象写入 JSON 文件 |
| `json.dumps(obj)` | Python -> JSON | 字符串 | 把 Python 对象转成 JSON 字符串 |



