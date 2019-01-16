import csv
import random,math
with open('data.csv',mode='w') as data_file:
	data_writer=csv.writer(data_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	for i in range(10000):
		h=random.randint(1,100)
		r=random.randint(1,100)
		area=math.pi*r*r*h
		data_writer.writerow([h,r,area])
