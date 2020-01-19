#! /usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib import pyplot

squares = [1, 4, 9, 16 ,25]
values = [1, 2, 3, 4, 5]
pyplot.plot(values, squares, linewidth=5)

# 设置图标的信息
pyplot.title('My first chart', fontsize=24)
pyplot.xlabel('Values', fontsize=14)
pyplot.ylabel('Squares of Values', fontsize=14)
pyplot.tick_params(axis='both', labelsize=14)

pyplot.show()