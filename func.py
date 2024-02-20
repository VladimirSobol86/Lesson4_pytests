import requests
import yaml
import logging
with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)

  
# def login():
#     response = requests.post(url="https://test-stand.gb.ru/gateway/login",
#     data={'username': data['login'], 'password': data['password']})
#     return response.json()['token']
def login():
    if data['password'] and data['login']:
        logging.info("Login and password are entered")
        response = requests.post(url="https://test-stand.gb.ru/gateway/login",
        data={'username': data['login'], 'password': data['password']})
        if 'token' in response.json():
            logging.info("Login and password are correct")
            return response.json()['token']
        else:
            logging.exception("Login or password is incorrect")
    else:
        logging.exception("Login or password is empty")

def get_post(token):
    resource = requests.get(data['url'],
                            headers={"X-Auth-Token": token})                          
    logging.info("Get own posts")
    return resource.json()

def create_post(token):
    resource = requests.post(data['url'],
                            headers={"X-Auth-Token": token},
                            params={"title": data['post_title'],
                                    "description": data['post_description'],
                                    "content": data['post_content']})
    logging.info("Create post")
    return resource.json()

#print(create_post(login()))
# print(get_post(login()))