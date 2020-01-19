import dice
import pygal

d = dice.Dice()
d2 = dice.Dice()

# 仅仅一个骰子的投掷结果
results = []
# 两个骰子的投掷结果
results_for_2_dices = []


for i in range(1000):
    d_r = d.roll()
    d2_r = d.roll()
    results.append(d_r)
    results_for_2_dices.append(d_r + d2_r)

# 分析结果
frequencies = []
for value in range(1, d.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 两个骰子的情况
frequencies_2 = []
for value in range(2, d.num_sides + d2.num_sides + 1):
    frequency = results_for_2_dices.count(value)
    frequencies_2.append(frequency)
print(frequencies_2)

# 可视化
hist = pygal.Bar()
hist.title = 'Result of rolling one dice 1000 times'
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = 'Results'
hist.y_title = 'Frequency of Results'
hist.add('D6', frequencies)
hist.render_to_file('test.svg')

# 两个骰子
hist2 = pygal.Bar()
hist2.title = 'Result of rolling two dices 1000 times'
hist2.x_labels = [x for x in range(2, 13)]
hist2.add('D6 + D6', frequencies_2)
hist2.render_to_file('two_dices.svg')