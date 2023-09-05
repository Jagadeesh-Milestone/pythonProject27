#methods:
#there are three types of methods in oops
#class method
#instance method
#static method

#instance method:
class milestone:
    productid=898989
    def product(self):
        productname='oneplus'
        productcost=20000
        print('product name is',productname)
        print('product cost is',productcost)
        print('product id is',milestone.productid)
obj1=milestone()
obj1.product()
print('product id is',milestone.productid)




