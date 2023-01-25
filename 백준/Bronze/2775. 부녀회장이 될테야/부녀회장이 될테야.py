t = int(input())

for i in range(t):
    f = int(input())        
    r = int(input())        
    people = [i for i in range(1, r+1)]  

    for x in range(f):
        new = []
        for y in range(r):
            new.append(sum(people[:y+1]))   
        people = new.copy()

    print(people[-1])