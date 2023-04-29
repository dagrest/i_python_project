
# Prerequisite
- Build docker image for AWS Mock: **docker build -t aws_mock .**  
- Run command: **docker run --rm -d --name zesty-ec2 -p 4000:4000 aws_mock**  

# Solution docker image  

- Build solution docker image: **docker build -t app_server .**  
- Run command: **docker run -d --rm -p 5000:5000 app_server**  

# Usage  
http://localhost:5000/regions/<region_name>  
Example:  
http://localhost:5000/regions/us-east-1

  
