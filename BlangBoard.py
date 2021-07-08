######## Getting Data ########

print ("Welcome to BlangBoard Programming Language Compiler")
print ("Please enter the codes after *--->* sign and Write *end;* to compile and run")
big_list = []
while True :
    put = input ("---> ")
    big_list.append(str(put).split())
    if (put == "end;") :
        big_list = big_list[:-1]
        break

######### Lexer ########
                
math_operators = ['+' , '-' , '*' , '/']
string_operators = ['write:']
token_list =[]
for i in range (len(big_list)) :
    for j in range (len(big_list[i])) :
        if big_list[i][j] in math_operators :
            Token = (i, "ALGEBRA")
            token_list.append(Token)
            if (i,"INVALID") in token_list :
                token_list.remove((i,"INVALID"))
            break
        elif big_list[i][j] in string_operators :
            Token = (i, "TEXT")
            token_list.append(Token)
            if (i,"INVALID") in token_list :
                token_list.remove((i,"INVALID"))
            break
        else :
            Token = (i, "INVALID")
            token_list.append(Token)

######### Parser #########

result_list = []

for x in range (len(token_list)) :
    if token_list[x][1] == "TEXT" :
        res = " ".join(big_list[x][1:])
        result_list.append((x,res))
    elif token_list[x][1] == "ALGEBRA" :
        if big_list[x][1] == "+" :
            plus = int(big_list[x][0])+int(big_list[x][2])
            result_list.append((x,plus))
        if big_list[x][1] == "-" :
            minus = int(big_list[x][0])-int(big_list[x][2])
            result_list.append((x,minus))
        if big_list[x][1] == "*" :
            cross = int(big_list[x][0])*int(big_list[x][2])
            result_list.append((x,cross))        
        if big_list[x][1] == "/" :
            division = int(big_list[x][0])/int(big_list[x][2])
            result_list.append((x,division))
    else :
        result_list.append("ERROR")

############ Code Generator ################
if "ERROR" in result_list :
    print ("Cannot compile !!! Correct the code and run again !")
else :
    for something in result_list :
        print (something[1])

