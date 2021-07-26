import requests

def patch_quota(namespace, cpu, ram):
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6Il8tN2hMYkFTOEJuTWNVM1daWkFLRi1EME4xTjI5ekpMUkF2UlRSMXhSZ0EifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6InJvYm90LWFjY291bnQtdG9rZW4tNXB2d2oiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoicm9ib3QtYWNjb3VudCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6ImE0YmZjYmVhLTk2NTItNDU1NC05ZmQwLTRhMmVjNWE3OTBlNCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OnJvYm90LWFjY291bnQifQ.OYNL28wXTM2kLo-yaDzKkyeDdEuTRnDvoSDIa-fI00ELrDbMsmHxZFjqeQiZCawCM6LgHUgVQiPKR75qoHPmHM9g-NQn_lQQP92W8cUSx-D-5bEj7XBWY7KTwBqwE1uuhtEZ9Ft3e6ALUSGhDhVbAIsN1cQuzymCx1DMdKOzBM47JoZmOt4QMYJqhnUmLmfSMvPSc__oRTLPzoBfS3HWTgwSk0VLZN4KhAi3FWwYgFTaeeLA58j9FhvrVOHPiBmIYesVXXG1fBaq_f4LeKg0GFNKECUuEZrEq8tXm83BC0gRQf3lCk-G2q9vYWPW2bssCiWFA6drKooQW47VhAC121w9xL7Q_dj4RTKACU2MyahtdK92aMaDliHJ8wgGgqvFWZSzbryg8a50_YLEEXQY2o6zQkehhkPH7LaJo8U7DXReo9q7wSYViFiT-ajEvmw_vzDypq7f-PkqYRINlAipM16S-79oztiuXLS0b9T6AwRj3IYH1V3yrmN5BEfbCzj1lPTajSr_Z1gnuldscXydzN_liUdxq_bmWzhRbJ02vL3GmTFKZb6fSqXFbB607rdKFm5Vs44yDrV3csJSwS1N-DzMlFPW-oO2YTEdfGzfmudpUsSn58kLOsgIJ3zayrHL8DReq4B_3o-MCGzEhio-fsi_VV9uBnRRcUcwX-hG9fE"
    url = "https://robinhood-6b54420c.hcp.eastus.azmk8s.io/api/v1/namespaces/{}/resourcequotas/rich-mem-cpu-demo".format(namespace)

    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Accept': 'application/json',
        'Connection': 'close',
        'Content-Type': 'application/json-patch+json'
    }
    body = [
        {"op": "replace", "path": "/spec/hard/requests.cpu", "value": cpu},
        {"op": "replace", "path": "/spec/hard/requests.memory", "value": ram}
    ]
    response = requests.request("PATCH", url, headers=headers, verify=False, json=body)
    return response.text
