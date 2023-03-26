
def print_formatted(n):
    for i in range(1,n + 1):
        pads = n.bit_length()
        #print(pad)
        print(f'{i:{pads}d}')
        print(f'{i:{pads}o}')
        print(f'{i:{pads}X}')
        print(f'{i:{pads}b}')

print_formatted(17)