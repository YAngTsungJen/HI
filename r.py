import random
start = input("請決定隨機數字範圍開始值: ")
end = input("請決定隨機數字範圍結束值: ")
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1 數幾次
	num = input("guess: ")
	num = int(num)
	if num == r:
		print("you are right")
		print("你猜了第", count, "次")
		break
	elif num > r:
		print(" bigger than answer ")
	elif num < r:
		print("smaller than answer ")
	print("你猜了第", count, "次")