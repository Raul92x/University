#Raul Diaz
#lab5

# tictactoe.py
# by Kerstin Voigt, Feb 2012

import random

class T3():
    def __init__(self):
        self.ttt = {'a': 0, 'b': 0, 'c':0, 'd': 0,'e': 0, 'f':0,
               'g': 0, 'h': 0, 'i': 0}
        self.row1 = ['a','b','c']
        self.row2 = ['d','e','f']
        self.row3 = ['g','h','i']
        self.col1 = ['a','d','g']
        self.col2 = ['b','e','h']
        self.col3 = ['c','f','i']
        self.dia1 = ['a','e','i']
        self.dia2 = ['c','e','g']

    def reset(self):
        self.ttt = {'a': 0, 'b': 0, 'c':0, 'd': 0,'e': 0, 'f':0,
               'g': 0, 'h': 0, 'i': 0}

    # row, col, or diag values
    def rcd_values(self,rcd):
        return [self.ttt[x] for x in rcd]

    def __str__(self):
        return " %s %s %s" % (self.rcd_values(self.row1),
                                   self.rcd_values(self.row2),
                                   self.rcd_values(self.row3))
    # a way to display the board
    def present(self):
        self.present_row(self.row1)
        self.present_row(self.row2)
        self.present_row(self.row3)
        print("\n")


    def present_row(self,row):
        for i in range(3):
            if self.ttt[row[i]] == 0:
                if i < 2:
                    print(row[i]),
                else:
                    print(row[i])
            else:
                if i < 2:
                    print(self.ttt[row[i]]),
                else:
                    print(self.ttt[row[i]])
        

    # prompt for and put X
    def put_X(self):
        self.present()
        while(True):
            pick = raw_input('Choose place for X: ')
            if self.ttt[pick] == 0:
                self.ttt[pick] = 'X'
                break
            else:
                print "Can't do; choose again:"

    # place a random O (the games current response)
    def random_O(self):
        self.present()
        print "Playing an @ ..."
        rest=[]
        for k in self.ttt.keys():
            if self.ttt[k] == 0:
                rest.append(k)
        pick = random.choice(rest)
        self.ttt[pick] = '@'
		
		

    # O responds by placing @ in any row with 2 X; random otherwise

    def responds_O(self):
        twox = self.has2X('X')
        if twox != None:
            self.present()
            print "Playing an @ ..."
            self.no3X(twox)
        else:
            self.random_O()



    # True if there is a full row of symbol 'symb'    
    def full_row(self,symb):
        rs = list(3*symb)
        return rs==self.rcd_values(self.row1) or\
               rs==self.rcd_values(self.row2) or\
               rs==self.rcd_values(self.row3)

    # True if there is a full col of symbol 'symb'
    def full_col(self,symb):
        rs = list(3*symb)
        return rs==self.rcd_values(self.col1) or\
               rs==self.rcd_values(self.col2) or\
               rs==self.rcd_values(self.col3)

    # True if there is a full diag of symbol 'symb'
    def full_diag(self,symb):
        rs = list(3*symb)
        return rs==self.rcd_values(self.dia1) or\
               rs==self.rcd_values(self.dia2)

    def has2X(self,mark):
        twos = self.row_has2X(mark)
        twos += self.col_has2X(mark)
        twos += self.dia_has2X(mark)
        if twos == []:
            return None
        else:
            return random.choice(twos)

    def no3X(self,twox):
        if twox[0] == 'r':
            self.norow3X(twox[1])
        elif twox[0] == 'c':
            self.nocol3X(twox[1])
        else:
            self.nodia3X(twox[1])

    def norow3X(self,rowno):
        if rowno == 1:
            for x in self.row1:
                if self.ttt[x] != 'X':
                    self.ttt[x] = '@'
        elif rowno == 2:
            for x in self.row2:
                if self.ttt[x] != 'X':
                    self.ttt[x] = '@'
        else:
            for x in self.row3:
                if self.ttt[x] != 'X':
                    self.ttt[x] = '@'

    def nocol3X(self,colno):
        if colno == 1:
            for x in self.col1:
                if self.ttt[x] != 'X':
                    self.ttt[x] = '@'
        elif colno == 2:
            for x in self.col2:
                if self.ttt[x] != 'X':
                    self.ttt[x] = '@'
        else:
            for x in self.col3:
                if self.ttt[x] != 'X':
                    self.ttt[x] = '@'
        

    def nodia3X(self,diano):
        if diano == 1:
            for x in self.dia1:
                if self.ttt[x] != 'X':
                    self.ttt[x] = '@'
        else: #diano == 2:
            for x in self.dia2:
                if self.ttt[x] !='X':
                    self.ttt[x] = '@'
				
            
    # row of two X
    def row_has2X(self,mark):
        twos = []
        opp = other(mark)
        if self.rcd_values(self.row1).count(mark) == 2 and\
           self.rcd_values(self.row1).count(opp) == 0:
            twos.append(('r',1))
        if self.rcd_values(self.row2).count(mark) == 2 and\
           self.rcd_values(self.row2).count(opp) == 0:
            twos.append(('r',2))
        if self.rcd_values(self.row3).count(mark) == 2 and\
           self.rcd_values(self.row3).count(opp) == 0:
            twos.append(('r',3))
        return twos

    def col_has2X(self,mark):
        twos = []
        opp = other(mark)
        if self.rcd_values(self.col1).count(mark) == 2 and\
           self.rcd_values(self.col1).count(opp) == 0:
            twos.append(('c',1))
        if self.rcd_values(self.col2).count(mark) == 2 and\
           self.rcd_values(self.col2).count(opp) == 0:
            twos.append(('c',2))
        if self.rcd_values(self.col3).count(mark) == 2 and\
           self.rcd_values(self.col3).count(opp) == 0:
            twos.append(('c',3))
        return twos

    def dia_has2X(self,mark):
        twos = []
        opp = other(mark)
        if self.rcd_values(self.dia1).count(mark) == 2 and\
           self.rcd_values(self.dia1).count(opp) == 0:
            twos.append(('d',1))
        if self.rcd_values(self.dia2).count(mark) == 2 and\
           self.rcd_values(self.dia2).count(opp) == 0:
            twos.append(('d',2))
        return twos    

    # True if X wins
    def winX(self):
        return self.full_row('X') or\
               self.full_col('X') or\
               self.full_diag('X')

    # True if O wins
    def winO(self):
        return self.full_row('@') or\
               self.full_col('@') or\
               self.full_diag('@')

    # the game loop
    def play(self):
        self.reset()
        print "\n\n"
        print "Starting a new game of tictactoe. X begins ...\n"
        while not self.winX() and not self.winO():
            self.put_X()
            if self.winX():
                self.present()
                print "X, you win  :-))\n\n"
                break
            self.responds_O()
            if self.winO():
                self.present()
                print "O wins, you loose  :-((\n\n"


def other(mark):
    if mark == 'X':
        return '@'
    else:
        return 'X'
    

ttt = T3()
ttt.play()

            

            

    
               
   
    
