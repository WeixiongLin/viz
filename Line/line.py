'''
python line.py
'''

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib import font_manager


times_new_roman_path = "./times new roman.ttf"
font_manager.fontManager.addfont(times_new_roman_path)
font_name = font_manager.FontProperties(fname=times_new_roman_path).get_name()


labels=['1','2','3','4']
xlim=range(0,4)
div = [0,1,2,3]

# '''
# 30 tasks sub
ours_train = [41.5, 43.7, 45.5, 44.0]
# ours_train_std = [1.7,2.3,1.5,2.4]
ours_train_std = [0, 0, 0, 0]
erm = [46.85] * 4
ylim=[40, 45, 50]

ymin=38
ymax=48
# title="30 tasks, sub-optimal, "+r'$\mathrm{S}=0.8$, m'
title="Title"
save_name="line"
#'''


plt.rcParams["font.family"] = font_name

fig, axes = plt.subplots(figsize=(6,4),ncols=1) # 设置绘图区域大小
ax1 = axes

size1= 25
size2= 25
width = 0.15

# colors = ['#82B0D2', '#FA7F6F']
colors = [[59, 108, 147], [253, 187, 71], [164,0,4]] # 256kb 蓝黄红
for i in range(len(colors)):
    r, g, b = colors[i]
    colors[i] = (r/255, g/255, b/255)
color_index = [0, 1]
colors = [colors[i] for i in color_index]

acc_lower = [ours_train[i]-ours_train_std[i] for i in range(len(ours_train))]
acc_upper = [ours_train[i]+ours_train_std[i] for i in range(len(ours_train))]

# 柱状图, 带误差, 黑色边框
# plt.bar(div, ours_train, width=width, color=colors[1], edgecolor='black', yerr=ours_train_std, capsize=5, label='Ours')
# plt.bar([x-width for x in div], erm, width=width, color=colors[0], edgecolor='black', yerr=erm_std, capsize=5, label='ERM')

ln1 = plt.plot(div, ours_train, color="teal", marker='s',)
ln1 = plt.plot(
    div, ours_train,
    color="teal", marker='s', markersize=20, label='Others',
    zorder=10, linewidth=2, markeredgewidth=2, markeredgecolor='black'
)

plt.fill_between(div, acc_lower, acc_upper, color="teal", alpha=0.2, zorder=0)
# erm 参考线
ln2 = plt.plot(div, erm, color=colors[0], linestyle='--', label='Ours', zorder=10, linewidth=4)
# grid ， 网格线放在柱状图后面作为背景
ax1.grid(linestyle='-', alpha=0.7, zorder=0)
# grid ， 网格线放在柱状图后面作为背景
# y
ax1.grid(axis='y', linestyle='-', alpha=0.7, zorder=0)
# 设置刻度
ax1.set_xticks([x for x in div])
ax1.set_xticklabels(div)

# 刻度字体大小
ax1.tick_params(axis='both', labelsize=size1)

# 设置坐标轴标签
ax1.set_xlabel('Cost (log FLOPS)', fontsize=size2)
ax1.set_ylabel('R@5 (%)', fontsize=size2)

# y轴范围
#ax1.set_ylim(0.93, 0.97)
#isicl ax1.set_ylim(0.77, 0.80)
# 设置图例
# ax1.legend(loc=4, fontsize=size2)
# ax1.legend(loc="center", fontsize=size2)
# # # plt.xticks([0,5,10,15,20,25,30],fontsize=20)

plt.yticks(ylim,fontsize=20)
ax1.set_ylim(ymin, ymax)
plt.title(title,fontsize=20)
plt.xticks(xlim,labels=labels)
#isicg plt.yticks([0.73,0.74,0.75,0.76],fontsize=20)
plt.legend(loc=4, fontsize=size2)
plt.tight_layout()

# plt.savefig(f"./imgs/{save_name}.pdf")
plt.savefig(f"./{save_name}.png")

# plt.show()
