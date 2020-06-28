prev = float('inf')
n = int(input())
dec = True
ans = "true"
for i in range(n):
	m = int(input())
	
	if ans=="false":
		break
	
	
	if dec:
		if m>=prev:
			dec = False
	else:
		if m<=prev:
			ans = "false"
	prev = m
print(ans)
