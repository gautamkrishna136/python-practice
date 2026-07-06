'''import pandas as pd
my_dataset={
    "cars":["bmw","volvo","ford"],
    "passing":[3,7,2]
}
myvar=pd.DataFrame(my_dataset)
print(myvar)
print(pd.__version__)'''


'''
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)'''


'''import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df.loc[0])'''

'''import pandas as pd
#pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df)'''

'''import pandas as pd
#pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(pd.options.display.max_rows)'''

'''import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5
  }
}

df = pd.DataFrame(data)

print(df) '''

'''import pandas as pd

df = pd.read_json('data.json')

print(df.to_string())'''


'''import pandas as pd

df = pd.read_csv('data1.csv')

new_df = df.dropna()

print(new_df.to_string())'''

#repairing the csv file:-

'''import os
print(os.getcwd())'''

'''import pandas as pd
df = pd.read_csv("data1.csv")
print("Before:", len(df))
new_df = df.dropna()
print("After:", len(new_df))
print(new_df.to_string())'''

'''import pandas as pd
df = pd.read_csv("data1.csv")
print(df.isnull().sum())'''

'''import pandas as pd
df = pd.read_csv("data1.csv")
print(repr(df.loc[18, "Calories"]))
print(repr(df.loc[22, "Date"]))
print(repr(df.loc[28, "Calories"]))'''

'''import pandas as pd
df = pd.read_csv("data1.csv")
print(df.columns.tolist())'''

'''import pandas as pd
df = pd.read_csv("data1.csv") 
print(df.isnull().sum())'''

'''import pandas as pd
df = pd.read_csv("data1.csv")
print(df.columns.tolist())
print(df.isnull().sum())
new_df = df.dropna()
print("Before:", len(df))
print("After:", len(new_df))'''

'''import pandas as pd
df = pd.read_csv('data1.csv')
new_df = df.dropna()
print(new_df.to_string())'''

'''import pandas as pd
df = pd.read_csv('data1.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())'''

'''import pandas as pd
df = pd.read_csv('data1.csv')
df.loc[7,'Duration'] = 45
print(df.to_string())'''

'''import pandas as pd
df = pd.read_csv('data1.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
print(df.to_string())'''

'''import pandas as pd
df = pd.read_csv('data1.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
#remember to include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy
print(df.to_string())'''

'''import pandas as pd
df = pd.read_csv('data1.csv')
print(df.duplicated())'''

'''import pandas as pd
df = pd.read_csv('data.csv')
df.drop_duplicates(inplace = True)
print(df.to_string())
#Notice that row 12 has been removed from the result'''































