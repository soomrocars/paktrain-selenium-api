from scrapeTrain2 import getFare2

from fastapi import FastAPI
from typing import Dict,List

app = FastAPI()

listObject = List
@app.post("/train")
async def getTicketData(inputedCities: listObject):
    s1,s2,s3 = inputedCities
    return await getFare2(s1,s2,s3)
#     #["Pak Business Express (LAHORE JN. To KARACHI CANTT)","HYDERABAD JN","DRIGH ROAD"]
#     #["Allama Iqbal Express (KARACHI CANTT To SIALKOT JN.)","KARACHI CANTT","LAHORE JN."]
#     #["Allama Iqbal Express (KARACHI CANTT To SIALKOT JN.)","HYDERABAD JN","RAHIM YAR KHAN"]
