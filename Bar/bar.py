'''
python bar.py
'''
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


save_name = 'bar'

# sns.set_theme(style="whitegrid")

# penguins = sns.load_dataset("penguins")
# raise RuntimeError( type(penguins) )
# raise RuntimeError( penguins['island'], penguins['sex'], penguins['body_mass_g'] )

data = [
    ['R@1', 'ITC', 25.53], ['R@1', 'MLM-T', 29.17], ['R@1', 'MLM-w/', 29.72],
    ['R@5', 'ITC', 53.48], ['R@5', 'MLM-T', 57.55], ['R@5', 'MLM-w/', 59.74],
    ['R@10','ITC', 64.64], ['R@10','MLM-T', 68.26], ['R@10','MLM-w/', 70.79],
]

offset = 0
new_data = []
for datum in data:
    attr_1, attr_2, attr_3 = datum
    new_data.append([attr_1, attr_2, attr_3 - offset])
# end for
data = new_data

df = pd.DataFrame(data, columns=['', 'ID', 'Recall'])


# 创建图形时设置constrained_layout=True
fig, ax = plt.subplots(constrained_layout=True)


palette = {'ITC': '#f7cac9', 'MLM-T': '#92a8d1', 'MLM-w/': '#e6f2da'}  # ffddc1
ax = sns.barplot(
    df, x="", y="Recall", hue="ID",
    palette=palette,
    width=0.6, bottom=offset, ax=ax
)

# 手动设置 y 轴范围
# ax.set_ylim((20, 80))  # y 轴数据范围


# 获取当前的 y 轴范围
ylim = ax.get_ylim()
# 假设你想在 y 轴两端留出 10% 的空白空间
margin = (ylim[1] - ylim[0]) * 0.1
new_ylim = (ylim[0] - margin, ylim[1] + margin)
# 设置新的 y 轴范围
ax.set_ylim(new_ylim)



# 设置全局字体大小
font = {'size': 14}  # 可以根据需要调整字体大小
matplotlib.rc('font', **font)


# 设置 x 轴和 y 轴标签的字体大小
ax.set_xlabel(ax.get_xlabel(), fontsize=14)
ax.set_ylabel(ax.get_ylabel(), fontsize=14)


# 设置 x 轴和 y 轴刻度标签的字体大小
for tick in ax.get_xticklabels():
    tick.set_fontsize(14)
for tick in ax.get_yticklabels():
    tick.set_fontsize(14)


ax.set_title('ROCO', font={'size': 14})


legend = ax.legend()
# 设置legend的字体大小
legend.set_title(None)  # 去掉legend的标题，可根据需要保留
# 设置legend中每个元素的字体大小，可根据需要调整
for text in legend.get_texts():
    text.set_fontsize(16)


fig = plt.gcf()

fig.savefig(f'{save_name}.png')


raise RuntimeError( 'stop' )



# Draw a nested barplot by species and sex
g = sns.catplot(
    data=penguins, kind="bar",
    x="species", y="body_mass_g", hue="sex",
    errorbar="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("", "Body mass (g)")
g.legend.set_title("")

