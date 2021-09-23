class LenVal():
    def __init__(self, data):
        self.data = data
        self.lenData = len(data)

    def sho_val(self):
        print(self.lenData)
        
        
c1 = LenVal("Head")
c1.sho_val()

c2 = LenVal([1,9,4,2,6])
c2.sho_val()

c3 = LenVal((1,))
c3.sho_val()
