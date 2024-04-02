"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot, and saves it to a file named "MFLOPS.png"

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plot_fname = "memoryBandwidth.png"

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

code1, code2, code3 = [], [], []

for i in range(0, 5):
    code1.append(memBandWidth[i])
    code2.append(memBandWidth[i + 5])
    code3.append(memBandWidth[i + 10])

print(code1)
print(code2)
print(code3)

plt.title("Comparison of 3 Codes")
barWidth = 1

X_axis = np.arange(len(code1))

plt.bar(X_axis + 0, code1, color='b', width=barWidth, edgecolor='grey', label='Direct')
plt.bar(X_axis + 10, code2, color='r', width=barWidth, edgecolor='grey', label='Indirect')
plt.bar(X_axis + 20, code3, color='g', width=barWidth, edgecolor='grey', label='Vector')

plt.ylabel("%memoryBandwidth")

varNames = ["Direct", "Indirect", "Vector"]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

# save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)


plt.show()

# EOF
