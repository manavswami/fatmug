to resgister vendor  we have to use  following curl

NOTE : JWT token should be pass in header while using api 

like this as shown in image 
![Alt text](image-2.png)

    or

![Alt text](image-3.png) 




to get all the purchase order details we can use below curl 

curl --location 'https://manavswami.pythonanywhere.com/api/purchase_orders/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDM3NzIwLCJpYXQiOjE3MDEzNTEzMjAsImp0aSI6ImNiMGQzZjE2N2IzYTQ2MDBiNjhlYzYzNGRkMjI0MjM5IiwidXNlcl9pZCI6Mn0.0LxJya6kUTEWQ3kS2Nm4cXqXDB2pNyKzgr6rXKBW-ag' \
--data ''


url : https://manavswami.pythonanywhere.com/api/purchase_orders/


to create order we can use below curl 

curl --location 'https://manavswami.pythonanywhere.com/api/purchase_orders/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDM3NzIwLCJpYXQiOjE3MDEzNTEzMjAsImp0aSI6ImNiMGQzZjE2N2IzYTQ2MDBiNjhlYzYzNGRkMjI0MjM5IiwidXNlcl9pZCI6Mn0.0LxJya6kUTEWQ3kS2Nm4cXqXDB2pNyKzgr6rXKBW-ag' \
--data '
{

    "issue_date":"2023-11-25T12:47:36.031324Z",
    "order_date": "2023-11-25",
    "delivery_date": "2023-11-26",
    "actual_delivery":"2023-11-27",
    "items": 12,
    "quantity": 12,
    "status": "pending",
    "quality_rating": 12.0,
    "acknowledgment_date": null,
    "vendor": 1

}
'


url : https://manavswami.pythonanywhere.com/api/purchase_orders/

body :

{

    "issue_date":"2023-11-25T12:47:36.031324Z",
    "order_date": "2023-11-25",
    "delivery_date": "2023-11-26",
    "actual_delivery":"2023-11-27",
    "items": 12,
    "quantity": 12,
    "status": "pending",
    "quality_rating": 12.0,
    "acknowledgment_date": null,
    "vendor": 1

}


NOTE here "vendor" id is pass not the vendor code

for updating any exiting order  we havr to use following curl


curl --location --request PUT 'https://manavswami.pythonanywhere.com/api/purchase_orders/d1a85337/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDM3NzIwLCJpYXQiOjE3MDEzNTEzMjAsImp0aSI6ImNiMGQzZjE2N2IzYTQ2MDBiNjhlYzYzNGRkMjI0MjM5IiwidXNlcl9pZCI6Mn0.0LxJya6kUTEWQ3kS2Nm4cXqXDB2pNyKzgr6rXKBW-ag' \
--data '{
    "issue_date":"2023-11-25T12:47:36.031324Z",
    "order_date": "2023-11-25",
    "delivery_date": "2023-11-26",
    "actual_delivery":"2023-11-27",
    "items": 12,
    "quantity": 12,
    "status": "pending",
    "quality_rating": 12.0,
    "acknowledgment_date": null,
    "vendor": 1
}'



url: http://127.0.0.1:8000/api/purchase_orders/{po_number}/
body :
{

    "issue_date":"2023-11-25T12:47:36.031324Z",
    "order_date": "2023-11-25",
    "delivery_date": "2023-11-26",
    "actual_delivery":"2023-11-27",
    "items": 12,
    "quantity": 12,
    "status": "pending",
    "quality_rating": 12.0,
    "acknowledgment_date": null,
    "vendor": 1

}
