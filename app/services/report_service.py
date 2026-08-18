# ============================
# Imports
# ============================

from app.database.database import get_connection

from app.database.queries import (
    GET_REPORT_TOTALS,
    GET_REPORT_AVERAGES
)

from app.core.response_mapper import (
    build_success_response
)


# ============================
# Resumo dos relatórios
# ============================

def get_report_summary():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Totais
        cursor.execute(
            GET_REPORT_TOTALS
        )

        totals = cursor.fetchone()

        # Médias
        cursor.execute(
            GET_REPORT_AVERAGES
        )

        averages = cursor.fetchone()

        return build_success_response({

            "total_tickets":
                totals["total_tickets"] or 0,

            "total_finished":
                totals["total_finished"] or 0,

            "total_absent":
                totals["total_absent"] or 0,

            "total_cancelled":
                totals["total_cancelled"] or 0,

            "total_priority":
                totals["total_priority"] or 0,

            "total_normal":
                totals["total_normal"] or 0,

            "average_wait_time_seconds":
                averages["average_wait_time_seconds"],

            "average_service_time_seconds":
                averages["average_service_time_seconds"]

        })

    finally:

        connection.close()