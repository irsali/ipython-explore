x = None
xl = globals()
print('type return by globals(): ', type(xl))
print('\nlist of global variables')
for x in xl:
    print(x)


def print_locals():
    print('\nlist of local variables')
    x = None
    xl = locals()
    for x in xl:
        print(x)
    print(xl)
    print('type return by locals(): ', type(xl))


print_locals()