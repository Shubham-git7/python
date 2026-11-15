#Let's create our own api
from fastapi import FastAPI
from day1.system_utils import get_system_info #this is a concept of importing a function from another module in python , import is a statement used to include the definitions (functions, classes, variables, etc.) from another module into the current module. In this case, it imports the get_system_info() function defined in the system_utiks module so that it can be used within the api.py file.

app = FastAPI(title="Devops utilities API") #this is a concept of creating an instance of the FastAPI class in python , FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It allows you to define your API endpoints and their behavior using Python functions and decorators. 

@app.get("/hello") #this is a concept of defining a GET endpoint in python , GET is an HTTP method used to retrieve data from a server. In this case, it defines a GET endpoint at the root URL ("/") of the API using the @app.get() decorator. When a client sends a GET request to this endpoint, the associated function will be executed.

def hello(): #this is a concept of defining a function in python , function is a block of reusable code that performs a specific task. In this case, it defines a function named hello() that will be executed when the GET request is made to the "/hello" endpoint.
    return {"message": "Hello, World!"} #this is a concept of returning a response in python , response is the data sent back from the server to the client after processing a request. In this case, it returns a JSON response containing a message key with the value "Hello, World!" when the hello() function is executed. 

#now in terminal install uvicorn via pip install uvicorn and run the command uvicorn api:app --reload to start the server and access the endpoint via http://
# also you need fastapi and pydantic library to run the api so install via pip install fastapi pydantic // pip install "fastapi[standard]" to install all the dependencies of fastapi and pydantic library
# just recall what we install : first we install fastapi and pydantic library via pip install fastapi pydantic // pip install "fastapi[standard]" to install all the dependencies of fastapi and pydantic library
#use fastapi dev server to run the api via uvicorn api:app --reload and access the endpoint via http://
######################################################RUN successfully 
# now we can try cpu check within our own file creation
@app.get("/metrics") #this is a concept of defining a GET endpoint in python , GET is an HTTP method used to retrieve data from a server. In this case, it defines a GET endpoint at the root URL ("/") of the API using the @app.get() decorator. When a client sends a GET request to this endpoint, the associated function will be executed.
def metrics():
    get_system_info() #this is a concept of function call in python , function call is a process of invoking a function by its name and passing the required arguments to it. In this case, it calls the get_system_info() function defined in the system_utiks module to retrieve and print the system information.
    return get_system_info() #this is a concept of returning a response in python , response is the data sent back from the server to the client after processing a request. In this case, it returns the system information obtained from the get_system_info() function when the metrics() function is executed.