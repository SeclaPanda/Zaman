numbers = input()
sumpr = 0
sumnpr = 0 
while numbers != 'stop':
	numbers1 = int(numbers)
	numbers2 = int(numbers)
	if numbers1 == 0:
		num3 = numbers1 + numbers2
	elif numbers1 < 0:
		print('Number is negative.')
	else:
		cou = 0
		for a in range(1, numbers1):
			if numbers1 % a == 0:
				cou += 1
			else:
				continue
		if cou == 2:
			sumpr += numbers1
		else:
			sumnpr += numbers1
	numbers = input()	
if (sumnpr > 100):
	sumnpr = sumnpr / 2
	sumpr = sumnpr		
print(f'Sum of all prime numbers is: {int(sumnpr)}')
print(f'Sum of all non prime numbers is: {int(sumpr)}') 