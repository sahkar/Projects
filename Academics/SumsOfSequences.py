import math

def n_fibonacci(n):
    #print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return n_fibonacci(n-1) + n_fibonacci(n-2)



option_select = input('Which of the floowing programs would you like to run today:\n 1. sums of sequences, \n 2. finding the nth terms of a sequence, \n 3. fibonacci check.\n')

if option_select == '1' or option_select == '1.':
    first_terms = input('Enter the first terms of the sequence \n')
    last_term = input('Enter the last terms of your sequence. if your sequence goes to infinity, write inf \n')

    first_terms = first_terms.split(',')
    is_arithmetic = True
    is_geometric = True

    for i in range (0, len(first_terms)):
        first_terms[i] = float(first_terms[i])
        if(first_terms[i] == 0):
            is_geometric = False
    
    for i in range (0, len(first_terms)-2):
        is_arithmetic = is_arithmetic and (first_terms[i+1] - first_terms[i]) == (first_terms[i+2] - first_terms[i+1])
        is_geometric = is_geometric and (first_terms[i+1] / first_terms[i]) == (first_terms[i+2] / first_terms[i+1])

    print('Arimetic Sequence: ', is_arithmetic)
    print('Geometric Sequence: ', is_geometric)

    if is_arithmetic == False and is_geometric == False:
        print('Sequence: False')

    second_term = float(first_terms[1])
    first_term = float(first_terms[0])
    if last_term != 'inf':
        last_term = float(last_term)  

    if is_arithmetic == True and last_term != 'inf':
        d_arithmetic = (second_term - first_term)
        d_arithmetic = float(d_arithmetic)
        n_arithmetic = (last_term - first_term)/(d_arithmetic) +1


    d_geometric = (second_term / first_term)
    d_geometric = float(d_geometric)
    if is_geometric == True and last_term != 'inf':   
        n_geometric = (math.log((last_term /first_term),(d_geometric)))+1


    if is_arithmetic and last_term != 'inf':
        print ('common differece: ' + str(d_arithmetic))
        print ('number of terms: ' + str(n_arithmetic))
    elif is_geometric and last_term != 'inf':
        print('common difference: ' + str(d_geometric))
        print('number of terms: ' + str(n_geometric))


    if is_arithmetic and last_term != 'inf':
        sequence_sum = (n_arithmetic/2*(first_term + last_term))

    elif is_geometric and last_term != 'inf':
        sequence_sum = first_term*(1-(d_geometric)**(n_geometric))/(1-d_geometric)

    elif is_arithmetic and last_term == 'inf':
        print('No Sum')

    elif is_geometric and last_term == 'inf':
        if (d_geometric >= 1) or (d_geometric <= -1):
            sequence_sum = ('Incalculable')
        else:
            sequence_sum= (first_term)/(1-d_geometric)

    if (is_arithmetic and last_term != 'inf') or is_geometric:
        print('Sum: ' + str(sequence_sum))



elif option_select == '2' or option_select == '2.':
    first_terms = input('Enter the first terms of the sequence \n')
    
    first_terms = first_terms.split(',')
    is_arithmetic = True
    is_geometric = True

    for i in range (0, len(first_terms)):
        first_terms[i] = float(first_terms[i])
        if(first_terms[i] == 0):
            is_geometric = False
    
    for i in range (0, len(first_terms)-2):
        is_arithmetic = is_arithmetic and (first_terms[i+1] - first_terms[i]) == (first_terms[i+2] - first_terms[i+1])
        is_geometric = is_geometric and (first_terms[i+1] / first_terms[i]) == (first_terms[i+2] / first_terms[i+1])

    print('Arimetic Sequence: ', is_arithmetic)
    print('Geometric Sequence: ', is_geometric)

    first_term = float(first_terms[0])
    second_term = float(first_terms[1])
    
    if is_arithmetic:
        d_arithmetic = (second_term - first_term)
        d_arithmetic = float(d_arithmetic)
        print('Common Difference: ' + str(d_arithmetic))

    elif is_geometric:
        d_geometric = (second_term / first_term)
        d_geometric = float(d_geometric)
        print('Common Difference: ' + str(d_geometric))
    
    if is_arithmetic:
        n_arithmetic= input('What term are you looking for?\n')
        n_arithmetic = float(n_arithmetic)
        print('Number of terms: ' + str(n_arithmetic))

    elif is_geometric:
        n_geometric = input('What term are you looking for?\n')
        n_geometric = float(n_geometric)   
        print('Number of terms: ' + str(n_geometric)) 
    
    if is_arithmetic:
        last_term = (first_term) + d_arithmetic*(n_arithmetic-1)
    
    elif is_geometric:
        last_term = (first_term)*((d_geometric)**(n_geometric-1))
    
    if is_arithmetic and is_geometric:
        print('Last term: ' + str(last_term))
    
    if is_arithmetic == False and is_geometric == False:
        print('No Sequence')
        
elif option_select == '3' or option_select == '3.':
    st = input('What is the term of the fibonaci sequence you are looking for \n')   
    nth = int(st)
    
    print(st + 'th Finonacci is ' + str(n_fibonacci(nth)))