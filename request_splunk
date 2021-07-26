import requests


def splunk(search_type, span):
    url = "https://40.71.31.225:8089/services/search/jobs"
    if search_type == "stats":
        search = 'search=search%20source%3D%22text.txt%22%20host%3D%22splunk-hackaton%22%20index%3D%22ocp-data%22%20sourcetype%3D%22aaa%22%20%7C%20stats%20perc90(ram)%20as%20ram90%20perc90(cpu)%20as%20cpu90%20max(ram)%20as%20maxram%20max(cpu)%20as%20maxcpu%20by%20namespace'
    elif search_type == "data":
        search = "search=search%20source%3D%22text.txt%22%20host%3D%22splunk-hackaton%22%20index%3D%22ocp-data%22%20sourcetype%3D%22aaa%22%7C%20timechart%20%20span%3D1h%20values(ram)%20as%20ram%20values(cpu)%20as%20cpu%20by%20namespace"
    payload = '{}&exec_mode=oneshot&output_mode=json&earliest=-{}'.format(search, span)
    headers = {
        'Authorization': 'Basic YWRtaW46QWRtaW4xMjM0NTY=',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, verify=False, data=payload)
    return response.json()["results"]
