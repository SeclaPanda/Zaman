country = str(input())
while country != "End":	
	price = int(input())
	money = int(input())
	while money < price:
		money += int(input())
	print(f'Going to {country}!')
	country = str(input())