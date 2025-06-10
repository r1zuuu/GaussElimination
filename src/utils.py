def save(equations, filename):
    with open(filename, 'w') as file:
        for equation in equations:
            file.write(' '.join(map(str, equation)) + '\n')