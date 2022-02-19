import pandas as pd
#import json

data = {
	"Product": ["Desktop Computer","Tablet","iPhone","Laptop"],
	"Price":[700,250,800,1200]
}

df = pd.DataFrame(data, columns=['Product', 'Price'])

df.to_json(r'json_output/test1.json', indent=4)
df.to_json(r'json_output/split.json',orient='split', indent=4)
df.to_json(r'json_output/records.json',orient='records', indent=4)
df.to_json(r'json_output/index.json',orient='index', indent=4)
df.to_json(r'json_output/columns.json',orient='columns', indent=4)
df.to_json(r'json_output/values.json',orient='values', indent=4)
df.to_json(r'json_output/table.json',orient='table', indent=4)


"""
result = df.to_json(orient='split')
parsed = json.loads(result)
a = json.dumps(parsed, indent=4)
print(a)
"""