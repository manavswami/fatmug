
NOTE : JWT token should be pass in header while using api 

like this as shown in image 

![image](https://github.com/manavswami/fatmug/assets/24460055/0fff63ad-c338-46f3-af7f-c3c5ed13d62f)



----------------------------------------------------------------POST method---------------------------------------------------------------------------



to resgister vendor  we have to use  following curl


for post method :

curl --location 'https://manavswami.pythonanywhere.com/api/vendors/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNzA2MjY3LCJpYXQiOjE3MDE2MTk4NjcsImp0aSI6ImU0ZWRkMjNjNjQ4MDRiODhiMjkzMjgzZjU5MGFhNzM0IiwidXNlcl9pZCI6Mn0.yN7W3DfyLa_l-qtMBw6BaXwmrf73TLQazwxwVf7lbvU' \
--data '{   
    "contact_details": "my 1 11112sa  vd  22contact",
    "name":"vendor",
    "address": "my22 address"
}'

url :https://manavswami.pythonanywhere.com/api/vendors/


body:
{   
    "contact_details": "my 1   vd  22contact",
    "name":"vendor",
    "address": "my22 address"
}

![image](https://github.com/manavswami/fatmug/assets/24460055/9153b410-1bac-42c3-b801-d519b5eb3c31)





----------------------------------------------------------------Get method---------------------------------------------------------------------------

Get method : get all vendor list 


curl --location 'https://manavswami.pythonanywhere.com/api/vendors/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDQ0NDg0LCJpYXQiOjE3MDEzNTgwODQsImp0aSI6IjY2ZWUxMGRiOTIyMzQxYjdhMDY2Mjc3NTg4YjQzZmUyIiwidXNlcl9pZCI6M30.X3IvmV0dJrmgFoVDiIfBYNjMX8DnYwS8-2OzmdYiMxM' \
--data ''



url : https://manavswami.pythonanywhere.com/api/vendors/
method :get

![image](https://github.com/manavswami/fatmug/assets/24460055/e93ff549-edae-400c-97b5-438fc9399065)


----------------------------------------------------------------Get method---------------------------------------------------------------------------


Get method :  Retrieve a specific vendor's details.


curl --location 'https://manavswami.pythonanywhere.com/api/vendors/123/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDQ0NDg0LCJpYXQiOjE3MDEzNTgwODQsImp0aSI6IjY2ZWUxMGRiOTIyMzQxYjdhMDY2Mjc3NTg4YjQzZmUyIiwidXNlcl9pZCI6M30.X3IvmV0dJrmgFoVDiIfBYNjMX8DnYwS8-2OzmdYiMxM' \
--data ''


url: https://manavswami.pythonanywhere.com/api/vendors/{vendor_id}/
method :get


![image](https://github.com/manavswami/fatmug/assets/24460055/faa0e6c4-789c-4948-9dd7-b0d211b7eebb)


----------------------------------------------------------------PUT method---------------------------------------------------------------------------



to edit and vendor details we have to use following curl 

curl --location --request PUT 'https://manavswami.pythonanywhere.com/api/vendors/123/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDQ0NDg0LCJpYXQiOjE3MDEzNTgwODQsImp0aSI6IjY2ZWUxMGRiOTIyMzQxYjdhMDY2Mjc3NTg4YjQzZmUyIiwidXNlcl9pZCI6M30.X3IvmV0dJrmgFoVDiIfBYNjMX8DnYwS8-2OzmdYiMxM' \
--header 'Content-Type: application/json' \
--data '{   
    "contact_details": "my 1   vd  22contact",
    "address": "my22 addre111ss"
}'



url :https://manavswami.pythonanywhere.com/api/vendors/{{vendor_code}}/
method :put
body :
{   
    "contact_details": "my 1   vd  22contact",
    "address": "my22 addre111ss"
}

![Alt text](image-5.png)

![image](https://github.com/manavswami/fatmug/assets/24460055/72b887ab-8a78-4513-acfa-9b75a17780c7)


----------------------------------------------------------------DELETE method-------------------------------------------------------------------------



to delete vendor 
use this url
curl --location --request DELETE 'https://manavswami.pythonanywhere.com/api/vendors/22/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDQ0NDg0LCJpYXQiOjE3MDEzNTgwODQsImp0aSI6IjY2ZWUxMGRiOTIyMzQxYjdhMDY2Mjc3NTg4YjQzZmUyIiwidXNlcl9pZCI6M30.X3IvmV0dJrmgFoVDiIfBYNjMX8DnYwS8-2OzmdYiMxM' \
--data ''


url : https://manavswami.pythonanywhere.com/api/vendors/{{vendor_code}}/
method :delete

![image](https://github.com/manavswami/fatmug/assets/24460055/fef13e80-0f78-4323-999f-91f2ddda98e0)
