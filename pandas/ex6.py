#data frame
import pandas as pd

data={'fruits':['apple','mango','banana','cherry'],
      'cost/kg':[150,60,40,100]
}
x=pd.DataFrame(data)
print(x)
print(x.loc[0])
print(x.loc[[1,3]])