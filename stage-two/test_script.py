""" This script automate action of performing CRUD operation an endpoint """
import os
import requests

ENDPOINT = "http://hngx-2.iyktech.tech/api"

def get_request(id=1):
    """ 
        Test get request
        take one arg the id of
        the to query.
    """
    
    endpoint = f"{ENDPOINT}/{id}"
    try:
        response = requests.get(url=endpoint)
        response.raise_for_status()
    except:
        print("GET TEST FAILED...")
        #print(response.json()) 
        return
    print(response.json(), response.status_code, "GET")
    return 
    
def post_request(data={"name":"mark"}):
    """ 
        Test Post request 
        takes one arg the user data.
        to create
    """
                
    try:
        response = requests.post(url=ENDPOINT, json=data)
        response.raise_for_status()
    except:
        print("CREATE TEST FAILED...")
        #print(response.json())
        return
    print(response.json(), response.status_code, "POST")
    return response.json()["id"]

def put_request(data={"name":"cally"}, id=1):
    """ 
       Test PUT request, takes two args
       first arg the data to be use for update  
       second arg the id of the user. 
    """

    endpoint = f"{ENDPOINT}/{id}"
    try:
        response = requests.put(url=endpoint, json=data)
        response.raise_for_status()
    except:
        print("UPDATE TEST FAILED...")
        #print(response.json())
        return
    print(response.json(), response.status_code, "PUT")
    return 
    
def delete_request(id=1):
    """ 
        Test DELETE request, takes in the
        id of the user as an arg    
    """
    
    endpoint = f"{ENDPOINT}/{id}"
    try:
        response = requests.delete(url=endpoint)
        response.raise_for_status()
    except:
        print("DELETE TEST FAILED...")
        #print(response.json())
        return
    print(response.status_code, "DELETE")
    return 

def run_test():
    """ Execute the script """
    id = post_request()
    get_request(id)
    put_request({"name":"testname"}, id)
    delete_request(id)

if __name__ == "__main__":
    run_test()

    
