# cj-app
Django 3.1 - Python 3.7

IMPORTANT NOTES:

    1. If the backend require any database please use any IN-MEMORY or SQLLite database Unless mentioned in Questions Otherwise .
    3. Make sure you follow the steps mentioned under "PROJECT START STEPS" and ensure that the steps execute successfully. 
    4. Make sure you follow the steps mentioned under "DOCKER START STEPS" and ensure that the steps execute successfully. 

PROJECT START STEPS:

    Pre-requisites:
    1. Install need python and pip to be installed in your system.


    Steps:
    1. To run this application, do the following:
        1.a. Go to the project root directory.
        1.b. Run the following commands to install dependencies of the app:
        	- pip install -r requirements.txt
        1.c. Run the following command(s) in the terminal/command line to run the app:    
            - python manage.py runserver 0.0.0.0:8080
    
    2. Go to http://localhost:8080 in your browser to view it.

APIS

- Register a driver:
    POST /api/v1/driver/register/
    Request Body: 

         {
            "name": "",               
            "email": "",              
            "phone_number":           
            "license_number": "",     
            "car_number": ""
        } 
    
   Response
        {
        "id": ,
        "name": "",
        "email": "",
        "phone_number":
        "license_number": "",
        "car_number": ""    
        } 
   
 - Share Driver Location
    Request Body: 

        {
            "latitude": 12.972442,
            "longitude": 77.580643 
        }
    Response Body:

        {
            "status": "success"
        }
 
 - Get Nearby Cabs
    Request Body: 

        {
            "latitude": 12.972442,
            "longitude": 77.580643,
        } 
   
   Response Body:  

        {
            "available_cabs": [
                {
                    "name": "",
                    "car_number": "",
                    "phone_number": 
                },
                {
                    "name": "",
                    "car_number": "",
                    "phone_number": 
                },
            ]
        }  



