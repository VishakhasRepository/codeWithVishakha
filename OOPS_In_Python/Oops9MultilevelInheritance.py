

class Dad:
    basketball = 1


class Son(Dad):
    dance = 1
    #basketball = 2
    def isDance(self):
        print(self.dance)

class Grandson(Son):
    #dance = 3
    guitar = 5

    def isDance(self):
        print(self.dance)


grandsonInstance = Grandson()
print(grandsonInstance.isDance())
print(grandsonInstance.basketball)

