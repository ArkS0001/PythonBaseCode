def TowerOfHanoi(n, begin, end, mid):
	if n == 0:
		return
	TowerOfHanoi(n-1, begin, mid, end)
	print("Move disk", n, "from rod", begin, "to rod", end)
	TowerOfHanoi(n-1, mid, end, begin)
N = 3
TowerOfHanoi(N, 'A', 'C', 'B')
