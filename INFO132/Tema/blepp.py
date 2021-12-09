def delbar(n):
	return not n%5

def get_deler(n):
	return(list(filter(delbar, range(n))))

print(get_deler(10))