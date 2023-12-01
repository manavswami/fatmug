to resgister vendor  we have to use  following curl

NOTE : JWT token should be pass in header while using api 

like this as shown in image 
![image](https://github.com/manavswami/fatmug/assets/24460055/decda016-a559-45aa-b78a-4a8489a94136)


    or

![image](https://github.com/manavswami/fatmug/assets/24460055/0fff63ad-c338-46f3-af7f-c3c5ed13d62f)





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
method :post
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

![image](https://github.com/manavswami/fatmug/assets/24460055/0f7707c8-aae6-4b9e-9e9f-94eb7e899faf)


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
method : put
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
![image](https://github.com/manavswami/fatmug/assets/24460055/21692c73-ebdb-4efd-ac29-6dc2eae980e1)



to delete po_order

curl --location --request DELETE 'https://manavswami.pythonanywhere.com/api/purchase_orders/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNTQwNzA0LCJpYXQiOjE3MDE0NTQzMDQsImp0aSI6IjM2NTYwNjQ3NjZhNzRjYjE4M2QwZjE1YjM3MTcxYTBhIiwidXNlcl9pZCI6Mn0.q7vaef15xqcwk0F1pA_Tr6PSu6iV9t_ecBhD_BAoqos' \
--data ''

url:https://manavswami.pythonanywhere.com/api/purchase_orders/{po_order}/

![image](https://github.com/manavswami/fatmug/assets/24460055/b30f638f-4c20-4fcc-8b75-0579059831bd)
