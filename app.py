from flask import Flask
import requests
import request_quota


app = Flask(__name__)


@app.route('/clients/<span>')
def get_splunk(span):
    if span not in ["1mon", "3mon", "6mon"]:
        return "{'error': 'Wrong time span'}"
    url = "https://40.71.31.225:8089/services/search/jobs"
    payload = 'search=search%20index%3D_internal&exec_mode=oneshot&output_mode=json&earliest=-{}'.format(span)
    headers = {
        'Authorization': 'Basic YWRtaW46QWRtaW4xMjM0NTY=',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, verify=False, data=payload)
    return(response.text)


@app.route('/quota/<namespace>/<cpu>/<ram>')
def change_quota(namespace, cpu, ram):
    return request_quota.patch_quota(namespace, cpu, ram)


if __name__ == '__main__':
    app.run()
