# The code can extract s and p (px, py and pz) orbitals data, not the d orbitals from the filproj produced data file for single type elements
# For SOC case

mylines = [] 						# Declare an empty list named mylines.
name = []
with open ('pbands1.projwfc_up', 'r') as myfile: 	# Open lorem.txt for reading text data.
	lines = len(myfile.readlines())	
                            		
with open ('pbands1.projwfc_up', 'rt') as myfile: 	# Open lorem.txt for reading text data.
	for myline in myfile:                		# For each line, stored as myline,
		mylines.append(myline)           		# add its contents to mylines.

name=mylines[0]

#lenght of lines containing DOS weights and orbital info
l1=len(mylines[0])					#orbital info
l2=len(mylines[1])					#DOS weights
print(l1,l2)
c=0

orbitals=list(('S','P','D'))

if name[17]==orbitals[0]:
	if name[36:40]==' 0.5':
		f = open(str(name[12:14])+name[16:18]+"0.5.txt", 'w')
	elif name[36:40]=='-0.5':
		f = open(str(name[12:14])+name[16:18]+"-0.5.txt", 'w')
elif name[17]==orbitals[1]:
	if name[36:40]=='-1.5' and 'name[31:34]'=='1.5':
		f = open(str(name[12:14])+name[16:18]+"y1.5.txt", 'w')
	elif name[36:40]=='-0.5' and 'name[31:34]'=='1.5':
		f = open(str(name[12:14])+name[16:18]+"y0.5.txt", 'w')
	elif name[36:40]==' 1.5' and 'name[31:34]'=='1.5':
		f = open(str(name[12:14])+name[16:18]+"x1.5.txt", 'w')
	elif name[36:40]==' 0.5' and 'name[31:34]'=='1.5':
		f = open(str(name[12:14])+name[16:18]+"x0.5.txt", 'w')
	elif name[36:40]==' 0.5' and 'name[31:34]'=='0.5':
		f = open(str(name[12:14])+name[16:18]+"z0.5.txt", 'w')
	elif name[36:40]=='-0.5' and 'name[31:34]'=='0.5':
		f = open(str(name[12:14])+name[16:18]+"z-0.5.txt", 'w')
elif name[17] == orbitals[2]:
	f = open(str(name[12:14])+name[16:18]+".txt", 'w')

for i in range(1,lines):
	if len(mylines[i])==l2:
		f.write(str(mylines[i]))
	elif len(mylines[i])==l1:
		f.close()
		name=mylines[i]
		if name[17]==orbitals[0]:
			if name[36:40]==' 0.5':
				f = open(str(name[12:14])+name[16:18]+"0.5.txt", 'w')
			elif name[36:40]=='-0.5':
				f = open(str(name[12:14])+name[16:18]+"-0.5.txt", 'w')
		elif name[17]==orbitals[1]:
			if name[36:40]=='-1.5' and name[31:34]=='1.5':
				f = open(str(name[12:14])+name[16:18]+"y1.5.txt", 'w')
			elif name[36:40]=='-0.5' and name[31:34]=='1.5':
				f = open(str(name[12:14])+name[16:18]+"y0.5.txt", 'w')
			elif name[36:40]==' 0.5' and name[31:34]=='1.5':
				f = open(str(name[12:14])+name[16:18]+"x0.5.txt", 'w')
			elif name[36:40]==' 1.5' and name[31:34]=='1.5':
				f = open(str(name[12:14])+name[16:18]+"x1.5.txt", 'w')
			elif name[36:40]==' 0.5' and name[31:34]=='0.5':
				f = open(str(name[12:14])+name[16:18]+"z0.5.txt", 'w')
			elif name[36:40]=='-0.5' and name[31:34]=='0.5':
				f = open(str(name[12:14])+name[16:18]+"z-0.5.txt", 'w')
		elif name[17]==orbitals[2]:
			f = open(str(name[12:14])+name[16:18]+".txt", 'w')
