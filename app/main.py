#TESTE DE CONEXAO

#===CRIA APLICACAO===

from fastapi import FastAPI

#===INICIA DATABASE===

from app.database.database import initialize_database

from app.routers.ticket_router import router as ticket_router
from app.routers.queue_router import router as queue_router
from app.routers.report_router import router as report_router

app = FastAPI(
    title="Sistema de Fila Virtual"
)

initialize_database()

#===REGISTRA OS ROUTERS / ROTAS===

app.include_router(ticket_router)
app.include_router(queue_router)
app.include_router(report_router)