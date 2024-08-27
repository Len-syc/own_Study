def multiplcation_generator(x):
	a = 0
	while True:
		a+=1
		c = a*x
		yield f"{a} x {x} = {c}"

mult_gen = multiplcation_generator(20)
for _ in range(1,1000+1):
	print(next(mult_gen))