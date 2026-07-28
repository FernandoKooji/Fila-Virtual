from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get(
    "/",
    response_class=HTMLResponse
)
def index(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@router.get(
    "/attendant",
    response_class=HTMLResponse
)
def attendant(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="attendant.html"
    )