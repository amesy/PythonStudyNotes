class DealWith:
    def __init__(self, lowercase, capital):
        self.lowercase = lowercase
        self.capital = capital
        self.lst = []
        self.add = self.add()

    def add(self):
        for i in self.capital:
            self.lst.append(str(i))
            for j in self.lowercase:
                self.lst.append(str(j))
                self.lowercase.pop(0)
                break
        return self.lst

    def number(self):
        for n in range(10):
            self.add.append(str(n))
        return ''.join(self.add)

		
def main():
    lowercase = [chr(i) for i in range(97, 123)]
    capital = [chr(j) for j in range(65, 91)]
    return DealWith(lowercase, capital).number()