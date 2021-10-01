import os, psutil

# import filestream method
from skmultiflow.data import FileStream
# import data generators
from skmultiflow.data import SEAGenerator
from skmultiflow.data import AGRAWALGenerator
# import classifiers
from skmultiflow.trees import HoeffdingTreeClassifier
from skmultiflow.trees import HoeffdingAdaptiveTreeClassifier
from skmultiflow.lazy import KNNClassifier
from skmultiflow.lazy import KNNADWINClassifier
# import evaluation method
from skmultiflow.evaluation import EvaluatePrequential

noise = .0


max_size = 40000

process = psutil.Process(os.getpid())
cpu1 = psutil.cpu_percent(interval=None)
mem1 = process.memory_info()[0]

# 1. dataset
#stream_elec = FileStream("https://raw.githubusercontent.com/scikit-multiflow/streaming-datasets/master/elec.csv")
stream_air = FileStream("https://raw.githubusercontent.com/scikit-multiflow/streaming-datasets/master/airlines.csv")
#stream_agr = AGRAWALGenerator(balance_classes=True, random_state=8, noise_percentage=noise)
#stream_sea = SEAGenerator(balance_classes=True, random_state=8, noise_percentage=noise)

# 2. classifier
vfdt = HoeffdingTreeClassifier()
hat =  HoeffdingAdaptiveTreeClassifier()
knn = KNNClassifier()
knnadwin = KNNADWINClassifier()

size = 10
# 3. Prequential Evaluation
evaluator = EvaluatePrequential(show_plot=False,
								pretrain_size=size,
								n_wait=size,
								metrics=['accuracy', 'running_time', 'model_size'],
                                max_samples=max_size,
                                #output_file=str(size)+'_knnadwin.csv'
                                )

# 4. Run evaluation
evaluator.evaluate(stream=stream_air, model=vfdt)
#evaluator.evaluate(stream=stream_elec, model=hat)
#evaluator.evaluate(stream=stream_elec, model=knn)
#evaluator.evaluate(stream=stream_elec, model=knnadwin)

cpu2 = psutil.cpu_percent(interval=None)
mem2 = process.memory_info()[0]
print("RAM usage: " + str((mem2-mem1)/1024) + " kb")
print((cpu1+cpu2)/2)