import pandas as pd

data = {'Name': ['Algi', 'Ryan', 'Dinova', 'Nindya'],
        'Age': [21,21,20,22],
        }

df = pd.DataFrame(data, columns = ['Name', 'Age'])

print(df)
df.to_csv('test.csv', index=False)