import math as m

# function to pretty print strings with *dim as a tensor in the console
def pretty_tensor(flat_tensor: str, dim: tuple):

    # lambda function to find tensor[row][col][dep]
    # pattern matching row, col, dep to dim
    find_index = lambda r, c, d, row, col: row*col*d + col*r + c
    if len(dim) == 3: row, col, dep = dim  
    else: row, col, dep = *dim, m.ceil(len(flat_tensor) / (dim[0] * dim[1]))

    res = ''
    res += '-'*2*col + '\n'

    # pretty prints flat_tensor
    # fills empty values with ❤
    for d in range(dep):
        for r in range(row):
            for c in range(col):
                i = find_index(r, c, d, dim[0], dim[1])
                res += (flat_tensor[i] if 0 <= i < len(flat_tensor) else '❤') + ' '
            res += '\n'
        res += '-'*2*col + '\n'
    res = res.strip('\n ') + '\n'

    print(res)

s = 'hello hello hello what are you doin ghere your not supposed to be here'
pretty_tensor(s, (4, 12))
