import statistics, csv

noises = ['n0.0', 'n0.15', 'n0.4']
sizes = ['10', '100', '1000']
models = ['vfdt', 'hat', 'knn', 'knnadwin']
x = 0


acc_list = []
curr_size = 0
max_size = 0

for model in models:
	for noise in noises:
		for size in sizes:
			csvfile = open(size+'_'+noise+'_'+model+'.csv', newline='')
			c = csv.DictReader(csvfile)
			for row in c:
				acc_list.append(float(row['current_acc_[M0]']))
			#print(noise+' '+ size +' '+model)
			#print("%.4f" % statistics.mean(acc_list))	# mean
			x = statistics.pstdev(acc_list) * 100
			print("%.2f" % x) # average distance to mean