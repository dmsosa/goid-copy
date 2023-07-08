class Raiser():
    def __set__(self, obj, value):
        obj.numberRaised = obj.number**value
    def __get__(self, obj, objtype=None):
        raised = obj.numberRaised
        c = 0
        while raised > 1:
            raised = raised/obj.number
            c += 1
        return c
class Device():
    func = Raiser()
    def __init__(self, n, r):
        self.number = n
        self.func = r
    def _discover(self):
        self.exponent = self.func

number = Device(2, 5)
print(number.numberRaised)
number._discover()
print(number.exponent)
