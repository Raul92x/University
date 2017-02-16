# tictactoe.py
# by Kerstin Voigt, Feb 2012

import random

INIT_T3 = {'a': 0, 'b': 0, 'c':0, 'd': 0,'e': 0, 'f':0, 'g': 0, 'h': 0, 'i': 0}

class T3():
    def __init__(self, init_ttt = INIT_T3 ):
        self.ttt = init_ttt
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

    def __eq__(self,other):
        for k in self.ttt.keys():
            if self.ttt[k] != other.ttt[k]:
                return  False
        return  True
    
    # a way to display the board
    def present(self):
        self.present_row(self.row1)
        self.present_row(self.row2)
        self.present_row(self.row3)
        print "        [%d]\n" % self.eval_fct()


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
        twox = self.has2XO('X')
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

    # True if there is a full  of symbol 'symb'
    def full_diag(self,symb):
        rs = list(3*symb)
        return rs==self.rcd_values(self.dia1) or\
               rs==self.rcd_values(self.dia2)

    def has2XO(self,mark):
        twos = self.has_row2XO(mark)
        twos += self.has_col2XO(mark)
        twos += self.has_dia2XO(mark)
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
    def has_row2XO(self,mark):
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

    def has_col2XO(self,mark):
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

    def has_dia2XO(self,mark):
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

    # number of still possible rows, cols, and diags for X minus
    # number of still possible rows, cols, and diags for O
    def eval_fct(self):
        # possible for X: all r,c,d that have < 3 X's and no @'s
        e1 = [self.possXO('X',self.row1),self.possXO('X',self.row2),\
              self.possXO('X',self.row3),self.possXO('X',self.col1),\
              self.possXO('X',self.col2),self.possXO('X',self.col3),\
              self.possXO('X',self.dia1),self.possXO('X',self.dia2)]
        e2 = [self.possXO('@',self.row1),self.possXO('@',self.row2),\
              self.possXO('@',self.row3),self.possXO('@',self.col1),\
              self.possXO('@',self.col2),self.possXO('@',self.col3),
              self.possXO('@',self.dia1),self.possXO('@',self.dia2)]
        return e1.count(True) - e2.count(True)

    def possXO(self,symb,rcd):
        return self.rcd_values(rcd).count(symb) < 3 and\
               self.rcd_values(rcd).count(other(symb)) == 0               

    def board_full(self):
        for k in self.ttt.keys():
            if self.ttt[k] != 'X' and self.ttt[k] != '@':
                return False
        return True

    # call with 'X' or '@' for turn;
    def successors (self, turn):
        succs = []
        rcds = ['row1','row2','row3','col1','col2','col3','dia1', 'dia2']
        
        for a in rcds:
            if self.possXO(turn,eval('self.'+a)):
                for k in eval('self.'+a):
                    if self.ttt[k] == 0:
                        newttt = self.ttt.copy()
                        newttt[k] = turn
                        newT3 = T3(newttt)
                        if not newT3 in succs:
                            succs.append(T3(newttt))
        return succs
    
                        
        
    # the game loop
    def play(self):
        self.reset()
        print "\n\n"
        print "Starting a new game of tictactoe. X begins ...\n"
        turn = 'X'
        while not self.board_full():
            #while not self.winX() and not self.winO():
            if turn == 'X':
                self.put_X()
                if self.winX():
                    self.present()
                    print "X, you win  :-))\n\n"
                    return
                turn = '@'
            else:
                #self.random_O()
                self.responds_O()
                if self.winO():
                    self.present()
                    print "O wins, you loose  :-((\n\n"
                    return
                turn = 'X'
        print "It a tie :-||\n\n"
        return 
        return

        # O responds with maxi-min reasoning
        def smart_response_O(self):
        
            # possible addition: at this point decide randomly (and only
            # occasionally, whether to go smart with maximin, or drop the
            # ball with an arbitrary move that will give 'X' a bit of
            # a chance ("artificial stupidity")
            
            succs1 = self.successors('@')
            succ2 = []
            for s1 in succs1:
                ss2 = s1.successors('X')
                succs2.append(ss2)
            # now find the max states among succs2 (max2s)

            # then find the min state among the max2s; return that state

            
            
    


    

def other(mark):
    if mark == 'X':
        return '@'
    else:
        return 'X'
    
            

            

    
               
   
                                   
