from math import sin
import random,csv
with open('data_proj2.csv',mode='w') as data_file:
	data_writer=csv.writer(data_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	data_writer.writerow(["a","b"])
	for i in range(1000000):
		a=i
		b=a*a
		data_writer.writerow([a,b])