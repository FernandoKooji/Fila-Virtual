# ============================
# Imports
# ============================

from fastapi import APIRouter

from app.schemas.report import (
    ReportSummaryResponse
)

from app.services.report_service import (
    get_report_summary
)


# ============================
# Router
# ============================

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


# ============================
# Routes
# ============================

@router.get(
    "/summary",
    response_model=ReportSummaryResponse
)
def report_summary_route():

    return get_report_summary()