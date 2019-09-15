import random

r = random.randint(1, 100)
while True:
	num = input("guess: ")
	num = int(num)
	if num == r:
		print("you are right")
		break
	elif num > r:
		print(" bigger than answer ")
	elif num < r:
		print("smaller than answer ")