def mult(x, y):
	return x * y

def div(x, y):
	return x / y

def is_float(value):
	try:
		float(value)
		return True
	except ValueError:
		return False

def calculate(function_, min_, max_):
	function_ = function_.split(' ')
	result = 0
	dx = 0.0001
	
	x = min_
	while x <= max_:
		if is_float(function_[0]):
			var = float(function_[0])
		else:
			var = x
		for i in range(1, len(function_)):
			if function_[i] == "*":
				if is_float(function_[i + 1]):
					var *= float(function_[i + 1])
				else:
					var *= x
			if function_[i] == "/":
				if is_float(function_[i + 1]):
					var /= float(function_[i + 1])
				else:
					var /= x
			if function_[i] == "^":
				if is_float(function_[i + 1]):
					power = float(function_[i + 1])
				else:
					power = x
				var *= pow(float(function_[i - 1]), float(function_[i + 1] - 1))
		result += var * dx
		x += dx
	return result

print round(calculate("x * 2", 0, 4), 3)

