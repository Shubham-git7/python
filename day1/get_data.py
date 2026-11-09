import requests

# Here i use pip install requests to install the requests library in python , requests library is a popular third-party library in python that allows you to send HTTP requests and handle responses easily. It provides a simple and intuitive API for making GET, POST, PUT, DELETE, and other types of HTTP requests, as well as handling cookies, headers, and authentication.
 
url  = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url=url) #this is a concept of GET request in python , GET request is a method used to retrieve data from a specified resource on the web. In this case, it sends a GET request to the specified URL using the requests library and stores the response in the response variable.
print(response.json()) #this is a concept of print in python , print is a built-in function that outputs the specified message to the console or other standard output device. In this case, it prints the status code of the HTTP response received from the GET request made to the specified URL using the requests library. The status code indicates the result of the request, such as 200 for success, 404 for not found, etc.

