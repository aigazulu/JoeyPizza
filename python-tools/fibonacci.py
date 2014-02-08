def fibonacci(z):
	if z == 1:
		return 1
	elif z == 0: 
		return 0
	elif z > 1:
		return fibonacci (z-1) + fibonacci (z-2)


print fibonacci(0)
print fibonacci(1)
print fibonacci(2)
print fibonacci(3)
print fibonacci(5)
print fibonacci(7)
print fibonacci(9)
print fibonacci(10)
print fibonacci(15)