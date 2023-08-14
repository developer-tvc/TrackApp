# TrackApp

Create .env file inside app folder contain credentails for postgres db connection.

# API DETAILS

GET - {{host}}/api/v1/visit?phonenumber=8907794409
Based on the phone number filter the units which the worker is linked. 
Kept phone number as unique field. 

Sample Response : 
[
    {
        "id": 2,
        "name": "Administration"
    },
    {
        "id": 3,
        "name": "Front Desk"
    }
]


POST - {{host}}/api/v1/visit?phonenumber=8907794409
Create visit entry based on the data entered

Sample response :
{
    "status": 201,
    "message": "Visit entry created succesfully",
    "data": {
        "id": 4,
        "visit_date": "2023-08-14T13:59:03.403753Z",
        "latitude": 40.6892,
        "longitude": 74.0445,
        "unit": 3
    }
}

If the phone number is not attach any unit(the worker has no unit) 
then following response returned.
Error Response :
{
    "status": 400,
    "message": "Worker does not associated to the unit"
}