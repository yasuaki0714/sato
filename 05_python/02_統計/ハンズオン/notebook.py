import pandas as pd
pd.set_option("display.max_columns", 100)
df = pd.read_csv("13101_20202_20202.csv", encoding="CP932")
df.head(3)

df.describe()

