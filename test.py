"""
このファイルに解答コードを書いてください
"""

# input.txtを読み取り、１行ずつ読み取る（\nを削除）
with open('input.txt', 'r') as f:
    l = [s.replace('\n', '') for s in f.readlines()]

"""
出力 >>> ['767:bFX4mJ', '905:U6bUU', '896:i3GJgV'...]
"""

# m
m = int(l[len(l)-1])

list_m =[]

# :にて分割する
for i in range(len(l) - 1):
    split_l = l[i].split(sep=':')         # ['767', 'bFX4mJ']
    
    number = int(split_l[0])

# mがiの倍数かどうかを判定
    if m % number == 0:
        list_m.append([split_l[0], split_l[1]])
        
# 小さい順番に並べる
list_m = sorted(list_m, key = lambda x: int(x[0]))

# 結果出力用
output = []

# なかったら
if not list_m:
    output.append(m)
    print(output[0])

# 存在したら
else:
    for i in range(len(list_m)):
        output += list_m[i][1]

# 結合する
    print(''.join(output))