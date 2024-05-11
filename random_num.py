import random
import csv

# 定义电子邮件后缀列表
email_suffixes = ['@qq.com', '@163.com', '@gmail.com']

# 初始化一个空列表来存储所有的电子邮件字典
all_emails = []

# 循环5000次，生成并添加电子邮件到列表中
for _ in range(5000):
    # 生成一个9位的随机数（可以是0-9之间的任意数字）
    random_part = ''.join(random.choices('0123456789', k=9))
    # 将第一位设置为1，并组合成一个10位的数字
    number = '1' + random_part
    # 随机选择一个电子邮件后缀
    suffix = random.choice(email_suffixes)
    # 组合数字和电子邮件后缀以创建完整的电子邮件地址
    email = number + suffix
    # 创建一个字典，其中键是'email'，值是我们生成的电子邮件地址
    email_dict = {'email': email}
    # 将字典添加到列表中
    all_emails.append(email_dict)

# 写入CSV文件和你希望的位置
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['email']  # CSV文件的列名
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入列名
    writer.writeheader()
    # 写入数据
    for row in all_emails:
        writer.writerow(row)

print("5000 email addresses have been written to 'output.csv'.")