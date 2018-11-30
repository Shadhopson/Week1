import requests
import json
summary_dict = {}
for i in range(20160611, 20160616):
    web_address ='http://api.wunderground.com/api/de9ed9b1fa35be23/history_'+str(i)+'/q/NY/New_York.json'
    resp = requests.get(web_address)
    json_data = json.loads(resp.text)
    print i
    wanted_section = json_data["history"]["observations"][10]
    summary_dict[str(i)] ={"tempi":wanted_section["tempi"], "condition":wanted_section["conds"], "rain":wanted_section["rain"], "snow":wanted_section["snow"], "thunder":wanted_section["thunder"] }

print summary_dict

