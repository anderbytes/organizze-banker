def validaData(self, texto: str):
    try:
        from datetime import datetime
        datetime.strptime(texto, "%Y-%m-%d")
    except ValueError:
        raise ValueError("O formato da data é inválida, esperado: AAAA-MM-DD")


def validaAno(self, numero: int, minimo: int, maximo: int):
    if not (minimo <= numero <= maximo):
        raise ValueError("O ano informado não é considerado válido.")


def enumera(lista: list):
    for i, t in enumerate(lista):
        print(f'[{i}] => {t}')
