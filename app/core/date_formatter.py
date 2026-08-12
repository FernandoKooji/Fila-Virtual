# ============================
# Date Formatter
# ============================

"""
Responsável por padronizar a exibição
de datas em toda a aplicação.

Formato padrão:

DD/MM/AAAA HH:MM:SS
"""

# ============================
# Imports
# ============================

from datetime import datetime


# ============================
# Formata data e hora
# ============================

def format_datetime(date_string):

    """
    Converte uma data do SQLite

        2026-08-05 13:25:42

    para

        05/08/2026 13:25:42

    Retorna None caso a data
    seja nula ou inválida.
    """

    if not date_string:

        return None

    try:

        date = datetime.strptime(

            date_string,

            "%Y-%m-%d %H:%M:%S"

        )

        return date.strftime(

            "%d/%m/%Y %H:%M:%S"

        )

    except (

        ValueError,

        TypeError

    ):

        return None


# ============================
# Apenas Data
# ============================

def format_date(date_string):

    """
    Converte

        2026-08-05

    para

        05/08/2026
    """

    if not date_string:

        return None

    try:

        date = datetime.strptime(

            date_string,

            "%Y-%m-%d"

        )

        return date.strftime(

            "%d/%m/%Y"

        )

    except (

        ValueError,

        TypeError

    ):

        return None


# ============================
# Apenas Hora
# ============================

def format_time(date_string):

    """
    Converte

        2026-08-05 13:25:42

    para

        13:25:42
    """

    if not date_string:

        return None

    try:

        date = datetime.strptime(

            date_string,

            "%Y-%m-%d %H:%M:%S"

        )

        return date.strftime(

            "%H:%M:%S"

        )

    except (

        ValueError,

        TypeError

    ):

        return None