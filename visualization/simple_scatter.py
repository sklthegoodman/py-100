# 散点图
from matplotlib import pyplot

x_values = list(range(0,100))
y_values = [x**2 for x in x_values]

pyplot.scatter(x_values, y_values, s=40, edgecolors='none', c='#cc00cc')
# todo 渐变怎么实现？
# pyplot.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm.Blues, edgecolor='none', s=40)


pyplot.title("Square Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of values", fontsize=14)

# 设置坐标轴的取值范围
pyplot.axis([0, 110, 0, 11000])

# pyplot.tick_params(axis='both', which='major', labelsize=14)


pyplot.show()
