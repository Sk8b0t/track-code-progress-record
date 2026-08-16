from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import format,formatter
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note=APIRouter()
templates=Jinja2Templates(directory="templates")



@note.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    newDocs = []
    docs = conn.notes.notes.find({})
    for item in docs:
        newDocs.append({ "id": str(item["_id"]),
                "title": item["title"],
                "desc": item["desc"],
                "important": item["important"]})
    
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"newDocs": newDocs}
    )

@note.post("/")
async def create_item(req:Request):
    form=await req.form()
    formDict=dict(form)
    formDict["important"]= True if formDict["important"]=="on" else False
    note=conn.notes.notes.insert_one(formDict)
    return {"Success": True}

