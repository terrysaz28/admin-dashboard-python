import pandas as pd

df = pd.read_excel("sales_data.xlsx", engine="openpyxl")
df = df.dropna()

summary = df.groupby("Department")["Sales"].sum()

summary.to_excel("report.xlsx", engine="openpyxl")

print("Excel report created!")