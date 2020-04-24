n = int(input())
sum = []
mat = 2 * n
par = [int(input()) for i in range(mat)]
for i in range(0, mat, 2):
	sum.append(par[i] + par[i+1])
prof = [sum[0]] * len(sum)
if prof == sum:
	print ("Yes, value=" + str(sum[0]))
else:
	for i in range(len(sum)-1):
		dif = -(sum[i] - sum[i+1])
	if dif < 0:
		dif  = -dif
	print ("No, maxdiff=" + str(dif))