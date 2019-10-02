def display() :
    l1 = ['   ','|','   ','|','   ']
    l2 = ['=','=','=','=','=','=','=''=','=','=','=']
    l3 = ['   ','|','   ','|','   ']
    l4 = ['=','=','=','=','=','=','=''=','=','=','=']
    l5 = ['   ','|','   ','|','   ']
    display = [l1,l2,l3,l4,l5]
    return display
def print_disp (x):
    for i in x:
        for j in i:
             print(j,end=f'')
        print()
