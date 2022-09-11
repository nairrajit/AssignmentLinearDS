# Write a program to implement Tower of Hanoi algorithm..

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
	if n == 0:
		return
	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
	print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

numbdisk = int(input("Enter number of disk: "))

TowerOfHanoi(numbdisk, 'A', 'C', 'B')
