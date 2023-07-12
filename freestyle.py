#Decorators

def dec(name):
    def f(num):
        return name*num
    return f


p = dec('durian')
repeated = p(6)

print(repeated)