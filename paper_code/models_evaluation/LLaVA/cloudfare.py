import http.client
import json

conn = http.client.HTTPSConnection("api.cloudflare.com")

account_identifier = 'c2e5e5e106e0b8c69e797dd75d0d229d'
database_identifier = 'b3c4749d-28f0-4578-ac16-5851fe8ef922' #'2b852298-2e07-40fa-b8fa-51356dd5b774' #1d844a27-7b0f-478a-9261-4e11045b997e'
table_identifier = 'minicpm_llama3' 

# Headers
headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer VsRg5J5EHTp6uV0tnNvmvMWBlW2XkU_09BjiQVrz"
    }

def test_database():
    """
    returns the statistics about the whole database we are using. useful as a test. 
    """
    conn.request("GET", f"/client/v4/accounts/{account_identifier}/d1/database/{database_identifier}", headers=headers)
    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

def post_request(query, params):
    """
    Default POST request to the database.
    """
    payload = json.dumps({"sql": query, "params": params})

    conn.request("POST", f"/client/v4/accounts/{account_identifier}/d1/database/{database_identifier}/query", payload, headers)
    res = conn.getresponse()
    data = res.read()

    response_string = data.decode("utf-8")
    response_json = json.loads(response_string)
    return response_string, response_json

def select_all_classified():
    query = f'SELECT * FROM {table_identifier} WHERE Pred_Label IS NOT NULL;'
    params = []

    response_string, response_json = post_request(query, params)
    print(response_string)
    res_data = response_json['result'][0]['results']

    return res_data
