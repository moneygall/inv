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
fjson_file = open('json_data/h_all_20221130_001.json', 'r', encoding="utf-8_sig")
df=pd.read_json(fjson_file)#.transpose()
dt= pd.DataFrame(df)
print(df[df['name'].isin(['株式会社ＴＫＣ', '株式会社山本製作所'])].filter(["name","registratedNumber"]))
