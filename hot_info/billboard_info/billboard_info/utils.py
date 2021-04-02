import json
with open('./today_data/new2.txt','r',encoding='utf-8') as f:
    text = f.read()
    
    json_t = json.loads(text)
    f.close()
    print(json_t)
