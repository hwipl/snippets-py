from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def get_root() -> str:
    return "Hello, world!"


@app.get("/hi", response_class=PlainTextResponse)
def get_hi() -> str:
    return "hi"

@app.get("/hi/{name}", response_class=PlainTextResponse)
def get_hi_name(name: str) -> str:
    return f"hi {name}"

@app.get("/bye", response_class=PlainTextResponse)
def get_bye() -> str:
    return "bye"

@app.get("/bye/{name}", response_class=PlainTextResponse)
def get_bye_name(name: str) -> str:
    return f"bye {name}"
