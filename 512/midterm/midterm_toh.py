# midterm_toh.py
# Kerstin Voigt, Nov 2014; to be used for CSE 512 midterm;

import copy
import random

# some global variables ...
MAXNODES = 10000

# MIDTERM (possibly having something to do with
# the size of the toh problem) 

TOH = 5
TOHTW = range(TOH+1)[1:]
TOHTW.reverse()

# do not change
def init_toh():
	toh = {'a':TOHTW, 'b':[], 'c':[]}
	return toh

# do not change
def toh_equal(toh1,toh2):
	for k in toh1.keys():
		if toh1[k] != toh2[k]:
			return False
	return True

# MIDTERM: return True if the tower in the initial state (on peg 'a')
# appears on peg 'c', and peb 'b' is empty; return False otherwise;

def toh_solved(toh):
	for x in toh.keys():
		if (toh.get('c')==TOHTW and toh.get('b')==[]):
			return True
	return False
	


# MIDTERM: a use function; given state toh, move the top disk from peg 'frm' to
# peg 'to'; return value None if either moving a disk from peg 'frm' makes no
# sense, or moving it to peg 'to' is not allowed; otherwise compute and return
# the toh state;

def move_disk(toh, frm, to):
	if toh[frm] == [] or toh[to] != [] and toh[frm][-1] > toh[to][-1]:
		return None
	else:
		disk = toh[frm][-1]
		toh[frm] = toh[frm][:-1]
		toh[to].append(disk)
		return toh

# MIDTERM: compute all possible immediate successor states of state toh;
# return a list of next possible states;

def toh_successors(toh):
	p1 = toh_check_ab(toh)
	p2 = toh_check_ac(toh)
	p3 = toh_check_ba(toh)
	p4 = toh_check_bc(toh)
	p5 = toh_check_ca(toh)
	p6 = toh_check_cb(toh)

	return [p for p in [p1,p2,p3,p4,p5,p6] if p != None]

def toh_check_ab(toh0):
	toh = copy.deepcopy(toh0)
	if toh['a'] == [] or toh['b'] != [] and toh['a'][-1] > toh['b'][-1]:
		return None
	else:
		if toh['b'] == [] and toh['a'] != [] and toh['a'[-1]] > toh['b'[-1]]:
			return move_disk(toh, 'a', 'b')
		elif toh['b'] != [] and toh['a'] != [] and toh['a'[-1]] < toh['b'[-1]]:
			return move_disk(toh, 'a', 'b')
		else:
			return False
			
def toh_check_ac(toh0):	
	toh = copy.deepcopy(toh0)		
	if toh['a'] == [] or toh['c'] != [] and toh['a'][-1] > toh['c'][-1]:
		return None
	else:
		if toh['c'] == [] and toh['a'] != [] and toh['a'[-1]] > toh['c'[-1]]:
			return move_disk(toh, 'a', 'c')
		elif toh['c'] != [] and toh['a'] != [] and toh['a'[-1]] < toh['c'[-1]]:
			return move_disk(toh, 'a', 'c')
		else:
			return False

def toh_check_ba(toh0):
	toh = copy.deepcopy(toh0)
	if toh['b'] == [] or toh['a'] != [] and toh['b'][-1] > toh['a'][-1]:
		return None
	else:
		if toh['a'] == [] and toh['b'] != [] and toh['b'[-1]] > toh['a'[-1]]:
			return move_disk(toh, 'b', 'a')
		elif toh['a'] != [] and toh['b'] != [] and toh['b'[-1]] < toh['a'[-1]]:
			return move_disk(toh, 'b', 'a')
		else:
			return False
			
def toh_check_bc(toh0):	
	toh = copy.deepcopy(toh0)		
	if toh['b'] == [] or toh['c'] != [] and toh['b'][-1] > toh['c'][-1]:
		return None
	else:
		if toh['c'] == [] and toh['b'] != [] and toh['b'[-1]] > toh['c'[-1]]:
			return move_disk(toh, 'b', 'c')
		elif toh['c'] != [] and toh['b'] != [] and toh['b'[-1]] < toh['c'[-1]]:
			return move_disk(toh, 'b', 'c')
		else:
			return False
			
def toh_check_ca(toh0):
	toh = copy.deepcopy(toh0)
	if toh['c'] == [] or toh['a'] != [] and toh['c'][-1] > toh['a'][-1]:
		return None
	else:
		if toh['a'] == [] and toh['c'] != [] and toh['c'[-1]] > toh['a'[-1]]:
			return move_disk(toh, 'c', 'a')
		elif toh['a'] != [] and toh['c'] != [] and toh['c'[-1]] < toh['a'[-1]]:
			return move_disk(toh, 'c', 'a')
		else:
			return False
			
def toh_check_cb(toh0):	
	toh = copy.deepcopy(toh0)		
	if toh['c'] == [] or toh['b'] != [] and toh['c'][-1] > toh['b'][-1]:
		return None
	else:
		if toh['b'] == [] and toh['c'] != [] and toh['c'[-1]] > toh['b'[-1]]:
			return move_disk(toh, 'c', 'b')
		elif toh['b'] != [] and toh['c'] != [] and toh['c'[-1]] < toh['b'[-1]]:
			return move_disk(toh, 'c', 'b')
		else:
			return False
		
# ... complete here ... 

# do not change
def toh_print(toh):
	pegs = toh.keys()
	pegs.sort()
	for k in pegs:
		print "%s |-" % k,
		for x in toh[k]:
			print x,
		print "  ",
	print "\n"

# MIDTERM: the evaluation function for toh; return the difference in height
# beteeen the given tower on peg 'c' in state toh and the height of the tower
# in the goal state; hint: check out info provided in the global variables
# above;

def toh_eval(toh):
	goal = TOH
	return (goal-len(toh['c']))

# MIDTERM: DO NOT MAKE CHANGES TO ANY OF THE GRAPHSEARCH RELATED FUNTIONS.


# test all functions by loading them into idle and make functions calls
# that will demonstrate that correctness of the code; 

# mode = 1 -- sort by length of path (= depth of node); uniform-cost search
# mode = 2 -- sort by evalfct; best-first search
# mode = 3 -- sort by depth + evalfct; A* if evalfct is "admissible"

# print_info = 0 (default) -- minimal printing of info
# print_info = 1 -- 0 + prints current state as come from open
# print_info = 2 -- 1 + prints contents of open_lst

def graphsearch(start,mode, equal_fct, solved_fct, eval_fct, succ_fct,\
				print_fct, print_info = 0):
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

		if solved_fct(curr):
			if print_info > 0:
				print "\n\nGoal found with path of length %d and node cost %d\n" % (len(pth),nodecount) 
				print_fct(curr)

				print "\nThe Path:"
				print_path(pth,eval_fct,mode,print_fct)

			return (pth,nodecount)

		if print_info > 1:
			if mode == 1:
				print "[step-%d] %s  <%d>" % (count, curr, len(pth)-1)
			elif mode == 2:
				print "[step-%d] %s  <%d>" % (count, curr, eval_fct(curr))
			else:
				print "[step-%d] %s  <%d+%d>" % (count, curr, len(pth)-1, eval_fct(curr))
			print_fct(curr)

		succ = succ_fct(curr)
		for  s in succ:
			if no_cycle(pth,s,equal_fct) and\
			   not_on_lst(open_lst,s,equal_fct) and\
			   not_on_lst(closed_lst,s,equal_fct):
				newpth = pth[:] + [s]
				open_lst.append([newpth,s])

		random.shuffle(open_lst)
		# sort open_lst according to mode
		if mode == 1:
			open_lst.sort(key = lambda x: len(x[0])-1)
		elif mode == 2:
			open_lst.sort(key = lambda x: eval_fct(x[1]))
		else:
			open_lst.sort(key = lambda x: len(x[0])-1+eval_fct(x[1]))
		
		if print_info > 2:
			print "[open-%d]" % count
			for x in open_lst:
				if mode == 1:
					print "%s -- %d" % (x[1], len(x[0])-1)
				elif mode == 2:
					print "%s -- %d" % (x[1], eval_fct(x[1]))
				else:
					print "%s -- %d" % (x[1],len(x[0])-1+eval_fct(x[1]))
			
		count += 1

	if print_info > 0:
		if nodecount >= MAXNODES:
			print "\n\nSearch exceeds maximum of %d nodes" % MAXNODES
		else:
			print "\n\nUnsolvable problem!"
			
	return ([], nodecount)


def no_cycle(path, x, equal_fct):
	for y in path:
		if equal_fct(x,y):
			return False
	return True

# lst is list of [pth,state], s is state that should not be on lst
def not_on_lst(lst,s,equal_fct):
	for x in lst:
		if equal_fct(x[1],s):
			return False
	return True


def print_path(pth, evalf, mode, print_fct):
	for i in range(len(pth)):
		if mode == 1:
			print "                            <%d>" % i
		elif mode == 2:
			print "                            <%d>" % evalf(pth[i])
		else:
			print "                            <%d+%d>" % (i,evalf(pth[i]))
		print_fct(pth[i])
	print "\n\n"




# MIDTERM TEST RUN ... DO NOT MODIFY
# you may comment these out while  debugging; make sure you uncomment later
# for test runs;

#mytoh = init_toh()

#graphsearch(mytoh, 3, toh_equal, toh_solved, toh_eval, toh_successors,\
#			toh_print, print_info = 1)





