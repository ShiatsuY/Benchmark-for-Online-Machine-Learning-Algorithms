# import matplotlib.pyplot as plt
# import csv

# acc_list_vfdt = []
# acc_list_hat = []
# acc_list_knn = []
# acc_list_knnadwin = []
# acc_mean_vfdt = []
# acc_mean_hat = []
# acc_mean_knn = []
# acc_mean_knnadwin = []
# noise = 'n0.4'
# size = '1000'
# models = ['vfdt', 'hat', 'knn', 'knnadwin']
# xscale = 40

# for model in models:
# 	csvfile = open(size+'_'+noise+'_'+model+'.csv', newline='')
# 	c = csv.DictReader(csvfile)
# 	if model == 'vfdt':
# 		for row in c:
# 			acc_list_vfdt.append(float(row['current_acc_[M0]']) * 100)
# 			acc_mean_vfdt.append(float(row['mean_acc_[M0]']) * 100)
# 	elif model == 'hat':
# 		for row in c:
# 			acc_list_hat.append(float(row['current_acc_[M0]']) * 100)
# 			acc_mean_hat.append(float(row['mean_acc_[M0]']) * 100)
# 	elif model == 'knnadwin':
# 		for row in c:
# 			acc_list_knn.append(float(row['current_acc_[M0]']) * 100)
# 			acc_mean_knn.append(float(row['mean_acc_[M0]']) * 100)
# 	else:
# 		for row in c:
# 			acc_list_knnadwin.append(float(row['current_acc_[M0]']) * 100)
# 			acc_mean_knnadwin.append(float(row['mean_acc_[M0]']) * 100)

# plt.plot(acc_mean_vfdt, label="VFDT mean",lw=.5)
# plt.plot(acc_mean_hat, label="HAT mean",lw=.5)
# plt.plot(acc_mean_knn, label="KNN mean",lw=.5)
# plt.plot(acc_mean_knnadwin, label="KNNADWIN mean",lw=.5)
# # this is only used when concept drift is occurring
# # plt.vlines(x=xscale/2, ymin=0, ymax=100, colors='black', ls=':', lw=1.5, label="Concept Drift")
# plt.axis([0, xscale, 45, 70])
# plt.xlabel('Batches')
# plt.ylabel('Acc (in %)')
# plt.legend()
# plt.show()