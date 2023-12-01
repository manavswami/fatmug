to resgister vendor  we have to use  following curl

NOTE : JWT token should be pass in header while using api 

like this as shown in image 
![Alt text](image-2.png)

    or

![Alt text](image-3.png) 



for post method :

curl --location 'https://manavswami.pythonanywhere.com/api/vendors/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDQ0NjUzLCJpYXQiOjE3MDEzNTgyNTMsImp0aSI6IjAzZjkzZWNmODVkOTQwYmZiZmVkYmNiODM5YzIwNGFkIiwidXNlcl9pZCI6NH0.d8ZFrAsU1wp9UawJJvl_wRml2hbUo9JW7uzMDplkqAg' \
--data '{   
    "contact_details": "my 1   vd  22contact",
    "address": "my22 address"
}'

url :https://manavswami.pythonanywhere.com/api/vendors/


body:
{   
    "contact_details": "my 1   vd  22contact",
    "address": "my22 address"
}

![Alt text](image-8.png)




filter all order by vendor code



curl --location 'https://manavswami.pythonanywhere.com/api/purchase_orders/?filter_by=123' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDM3NzIwLCJpYXQiOjE3MDEzNTEzMjAsImp0aSI6ImNiMGQzZjE2N2IzYTQ2MDBiNjhlYzYzNGRkMjI0MjM5IiwidXNlcl9pZCI6Mn0.0LxJya6kUTEWQ3kS2Nm4cXqXDB2pNyKzgr6rXKBW-ag' \
--data ''

url :https://manavswami.pythonanywhere.com/api/purchase_orders/?filter_by={vendor_code} 

param {
    filter_by:{vendor_code} 
}

![Alt text](image-7.png)


Get method : get all vendor list 



curl --location 'https://manavswami.pythonanywhere.com/api/vendors/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDQ0NDg0LCJpYXQiOjE3MDEzNTgwODQsImp0aSI6IjY2ZWUxMGRiOTIyMzQxYjdhMDY2Mjc3NTg4YjQzZmUyIiwidXNlcl9pZCI6M30.X3IvmV0dJrmgFoVDiIfBYNjMX8DnYwS8-2OzmdYiMxM' \
--data ''



url : https://manavswami.pythonanywhere.com/api/vendors/



Get method :  Retrieve a specific vendor's details.


curl --location 'https://manavswami.pythonanywhere.com/api/vendors/123/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDQ0NDg0LCJpYXQiOjE3MDEzNTgwODQsImp0aSI6IjY2ZWUxMGRiOTIyMzQxYjdhMDY2Mjc3NTg4YjQzZmUyIiwidXNlcl9pZCI6M30.X3IvmV0dJrmgFoVDiIfBYNjMX8DnYwS8-2OzmdYiMxM' \
--data ''


url: https://manavswami.pythonanywhere.com/api/vendors/{vendor_id}/

![Alt text](image-4.png)



to edit and vendor details we have to use following curl 

curl --location --request PUT 'https://manavswami.pythonanywhere.com/api/vendors/123/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDQ0NDg0LCJpYXQiOjE3MDEzNTgwODQsImp0aSI6IjY2ZWUxMGRiOTIyMzQxYjdhMDY2Mjc3NTg4YjQzZmUyIiwidXNlcl9pZCI6M30.X3IvmV0dJrmgFoVDiIfBYNjMX8DnYwS8-2OzmdYiMxM' \
--header 'Content-Type: application/json' \
--data '{   
    "contact_details": "my 1   vd  22contact",
    "address": "my22 addre111ss"
}'



url :https://manavswami.pythonanywhere.com/api/vendors/{{vendor_code}}/

body :
{   
    "contact_details": "my 1   vd  22contact",
    "address": "my22 addre111ss"
}

![Alt text](image-5.png)



to delete vendor 
use this url
curl --location --request DELETE 'https://manavswami.pythonanywhere.com/api/vendors/22/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDQ0NDg0LCJpYXQiOjE3MDEzNTgwODQsImp0aSI6IjY2ZWUxMGRiOTIyMzQxYjdhMDY2Mjc3NTg4YjQzZmUyIiwidXNlcl9pZCI6M30.X3IvmV0dJrmgFoVDiIfBYNjMX8DnYwS8-2OzmdYiMxM' \
--data ''


url : https://manavswami.pythonanywhere.com/api/vendors/{{vendor_code}}/

![Alt text](image-6.png)
