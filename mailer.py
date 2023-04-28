import requests

url = "https://send.api.mailtrap.io/api/send"

payload = "{\"from\":{\"email\":\"mailtrap@lotus.com\",\"name\":\"Mailtrap Test\"},\"to\":[{\"email\":\"janroederer@web.de\"}],\"subject\":\"You are awesome!\",\"text\":\"Congrats for sending test email with Mailtrap!\",\"category\":\"Integration Test\"}"
headers = {
  "Api-Token": "eb93a98722f3f4521acc1c819d223628",
  "Content-Type": "application/json"
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)