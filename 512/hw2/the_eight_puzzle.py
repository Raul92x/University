# Raul Diaz
# cse512
# homework2

# the_eight_puzzle.py
# Kerstin Voigt, for CSE 512, October 2014
# diferent puzzle sizes can te run by setting global variables R and C
# R = C = 3 for the 8 puzzle (3x3-1 tiles with labels 1,2,..8)

#from graphsearch import *
import random

R = 3
C = 3

MAXNODES = 5000

start1 = {(1,1):3, (1,2):4, (1,3):'B', (2,1):1, (2,2):8, (2,3):2,\
         (3,1):7, (3,2):6, (3,3):5}

# what is your goal state?

goal1 = {(1,1):1, (1,2):2, (1,3):3, (2,1):8, (2,2):'B', (2,3):4,\
         (3,1):7, (3,2):6, (3,3):5}

# prints a puzzle state

def prp(puzz):
    #print "\n"
    for i in range(R):
        for j in range(C):
            print "%s " % puzz[(i+1,j+1)],
        print "\n"
    
# return (row,col) of location of blank in puzzle puzz

def locate_blank(puzz):
    for k in puzz.keys():
        if puzz[k] == 'B':
            return k
    return (-1,-1)

# returns True if puzz1 and puzz2 are equal; both parameters are
# dictionaries  in the style of start1 and goal1; 

def puzz_equal(puzz1, puzz2):
    for x in xrange (0, len(puzz1)):
        if puzz1 == puzz2:
            return True

    return False


# returns a positive integer;
# number of tiles out of place in puzz relative to the goal (global)

def puzz_eval1(puzz):
    n=0;
    for x in puzz.keys():
        if puzz[x] != goal1[x]:
            n += 1
    return n

# returns the sum of horizontal and vertical displacements of each 
# puzzle tile relative to the (global) goal state
def puzz_eval2(puzz):
    row1=0;
    row2=0;
    row3=0;
    col1=0;
    col2=0;
    col3=0;

    if puzz[(1,1)] != goal1[(1,1)] and puzz[(1,2)] != goal1[(1,2)] and [(1,3)] != goal1[(1,3)]:
        row1 = 1

    if puzz[(2,1)] != goal1[(2,1)] and [(2,2)] != goal1[(2,2)] and [(2,3)] != goal1[(2,3)]:
        row2 = 1

    if puzz[(3,1)] != goal1[(3,1)] and [(3,2)] != goal1[(3,2)] and [(3,3)] != goal1[(3,3)]:
        row3 = 1

    if puzz[(1,1)] != goal1[(1,1)] and [(2,1)] != goal1[(2,1)] and [(3,1)] != goal1[(3,1)]:
        col1 = 1

    if puzz[(1,2)] != goal1[(1,2)] and [(2,2)] != goal1[(2,2)] and [(3,2)] != goal1[(3,2)]:
        col2 = 1

    if puzz[(1,3)] != goal1[(1,3)] and [(2,3)] != goal1[(2,3)] and [(3,3)] != goal1[(3,3)]:
        col3 = 1        

    return row1 + row2 + row3 + col1 + col2 + col3

# utility function: returns  key (row,col) of item  with value val in
# the dictionary diction

def key_of(val,diction):
    for k in diction.keys():
        if diction[k] == val:
            return k
    return None
    

# returns a list of puzzle states that can be reached by a single
# move of the blank;

def puzz_successors(puzz):
    p1 = move_blank_down(puzz)
    p2 = move_blank_up(puzz)
    p3 = move_blank_left(puzz)
    p4 = move_blank_right(puzz)

    return [p for p in [p1,p2,p3,p4] if p != None]

def move_blank_down(puzz0):
    global blank_at
    puzz = puzz0.copy()   #<<<<<< IMPPORTANT!! 
    blank_at = locate_blank(puzz)
    blanktile_no = puzz[blank_at]
    brow = blank_at[0]
    bcol = blank_at[1]

    if brow >= R:
        return None

    tilebelow_no = puzz[brow+1,bcol]

    temp = blanktile_no
    puzz[(brow,bcol)] = tilebelow_no
    puzz[(brow+1,bcol)] = temp
    return puzz


def move_blank_up(puzz0):
    global blank_at
    puzz = puzz0.copy()
    blank_at = locate_blank(puzz)
    blanktile_no = puzz[blank_at]
    brow = blank_at[0]
    bcol = blank_at[1]

    if brow <= 1:
        return None

    tileabove_no = puzz[brow-1,bcol]

    temp = blanktile_no
    puzz[(brow,bcol)] = tileabove_no
    puzz[(brow-1,bcol)] = temp
    return puzz
    
def move_blank_left(puzz0):
    global blank_at
    puzz = puzz0.copy()
    blank_at = locate_blank(puzz)
    blanktile_no = puzz[blank_at]
    brow = blank_at[0]
    bcol = blank_at[1]

    if bcol <= 1:
	   return None

    tilebelow_no = puzz[brow,bcol-1]

    temp = blanktile_no
    puzz[(brow,bcol)] = tilebelow_no
    puzz[(brow,bcol-1)] = temp
    return puzz

def move_blank_right(puzz0):
    puzz = puzz0.copy()
    blank_at = locate_blank(puzz)
    blanktile_no = puzz[blank_at]
    brow = blank_at[0]
    bcol = blank_at[1]

    if bcol >= C:
		return None

    tilebelow_no = puzz[brow,bcol+1]

    temp = blanktile_no
    puzz[(brow,bcol)] = tilebelow_no
    puzz[(brow,bcol+1)] = temp
    return puzz
    
    
    
# test all functions by loading them into idle and make functions calls
# that will demonstrate that correctness of the code; 

# mode = 1 -- sort by length of path (= depth of node); uniform-cost search
# mode = 2 -- sort by evalfct; best-first search
# mode = 3 -- sort by depth + evalfct; A* if evalfct is "admissible"

# print_info = 0 (default) -- minimal printing of info
# print_info = 1 -- 0 + prints current state as come from open
# print_info = 2 -- 1 + prints contents of open_lst

def graphsearch(start,mode,puzz_eval,print_info = 0):
    open_lst = [[[start],start]]
    closed_lst = []
    count = 1
    pathcount = 0
    nodecount = 0
    while open_lst != [] and nodecount < MAXNODES:
        curr0 = open_lst[0]
        curr = curr0[1]
        pth = curr0[0]
        open_lst = open_lst[1:]
        closed_lst.append(curr0)
        nodecount += 1  # count node about to be expanded

        #if curr in goals:
        if puzz_equal(curr,goal):
            if print_info > 0:
                print "\n\nGoal found with path of length %d and node cost %d\n" % (len(pth),nodecount) 
                prp(curr)

                print "\nThe Path:"
                print_path(pth,puzz_eval,mode)
                
            return (pth,nodecount)

        if print_info > 1:
            if mode == 1:
                print "[step-%d] %s  <%d>" % (count, curr, len(pth)-1)
            elif mode == 2:
                print "[step-%d] %s  <%d>" % (count, curr, puzz_eval(curr))
            else:
                print "[step-%d] %s  <%d+%d>" % (count, curr, len(pth)-1, puzz_eval(curr))
            prp(curr)

        succ = puzz_successors(curr)
        for  s in succ:
            if no_cycle(pth,s) and\
               not_on_lst(open_lst,s) and\
               not_on_lst(closed_lst,s):
                newpth = pth[:] + [s]
                open_lst.append([newpth,s])

        random.shuffle(open_lst)
        # sort open_lst according to mode
        if mode == 1:
            open_lst.sort(key = lambda x: len(x[0])-1)
        elif mode == 2:
            open_lst.sort(key = lambda x: puzz_eval(x[1]))
        else:
            open_lst.sort(key = lambda x: len(x[0])-1+puzz_eval(x[1]))
        
        if print_info > 2:
            print "[open-%d]" % count
            for x in open_lst:
                if mode == 1:
                    print "%s -- %d" % (x[1], len(x[0])-1)
                elif mode == 2:
                    print "%s -- %d" % (x[1], puzz_eval(x[1]))
                else:
                    print "%s -- %d" % (x[1],len(x[0])-1+puzz_eval(x[1]))
            
        count += 1

    if print_info > 0:
        if nodecount >= MAXNODES:
            print "\n\nSearch exceeds maximum of %d nodes" % MAXNODES
        else:
            print "\n\nUnsolvable problem!"
            
    return ([], nodecount)

def no_cycle(path, x):
    for y in path:
        if puzz_equal(x,y):
            return False
    return True

# lst is list of [pth,state], s is state that should not be on lst
def not_on_lst(lst,s):
    for x in lst:
        if puzz_equal(x[1],s):
            return False
    return True

def print_path(pth, evalf, mode):
    for i in range(len(pth)):
        if mode == 1:
            print "           <%d>" % i
        elif mode == 2:
            print "           <%d>" % evalf(pth[i])
        else:
            print "           <%d+%d>" % (i,evalf(pth[i]))
        prp(pth[i])
    print "\n\n"
    


start = None
goal = None

# runs all modes of graphsearch for a given problem (start and goal state
# combination, and give evalfct); get more or less info printed
# allows for comparison of each mode;

def allgs(st,gl,evalf, info = 0):
    global start
    global goal
    start = st
    goal = gl
    p1,n1 = graphsearch(start,1,evalf)
    p2,n2 = graphsearch(start,2,evalf)
    p3,n3 = graphsearch(start,3,evalf)

    if info == 1:
        print "uniform: %d,  %d" % (len(p1),n1)
        print "best1st: %d,  %d" % (len(p2),n2)
        print "a*-srch: %d,  %d\n" % (len(p3),n3)

    return ((len(p1),n1),(len(p2),n2), (len(p3),n3))

# do k runs of allgs; outpu averages, min and max for solution path
# lengths and search-cost in terms of number of nodes expanded

def allgs_runs(st,gl, evalf,k):
    sump1 = 0
    sumn1 = 0
    sump2 = 0
    sumn2 = 0
    sump3 = 0
    sumn3 = 0

    minp1 = 10000
    maxp1 = -1
    minn1 = 10000
    maxn1 = -1

    minp2 = 10000
    maxp2 = -1
    minn2 = 10000
    maxn2 = -1

    minp3 = 10000
    maxp3 = -1
    minn3 = 10000
    maxn3 = -1
    
    for i in range(k):
        ((p1,n1),(p2,n2), (p3,n3)) = allgs(st,gl,evalf)

        if p1 < minp1:
            minp1= p1
        elif p1 > maxp1:
            maxp1 = p1

        if n1 < minn1:
            minn1= n1
        elif n1 > maxn1:
            maxn1 = n1

        if p2 < minp2:
            minp2= p2
        elif p2 > maxp2:
            maxp2 = p2

        if n2 < minn2:
            minn2  = n2
        elif n2 > maxn2:
            maxn2 = n2

        if p3 < minp3:
            minp3= p3
        elif p3 > maxp3:
            maxp3 = p3

        if n3 < minn3:
            minn3= n3
        elif n3 > maxn3:
            maxn3 = n3
            
        sump1 += p1
        sumn1 += n1
        sump2 += p2
        sumn2 += n2
        sump3 += p3
        sumn3 += n3

    print "\n\n"
    print "average p1,n1: %d,  %d   min p1,n1: %d,  %d   max p1,n2: %d   %d" %\
          (float(sump1)/k, float(sumn1)/k, minp1,minn1, maxp1,maxn1)
    print "average p2,n2: %d,  %d   min p1,n1: %d,  %d   max p1,n2: %d   %d" %\
          (float(sump2)/k, float(sumn2)/k, minp2,minn2, maxp2,maxn2)
    print "average p3,n3: %d,  %d   min p1,n1: %d,  %d   max p1,n2: %d   %d" %\
          (float(sump3)/k, float(sumn3)/k, minp3,minn3, maxp3,maxn3)
    return






    




        






        







    
    






    
