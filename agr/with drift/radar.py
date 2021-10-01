import pandas as pd
import statistics
import matplotlib.pyplot as plt
from math import pi

filename = 'data_agr_with_drift.csv'

vfdt_acc = []
vfdt_std = []
vfdt_training = []
vfdt_testing = []
vfdt_size = []
vfdt_ram = []
vfdt_cpu = []

hat_acc = []
hat_std = []
hat_training = []
hat_testing = []
hat_size = []
hat_ram = []
hat_cpu = []

knn_acc = []
knn_std = []
knn_training = []
knn_testing = []
knn_size = []
knn_ram = []
knn_cpu = []

knnadwin_acc = []
knnadwin_std = []
knnadwin_training = []
knnadwin_testing = []
knnadwin_size = []
knnadwin_ram = []
knnadwin_cpu = []

vfdt_points = []
hat_points = []
knn_points = []
knnadwin_points = []

min_std = float('inf')
min_training = float('inf')
min_testing = float('inf')
min_size = float('inf')
min_ram = float('inf')
min_cpu = float('inf')

max_std = 0
max_training = 0
max_testing = 0
max_size = 0
max_ram = 0
max_cpu = 0

csv = pd.read_csv(filename, skipinitialspace=True)

training = csv['training']
testing = csv['testing']
size = csv['size']
ram = csv['ram']
cpu = csv['cpu']
std = csv['std']

for x in training:
	if min_training > x:
		min_training = x
	if max_training < x:
		max_training = x

for x in testing:
	if min_testing > x:
		min_testing = x
	if max_testing < x:
		max_testing = x

for x in size:
	if min_size > x:
		min_size = x
	if max_size < x:
		max_size = x

for x in ram:
	if min_ram > x:
		min_ram = x
	if max_ram < x:
		max_ram = x

for x in cpu:
	if min_cpu > x:
		min_cpu = x
	if max_cpu < x:
		max_cpu = x

for x in std:
	if min_std > x:
		min_std = x
	if max_std < x:
		max_std = x

def score_below(mean, lower, upper):
	return (((mean - lower) / (upper - lower)) * -100) + 100

def score_above(mean, lower, upper):
	return (((mean - lower) / (upper - lower)) * 100)

for i in range(0,9):
	vfdt_acc.append(csv['accuracy'][i])
	hat_acc.append(csv['accuracy'][i+9])
	knn_acc.append(csv['accuracy'][i+18])
	knnadwin_acc.append(csv['accuracy'][i+27])

	vfdt_std.append(csv['std'][i])
	hat_std.append(csv['std'][i+9])
	knn_std.append(csv['std'][i+18])
	knnadwin_std.append(csv['std'][i+27])

	vfdt_training.append(csv['training'][i])
	hat_training.append(csv['training'][i+9])
	knn_training.append(csv['training'][i+18])
	knnadwin_training.append(csv['training'][i+27])

	vfdt_testing.append(csv['testing'][i])
	hat_testing.append(csv['testing'][i+9])
	knn_testing.append(csv['testing'][i+18])
	knnadwin_testing.append(csv['testing'][i+27])
	
	vfdt_size.append(csv['size'][i])
	hat_size.append(csv['size'][i+9])
	knn_size.append(csv['size'][i+18])
	knnadwin_size.append(csv['size'][i+27])
	
	vfdt_ram.append(csv['ram'][i])
	hat_ram.append(csv['ram'][i+9])
	knn_ram.append(csv['ram'][i+18])
	knnadwin_ram.append(csv['ram'][i+27])
	
	vfdt_cpu.append(csv['cpu'][i])
	hat_cpu.append(csv['cpu'][i+9])
	knn_cpu.append(csv['cpu'][i+18])
	knnadwin_cpu.append(csv['cpu'][i+27])

#------------------------------------------

vfdt_points.append("%.2f" % statistics.mean(vfdt_acc))
hat_points.append("%.2f" % statistics.mean(hat_acc))
knn_points.append("%.2f" % statistics.mean(knn_acc))
knnadwin_points.append("%.2f" % statistics.mean(knnadwin_acc))

vfdt_points.append("%.2f" % score_below(statistics.mean(vfdt_std), min_std, max_std))
hat_points.append("%.2f" % score_below(statistics.mean(hat_std), min_std, max_std))
knn_points.append("%.2f" % score_below(statistics.mean(knn_std), min_std, max_std))
knnadwin_points.append("%.2f" % score_below(statistics.mean(knnadwin_std), min_std, max_std))

vfdt_points.append("%.2f" % float((score_below(statistics.mean(vfdt_training), min_training, max_training) + score_below(statistics.mean(vfdt_testing), min_testing, max_testing)) / 2))
hat_points.append("%.2f" %float((score_below(statistics.mean(hat_training), min_training, max_training) + score_below(statistics.mean(hat_testing), min_testing, max_testing)) / 2))
knn_points.append("%.2f" %float((score_below(statistics.mean(knn_training), min_training, max_training) + score_below(statistics.mean(knn_testing), min_testing, max_testing)) / 2))
knnadwin_points.append("%.2f" %float((score_below(statistics.mean(knnadwin_training), min_training, max_training) + score_below(statistics.mean(knnadwin_testing), min_testing, max_testing)) / 2))

vfdt_points.append("%.2f" %score_below(statistics.mean(vfdt_size), min_size, max_size))
hat_points.append("%.2f" %score_below(statistics.mean(hat_size), min_size, max_size))
knn_points.append("%.2f" %score_below(statistics.mean(knn_size), min_size, max_size))
knnadwin_points.append("%.2f" %score_below(statistics.mean(knnadwin_size), min_size, max_size))

vfdt_points.append("%.2f" %float((score_below(statistics.mean(vfdt_ram), min_ram, max_ram) + score_below(statistics.mean(vfdt_cpu), min_cpu, max_cpu)) / 2))
hat_points.append("%.2f" %float((score_below(statistics.mean(hat_ram), min_ram, max_ram) + score_below(statistics.mean(hat_cpu), min_cpu, max_cpu)) / 2))
knn_points.append("%.2f" %float((score_below(statistics.mean(knn_ram), min_ram, max_ram) + score_below(statistics.mean(knn_cpu), min_cpu, max_cpu)) / 2))
knnadwin_points.append("%.2f" %float((score_below(statistics.mean(knnadwin_ram), min_ram, max_ram) + score_below(statistics.mean(knnadwin_cpu), min_cpu, max_cpu)) / 2))

vfdt_points_f = list(map(round, map(float, vfdt_points)))
hat_points_f = list(map(round, map(float, hat_points)))
knn_points_f = list(map(round, map(float, knn_points)))
knnadwin_points_f = list(map(round, map(float, knnadwin_points)))

#################

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(polar="True")

categories = ['Accuracy', 'Robustness', 'Computation Time', 'Size', 'RAM/CPU usage']
n = len(categories)

s = sum(knnadwin_points_f)
values = knnadwin_points_f
plt.title('KNNADWIN:' + str(s), size=15, y=1.05)

values += values[:1]

angles = [x / float(n) * 2 * pi for x in range(n)]
angles += angles[:1]

plt.polar(angles, values, marker=".")
plt.fill(angles, values, alpha=0.3)
plt.xticks(angles[:-1], categories)

ax.set_rlabel_position(0)
plt.yticks([20,40,60,80], color="grey", size=10)
plt.ylim(0,100)

plt.show()