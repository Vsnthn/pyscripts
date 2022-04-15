import xlwt
from xlwt import Workbook
wb = Workbook()
odd=[]
even=[]
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0,'ODD')
for i in range(1,100):
    if i%2!=0:
        odd.append(i)
for j in range(1,len(odd)+1):
    sheet1.write(j,0,odd[j-1])  



sheet2 = wb.add_sheet('Sheet 2')
sheet2.write(0, 0,'EVEN')
for i in range(1,100):
    if i%2==0:
        even.append(i)
for j in range(1,len(even)+1):
    sheet2.write(j,0,even[j-1])  

wb.save('xlwt example.xls')
