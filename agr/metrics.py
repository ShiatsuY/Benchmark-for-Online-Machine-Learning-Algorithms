import statistics, csv
acc_list = []
curr_size = 0
max_size = 0
total_time = 0
csvfile = open('n100_40k_noise00_knnadwin.csv', newline='')
c = csv.DictReader(csvfile)
for row in c:
	acc_list.append(float(row['current_acc_[M0]']))
	curr_size = float(row['model_size_[M0]'])
	if curr_size > max_size:
		max_size = curr_size
	curr_time = float(row['total_running_time_[M0]'])
	if curr_time > total_time:
		total_time = curr_time	
csvfile.close()

print(statistics.mean(acc_list))	# mean
print("%.4f" % statistics.pstdev(acc_list)) # average distance to mean
print(total_time)
print(max_size)