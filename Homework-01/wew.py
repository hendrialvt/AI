import pandas as pd
import openpyxl

wBook = openpyxl.load_workbook(r'C:\Users\Dinova\Desktop\Important\Semester 6\AI\Homework-01\Tugas 7.xlsx')
sheet = wBook.active

n = int(input('How many records you want to insert: '))
for i in range(n):
    Nama = input(f'{i+1}. Enter Nama: ')
    NPM = input(f'{i+1}. Enter NPM: ')
    JenisKelamin = input(f'{i+1}. Enter JenisKelamin: ')
    data = [Nama, NPM, JenisKelamin ]
    wBook.save(r'C:\Users\Dinova\Desktop\Important\Semester 6\AI\Homework-01\Tugas 7.xlsx')
print('Berhasil')