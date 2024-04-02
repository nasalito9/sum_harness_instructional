"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fname = "3vars_dataset.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
total_time = df[var_names[1]].values.tolist()
mflops_time = df[var_names[2]].values.tolist()
memBandWidth = df[var_names[3]].values.tolist()
memoryLatency = df[var_names[4]].values.tolist()

mflops1, mflops2, mflops3 = [], [], []

for i in range(0, 5):
    mflops1.append(mflops_time[i])
    mflops2.append(mflops_time[i + 5])
    mflops3.append(mflops_time[i + 10])

print(mflops1)
print(mflops2)
print(mflops3)

plt.title("Comparison of 3 Codes")

# here, we are plotting the raw values read from the input .csv file, which
# we interpret as being "time" that maps directly to the y-axis.
#
# what if we want to plot MFLOPS instead? How do we compute MFLOPS from
# time and problem size? You may need to add some code here to compute
# MFLOPS, then modify the plt.plot() lines below to plot MFLOPS rather than time.
barWidth = 1

# Set position of bar on X axis
#plt.xscale("log")
#plt.yscale("log")

X_axis = np.arange(len(mflops1))

plt.bar(X_axis + 0, mflops1, color='b', width=barWidth, edgecolor='grey', label='Direct')
plt.bar(X_axis + 10, mflops2, color='r', width=barWidth, edgecolor='grey', label='Indirect')
plt.bar(X_axis + 20, mflops3, color='g', width=barWidth, edgecolor='grey', label='Vector')

plt.xlabel("Problem Sizes")
plt.ylabel("Runtime")

varNames = ["Direct", "Indirect", "Vector"]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.show()

# EOF
