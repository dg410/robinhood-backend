from flask import Flask
import requests

app = Flask(__name__)


@app.route('/clients')
def get_splunk():
    url = "https://40.71.31.225:8089/services/search/jobs"

    payload = 'search=search%20index%3D_internal&exec_mode=oneshot&output_mode=json&earliest=-1h'
    headers = {
        'Authorization': 'Basic YWRtaW46QWRtaW4xMjM0NTY=',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, verify=False, data=payload)
    return(response.text)


if __name__ == '__main__':
    app.run()
