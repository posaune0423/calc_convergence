import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


pref_gdppcs = pd.read_csv('pref_gdppc.csv', sep=',')
pref_gdppc_growth_rates = pd.read_csv('pref_gdppc_growth.csv', sep=',')

initial_gdppcs = list(map(math.log, pref_gdppcs['2016']))

# the array which contains each pref's avg growth rate between 2006 n 2017
growth_avgs = []
for i in range(0, 47):
    row = pref_gdppc_growth_rates.loc[i]
    growth_avgs.append(row.iloc[2:].mean())


# if Correlation coefficient is needed, comment out here
# s1=pd.Series(initial_gdppcs)
# s2=pd.Series(growth_avgs)
# res=s1.corr(s2)
# print(res)

# plot dataframe
plt.scatter(initial_gdppcs, growth_avgs)
plt.ylabel('per capita growth rate, 2006-2017')
plt.xlabel('log 2006 per capita gdp in prefecture')
plt.show()
