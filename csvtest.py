import pandas as pd

df_sales=pd.read_csv("sales.csv",index_col=["Sales_No"])
lst= ["C03", "C09"]

#print(df_sales["Customer_ID"] =="C01")

#print([ i for i in lst if i== "C04"])
n=[]
for i in df_sales["Customer_ID"]:
    if i in lst:
       n.append(i) 
print(n)
