from pydantic import BaseModel


# ============================
# Resumo dos relatórios
# ============================

class ReportSummaryResponse(BaseModel):

    success: bool

    total_tickets: int

    total_finished: int

    total_absent: int

    total_cancelled: int

    total_priority: int

    total_normal: int

    average_wait_time_seconds: float | None = None

    average_service_time_seconds: float | None = None