def validaData(texto):
    try:
        from datetime import datetime
        datetime.strptime(texto, "%Y-%m-%d")
    except ValueError:
        raise ValueError("O formato da data é inválida, esperado: AAAA-MM-DD")