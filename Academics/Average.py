
averaging = True

while averaging == True:
    series = input('Enter a series to sum \n')
    series = series.split(',')
    sum_value = 0
    average = 0
    for i in range (0, len(series)):
        sum_value = int(series[i]) + sum_value
        average = (sum_value/len(series))
        averaging = False
    print('Sum is: ' + str(sum_value))
    print('Average is:  ' + str(average))
    averaging = True
    