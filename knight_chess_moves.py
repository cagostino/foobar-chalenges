def solution(src, dest):
    x1 = src % 8
    x2 = dest % 8
    y1 = src // 8
    y2 = dest // 8
    if src==dest:
        return 0
    num = getanswers(x1,x2,y1,y2)
    if num is not None:
        return num
    nstep = 0
    mvs_x, mvs_y = getmoves(x1,y1)
    lowest_scores=[]
    while len(lowest_scores) ==0:
        nstep+=1
        for i in range(len(mvs_x)):
            num = getanswers(mvs_x[i], x2, mvs_y[i], y2)
            if num:
                lowest_scores.append(nstep+num)  
        updated_x = []
        updated_y = []
        for i in range(len(mvs_x)):
            newx_, newy_ =getmoves(mvs_x[i], mvs_y[i])
            updated_x.extend(newx_)
            updated_y.extend(newy_)            
        mvs_x = updated_x
        mvs_y = updated_y
    return min(lowest_scores)
def getmoves(x1,y1):
    newsrc_mvs = [[1,2], [-1,2],[1,-2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]    
    mvs_x = []
    mvs_y = []
    for i in newsrc_mvs:
        newx_ = x1+i[0]
        newy_ = y1+i[1] 
        if newx_>=0 and newx_<=7 and newy_ >=0 and newy_<=7:                             
            mvs_x.append(newx_)
            mvs_y.append(newy_)
    return mvs_x, mvs_y                    
def getanswers(x1,x2,y1,y2):
    maxdiff = max(abs(x1-x2), abs(y1-y2))
    n2 = maxdiff //2
    nremain = maxdiff % 2
    if (x1 == x2) or (y1==y2):
        if n2 >=3:
            if nremain==0:
                return 4
            elif nremain==1:
                return 5
        else:
            if nremain == 0:    
                return 2
            else:
                return 3        
    if abs(x1-x2)==abs(y1-y2):
        if (abs(x1-x2)==2) or ((abs(x1-x2)==1) and ( (x1==0 and y1==0) or (x1==0 and y1==7) or (x1==7 and y1==7) or (x1==7 and y1==0))):
            return 4
        else:
            return int(2*((abs(y2-y1)+2)/3))
      
    elif (abs(x1-x2) ==1 and abs(y1-y2)==2) or (abs(y1-y2)==1 and abs(x1-x2)==2):
        return 1
