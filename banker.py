import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth


def _validaData(texto):
    try:
        datetime.strptime(texto, "%Y-%m-%d")
    except ValueError:
        raise ValueError("O formato da data é inválida, esperado: AAAA-MM-DD")


class Banker:

    # Parametros oriundos da documentação da API da Organizze
    URL_API      = 'https://api.organizze.com.br/rest/v2/'
    CONTENT_TYPE = {'Content-Type': 'application/json; charset=utf-8'}

    def __init__(self, email, token, autor='SemNome'):
        if email is None:
            raise ValueError('Preencha um Email')
        if token is None:
            raise ValueError('Preencha um Token')
        self.sessao = requests.Session()
        self.sessao.auth = HTTPBasicAuth(email, token)
        self.sessao.headers.update(self.CONTENT_TYPE)
        self.sessao.headers.update({'User-Agent': f'{autor} ({email})'})

    def getUsuarios(self):
        return self.sessao.get(self.URL_API + "users/").json()

    def getUsuario(self, idUsuario):
        return self.sessao.get(self.URL_API + "users/" + str(idUsuario)).json()

    def getContas(self):
        return self.sessao.get(self.URL_API + "accounts/").json()

    def getConta(self, idConta):
        return self.sessao.get(self.URL_API + "accounts/" + str(idConta)).json()

    def getMetas(self):
        return self.sessao.get(self.URL_API + "budgets/").json()

    def getCategorias(self):
        return self.sessao.get(self.URL_API + "categories/").json()

    def getCategoria(self, idCategoria):
        return self.sessao.get(self.URL_API + "categorias/" + str(idCategoria)).json()

    def getCartoesCredito(self):
        return self.sessao.get(self.URL_API + "credit_cards/").json()

    def getCartaoCredito(self, idCartao):
        return self.sessao.get(self.URL_API + "credit_cards/" + idCartao).json()

    def getFaturasCartao(self, idCartao):
        return self.sessao.get(self.URL_API + "credit_cards/" + idCartao + "/invoices").json()

    def getFaturaCartao(self, idCartao, idFatura):
        return self.sessao.get(self.URL_API + "credit_cards/" + idCartao + "/invoices" + str(idFatura)).json()

    def getPagamentosFatura(self, idCartao, idFatura):
        return self.sessao.get(self.URL_API + "credit_cards/" + idCartao + "/invoices" + str(idFatura) + "/payments").json()

    def getLancamentos(self, dataInicio=None, dataFim=None):
        if (dataInicio is None and dataFim is None):
            return self.sessao.get(self.URL_API + "transactions/").json()
        else:
            parametros = ""
            if (dataInicio is not None):
                _validaData(dataInicio)
                parametros = "&start_date=" + dataInicio
            if (dataFim is not None):
                _validaData(dataFim)
                parametros += ("&end_date=" + dataFim)
            return self.sessao.get(self.URL_API + "transactions/", params=parametros).json()

    def getLancamento(self, idTransacao):
        return self.sessao.get(self.URL_API + "transactions/" + str(idTransacao)).json()
