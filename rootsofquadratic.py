a = float(input("Enter the value of a :"))
b = float(input("Enter the value of b :"))
c = float(input("Enter the value of c :"))

# d = discriminant
d = (b**2) - (4*a*c)

if d < 0:
	print("This quadratic function has no any real roots.")
	
elif d == 0:
	print("This quadratic function has One real root.")
	
	root = -b / 2*a 
	
	print("Real root = {}".format(root))
	
elif d > 0:
	print("This quadratic function has Two real roots.")
	
	root1 = -b + d / 2*a
	root2 = -b - d / 2*a 
	
	print("Real roots = {} or {}".format(root1, root2))
