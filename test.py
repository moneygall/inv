import json
f= "json_data/h_all_20221130_001.json"
json_open = open(f, 'r', encoding="utf-8_sig")
json_load = json.load(json_open)

f2= "json_data/h_all_20221130_002.json"
json_open2 = open(f2, 'r', encoding="utf-8_sig")
json_load2 = json.load(json_open2)

f3= "json_data/h_all_20221130_003.json"
json_open3 = open(f3, 'r', encoding="utf-8_sig")
json_load3 = json.load(json_open3)

f4= "json_data/h_all_20221130_004.json"
json_open4 = open(f4, 'r', encoding="utf-8_sig")
json_load4 = json.load(json_open4)

f5= "json_data/h_all_20221130_005.json"
json_open5 = open(f5, 'r', encoding="utf-8_sig")
json_load5 = json.load(json_open5)


print("json_load", len(json_load))
print("json_load2", len(json_load2))
print("json_load3", len(json_load3))
print("json_load4", len(json_load4))
print("json_load5", len(json_load5))

json_load.extend(json_load2)
json_load.extend(json_load3)
json_load.extend(json_load4)
json_load.extend(json_load5)

#print('株式会社サン企画' in json_load[1100].values())
data_count= len(json_load)
print(f"data-count...{data_count}")
for j in json_load:
    if('株式会社ＴＫＣ' in j.values()):
        print(j["sequenceNumber"], j["registratedNumber"], j["name"], j["address"])
