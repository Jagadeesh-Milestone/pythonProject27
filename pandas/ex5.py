import pandas as pd

fruits={'one':'banana','two':'cherry','three':'mango'}
x=pd.Series(fruits,index=['one','three'])
print(x)