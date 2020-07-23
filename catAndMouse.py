#https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse(x, y, z):
    x_count = 0
    y_count =0
    for i in range(100):
        if(x<z and x != z):
            x+=1
            x_count += 1
        if(y<z and y != z):
            y+=1
            y_count += 1
        if(x>z and x != z):
            x-=1
            x_count += 1
        if(y>z and y != z):
            y-=1
            y_count += 1
        
    if(x_count>y_count):
        result = 'Cat B'
    if(y_count>x_count):
        result ='Cat A'
    if(x_count==y_count):
        result ='Mouse C'
    
    return result

catAndMouse(1, 2, 3)
catAndMouse(1, 3, 2)
