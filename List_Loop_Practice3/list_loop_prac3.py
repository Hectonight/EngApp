scores = [float(input(f'The score for test {num} was: ')) for num in range(1, 20)]
print(f'The class average was {round(sum(scores)/19, 2)}%')