# version 2022-04-22
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


date_values = (
    ("2012/2/29", 0),
    ("2013/10/31", 2000000),
    ("2014/6/11", 3000000),
    ("2015/2/18", 5000000),
    ("2015/10/13", 7000000),
    ("2016/2/29", 8000000),
    ("2016/9/8", 10000000),
    ("2016/11/25", 11000000),
    ("2018/3/14", 19000000),
    ("2019/12/14", 30000000),
    ("2021/1/21", 37000000),
    ("2021/5/12", 40000000),
    ("2021/9/22", 42000000),
    ("2021/11/16", 43000000),
    ("2022/2/28", 46000000),
    )
dates, values = zip(*date_values)

x = [dt.datetime.strptime(d, '%Y/%m/%d').date() for d in dates]
y = [int(v) for v in values]

fig = plt.figure(dpi=300, figsize=(3.0, 2.5), tight_layout=True)
ax = fig.add_subplot(111)

fig.patch.set_alpha(0)

canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(fig)


# FIG_TITLE = 'Raspberry Pi 累計出荷台数 (百万台)'
FIG_TITLE = 'Cumulative Shipment Units (mil)'
UNITS_DIV = 1000000
UNITS_LIM = 50000000

# FONT_NAME1 = "./Hackgen"
# ax.set_title(FIG_TITLE, fontsize=8, fontproperties=FONT_NAME1)

ax.set_title(FIG_TITLE, fontsize=8)
ax.set_xlim([dt.date(2012, 1, 1), dt.date(2023, 1, 31)])

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
