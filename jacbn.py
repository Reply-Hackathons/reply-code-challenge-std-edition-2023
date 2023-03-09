snakes = []
cols = 0
rows = 0
num_snakes = 0
matrix = []

with open("tests/00-example.txt") as topo_file:
    count = 0
    for line in topo_file:
        variables = line[:-1].split(" ")
        if count == 0:
            cols = int(variables[0])
            rows = int(variables[1])
            num_snakes = int(variables[2])
        elif count == 1:
            for n in range(int(num_snakes)):
                snakes.append(int(variables[n]))
        else:
            row = []
            for n in range(int(cols)):
                row.append(variables[n])
            matrix.append(row)

        count += 1

max_snake = max(snakes)
dps = []
for bound in range(1, max_snake + 1):
    if bound == 1:
        dp = list(map(lambda x: list(map(lambda y: 0 if y == "*" else int(y), x)), matrix))
    else:
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                prev = dps[bound - 2]
                optimal_path = max(prev[(row - 1) % rows][col], 
                                   prev[(row + 1) % rows][col], 
                                   prev[row][(col - 1) % cols], 
                                   prev[row][(col + 1) % cols])
                dp[row][col] = optimal_path + int(matrix[row][col])
    dps.append(dp)

print(dps[1])
