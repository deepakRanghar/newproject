equation=list(input())
demo=list(equation)
a=len(equation)
i=j=x=D=c=0


for i in range(i,a):
    if equation[i]>="a" and equation[i]<="z":
        print(equation[i])
        equation[i]=int(input())
        equation[i-D]=int(equation[i-1])*equation[i]
        D-=1
    D+=1
while j<a:
    if demo[j]=="("
        c+=j+1
        for c in range(c,a):
    elif demo[j]=="/":
        x+=1
        equation[0]=float(equation[0]/equation[x])
        print(equation)
    elif demo[j]=="*":
        x+=1
        equation[0]=equation[0]*equation[x]
        print(equation)
    elif demo[j]=="+":
        x+=1
        equation[0]=equation[0]+equation[x]
        print(equation)
    elif demo[j]=="-":
        x+=1
        equation[0]=equation[0]-equation[x]
        print(equation)
    
   
    j+=1      
            
