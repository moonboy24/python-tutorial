import pandas as pd
data = {
    'Name' : ['alice' , 'julie' , 'aestia'],
    'Age' : [25 , 24 ,24],
    'City' : ['Chennai' , 'Bangalore' , 'Hyderabad']
}

df = pd.DataFrame(data)
print(df.dtypes)
print(df['Name'])
