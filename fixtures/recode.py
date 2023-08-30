import json
 
with open('test_data.json', encoding='utf-16') as f:
    data = json.load(f)
with open('test_data_2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)