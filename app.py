from flask import Flask
import request_quota
import request_splunk
import json

app = Flask(__name__)


@app.route('/clients/<search_type>/<span>')
def get_stats(search_type, span):
    if span not in ["1mon", "3mon", "6mon"]:
        return "{'error': 'Wrong time span'}"
    return json.dumps(request_splunk.splunk(search_type, span))



@app.route('/quota/<namespace>/<cpu>/<ram>')
def change_quota(namespace, cpu, ram):
    return request_quota.patch_quota(namespace, cpu, ram)


if __name__ == '__main__':
    app.run()
