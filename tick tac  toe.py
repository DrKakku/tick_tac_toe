from display import *
print_disp(display())
x = display() 
global counter
counter = 0
cont = 'y'
win = False
while win == False:
    counter = counter + 1
    print(counter)
    if counter % 2 > 0 and counter < 10:
        print("Player 1 :")
        print_disp(play(" X ",x))
        if x[4][4] == '    ':
            counter = counter + 1
            x[4][4] = '   '
        if x[0][0] == x[0][2] == x[0][4] != '   ' or x[2][0] == x[2][2] == x[2][4] != '   ' or x[4][0] == x[4][2] == x[4][4] != '   ' or x[0][0] == x[2][0] == x[4][0] != '   ' or x[0][2] == x[2][2] == x[4][2] != '   ' or x[0][4] == x[2][4] == x[4][4] != '   ' or x[0][0] == x[2][2] == x[4][4] != '   ' or x[0][4] == x[2][2] == x[4][0] != '   ' :
            print("congulation PLAYER 1 won ")
            win = True
            input()
    elif counter % 2 == 0 and counter < 10:
        print("Player 2 :")
        print_disp(play(" O ",x))
        if x[4][4] == '    ':
            counter = counter + 1
            x[4][4] = '   '        
        if x[0][0] == x[0][2] == x[0][4] != '   ' or x[2][0] == x[2][2] == x[2][4] != '   ' or x[4][0] == x[4][2] == x[4][4] != '   ' or x[0][0] == x[2][0] == x[4][0] != '   ' or x[0][2] == x[2][2] == x[4][2] != '   ' or x[0][4] == x[2][4] == x[4][4] != '   ' or x[0][0] == x[2][2] == x[4][4] != '   ' or x[0][4] == x[2][2] == x[4][0] != '   ' :
            print("congulation PLAYER 2 won ")
            win = True
            input()
    else:
        print("The game was a draaw and no one won")
        print("Do you want to play again")
        cont = input("for yes press y for no press n (y/n)")
        if cont == 'y':
            x = display()
            counter = 0
        else:
            input()    
            
