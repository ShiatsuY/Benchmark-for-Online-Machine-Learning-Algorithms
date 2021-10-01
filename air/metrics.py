import statistics, csv
acc_list = []
curr_size = 0
max_size = 0
csvfile = open('10_knnadwin.csv', newline='')
c = csv.DictReader(csvfile)
for row in c:
	acc_list.append(float(row['current_acc_[M0]']))
	curr_size = float(row['model_size_[M0]'])
	if curr_size > max_size:
		max_size = curr_size
csvfile.close()

print(statistics.mean(acc_list))	# mean
print("%.4f" % statistics.pstdev(acc_list)) # average distance to mean
print(max_size)