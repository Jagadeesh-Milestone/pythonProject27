#keys/values as series

import  pandas as pd

users={'user1':'hari','user2':'mahesh','user3':'naresh'}
x=pd.Series(users)
print(x)
print(x['user2'])