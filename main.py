from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import python_rust

app = FastAPI()
# app.mount('/static', StaticFiles(directory='static'), name='static')


SECRECT_KEY = '69906dd7545790cfbc6dfee552a537f44e1ddcf87f16537490a8e5520c256177'


templates = Jinja2Templates(directory='templates')


@app.get('/')
async def index(request: Request):
    system_os = python_rust.sum_as_string()
    return templates.TemplateResponse('index.html', {'request': request, 'sys': system_os})
