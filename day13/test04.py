# 备份文件
file_name = input("请输入需要备份的文件名")
# 我的写法
# bf_file_name = f"{file_name.split('.',-1)[0]}[备份].{file_name.split('.',-1)[1]}"
# 课程写法
index = file_name.rfind('.')  # 找到指定字符的位置
postfix = None
if index > 0:
    postfix = file_name[index:]
else:
    exit("文件名有误")
bf_file_name = file_name[:index] + '[备份]' + postfix  # 使用切片组合字符
print(f"已经生成的备份文件名：{bf_file_name}")
f1 = open(file_name, 'rb')
f2 = open(bf_file_name, 'wb')
while True:
    words = f1.read(1024)
    f2.write(words)
    if len(words) == 0:
        break
f1.close()
f2.close()
