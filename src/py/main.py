from fastapi import FastAPI
from starlette.responses import HTMLResponse

from db import create_db_and_tables
from router import api_router

app = FastAPI()
app.include_router(api_router, tags=["users"])

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sigmatasking</title>
</head>
<body>
    <h1>Sigmatasking</h1>
    <div> To access docs please visit <a href="/docs">here</a>.</div>
</body>
</html>"""


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return HTMLResponse(template)
