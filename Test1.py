
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n = int(input("请输入要输出的斐波那契项数 n： "))

# 处理 n <= 0 的情况
if n <= 0:
    print("请输入大于 0 的整数。")
else:
    fib = []  # 用来存储结果

    # 特殊情况 n=1 或 n=2
    if n >= 1:
        fib.append(1)
    if n >= 2:
        fib.append(1)

    # 生成后续项
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    print(f"前 {n} 个斐波那契数列为：")
    print(fib)
    print('First commit')
    print('Second commit')   
    print('Third commit')
    print('from vs code')
    print('From github main')
