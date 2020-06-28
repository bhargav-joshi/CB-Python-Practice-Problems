rows = input()
rows = int (rows)

for i in range (rows,0,-1):
    for j in range(1, i + 1):
        print(j, end=' ')
    n_of_stars = 2* ( rows-i) - 1 
    for j in range(1,n_of_stars+1):
        print("*",end = ' ')
    print()
