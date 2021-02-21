from flask import Flask
import requests, base64
app = Flask(__name__)

client_id = "356edb8bd2fe40249a700e7671702a6c"
client_secret = "8c265ad9925d4237acb25487aad80a13"

client_credentials = f"{client_id}:{client_secret}"
client_credentials64 = base64.b64encode(client_credentials.encode())
token_url = "https://accounts.spotify.com/api/token"
token_data = {
    "grant_type" : "client_credentials"
}

token_headers = {
    "Authorization" : f"Basic {client_credentials64.decode()}"
}
 
res =  requests.post(token_url, data=token_data, headers=token_headers)
print(res.json())
@app.route('/')
def hello():
    return "Hello World!"
