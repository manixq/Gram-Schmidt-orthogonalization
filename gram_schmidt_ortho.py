def get_data():
	with open("vector_data.txt") as data: 
		vectors = data.read().splitlines()
		i=0
		print("Inputs:")
		for v in vectors:
			vectors[i] = v.split(",")
			vectors[i] = list(map(int, vectors[i]))
			print(vectors[i])
			i += 1
	return vectors

def dot_product(vector_1, vector_2):
	dot_product = 0
	for i in range(0, len(vector_1)):
		dot_product += vector_1[i] * vector_2[i]
	return dot_product

def sub_vec(vector_1, vector_2):
	vector = []
	for i in range(0, len(vector_1)):
		vector.append(vector_1[i] - vector_2[i])
	return list(map(int, vector))

def gram_schmidt(vectors):
	result = []
	if len(vectors) > 1:
		for n in range(0, len(vectors)):
			result.append(vectors[n])
			for k in range(0, n):
				result[-1] = sub_vec(result[-1] ,[x * dot_product(vectors[n], result[k]) / dot_product(result[k], result[k]) for x in result[k]]) 
	else:
		return vectors
	return result

result = gram_schmidt(get_data())
print("\n\nOutputs:")
for v in result:
	print(v)
input("\nPress enter to exit ;)")
