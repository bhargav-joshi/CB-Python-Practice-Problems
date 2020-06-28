cum = 0
list_of_ele = []
while cum >= 0:
    a = int(input())
    cum+=a
    if cum>=0:
        list_of_ele.append(a)
    else:
        break
for x in list_of_ele:
	print(x)
