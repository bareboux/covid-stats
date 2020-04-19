import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt 

df = pd.read_csv("covid_data.csv", usecols = ["Date", "Country/Region", "Confirmed", "Recovered", "Deaths"], index_col=[1])
population = pd.read_csv("population.csv", index_col=[0])
df_diff_nodate = df[["Confirmed", "Recovered", "Deaths"]].diff()

fig, axs = plt.subplots(nrows=3, ncols=1, sharex=True)

#countries = ["Russia", "Italy", "Spain", "Poland"]
countries = ["Russia", "Poland"]
for name in countries:
    axs[0].plot(df.loc[name].Date, df.loc[name].Confirmed, label = name)
    axs[1].plot(df.loc[name].Date, df.loc[name].Confirmed/population.loc[name].Population*100, label = name)
    axs[2].plot(df.loc[name].Date, df_diff_nodate.loc[name].Confirmed, label = name)

for i in range(3):
    axs[i].set_ylabel("cases", fontsize = 14)
    axs[i].xaxis.set_major_locator(plt.MaxNLocator(10))
    axs[i].set_xlim(40)
    axs[i].set_ylim(0)
    axs[i].grid()
    axs[i].legend()

axs[1].set_ylabel("cases_%", fontsize = 14)
axs[2].set_xlabel("date", fontsize=14)
axs[2].set_ylabel("cases_diff", fontsize = 14)

plt.show() 