import json

import requests
from fastapi import FastAPI,Request

app=FastAPI()


@app.get('/chetan')
async def chetan():
    return {"message":"Welcome"}

@app.post('/sales')
async def sales(request:Request):
    requestData = await request.json()

    print(type(requestData))
    #print(requestData)
    for i ,j in requestData.items():
        #print(i)
        print('\n')
        for x, y in j.items():
            print(x,'<----->' ,y)
            r = requests.post('https://stagegw.transnox.com/servlets/Transnox_API_serverstatus', json=requestData)
            print('*********')
            print(r.text)
    return {"received_request_body":  request.body()}

