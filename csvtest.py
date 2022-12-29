
df_sales=pd.read_csv("sales.csv",index_col=["Sales_No"])
lst= ["C03", "C09"]


n=[]
for i in df_sales["Customer_ID"]:
    if i in lst:
       n.append(i) 
print(n)

