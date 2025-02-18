# version 2025-02-13
# wikipedia  https://ja.wikipedia.org/wiki/Raspberry_Pi


import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg

# Create a canvas with Agg backend then save it as a file.
#     canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(fig)
#     canvas.print_figure(file_name, dpi=300)
#     print(file_name + ' has been saved.')
# You can show the plot on the display, too.
#     show.plt


date_time_now = dt.datetime.now().strftime('%Y%m%d%H%M%S')
#file_name = 'images/Raspberry Pi Cumulative Shipment Units' + date_time_now + '.png'
file_name = 'images/Raspberry Pi Cumulative Shipment Units' + '.png'
# for Google Colab environment
# file_name = '/content/images/RaspberryPiCumulativeShipmentUnits_' + date_time_now + '.png'


def pre_process():
    date_values = (
        "2012/02/29",  0,
        "2012/12/03", 840000,
        "2013/01/14", 1000000,
        "2013/10/08", 1750000,
        "2013/11/13", 2000000,
        "2014/03/03", 2500000,
        "2014/06/11", 3000000,
        "2014/08/20", 3500000,
        "2014/10/13", 3800000,
        "2015/02/18", 5000000,
        "2015/12/10", 7000000,
        "2016/02/29", 8000000,
        "2016/09/09", 10000000,
        "2016/11/25", 11000000,
        "2017/03/18", 12500000,
        "2017/07/19", 14500000,
        "2017/12/20", 17000000,
        "2018/12/21", 23000000,
        "2019/03/01", 25000000,
        "2019/12/17", 30000000,
        "2021/01/21", 37000000,
        "2021/05/12", 40000000,
        "2021/09/22", 42000000,
        "2021/11/16", 43000000,
        "2022/02/28", 46000000,
        "2023/01/03", 50000000,
        "2023/10/09", 55000000,
        "2024/05/15", 60000000,)

    dates = []
    values = []
    for item in date_values:
        if type(item) is str:
            dates.append(item)
        elif type(item) is int:
            values.append(item)
    return dates, values


dates, values = pre_process()

x = [dt.datetime.strptime(d, '%Y/%m/%d').date() for d in dates]
y = [int(v) for v in values]

fig = plt.figure(dpi=300, figsize=(3.0, 2.5), tight_layout=True)
ax = fig.add_subplot(111)

fig.patch.set_alpha(0)

canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(fig)


# FIG_TITLE = 'Raspberry Pi 累計出荷台数 (百万台)'
FIG_TITLE = 'Cumulative Shipment Units (mil)'
UNITS_DIV = 1000000
UNITS_LIM = 70000000

# FONT_NAME1 = "./Hackgen"
# ax.set_title(FIG_TITLE, fontsize=8, fontproperties=FONT_NAME1)

ax.set_title(FIG_TITLE, fontsize=9)
ax.set_xlim([dt.date(2012, 1, 1), dt.date(2026, 1, 1)])

ax.set_ylim(0, UNITS_LIM)
ax.axes.tick_params(direction='in', width=1.2)
ax.tick_params(axis="x", labelsize=8, labelrotation=45)
ax.tick_params(axis="y", labelsize=7.4)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x / UNITS_DIV))))
ax.axes.grid(visible=True, linestyle='--', linewidth=0.3)

ax.plot(x, y,  linewidth=1.2, color='#8080e0',
        marker='D', markersize=3.0, markeredgewidth=0.5,
        markeredgecolor='#80a080', markerfacecolor='#e08080')

# You can show the plot on the display by uncommenting the following line.
# plt.show()

canvas.print_figure(file_name, dpi=300)
print(file_name + ' has been saved.')
