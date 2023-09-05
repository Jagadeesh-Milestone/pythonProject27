#static method
class milestone:
    productid=787887
    @staticmethod
    def product():
        productname='oneplus'
        productcost=25000
        print('product name is',productname)
        print('product cost is',productcost)
        print('product id is',milestone.productid)
milestone.product()
obj1=milestone()
obj1.product()

print('product id is',milestone.productid)