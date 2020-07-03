import base


def calc(n):
    string = input('Enter your String : ')
    print('''
                [1] Base64
                [2] Base32
                [3] Base16
                [4] Base85 
        ''')
    x = int(input('Enter base (1/2/3/4) : '))
    if n == 1:
        if x == 1:
            base.b64enc(string)
        elif x == 2:
            base.b32enc(string)
        elif x == 3:
            base.b16enc(string)
        elif x == 4:
            base.b85enc(string)
        else:
            print('Wrong Input !!!')

    elif n == 2:
        if x == 1:
            base.b64dec(string)
        elif x == 2:
            base.b32dec(string)
        elif x == 3:
            base.b16dec(string)
        elif x == 4:
            base.b85dec(string)
        else:
            print('Wrong Input !!!')

