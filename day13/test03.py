f = open('test.txt', 'r+')
# words = f.read()
f.write("in the head")
f.seek(0,2)     # ��һ������˵����ƫ���� ���ڶ�������˵���� 0�ļ���ͷ 1��ǰλ�� 2�ļ���β
f.write("in the end")
f.close()
# print(words)