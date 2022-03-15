n = int(input("Enter N x N Matrix: "))
ball_position = n//2
# MATRIX CREATION 
dp = [[" "]*n for i in range(n)]
for row in range(n):
    for col in range(n):
        if row == 0 :
            dp[row][col] = "W"
        elif row == n-1 :
            dp[row][col] = "G"
    dp[row][-1] = "W"
    dp[row][0]  = "W"
dp[-1][ball_position] = "O"
# MATRIX PRINTING & CHECKING
def matrix_check(dp,n):
    global c
    c = 0
    for row in range(n):
        print(*dp[row])
        if row != 0 and row != n-1:
            if "".join(dp[row][1:n-1]).strip() == "":
                pass
            else:
                c = 1 
    if c == 0 :
        print(" "*35,"==== * HURRAY * ====")
# DE FUNCTION       
def DE(dp,n,row):
    dp[-row] = [" "]*n
    dp[-row][0] = dp[-row][-1] = "W"   
# DS FUNCTION
def DS(dp,n,row):
    # UPPER ROW
    if dp[-row-1][ball_position] != "W":
        dp[-row-1][ball_position] = " "
    if dp[-row-1][ball_position+1] != "W":
        dp[-row-1][ball_position+1] = " "
    if dp[-row-1][ball_position-1] != "W":
        dp[-row-1][ball_position-1] = " "
    # DOWN ROW
    if dp[-row+1][ball_position] not in "WO_G":
        dp[-row+1][ball_position] = " "
    if dp[-row+1][ball_position+1] not in "WO_G":
        dp[-row+1][ball_position+1] = " "
    if dp[-row+1][ball_position-1] not in "WO_G":
        dp[-row+1][ball_position-1] = " "
    # CURRENT ROW
    if dp[-row][ball_position] != "W":
        dp[-row][ball_position] = " "
    if dp[-row][ball_position+1] != "W":
        dp[-row][ball_position+1] = " "
    if dp[-row][ball_position-1] != "W":
        dp[-row][ball_position-1] = " "
#B FUNCTION
def B(dp,n):
    if dp[-1][ball_position:n].count("_") == dp[-1][:ball_position].count("_"):
        for i in range(ball_position+1,n-1):
            if dp[-1][i] != "_":
                dp[-1][i] = "_"
                break
    else:
        for j in range(ball_position-1,0,-1):
            if dp[-1][j] != "_":
                dp[-1][j] = "_"
                break
l = list(map(str,input("Enter the brick's position and the brick type: ").split()))
if (int(l[0]) in range(1,n-1) and int(l[1]) in range(1,n-1)):
    dp[int(l[0])][int(l[1])] = l[2]
else:
    print(" "*10,"WRONG INPUT :- ENTER THE INDEX VALUES IN RANGE OF 1 TO",n-2)
while True:
    value = input("Do you want to continue Y/N: ")
    if value == "Y":
        l = list(map(str,input("Enter the brick's position and the brick type: ").split()))
        if (int(l[0]) in range(1,n)and int(l[1]) in range(1,n)):
            dp[int(l[0])][int(l[1])] = l[2]
        else:
            print(" "*10,"WRONG INPUT :- ENTER THE INDEX VALUES IN RANGE OF 1 TO",n-1)
    elif value != "N":
        print(" "*10,"OPTION ERROR :- CHOOSE CORRECT OPTION")
    elif value == "N":
        ball_count = int(input("Enter The Ball Count: "))
        for i in range(n):
            print(*dp[i])
        break
print("Ball Count",ball_count)
while True:
    if ball_count == 0:
        print(" "*35,"==== * GAME OVER * ====")
        break
    else:
        direction = input("Enter the Direction: ")
        if direction not in "ST,st,LD,ld,RD,rd":
            print("Select Valid Options ST/st , LD/ld , RD/rd")
        # STRAIGHT TRAVERSAL
        if direction in "ST,st":
            for row in range(2,n+1):
                if dp[-row][ball_position] not in " W":
                    if dp[-row][ball_position] == "1" :
                       dp[-row][ball_position] = " " 
                       break
                    elif dp[-row][ball_position] == "DS":
                        DS(dp,n,row)
                        break
                    elif dp[-row][ball_position] == "DE":
                        DE(dp,n,row)
                        break
                    elif dp[-row][ball_position] == "B":
                        dp[-row][ball_position] = " "
                        B(dp,n) 
                        break
                    else:
                        dp[-row][ball_position] = str(int(dp[-row][ball_position]) - 1) 
                        break
            matrix_check(dp,n)
            if c == 0:
                break
            print("Ball count",ball_count)
        # LEFT TRAVERSAL
        elif direction in "LD,ld":
            hor = -n
            for ldia in range(2,(n//2)+2):
                if dp[-ldia][ball_position-(ldia-1)] != " ":
                    if dp[-ldia][ball_position-(ldia-1)] == "1":
                        dp[-ldia][ball_position-(ldia-1)] = " "
                        break
                    elif dp[-ldia][ball_position-(ldia-1)] == "DE":
                        DE(dp,n,ldia)
                        break
                    elif dp[-ldia][ball_position-(ldia-1)] == "DS":
                        DS(dp,n,ldia)
                        break
                    elif dp[-ldia][ball_position-(ldia-1)] == "B":
                        dp[-ldia][ball_position-(ldia-1)] = " "
                        B(dp,n)
                        break
                    # HITTING WALL
                    elif dp[-ldia][ball_position-(ldia-1)] == "W":
                        for hor in range(1,n):
                            if dp[-ldia][hor] != " ":
                                if dp[-ldia][hor] == "1":
                                    dp[-ldia][hor] = " "
                                    break
                                elif dp[-ldia][hor] == "DE":
                                    DE(dp,n,ldia)
                                    break
                                elif dp[-ldia][hor] == "DS":
                                    DS(dp,n,ldia)
                                    break
                                elif dp[-ldia][hor] == "B":
                                    dp[-ldia][hor] = " "
                                    B(dp,n)
                                    break
                                elif dp[-ldia][hor] == "W":
                                    break
                                else:
                                    dp[-ldia][hor] = str(int(dp[-ldia][hor])-1)
                                    break
                    else:
                        dp[-ldia][ball_position-(ldia-1)] = str(int(dp[-ldia][ball_position-(ldia-1)])-1)
                        break
            matrix_check(dp,n)
            if c == 0:
                break
            if dp[-1][max(ball_position-(ldia-1),hor)] != "_":
                ball_count -= 1
            print("Ball Count",ball_count)

        #RIGHT TRAVERSAL
        elif direction in "RD,rd":
            i = 1 ; hor = -n
            for rdia in range(2,(n//2)+2):
                if dp[-rdia][ball_position+i] == " ":
                    i += 1
                elif dp[-rdia][ball_position+i] == "1":
                    dp[-rdia][ball_position+i] = " "
                    break
                elif dp[-rdia][ball_position+i] == "DE":
                    DE(dp,n,rdia)
                    break
                elif dp[-rdia][ball_position+i] == "DS":
                    DS(dp,n,rdia)
                    break
                elif dp[-rdia][ball_position+i] == "B":
                    dp[-rdia][ball_position+i] = " "
                    B(dp,n)
                    break
                # HITTING WALL
                elif dp[-rdia][ball_position+i] == "W":
                    for hor in range(2,n):
                        if dp[-rdia][-hor] != " ":
                            if dp[-rdia][-hor] == "1":
                                dp[-rdia][-hor] = " "
                                break
                            elif dp[-rdia][-hor] == "DE":
                                DE(dp,n,rdia)
                                break
                            elif dp[-rdia][-hor] == "DS":
                                DS(dp,n,rdia)
                                break
                            elif dp[-rdia][-hor] == "B":
                                dp[-rdia][-hor] = " "
                                B(dp,n)
                                break
                            elif dp[-rdia][-hor] == "W":
                                break
                            else:
                                dp[-rdia][-hor] = str(int(dp[-rdia][-hor])-1)
                                break
                else:
                    dp[-rdia][ball_position+i] = str(int(dp[-rdia][ball_position+i])-1)
                    break
            matrix_check(dp,n)
            if c == 0:
                break
            if dp[-1][min(ball_position+i,-hor)] != "_":
                ball_count -= 1
            print("Ball Count",ball_count)
            

                            
