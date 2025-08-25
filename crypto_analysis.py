import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
df=pd.read_csv("Portfoliyo/Crypto Currency/data/coin_Bitcoin.csv")
print(df.head(10))
#Dataset info & summary
print(df.info())
print(df.describe())
#Check any missing value
print(df.isnull().sum())
#Check any duplicates
print(df.duplicated().sum())
#Convert Date into datetime
df["Date"]=pd.to_datetime(df["Date"])
#Basic statistics of high value
sns.histplot(df['High'],kde=True)
plt.show()
#Line plot for open,high,low,close prices
plt.figure(figsize=(32,6))
plt.plot(df["Date"],df["Open"],label="Open",color="green")
plt.plot(df["Date"],df["High"],label="High",color="blue")
plt.plot(df["Date"],df["Low"],label="Low",color="red")
plt.plot(df["Date"],df["Close"],label="Close",color="orange")
plt.title("Bitcoin Prices Trends over Time")
plt.xlabel("Date")
plt.ylabel("Prices (USD)")
plt.show()
#Line plot volume over marketcap
plt.figure(figsize=(12,6))
plt.plot(df["Date"],df["Volume"],label="Volume",color="purple")
plt.plot(df["Date"],df["Marketcap"],label="Marketcap",color="brown")
plt.title("Bitcoin Volume over Marketcap over the Time")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.show()
#We use scattered plot to check relation between high  prices and volume
plt.figure(figsize=(10,6))
sns.scatterplot(x="Volume",y="High",data=df,color="yellow")
plt.title("High Prices vs Volume")
plt.xlabel("Volume")
plt.ylabel("High")
plt.show()
#Correlation Heatmap
numeric_df=df.select_dtypes(include="number")
plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
fig=go.Figure(data=[go.Candlestick(
    x=df["Date"],
    open=df["Open"],
    high=df["High"],
    low=df["Low"],
    close=df["Close"]
)])
fig.update_layout(
    title="Crypto Candlestick Chart",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    xaxis_rangeslider_visible=False
)
fig.show()