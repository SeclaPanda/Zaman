def ab(k1, k2, k3, k4):
	a = abs(k3-k1)
	b = abs(k4-k2)
	p = ((a+b)*2)
	s = (a * b)
	print('\n%.2f' % s, '\n%.2f' % p)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
ab(x1, y1, x2, y2)