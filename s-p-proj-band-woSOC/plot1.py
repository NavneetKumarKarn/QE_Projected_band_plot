#This code plots only s and p (px, py and pz) orbitals data, not the d orbitals from the filproj produced data file for single type elements
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#from matplotlib import cm
import glob

# Set global font to Times New Roman
#mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams.update({'font.size': 20,})
mylines=[]
#import band data obtained from bands.x
data1=np.loadtxt('bands.out.gnu')
#load the input file
with open ('input.in', 'rt') as myfile:
	for myline in myfile:
		mylines.append(myline)
#input_load=np.loadtxt(input.in)
#projected dos weights
n=int(mylines[0])
#file=input("enter orbital file name:")
k1=int(mylines[1])
#enter the fermi energy
Eg=float(mylines[2])
print(n, k1, Eg)
ps=int(mylines[16]) #point size in the plot
#load datafile names
files=glob.glob("*.txt")
files.sort()
print(files)
a=int(len(files))

#Load k points and energy in numpy array
k= np.array(data1[:, 0])	# k-points
e=np.zeros((np.size(np.array(data1[:, 0])),a))
for i in range(a):
	e[:,i] = np.array(data1[:, 1])	# band energy values

#load colormap names
#colormap=['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu','GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
colormap=["red","cyan","blue","black","red","magenta","blue","yellow","purple","beige","gray","cyan","green","pink","brown","black","orange"]
c=0
fig, ax = plt.subplots()
#loading projcted dos data of each orbital and plotting them
for f in files:
	data=np.loadtxt(f)													# load all orbital data files in the directory
	dos=np.zeros((np.size(np.array(data1[:, 0])),a))						# Creat numpy array for dos data storage according to k and e
	m=0
	#dos[0]=data[0,2]
	for i in range(n):
		for j in range(k1):
			l=int(n*j+i)
			dos[m,c]= data[l,2] # dos values
			m=m+1

	#cmap = cm.get_cmap(colormap[c])
	#color = cmap(dos[:,c])[..., :3]
	ax.scatter(k,e[:,c] - Eg,c=colormap[c],s=dos[:,c]*ps, alpha=0.5)
	c=c+1
ax.legend([r"p$_x$", "p$_y$", "p$_z$", "s"], fontsize=16,fancybox=True, framealpha=1 )
#Plce the horizontal line at fermi level
ax.axhline(y = 0, color = 'black', linestyle = 'dashed')
Nhsp=int(mylines[3])
#Place the line at high symmetric points
for i in range(4,Nhsp+3):
	ax.axvline(x = float(mylines[i]), color = 'black')
#Enter the name/position of high symmetric path manually
ax.text(-0.05,-3.45, r"$ \Gamma $",fontsize=20)
ax.text(0.50378,-3.45, 'T',fontsize=20)
ax.text(0.85819,-3.45, 'H2|H0',fontsize=20)
ax.text(1.6360,-3.45, 'L',fontsize=20)
ax.text(2.3046,-3.45, r"$\Gamma $",fontsize=20)
ax.text(2.85508,-3.45, 'S0|S2',fontsize=20)
ax.text(4.0747,-3.45, 'F2',fontsize=20)
ax.text(4.83,-3.45, r"$\Gamma $",fontsize=20)
ax.set_xlim(float(mylines[4]), float(mylines[Nhsp+3]))
ax.set_ylim(float(mylines[14]),float(mylines[15]))
ax.set_xticks([])
ax.tick_params(axis='y', direction='in')
#plt.xlabel("")
ax.set_ylabel(r"E-E$_g$ (eV)", fontsize=20)
plt.show()
