from pathlib import Path


import requests

r = requests.head("https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv")
print(r.headers["Content-Length"])
print(r.headers)
print(len(open(Path.cwd() / "covid-stats" / "time-series-19-covid-combined.csv").readlines(  )))
print((Path.cwd() / "covid-stats" / "time-series-19-covid-combined.csv").stat().st_size)
#print(parsedate(r.headers))

#df = pd.read_csv(Path.cwd() / "covid-stats" / "time-series-19-covid-combined_csv.csv", usecols = ["Date", "Country/Region", "Confirmed", "Recovered", "Deaths"], index_col=[1])
#df = pd.read_csv(r.content, usecols = ["Date", "Country/Region", "Confirmed", "Recovered", "Deaths"], index_col=[1])
print(Path.cwd())
print("dsssd")