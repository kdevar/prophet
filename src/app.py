import pandas as pd
from fbprophet import Prophet


df = pd.read_csv('sample.csv')
print(df.head())
m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=365)
future.tail()
forecast = m.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())