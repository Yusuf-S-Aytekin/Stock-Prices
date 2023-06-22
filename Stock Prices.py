import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import mplcyberpunk
df=pd.read_csv("stock_data.csv")

tick=[df["Date"].iloc[np.int64(np.round(i))] for i in np.linspace(0,1711,8)]
tick
mpl.rcParams.update(mpl.rcParamsDefault)
plt.style.use("cyberpunk")
fig = plt.figure(figsize=(14,8))
plt.plot(df["Date"], df["FB"], label="Facebook Stock Prices",color=(0.1,0.3,1),linewidth=1)
plt.plot(df["Date"], df["TWTR"], label="Twitter Stock Prices",color=(0.1,0.9,1),linewidth=1)
plt.plot(df["Date"], df["NFLX"], label="Netfix Stock Prices", color=(1,0.25,0.3),linewidth=1)
for g in range(10):
    plt.plot(df["Date"], df["FB"], color=(0.1,0.3,1),alpha=0.03,linewidth=g+1)
    plt.plot(df["Date"], df["TWTR"], color=(0.1,0.9,1),alpha=0.03,linewidth=g+1)
    plt.plot(df["Date"], df["NFLX"], color=(1,0.25,0.3),alpha=0.03,linewidth=g+1)

for color,column,alpha in zip([(0.1,0.3,1),(0.1,0.9,1),(1,0.2,0.35)], df.columns[1:], [0.2,0.18,0.1]):
    plt.fill_between(df["Date"], [0]*len(df),df[column], color=color,alpha=alpha)

plt.xticks(tick)
plt.xlim((tick[0],tick[-1]))
plt.ylim((0,df["NFLX"].max()+30))
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.title("Stock Prices")
plt.legend()
plt.show()