# Benchmark for Online Machine Learning Algorithms
###### Version: 0.1
The benchmark is divided in two phases. To begin the program needs to know which algorithms and datasets are going to be used.<br>
Algorithms used: Four classifiers (<em>VFDT, HAT, KNN, KNNADWIN</em>).<br>
Datasets used: Two real, two synthetic and two synthetic with concept drift (<em>Airlines, Electricity, AGRAWAL Generator, SEA Generator</em>).

### First Phase: Data Acquisiton

To monitor performances it is advised not to use the machine while running the monitoring because the program monitors CPU load and RAM usage.
After a run completes a .csv file (a table) is produced to store the data of the performance. Unfortunately every run has to be configured manually (choosing model and dataset).
Internally it is processed first choosing the datasets and then the models (and further noise and batch size levels) until every dataset with every model was run.
[Link](stream_template.py)
<br>
<br>
After the tables were generated another single table will be created containing and compressing the perfomance information for this specific dataset. 
Used to gain Variance on Accuracy values. [Link](metric.py)

### Second Phase: Evaluation
After acquiring information the program can deploy this information as plots and radar charts.
As the plots display the average Accuracy values, the program fetches this data from the corresponding tables to compute and display them. 
Here the attributes <em>Accuracy</em> and <em>Robustness</em> are prepared from the tables for this reason. [Link](plots_template.py)
<br><br>
Then additionally radar charts can be deployed to show attributes of the average performances. Values for <em>RAM/CPU usage, Size and Computation Time</em> are being 
computed here using the tables created before. [Link](radar_chart_template.py)

### Results: Tables, Plots and Radar Charts with corresponding scores
The purpose of this benchmark is to compare different models in the stream setting. Average performances are computed and used for visualizing the learning progress
and creating radar charts for a better view for comparison. Scores are then presented by the radar charts because these charts are the final statement in the chosen setting.
For given algorithms and datasets the benchmark will create a comparable scores using this environment.

### Last Words
This benchmark is very young and not used easily, but it does function properly and can express comparable information and images. 
The computation time was enormously high because every run needs to be monitored individually. Any algorithms which has a high computation time will drastically increase the
overall computation time of the benchmark. On the other hand the benchmark only has to be run once altogether. 
