import ipfshttpclient

# ** add part
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/8560')  # Connects to: /dns/localhost/tcp/5001/http
add_info = client.add('hello.sh').as_json()
print(add_info)

# ** retrieve part
file_content = client.cat(add_info["Hash"])
print(file_content.decode('utf-8'))