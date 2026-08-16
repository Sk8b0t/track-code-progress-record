from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="templates")
conn=MongoClient("mongodb+srv://sayanbiswas0812_db_user:9a19aqqmDjhl5dXz@cluster0.cravppu.mongodb.net")


@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    newDocs = []
    docs = conn.notes.notes.find({})
    for itm in docs:
        newDocs.append({
            "id": str(itm["_id"]),
            "note": itm["note"]
        })
    
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"newDocs": newDocs}
    )


   
    
    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)