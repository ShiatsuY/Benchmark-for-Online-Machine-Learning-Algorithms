import matplotlib.pyplot as plt
import csv

acc_list_vfdt10 = []
acc_list_vfdt100 = []
acc_list_vfdt1000 = []
acc_mean_vfdt10 = []
acc_mean_vfdt100 = []
acc_mean_vfdt1000 = []
noises = ['n0.0', 'n0.15', 'n0.4']
sizes = ['10', '100', '1000']
models = ['vfdt', 'hat', 'knn', 'knnadwin']

#for model in models:
	#for noise in noises:
		#for size in sizes:
#csvfile = open(size+'_'+noise+'_'+model+'.csv', newline='')
for size in sizes:
	csvfile = open(size+'_VFDT'+'.csv', newline='')
	c = csv.DictReader(csvfile)
	if size == '10':
		for row in c:
			acc_list_vfdt10.append(float(row['current_acc_[M0]']) * 100)
			acc_mean_vfdt10.append(float(row['mean_acc_[M0]']) * 100)
	elif size == '100':
		for row in c:
			acc_list_vfdt100.append(float(row['current_acc_[M0]']) * 100)
			acc_mean_vfdt100.append(float(row['mean_acc_[M0]']) * 100)
	else:
		for row in c:
			acc_list_vfdt1000.append(float(row['current_acc_[M0]']) * 100)
			acc_mean_vfdt1000.append(float(row['mean_acc_[M0]']) * 100)

#x1 = list(range(0, 40000, 10))
x2 = list(range(0, 40000, 100))
x3 = list(range(0, 40000, 1000))

#plt.plot(acc_list, lw=0.5, label="Accuracy values", color='lightblue')
plt.plot(acc_mean_vfdt10,  label="VFDT 10",lw=.5)
#plt.plot(acc_mean_vfdt100, x2, label="VFDT 100",lw=.5)
#plt.plot(acc_mean_vfdt1000, x3, label="VFDT 1000",lw=.5)
plt.vlines(x=2000, ymin=0, ymax=100, colors='black', ls=':', lw=1.5, label="Concept Drift")
plt.axis([0, 4000, 0, 100])
plt.xlabel('Batches')
plt.ylabel('Acc (in %)')
plt.legend()
plt.show()