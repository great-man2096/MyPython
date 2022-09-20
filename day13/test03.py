f = open('test.txt', 'r+')
# words = f.read()
f.write("in the head")
f.seek(0,2)     # 第一个参数说明：偏移量 ；第二个参数说明： 0文件开头 1当前位置 2文件结尾
f.write("in the end")
f.close()
# print(words)