import psutil
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path


import uvicorn
BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))


app = FastAPI()

@app.get("/",response_class=HTMLResponse)
def index(request:Request):
    cpu_percent=psutil.cpu_percent()
    mem_percent =psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or mem_percent >80 :
        Message ="High CPU or Memory Utilisation detected, please scale UP..."
    return templates.TemplateResponse("index.html",{"request":request,"cpu_percent":cpu_percent,"mem_percent":mem_percent,"message":Message})
        
    #return f"CPU utilisation: {cpu_percent} and Memory Utilisation : {mem_percent}"
    return

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)



