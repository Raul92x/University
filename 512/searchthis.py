# searchthis.py
# example graph ("net") for demonstrations of traversal and searching;

net = {(20,20):[(460,20),(20,180)], (460,20):[(460,460)], (20,180):[(20,340),(160,180)],\
       (20,340):[(160,340)], (160,180):[(160,100),(160,340)], (160,100):[(320,100)],\
       (320,100):[(320,340)], (160,340):[(320,340),(160,440)], (160,440):[(80,440),(260,440)],\
       (320,340):[(380,340),(320,460)],(380,340):[(380,220),(380,460)], (380,460):[(460,460)],\
       (320,460):[(380,460)]}

                                                                  
start = (20,20)
goal = (460,460)

def traverse_net(start,net,mode="bfs"):
    open_lst = [start]
    closed_lst = []

    count = 1
    while open_lst != []:
        curr = open_lst[0]
        open_lst = open_lst[1:]
        if not curr in closed_lst:
            closed_lst.append(curr)
        print "[step-%d] %s\n" % (count, curr)
        if net.has_key(curr):
            succ = net[curr]
            for  s in succ:
                if not s in open_lst and not s in closed_lst:
                    if mode == "bfs":
                        open_lst.append(s)
                    elif mode == "dfs":
                        open_lst = [s] + open_lst
        print "[open-%d] %s" % (count, open_lst)
        print "[clos-%d] %s\n" % (count, closed_lst)
        count += 1
