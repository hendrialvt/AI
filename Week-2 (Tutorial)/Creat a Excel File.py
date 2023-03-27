import pandas as pd

data = {'Name': ['Algi', 'Ryan', 'Dinova', 'Nindya'],
        'Age': [21,21,20,22],
        }

df = pd.DataFrame(data, columns = ['Name', 'Age'])

print(df)
writer = pd.ExcelWriter("test.xlsx", engine='xlsxwriter')

df.to_excel(writer,sheet_name='Sheet1', index=False)
writer.save()