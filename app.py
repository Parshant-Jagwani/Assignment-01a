import uvicorn                  # pip install uvicorn
from fastapi import FastAPI     # pip install fastapi

app = FastAPI()

#Declare Counter
counter = 0

# Define a Home Route
@app.get("/")
def get_home():
    """
    Return the Response from Home Route
    """
    return "In this app while hiting the reload it will let you know \n how many time it hited and mulitiply by 2"

# Define a Home Route
@app.get("/hits")
def get_hits():
    """
    Return the Response from Home Route
    """
    global counter
    global sum 
    counter = counter + 1 
    sum = 2 * counter
    return f"I have been hit {counter} times, counter 2 X {counter}={sum} " 

uvicorn.run(app)
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=1010)

# for runing server online EC2 Instance
# uvicorn.run(app, host="0.0.0.0", port=80) 