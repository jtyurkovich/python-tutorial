
# coding: utf-8

# In[42]:

# open workbook
import xlrd
workbook = xlrd.open_workbook('exercises3.xls')


# In[43]:

# get sheet names
sheets = workbook.sheet_names()


# In[44]:

# use first sheet
sheet1 = workbook.sheet_by_name(sheets[0])

rownum = sheet1.nrows

currentrow = 0

'''while currentrow < rownum:
    row = sheet1.row(currentrow)
    currentrow += 1
    
    print row'''
    
for currentrow in range(0,rownum):
    row = sheet1.row(currentrow)
    
    print row


# In[45]:

# print the first column as a sentence (minus the header)
text = ''

cellnum = sheet1.ncols

currentrow = 0

while currentrow < rownum - 1:
    row = sheet1.row(currentrow)
    currentrow += 1
    
    currentcell = 0
    
    while currentcell < cellnum:
        val = sheet1.cell_value(currentrow,currentcell)
        currentcell += 1
        
        text += val + ' '
        
print text


# In[46]:

# read in the colors in the second sheet
sheet2 = workbook.sheet_by_name(sheets[1])

rownum = sheet2.nrows
cellnum = sheet2.ncols

colors = []
codes = []
orders = []

currentrow = 0

for index in range(1,rownum):
    color = sheet2.cell_value(index,0)
    code = sheet2.cell_value(index,1)
    order = int(sheet2.cell_value(index,2) - 1)
    
    colors.append(color)
    codes.append(code)
    orders.append(order)
    
print colors


# In[47]:

# print the colors as they would appear in a rainbow. (Hint: use the third column to sort them.)
colors = [color for (order,color) in sorted(zip(orders,colors), key = lambda pair: pair[0])]
codes = [code for (order,code) in sorted(zip(orders,codes), key = lambda pair: pair[0])]

print colors
print codes


# In[48]:

# get (x,y) coordinate pairs from sheet 3
sheet3 = workbook.sheet_by_name(sheets[2])

rownum = sheet3.nrows
cellnum = sheet3.ncols

X = []
Y = []

currentrow = 0

for index in range(1,rownum):
    x = sheet3.cell_value(index,0)
    y = sheet3.cell_value(index,1)
    
    X.append(x)
    Y.append(y)


# In[49]:

# plot coordinate pairs from sheet 3 
get_ipython().magic(u'matplotlib inline')
from pylab import *
import matplotlib

matplotlib.pyplot.plot(X,Y)
xlabel('x coordinate')
ylabel('y coordinate')
title('EKG')
matplotlib.pyplot.show()


# In[55]:

# replot, this time as a scatter plot using the color order from sheet 2
figure = matplotlib.pyplot.figure()

matplotlib.pyplot.scatter(X,Y,color=codes)
matplotlib.pyplot.plot(X,Y,'k:')
title('EKG')

matplotlib.pyplot.savefig('exercises3.png', dpi=600, pad_inches=0)

show()


# In[60]:

# plot a bar plot of the data on sheet 4
sheet4 = workbook.sheet_by_name(sheets[3])

rownum = sheet4.nrows
cellnum = sheet4.ncols

X = []
Y = []

currentrow = 0

for index in range(1,rownum):
    x = sheet4.cell_value(index,0)
    y = sheet4.cell_value(index,1)
    
    X.append(x)
    Y.append(y)
    
yerror = 2.5
    
matplotlib.pyplot.bar(X,Y,color = codes,yerr = yerror,align = 'center',ecolor = '#FF0000')
title('bar plot with error bars')

matplotlib.pyplot.savefig('exercises3.pdf', dpi=120, pad_inches=0)

show()

