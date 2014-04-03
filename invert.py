import ast
import copy
import inspect

FLIP_MAP = {
        'a' : 'ɐ',
        'b' : 'q',
        'c' : 'ɔ',
        'd' : 'p',
        'e' : 'ǝ',
        'f' : 'ɟ',
        'g' : 'ƃ',
        'h' : 'ɥ',
        'i' : 'ᴉ',
        'j' : 'ɾ',
        'k' : 'ʞ',
        'l' : 'l',
        'm' : 'ɯ',
        'n' : 'u',
        'o' : 'o',
        'p' : 'd',
        'q' : 'b',
        'r' : 'ɹ',
        's' : 's',
        't' : 'ʇ',
        'u' : 'n',
        'v' : 'ʌ',
        'w' : 'ʍ',
        'x' : 'x',
        'y' : 'ʎ',
        'z' : 'z',
        'A' : '∀',
        'B' : 'q',
        'C' : 'Ɔ',
        'D' : 'p',
        'E' : 'Ǝ',
        'F' : 'Ⅎ',
        'G' : 'פ',
        'H' : 'H',
        'I' : 'I',
        'J' : 'ſ',
        'K' : 'ʞ',
        'L' : '˥',
        'M' : 'W',
        'N' : 'N',
        'O' : 'O',
        'P' : 'Ԁ',
        'Q' : 'Q',
        'R' : 'ɹ',
        'S' : 'S',
        'T' : '┴',
        'U' : '∩',
        'V' : 'Λ',
        'W' : 'M',
        'X' : 'X',
        'Y' : '⅄',
        'Z' : 'Z',
        '_' : '‾',
        '!' : '¡'}

def flip(var):
    # flip strings
    if isinstance(var, str):
        return flip_string(var)

    # flip multi-dimensional arrays
    try:
        new_var = copy.copy(var)
        for index, row in enumerate(var):
            new_var[index] = row[::-1]

        return new_var
    except:
        pass
    
    # can't be flipped
    return var

def flip_string(s):
    return ''.join([FLIP_MAP[c] if c in FLIP_MAP else c for c in s])

def add_inverts(var):
    current_frame = inspect.currentframe()
    caller = inspect.getouterframes(current_frame)[1]

    # find variable name
    var_name = None
    for k, v in caller[0].f_locals.items():
        if v is var:
            var_name = k
            break

    if var_name is None:
        raise ValueError('Could not find varaible')

    caller[0].f_globals[flip_string(var_name)] = flip(var)
    caller[0].f_globals[var_name[::-1]] = var[::-1]
    caller[0].f_globals[flip_string(var_name[::-1])] = flip(var[::-1])

def main():
    mystring = 'Hello World!'
    add_inverts(mystring)

    print(mystring)
    print(ɯʎsʇɹᴉuƃ)
    print(ƃuᴉɹʇsʎɯ)
    print(gnirtsym)
    print()

    mylist = [[1,2,3], [4,5,6]]
    add_inverts(mylist)

    print(mylist)
    print(ɯʎlᴉsʇ)
    print(ʇsᴉlʎɯ)
    print(tsilym)
    print()

    import numpy
    mymatrix = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
    add_inverts(mymatrix)

    print(mymatrix)
    print(xirtamym)
    print(ɯʎɯɐʇɹᴉx)
    print(xᴉɹʇɐɯʎɯ)

if __name__ == '__main__':
    exit(main())
    
