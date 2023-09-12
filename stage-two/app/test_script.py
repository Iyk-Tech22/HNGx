""" This script automate action of performing CRUD operation an endpoint """
import requests

ENDPOINT = "http://localhost:5000/api"

def get_request(id=1):
    """ Test get request """
    ENDPOINT = f"{ENDPOINT}/{id}"
    try:
        response = requests.get(url=ENDPOINT)
        response.raise_for_status()
    except:
        return
    print(response.json())
    return response.status_code

def post_request(data={"name":"mark"}):
    """ Test Post request """
    try:
        response = requests.post(url=ENDPOINT, data=data)
        response.raise_for_status()
    except:
        return
    print(response.json())
    return response.status_code

def put_request(data={"name":"cally"}, id=1):
    """ Test PUT request """

    ENDPOINT = f"{ENDPOINT}/{id}"
    try:
        response = requests.put(url=ENDPOINT, data=data)
        response.raise_for_status()
    except:
        return
    print(response.json())
    return response.status_code
    
def delete_request(id=1):
    """ Test DELETE request """
    ENDPOINT = f"{ENDPOINT}/{id}"
    try:
        response = requests.delete(url=ENDPOINT)
        response.raise_for_status()
    except:
        return "FAILED"
    return response.status_code

def run_test():
    """ Execute the script """
    get_request()
    post_request()
    put_request()
    delete_request()

if __name__ == "__main__":
    run_test()

    
