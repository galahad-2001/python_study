# -*- coding:utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
import xlrd
workbook = xlrd.open_workbook("C:\Users\Jayden\Desktop\IR02812-MFZ2.0 tracking curve_V1.4.xlsx")
sheet = workbook.sheet_by_index(0)

x = []
yinf = []
y3 = []
y25 = []
y2 = []
y15 = []
y1 = []

for i in range(6, 1325):
	x.append(sheet.cell(i,1).value)
	yinf.append(sheet.cell(i,3).value)
	y3.append(sheet.cell(i,5).value)
	y25.append(sheet.cell(i,7).value)
	y2.append(sheet.cell(i,9).value)
	y15.append(sheet.cell(i,11).value)
	y1.append(sheet.cell(i,13).value)

polyfitinf = np.polyfit(x, yinf, 4)
ppolyfitinf = np.poly1d(polyfitinf)

print polyfitinf
print ppolyfitinf

plotpolyfit = plt.plot(x, ppolyfitinf(x), color='black',label='ppolyfitinf')
plotinf = plt.plot(x, yinf, 'r-',label='yinf')
ploty3 = plt.plot(x, y3, 'g-',label='y3')
ploty25 = plt.plot(x, y25, 'b-',label='y25')
ploty2 = plt.plot(x, y2, 'r--',label='y2')
ploty15 = plt.plot(x, y15, 'g--',label='y15')
ploty1 = plt.plot(x, y1, 'b--',label='y1')

plt.show()