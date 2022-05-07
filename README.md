# RESTful-Web-Service-Implementation-Docker
Prerequisites:
1.Install Docker
2.Install docker and flask extensions in vs code.
Steps:
1. Download the Git zip file.
2. Open in vs code
3. Create the docker image:
    docker build -t challanimg .
    
4.Once the docker image is created, run the "flask-test-sample" in docker container
   docker run -d -p 5000:5000 challanimg
   
5. Open localhost:5000/getchallans/ to get list of challans
6. Open localhost:5000/getchallans/1/ to get a single record
7. Open localhost:5000/getchallans/car/ferrari/ to get list of challans on ferrari car.
