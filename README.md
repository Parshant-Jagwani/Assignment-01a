## Assignment-01a

First DevOps Assignment Part-01

#Step 1: Identify a Sample Application

Decription:  made a multiplication of url hits counts and actual URL hits count

CMD for verifing the app in vs code: 
  
  pip install uvicorn

  pip install fastapi
  
  python app.py
  
  / dictroy has discription
  
  /hits has url hits count and its multipler of 2.

#Step 2: Identify the Dependencies

link: https://github.com/Parshant-Jagwani/Assignment-01a/blob/master/requirements.txt

Dependencies: uvicorn and fastapi named as requirements.txt

#Step 3 (15 marks): Create a Docker file

File link: https://github.com/Parshant-Jagwani/Assignment-01a/blob/master/Dockerfile

#Step 4: Build the Docker Image

  CMD: docker images
  
  Output: https://github.com/Parshant-Jagwani/Assignment-Outputs/blob/main/docker%20image%20cmd.png

  CMD: docker build -t assignment-01a-pj-image:v1 .
  
  Output: https://github.com/Parshant-Jagwani/Assignment-Outputs/blob/main/Docker%20Build%20cmd.png 

  CMD: docker login

  CMD: docker push parshantjagwani/assignment-01a-pj-image:v1

  CMD: docker run -d -p 1010:1010 --name assign-01a 394fa1b73e71

#Step 5: Push the Docker Image to Docker Hub

Output: https://github.com/Parshant-Jagwani/Assignment-Outputs/blob/main/Docker%20push%20cmd.png

#Step 6: Create a GitHub Repository

  CMD: git init
  
  CMD: git add .
  
  CMD: git commit -m "Creating hits counts and hits multiply by 2,  with code and all required files"

Output: https://github.com/Parshant-Jagwani/Assignment-Outputs/blob/main/Creating%20git%20Repo.png

#Step 7: Include a README.md file

included in main Branch

#Step 8: Push the Codebase to GitHub

CMD: git remote add origin https://github.com/Parshant-Jagwani/Assignment-01a

CMD: git push -u origin master  

CMD: git push -u origin master

CMD: git pull

Output: https://github.com/Parshant-Jagwani/Assignment-Outputs/blob/main/Pushing%20code%20on%20git%20hub.png

