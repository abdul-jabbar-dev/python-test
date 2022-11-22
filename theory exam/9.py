class Sum_pow:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def sum(self):
        return self.x+self.n

    def pow(self):
        return self.x**self.n

examiner  = Sum_pow(5,3)
print(examiner.sum())
