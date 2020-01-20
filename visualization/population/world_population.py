import json
from countries import get_country_code
import pygal_maps_world.maps as maps

filename = 'population_data.json'

cc_population = {}
with open(filename) as f:
    pop_data = json.load(f)
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            
            code = get_country_code(country_name)
            if code:
                print(code + ':' + str(population))
                cc_population[code] = population
            else:
                print('Error: not find ' + country_name)

    # 把国家们分组
    p1, p2, p3 = {}, {}, {}
    for cc, pop in cc_population.items():
        if pop < 10000000:
            p1[cc] = pop
        elif pop < 1000000000:
            p2[cc] = pop
        else:
            p3[cc] = pop

    wm = maps.World()
    wm.add('0 - 10m', p1)
    wm.add('10m - 1bn', p2)
    wm.add('> 1bn', p3)
    wm.render_to_file('world_population.svg')