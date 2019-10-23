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
             print (j , end = '')
        print()
     return x
#This code shoud replace the element of the table to the desired element z to the desired position (coordinates) to the table disp in a tic tac toe matrix
def play (z,disp):
#This code will take input and convert it into a list of single cordinate which is seprated by " " the cordinates are intiger in nature so can be used in spliting   
#__________________________________________________________________________________________________________________#
     cordinates = []  
     num = ['1','2','3']
     conditin = False
     while conditin == False: 
          raw_input = input ("what do you want to play input in x(row) y(column) location :- ") 
          if raw_input[0] in num and raw_input[2] in num:
            conditin = True
            list_input = raw_input.split(" ")
            for i in list_input:
                 i = int(i)
                 cordinates.append(i)
          else :
              print ("please enter a numeric value ")          

#______________________________________________________________________________________________________________________#



     x = y = int()
     x = cordinates[0]
     y = cordinates[1]
     global counter
     if x == 1:
          x = 0
     if y == 1:
          y = 0
     if y == 3:
          y = y + 1               
     if x == 3:
          x = x + 1
     if disp[x][y] != '   ':
          print ("Acting smart are we try to play on another position ")
          disp[4][4] = '    '
          return disp
          
     disp[x][y] = z
     return disp
