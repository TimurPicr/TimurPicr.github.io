def func(size, symb, var=0):
    if (var != int(size/2)+1):
        print(symb*var)
        print(func(size, symb, var+1))
        return symb*var
    else:
        return symb*var
func(7, 'c')
