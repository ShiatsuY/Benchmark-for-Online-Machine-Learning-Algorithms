import statistics, csv
acc_list = []
curr_size = 0
max_size = 0
csvfile = open('1000_knnadwin.csv', newline='')
c = csv.DictReader(csvfile)
for row in c:
	acc_list.append(float(row['current_acc_[M0]']))	
csvfile.close()

print(statistics.mean(acc_list))	# mean
print("%.4f" % statistics.pstdev(acc_list)) # average distance to mean