def ShuntingYard(eq):
    equation=eq.split()
    operator,output=[],[]
    
    for token in equation:
        if (token in precedence):                                       #This would mean it is an operator
            if(token=='('):
                operator.append(token)
            elif(token==')'):
                while(operator[-1]!= '('):
                    output.append(operator.pop())
                operator.pop()
            elif (len(operator)==0): 
                operator.append(token)
            elif(precedence[token]>precedence[operator[-1]]):
                operator.append(token)
            elif (token==operator[-1]):
                operator.append(token)
            elif(precedence[token] <= precedence[operator[-1]]):
                while (precedence[token] <= precedence[operator[-1]]):
                    if (operator[-1]=='('):
                        break
                    else:
                        output.append(operator.pop())
                    if (len(operator)==0): break
                operator.append(token)
                
        else:                                                           #This would mean it is a token
            output.append(token)
    return output+operator[::-1]


def RPN(infix):
    stck=[]
    infix=infix[::-1]
    while(len(infix)>0):
        ipop=infix.pop()
        if (ipop in precedence):
            if (ipop=='-'):
                stck.append((-float(stck.pop()))+float(stck.pop()))
            elif (ipop=='+'):
                stck.append(float(stck.pop())+float(stck.pop()))
            elif (ipop=='*'):
                stck.append(float(stck.pop())*float(stck.pop()))
            elif (ipop=='/'):
                stck.append((1/float(stck.pop()))*float(stck.pop()))
            elif (ipop=='^'):
                power=float(stck.pop())
                stck.append(float(stck.pop())**power)   
        else:
            stck.append(ipop)
    return (stck.pop())


######Main######

eqn='3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'                                     # <-- Eqn used on Wikipedia

precedence={'-':2,'+':2,'/':3,'*':3,'^':4,'(':10,')':10}

print (RPN(ShuntingYard(eqn)))
    
        
    
