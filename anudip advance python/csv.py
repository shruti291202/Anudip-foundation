import csv
f=open("tanishq.csv",'a',newline='')
wo=csv.writer(f)
data=[["a","b","c"],[14,15,18],[47,19,48]]
wo.writerow(data)
f.close()
