# django-drf-post-like-unlike

## local setup 
- win
  - py -m venv venv
  - venv\Scripts\activate
  - pip install -r req.txt
- linux
  - python3 -m venv venv
  - venv/bin/activate
  - pip install -r req.txt


### endpoints - just create json file and import in thunder client in vscode
{
    "client": "Thunder Client",
    "collectionName": "django",
    "dateExported": "2023-05-07T07:02:31.109Z",
    "version": "1.1",
    "folders": [],
    "requests": [
        {
            "_id": "8287ae5f-ddea-4fb7-87dc-25ab9c483ddc",
            "colId": "80127b7c-7f83-4016-a284-e0cc82d56899",
            "containerId": "",
            "name": "register",
            "url": "http://127.0.0.1:8000/account/register/",
            "method": "POST",
            "sortNum": 10000,
            "created": "2023-05-06T05:25:04.670Z",
            "modified": "2023-05-06T05:32:28.927Z",
            "headers": [],
            "params": [],
            "body": {
                "type": "json",
                "raw": "{\n  \"username\":\"dhritesh\",\n  \"password\":\"Admin@123\"\n}",
                "form": []
            },
            "tests": []
        },
        {
            "_id": "a084b972-3fd7-4459-baae-8b11690e795b",
            "colId": "80127b7c-7f83-4016-a284-e0cc82d56899",
            "containerId": "",
            "name": "login",
            "url": "http://127.0.0.1:8000/account/login/",
            "method": "POST",
            "sortNum": 20000,
            "created": "2023-05-06T05:32:53.178Z",
            "modified": "2023-05-06T05:33:47.132Z",
            "headers": [],
            "params": [],
            "body": {
                "type": "json",
                "raw": "{\n  \"username\":\"dhritesh\",\n  \"password\":\"Admin@123\"\n}",
                "form": []
            },
            "tests": []
        },
        {
            "_id": "50b806bd-5db1-4a6c-bbc7-8f38f5fb40c3",
            "colId": "80127b7c-7f83-4016-a284-e0cc82d56899",
            "containerId": "",
            "name": "create",
            "url": "http://127.0.0.1:8000/post/create/",
            "method": "POST",
            "sortNum": 30000,
            "created": "2023-05-07T05:43:32.248Z",
            "modified": "2023-05-07T06:45:33.665Z",
            "headers": [
                {
                    "name": "Authorization",
                    "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzNDQyMTExLCJpYXQiOjE2ODM0NDExODIsImp0aSI6ImMxNzQwN2I1Zjc5NTRjYzE4ODMxNDIxZGZmMjhlNDI0IiwidXNlcl9pZCI6MX0.oguVkjmm11H6G2O2GePOG-dOuiHzPnn5bbGW4o5X6Zo"
                }
            ],
            "params": [],
            "body": {
                "type": "formdata",
                "raw": "",
                "form": [
                    {
                        "name": "title",
                        "value": "sdfsdf"
                    },
                    {
                        "name": "content",
                        "value": "sdfsdfs"
                    },
                    {
                        "name": "image",
                        "value": "",
                        "isDisabled": true
                    }
                ],
                "files": [
                    {
                        "name": "image",
                        "value": "d:\\downloads\\angry.png"
                    }
                ]
            },
            "tests": []
        },
        {
            "_id": "0a329845-431e-4ab0-963e-1c81c9117857",
            "colId": "80127b7c-7f83-4016-a284-e0cc82d56899",
            "containerId": "",
            "name": "get",
            "url": "http://127.0.0.1:8000/post/",
            "method": "GET",
            "sortNum": 40000,
            "created": "2023-05-07T06:02:12.738Z",
            "modified": "2023-05-07T06:43:49.807Z",
            "headers": [
                {
                    "name": "Authorization",
                    "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzNDQyMTExLCJpYXQiOjE2ODM0NDExODIsImp0aSI6ImMxNzQwN2I1Zjc5NTRjYzE4ODMxNDIxZGZmMjhlNDI0IiwidXNlcl9pZCI6MX0.oguVkjmm11H6G2O2GePOG-dOuiHzPnn5bbGW4o5X6Zo"
                }
            ],
            "params": [],
            "tests": []
        },
        {
            "_id": "2660fc67-e0c7-4e40-a1b9-75ad85ed708c",
            "colId": "80127b7c-7f83-4016-a284-e0cc82d56899",
            "containerId": "",
            "name": "like",
            "url": "http://127.0.0.1:8000/post/1/like/",
            "method": "PATCH",
            "sortNum": 50000,
            "created": "2023-05-07T06:05:16.190Z",
            "modified": "2023-05-07T06:22:37.338Z",
            "headers": [
                {
                    "name": "Authorization",
                    "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzNDQwODQ4LCJpYXQiOjE2ODM0NDA1NDgsImp0aSI6IjQ1N2IyYjIwNjI2ZDRiMDE4NGY4YTA1NDY1NzA5M2Q4IiwidXNlcl9pZCI6MX0.YPFAUKmEOCX0NQZEWs9MpkdtwgJX_VWZSMZW5GPqXlQ"
                }
            ],
            "params": [],
            "tests": []
        },
        {
            "_id": "161937ae-ce6b-4f86-858a-372af9ecce1d",
            "colId": "80127b7c-7f83-4016-a284-e0cc82d56899",
            "containerId": "",
            "name": "refresh",
            "url": "http://127.0.0.1:8000/account/token/refresh/",
            "method": "POST",
            "sortNum": 60000,
            "created": "2023-05-07T06:20:15.754Z",
            "modified": "2023-05-07T06:43:23.671Z",
            "headers": [],
            "params": [],
            "body": {
                "type": "json",
                "raw": "{\n  \"refresh\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MzUyNzU4MiwiaWF0IjoxNjgzNDQxMTgyLCJqdGkiOiI3YjAwYzU1YWY1N2E0MzI0OWFmZTNhYjYyMDgzMGJkZCIsInVzZXJfaWQiOjF9.D32t2z06kpFaEvA5Wsj_ZbMO7Z1bosHhFQSxQgyet64\"\n}",
                "form": []
            },
            "tests": []
        }
    ]
}







