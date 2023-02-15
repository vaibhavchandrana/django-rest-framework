import requests
URL="http://localhost:8000/all_student_detail/"
response_data=requests.get(url=URL)
data=response_data.json()
print(data)