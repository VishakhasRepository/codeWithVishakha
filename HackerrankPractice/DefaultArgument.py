
class OddStream:
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current = self.current + 2
        return to_return

class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current = self.current + 2
        return to_return

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()

    for i in range(n):
        print(stream.get_next())



num = int(input())
for i in range(num):
    func,m = input().split()
    if func == "even":
        print_from_stream(int(m))
    else:
        print_from_stream(int(m), OddStream())








