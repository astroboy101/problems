x=list(map(int,input('enter the values').split()))
req=int(input('enter the required values'))
x_leng=len(x)

def backtrack_sol(x,req,x_leng,li=[],x_value=0,value=0):
    if req==value:
        print(li,"---------")
        return 'break'
    elif req<value:
        return None
    else:
        value=value+x_value;
        li.append(x_value)
        for i in x:
            k=li.copy()
            k1=backtrack_sol(x,req,x_leng,li,i,value)
            li=k
            if k1=='break':
                break
            
            
backtrack_sol(x,req,x_leng)
        
