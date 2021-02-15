# version 2021-02-14
# wikipedia  https://ja.wikipedia.org/wiki/Raspberry_Pi
# 累計出荷台数は2013年10月31日までで200万台[7]、2014年6月11日までで300万台[8]、2015年2月18日までで500万台[9]、
# 2015年10月13日までで700万台[10]、2016年2月29日までで800万台[11]、2016年9月8日までで1,000万台[12]、
# 2016年11月25日までで1,100万台[13]と、3年間で約1,000万台のペースであった。
# その後、累計出荷台数は、ペースが上がり、2018年3月14日までで1,900万台[14]、 2019年12月14日までで3,000万台[15]、
# 2021年1月21日までで3,700万台[16]と 1年で約600万台の直線的な増加となっている。

import datetime as dt

import matplotlib.pyplot as plt
# import datetime

date_values = (
    "2012/2/29", 0,
    "2013/10/31", 2000000,
    "2014/6/11", 3000000,
    "2015/2/18", 5000000,
    "2015/10/13", 7000000,
    "2016/2/29", 8000000,
    "2016/9/8", 10000000,
    "2016/11/25", 11000000,
    "2018/3/14", 19000000,
    "2019/12/14", 30000000,
    "2021/1/21", 37000000)
dates = []
values = []
for item in date_values:
    if type(item) is str:
        dates.append(item)
    elif type(item) is int:
        values.append(item / 10000)

x = [dt.datetime.strptime(d, '%Y/%m/%d').date() for d in dates]
y = [int(v) for v in values]

fig = plt.figure(dpi=200, figsize=(4.0, 2.5))
ax = fig.add_subplot(1, 1, 1)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
ax.set_xlim([dt.date(2012, 1, 1), dt.date(2024, 12, 31)])
ax.set_ylim(0, 5000)

FONT_NAME1 = "HackGen35"

plt.rcParams["font.family"] = FONT_NAME1
plt.rcParams["font.size"] = 9.9
plt.title('Raspberry Pi 累計出荷台数 (万台)', fontsize=11, fontname=FONT_NAME1)
plt.rcParams['axes.grid'] = True
plt.rcParams['axes.linewidth'] = 0.6
plt.rcParams['grid.linestyle'] = '-'
plt.rcParams['grid.linewidth'] = 0.8
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.width'] = 1.2
plt.rcParams['ytick.major.width'] = 1.2

plt.plot(x, y,  linewidth=1.5,
         marker="D", markersize=2.5, markeredgewidth=0.5,
         markeredgecolor="green", markerfacecolor="#a08080")
plt.show()
