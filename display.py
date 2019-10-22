#This function creates a ticktacktoe matrice for you so you do not have to go through the hassle
def display() :
    d11 = d12 = d13 = d21 = d22 = d23 = d31 = d32 = d33 = '   '
    l1 = [d11,'|',d12,'|',d13]
    l2 = ['=''=''=''=','=''=''=''=','=''=''=']
    l3 = [d21,'|',d22,'|',d23]
    l4 = ['=''=''=''=','=''=''=''=','=''=''=']
    l5 = [d31,'|',d32,'|',d33]
    display = [l1,l2,l3,l4,l5]
    return display
#This function prints the matrice so that the " " do not interfere and we can have a clean matrice
def print_disp (x):
    for i in x:
        for j in i:
             print(j, end = '')
        print()
#This code shoud replace the element of the table to the desired element z to the desired position (coordinates) to the table disp in a tic tac toe matrix
def play (cordinates,z,disp):
     x = y = int()
     cordinates[0] = x
     cordinates[1] = y
     if x == 2:
          x = x + 1
     elif y == 2:
          y = y + 1
     elif y == 3:
          y = y + 2               
     elif x == 3:
          x = x + 2
     disp[x][y] = z
     return disp
def inp ():
     raw_input = input ("Player 1 what do you want to play input in x , y location")
     cordinate = []    
     list_input = raw_input.split(",",1)
     for i in list_input:
           i = int(i)
           cordinate.append(i)
     return cordinate
