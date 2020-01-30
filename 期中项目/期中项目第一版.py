with open("D:/jupyter_notebook_files/Crossin/report.txt", 'r', encoding='UTF-8', errors='ignore') as f:
    f.seek(0)
    info1 = [line.strip() for line in f.readlines()]
# print(repr(info1))

info2 = []
for i in info1:
    i2 = i.split(' ')
    info2.append(i2)
# print("info2: ", info2)

def change(x):
    try:
        return float(x)
    except:
        return ''.join((x[0],x[1]))

info3 = info2[:]
info4 = []
for j in info3[1 : ]:
    info4.append(list(map(change, j)))
# print("info4: ", info4, '\n'*2)
info5 = info4[:]
for n in info5:
#     print(n[1])
    n.append(sum(n[1:]))
    n.append(float('%.1f'%((sum(n[1:]) - max(n[1:])) / (len(n[1:]) - 1))))
#     print(n[1])
# print("info5: ", info5, '\n'*2)
info6 = sorted(info5, key=lambda x:(x[-1]), reverse=True)
# print('\n'*2, "info6: ", info6)
sum1 = 0
total_ave = []
for k in range(1, 12):
    for m in info6:
        # info6[0][1] + info6[1][1] + info6[2][1] + ...+ info6[m][1]
        sum1 += m[k]
    total_ave.append(float('%.1f'%(sum1 / 30)))
    sum1 = 0
total_ave.insert(0, 0)
total_ave.insert(1, '平均')
total_ave.append('\n')
# print('\n', "total_ave: ", total_ave)
q = 1
for k in info6:
    k.insert(0, q)
    q += 1
# print('\n'*2, "info6: ", info6)
str_total_ave = list(map(str, total_ave))
# print(str_total_ave)
info7 = []
for l in info6:
    info7.append(list(map(str, l)))
# print("info7: ", info7)
info8 = []
for w in info7:
    g = ['不及格' if float(x) < 60 else x for x in w[2:]]
    g.insert(0, w[1])
    g.insert(0, w[0])
    # print(g, '\n')
    info8.append(g)
# print("info8: ", info8)
with open("result.txt", 'w') as f:
    f.writelines('名次\t姓名\t语文\t数学\t英语\t物理\t化学\t生物\t政治\t历史\t地理\t总分\t平均分\n')
    f.writelines('\t'.join(str_total_ave))
    for p in info8:
        f.writelines('\t'.join(p) + '\n')
print("Done!")