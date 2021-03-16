print('n!')
n = int(input('n = '))
orig_val = n

for n_fact in range(1, n):
	n *= n_fact

print(f'{orig_val}! = {n}')