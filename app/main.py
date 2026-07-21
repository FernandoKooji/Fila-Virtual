#TESTE DE CONEXAO

#===CRIA APLICACAO===

from fastapi import FastAPI

#===INICIA DATABASE===

from app.database.database import initialize_database
from app.routers.ticket_router import router as ticket_router
from app.routers.queue_router import router as queue_router
from app.routers.report_router import router as report_router
from app.routers.page_router import router as page_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Sistema de Fila Virtual"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

initialize_database()

#===REGISTRA OS ROUTERS / ROTAS===

app.include_router(ticket_router)
app.include_router(queue_router)
app.include_router(report_router)
app.include_router(page_router)

