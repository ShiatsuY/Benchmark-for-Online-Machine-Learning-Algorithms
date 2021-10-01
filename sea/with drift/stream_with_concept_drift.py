import os, psutil

# import filestream method
from skmultiflow.data import FileStream
# import data generators
from skmultiflow.data import SEAGenerator
from skmultiflow.data import AGRAWALGenerator
from skmultiflow.data import ConceptDriftStream
# import classifiers
from skmultiflow.trees import HoeffdingTreeClassifier
from skmultiflow.trees import HoeffdingAdaptiveTreeClassifier
from skmultiflow.lazy import KNNClassifier
from skmultiflow.lazy import KNNADWINClassifier
# import evaluation method
from skmultiflow.evaluation import EvaluatePrequential

max_size = 40000

process = psutil.Process(os.getpid())
cpu1 = psutil.cpu_percent(interval=None)
mem1 = process.memory_info()[0]

size = 10
noise = .0

# 1. dataset
#stream = FileStream("https://raw.githubusercontent.com/scikit-multiflow/streaming-datasets/master/elec.csv")
#stream = FileStream("https://raw.githubusercontent.com/scikit-multiflow/streaming-datasets/master/airlines.csv")
#stream = AGRAWALGenerator(balance_classes=True, random_state=8, noise_percentage=noise)
#stream = SEAGenerator(balance_classes=True, random_state=8, noise_percentage=noise)
stream = ConceptDriftStream(stream=SEAGenerator(
								balance_classes=True,
								classification_function=0,
								random_state=8,
								noise_percentage=noise,
								),
							drift_stream=SEAGenerator(
								balance_classes=True,
								classification_function=2,
								random_state=8,
								noise_percentage=noise,
								),
							position=20000
							)

# 2. classifier
vfdt = HoeffdingTreeClassifier()
hat =  HoeffdingAdaptiveTreeClassifier()
knn = KNNClassifier()
knnadwin = KNNADWINClassifier()

# 3. Prequential Evaluation
evaluator = EvaluatePrequential(show_plot=True,
								pretrain_size=size,
								n_wait=size,
								metrics=['accuracy', 'running_time', 'model_size'],
                                max_samples=max_size,
                                #output_file=str(size)+'_n'+str(noise)+'_knnadwin.csv'
                                )

# 4. Run evaluation
evaluator.evaluate(stream=stream, model=vfdt)
#evaluator.evaluate(stream=stream, model=hat)
#evaluator.evaluate(stream=stream, model=knn)
#evaluator.evaluate(stream=stream, model=knnadwin)

cpu2 = psutil.cpu_percent(interval=None)
mem2 = process.memory_info()[0]
print("RAM usage: " + str((mem2-mem1)/1024))
print((cpu1+cpu2)/2)