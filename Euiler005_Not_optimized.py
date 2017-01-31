keyval = True
regi = 2520
#judge = []
factor = [16, 9, 5 ,7, 11, 13, 17, 19]

while keyval == True:
    regi = regi + 1
    judge = []
    for i in factor:
        # tmp_memory = []
        #judge = []
        if regi % i == 0:
            judge.append(0)
        elif regi % i != 0:
            break
        print regi
    if len(judge) == 8:
        keyval = False
        print("[[[[" + str(regi) + "]]]]")



