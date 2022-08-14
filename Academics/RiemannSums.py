from math import sin, cos, tan, pi
#input
sum_type = input("Right,Left,Middle,Trapezoid: \n")
function = input("Function: \n")
sum_range = (input("Range: \n"))
sum_range = sum_range.split(",")
try:
    sum_range = [float(a) for a in sum_range]
except ValueError:
    for b in range(0,len(sum_range)):
        if "pi" in sum_range[b]:
            sum_range[b] = eval(sum_range[b])
        else:
            sum_range[b] = float(sum_range[b])
N = float(input("Number of intervals: \n"))
riemann_sum = 0


if N != float('inf'):
    #right sum
    if (sum_type.lower() == "right"):
        interval = (sum_range[1] - sum_range[0])/N
        x = sum_range[0]+interval
        while round(x,10) <= sum_range[1]:
            riemann_sum = riemann_sum + eval(function)
            x = x + interval
        riemann_sum = interval * riemann_sum

    #left sum
    elif (sum_type.lower() == "left"):
        interval = (sum_range[1] - sum_range[0])/N
        x = sum_range[0]
        while round(x,4) <= sum_range[1] - interval:
            riemann_sum = riemann_sum + eval(function)
            x = x + interval
        riemann_sum = interval * riemann_sum

    #middle sum
    elif (sum_type.lower() == "middle"):
        interval = (sum_range[1] - sum_range[0])/N
        x = sum_range[0] + interval/2
        while round(x,4) <= sum_range[1] - interval/2:
            riemann_sum = riemann_sum + eval(function)
            x = x + interval
        riemann_sum = interval * riemann_sum
    
    #trapezoid sum
    elif sum_type.lower() == "trapezoid":
        interval = (sum_range[1] - sum_range[0])/N
        x = sum_range[0]
        while round(x,4) <= sum_range[1]:
            if x == sum_range[0] or x == sum_range[1]:
                riemann_sum = riemann_sum + eval(function)
            else:
                riemann_sum = riemann_sum + 2*eval(function)
            
            x = x+interval

        riemann_sum = (interval/2)*(riemann_sum)

    print("Riemann Sum: " + str(riemann_sum))
elif N == float('inf'):
    print("That functionality is not yet available")
