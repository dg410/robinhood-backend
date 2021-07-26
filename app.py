from flask import Flask
import request_quota
import request_splunk


app = Flask(__name__)


@app.route('/clients/<span>')
def get_stats(span):
    if span not in ["1mon", "3mon", "6mon"]:
        return "{'error': 'Wrong time span'}"
    results = {}
    for namespace in ["poor_project", "rich_project"]:
        results[namespace] = request_splunk.splunk(namespace, span)
    return results



@app.route('/quota/<namespace>/<cpu>/<ram>')
def change_quota(namespace, cpu, ram):
    return request_quota.patch_quota(namespace, cpu, ram)


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == '__main__':
    app.run()
