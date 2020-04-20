import pandas as pd
import numpy as np
#import datetime
import matplotlib.pyplot as plt 
from pathlib import Path
import requests

r = requests.get("https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv")
with open(Path.cwd() / "covid-stats" / "time-series-19-covid-combined.csv", "wb") as f:
    f.write(r.content)
df = pd.read_csv(Path.cwd() / "covid-stats" / "time-series-19-covid-combined.csv", usecols = ["Date", "Country/Region", "Confirmed", "Recovered", "Deaths"], index_col=[1])
population = pd.read_csv(Path.cwd() / "covid-stats" / "population.csv", index_col=[0])
df_diff_nodate = df[["Confirmed", "Recovered", "Deaths"]].diff()

fig, axs = plt.subplots(nrows=4, ncols=1, sharex=True)

countries = ["Russia", "Italy", "Spain", "Poland"]
#countries = ["Russia", "Poland"]
for name in countries:
    axs[0].plot(df.loc[name].Date, df.loc[name].Confirmed, label = name)
    axs[1].plot(df.loc[name].Date, df.loc[name].Confirmed/population.loc[name].Population*100, label = name)
    axs[2].plot(df.loc[name].Date, df_diff_nodate.loc[name].Confirmed, label = name)
    axs[3].plot(df.loc[name].Date, df_diff_nodate.loc[name].Confirmed/population.loc[name].Population*100, label = name)

for i in range(4):
    axs[i].xaxis.set_major_locator(plt.MaxNLocator(10))
    axs[i].set_xlim(40)
    axs[i].set_ylim(0)
    axs[i].grid()
    axs[i].legend()
axs[0].set_ylabel("cases", fontsize = 10)
axs[1].set_ylabel("cases_%", fontsize = 10)
axs[2].set_ylabel("daily_growth", fontsize = 10)
axs[3].set_ylabel("daily_growth_%", fontsize = 10)
axs[3].set_xlabel("date", fontsize=10)

plt.show() 