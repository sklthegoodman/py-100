import csv
from matplotlib import pyplot
from datetime import datetime

with open('./data/death_valley_2014.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    # 处理头部
    for index, column in enumerate(header_row):
        print(index, column)

    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            low = int(row[3])
            high = int(row[1])
        except ValueError:
            print(current_date, 'missing data.')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

    fig = pyplot.figure(dpi=128, figsize=(10, 6))

    pyplot.plot(dates, highs, c='red', alpha=0.5)
    pyplot.plot(dates, lows, c='blue', alpha=0.5)
    pyplot.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    pyplot.title('Daily temperatures - 2014')
    pyplot.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    pyplot.ylabel('Temperature F', fontsize=16)
    pyplot.tick_params(axis='both', which='major', labelsize=16)
    # pyplot.axis([0, 32, 0, 80])
    
    pyplot.show()