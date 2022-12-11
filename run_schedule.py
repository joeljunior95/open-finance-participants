import requests
import time

host = 'http://localhost:5000'
endpoint = '/participants/update/all'

def update_database():
    print('Requesting database update')
    r = requests.put(host + endpoint)
    if r.status_code!= 200:
        print("Request failed")
        return False
    else:
        print("Request succeeded")
        return True
if __name__ == '__main__':
    time_to_sleep = 60*60
    while True:
        update_database()
        time.sleep(time_to_sleep)