from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import pygal

def draw_bar(x_labels, values):
    # 设置我们自己的颜色
    my_style = LS('#336633',base_style=LCS)
    # 描绘的配置
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred JavaScript Projects on GitHub'
    chart.x_labels = x_labels
    chart.add('', values)
    chart.render_to_file('py_repos.svg')