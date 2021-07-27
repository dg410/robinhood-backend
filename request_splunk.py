import requests


def splunk(namespace, span):
    url = "https://40.71.31.225:8089/services/search/jobs"
    search_stats = "search=search%20source%3D%22text.txt%22%20host%3D%22splunk-hackaton%22%20index%3D%22ocp-data%22%20sourcetype%3D%22aaa%22%20namespace%3D{}%7Cstats%20perc90(ram)%20as%20perc99ram%20perc90(ram_request)%20as%20perc99ramreq%20max(ram)%20as%20maxram%20values(ram_quota)%20as%20ram_quota".format(namespace)
    search_data = 'search=search%20source%3D%22text.txt%22%20host%3D%22splunk-hackaton%22%20index%3D%22ocp-data%22%20sourcetype%3D%22aaa%22%20namespace%3D{}%7C%20timechart%20span%3D1h%20values(ram)%20as%20ram%20values(cpu)%20as%20cpu%20values(ram_quota)%20as%20ram-quota%20values(cpu_quota)%20as%20cpu-quota'.format(namespace)
    results = []
    for search in [search_stats, search_data]:
        payload = '{}&exec_mode=oneshot&output_mode=json&earliest=-{}'.format(search, span)
        headers = {
            'Authorization': 'Basic YWRtaW46QWRtaW4xMjM0NTY=',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, verify=False, data=payload)
        results.append(response.json()["results"])
    return results
