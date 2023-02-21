import pandas as pd

data = {'Nama': ['Hendriawan Alfitodinova','Made Devinda Adyapti','Siti Shafa Adilah','z'],
        'NPM': [2006570050,2006483712,2006572301,3],
        'Jenis Kelamin': ['Laki-Laki','Perempuan','Perempuan','z'],
        'Tempat Lahir': ['Jakarta','Bogor','Jakarta','z'],
        'Tanggal Lahir': ['24 Desember 2001','17 Febuari 2003','20 Juni 2002','z'],
        'No HP': ['082249329428','085719750846','08180754099','08xxxxxxxxx']
        }

df = pd.DataFrame(data, columns = ['Nama','NPM','Jenis Kelamin','Tempat Lahir','Tanggal Lahir','No HP'])

print(df)
writer = pd.ExcelWriter(r'C:\Users\Dinova\Desktop\Important\Semester 6\AI\Homework-01\Tugas 7.xlsx', engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1', index=False)
writer.save()
print('Berhasil di Save ke Excel')