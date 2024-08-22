import requests
import datetime as dt

# information
USER_NAME = "frenchfernance12"
TOKEN = "hfksu38ejd83lk"
GRAPH_ID = "graph1"

# Creating User
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)


# creating habit graph
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"


headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}


# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)


# posting a pixel
send_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today_date = dt.datetime.now()
formatted_today_date = today_date.strftime("%Y%m%d")

pixel_config = {
    "date": formatted_today_date,
    "quantity": float(input("input KM you ran "))
}

# pixel_response = requests.post(url=send_pixel_endpoint, json=pixel_config, headers=headers)
# print(pixel_response.text)


# updating pixel
update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{formatted_today_date}"

pixel_updated_config = {
    "quantity": float(input("Wrong input? try entering KM again "))
}

# update_pixel_response = requests.put(url=update_pixel_endpoint, json=pixel_updated_config, headers=headers)
# print(update_pixel_response.text)


# deleting pixels
delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{formatted_today_date}"

# delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_pixel_response.text)
