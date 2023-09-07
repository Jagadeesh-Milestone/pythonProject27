#method overriding
class parent:
    def mobile(self):
        print('i will give 20000 to buy a mobile')
class child(parent):
    def mobile(self):
        print('I will buy mobile for 30000')
c=child()
c.mobile()