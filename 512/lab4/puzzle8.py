#Raul Diaz
#lab4

# puzzle8.py

#starting state from Nils Nilson, p. 140

start = { (1,1):2, (1,2):8, (1,3):3, (2,1):1, (2,2):'B', (2,3):4, \
			 (3,1):7, (3,2):6, (3,3):5}\

# what is your goal state?
goal = { (1,1):1, (1,2):2, (1,3):3, (2,1):8, (2,2):'B', (2,3):4, \
			 (3,1):7, (3,2):6, (3,3):5}\

blank_at = (2,2)

def print_puzz8 (puzz):
	print "\n"
	for i in range(3):
		for j in range(3):
			print "%s " % puzz[(i+1,j+1)],
		print "\n"
	print "\n"
    
# return (row,col) of location of blank in puzzle puzz
def locate_blank(puzz):
    for k in puzz.keys():
        if puzz[k] == 'B':
            return k
    return (-1,-1)

# returns True or False if start = goal
def puzz8_equal(puzz1, puzz2):
    for x in xrange (0, len(puzz1)):
        if puzz1 == puzz2:
            return True
    return False

# returns a positive integer;
#number of tiles out of place in puzz relative to the goal (global)
def puzz8_eva1(puzz):
    n=0;
    for x in puzz.keys():
        if puzz[x] != goal[x]:
            n += 1
    return n

# returns a list of puzzle states that can be reached by a single
# move of the blank;
def puzz8_successors(puzz):
    p1 = move_blank_down(puzz)
    p2 = move_blank_up(puzz)
    p3 = move_blank_left(puzz)
    p4 = move_blank_right(puzz)

    return [p for p in [p1,p2,p3,p4] if p != None]


def move_blank_down(puzz0):
	global blank_at
	puzz = puzz0.copy()
	blank_at = locate_blank(puzz)
	blanktile_no = puzz[blank_at]
	brow = blank_at[0]
	bcol = blank_at[1]

	if brow >= 3:
		return None

	tilebelow_no = puzz[brow+1,bcol]

	temp = blanktile_no
	puzz[(brow,bcol)] = tilebelow_no
	puzz[(brow+1,bcol)] = temp

	blank_at = (brow+1,bcol)
	return print_puzz8 (puzz)

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
    return print_puzz8 (puzz)
    
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
    return print_puzz8 (puzz)
	
def move_blank_right(puzz0):
    puzz = puzz0.copy()
    blank_at = locate_blank(puzz)
    blanktile_no = puzz[blank_at]
    brow = blank_at[0]
    bcol = blank_at[1]

    if bcol >= 3:
		return None

    tilebelow_no = puzz[brow,bcol+1]

    temp = blanktile_no
    puzz[(brow,bcol)] = tilebelow_no
    puzz[(brow,bcol+1)] = temp
    return print_puzz8 (puzz)
