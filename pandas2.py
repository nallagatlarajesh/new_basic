import numpy as np
import pandas as pd

labels=["a","b","c"]
my_data=[10,20,30]
arr=np.array(my_data)
d={"a":10,"b":20,"c":30}

print("l",labels)
print(my_data)
print(d)
print(arr)
pd.Series(data=my_data)
pd.Series(data=my_data,index=labels)
pd.Series(d)
pd.Series(arr,labels)#using pre defined object
