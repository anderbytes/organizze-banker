class Banker:
    import requests
    from requests.auth import HTTPBasicAuth
    from auxiliar import validaData

    # Parametros oriundos da documentação da API da Organizze
    URL_API = 'https://api.organizze.com.br/rest/v2/'
    CONTENT_TYPE = {'Content-Type': 'application/json; charset=utf-8'}

    def __init__(self, email, token, autor='SemNome'):
        if email is None:
            raise ValueError('Preencha um Email no 1º parâmetro')
        if token is None:
            raise ValueError('Preencha um Token no 2º parâmetro')
        if not isinstance(autor, str):
            raise ValueError('O campo AUTOR precisa conter uma string')

        self.sessao = self.requests.Session()
        self.sessao.auth = self.HTTPBasicAuth(email, token)
        self.sessao.headers.update(self.CONTENT_TYPE)
        self.sessao.headers.update({'User-Agent': f'{autor} ({email})'})

    ## USUARIOS #################################################################
    def getUsuarios(self):
        return self.sessao.get(self.URL_API + "users/").json()

    def getUsuario(self, idUsuario):
        return self.sessao.get(self.URL_API + "users/" + str(idUsuario)).json()

    ## CONTAS   #################################################################
    def getContas(self):
        return self.sessao.get(self.URL_API + "accounts/").json()

    def getConta(self, idConta):
        return self.sessao.get(self.URL_API + "accounts/" + str(idConta)).json()

    ## METAS    #################################################################
    def getMetas(self):
        return self.sessao.get(self.URL_API + "budgets/").json()

    ## CATEGORIAS ###############################################################
    def getCategorias(self):
        return self.sessao.get(self.URL_API + "categories/").json()

    def getCategoria(self, idCategoria):
        return self.sessao.get(self.URL_API + "categories/" + str(idCategoria)).json()

    def updCategoria(self, idCategoria, JSON_params):
        self.sessao.put(self.URL_API + "categories/" + str(idCategoria), params=JSON_params)

    def delCategoria(self, idCategoria, idNovaCategoria):
        self.sessao.delete(self.URL_API + "categories/" + str(idCategoria), params={'replacement_id': idNovaCategoria})

    ## CARTÕES DE CRÉDITO #######################################################
    def getCartoesCredito(self):
        return self.sessao.get(self.URL_API + "credit_cards/").json()

    def getCartaoCredito(self, idCartao):
        return self.sessao.get(self.URL_API + "credit_cards/" + idCartao).json()

    def updCartaoCredito(self, idCartao, JSON_params):
        self.sessao.put(self.URL_API + "credit_cards/" + str(idCartao), params=JSON_params)

    def delCartaoCredito(self, idCartao):
        self.sessao.delete(self.URL_API + "credit_cards/" + str(idCartao))

    def getFaturasCartao(self, idCartao):
        return self.sessao.get(self.URL_API + "credit_cards/" + idCartao + "/invoices").json()

    def getFaturaCartao(self, idCartao, idFatura):
        return self.sessao.get(self.URL_API + "credit_cards/" + idCartao + "/invoices" + str(idFatura)).json()

    def getPagamentosFatura(self, idCartao, idFatura):
        return self.sessao.get(
            self.URL_API + "credit_cards/" + idCartao + "/invoices" + str(idFatura) + "/payments").json()

    ## LANÇAMENTOS #################################################################
    def getLancamentos(self, dataInicio=None, dataFim=None):

        if (dataInicio is None and dataFim is None):
            return self.sessao.get(self.URL_API + "transactions/").json()
        else:
            parametros = ""
            if (dataInicio is not None):
                self.validaData(dataInicio)
                parametros = "&start_date=" + dataInicio
            if (dataFim is not None):
                self.validaData(dataFim)
                parametros += ("&end_date=" + dataFim)
            return self.sessao.get(self.URL_API + "transactions/", params=parametros).json()

    def getLancamento(self, idTransacao):
        return self.sessao.get(self.URL_API + "transactions/" + str(idTransacao)).json()

    def updLancamento(self, idLancamento, JSON_params):
        self.sessao.put(self.URL_API + "transactions/" + str(idLancamento), params=JSON_params)

    def delLancamento(self, idLancamento):
        self.sessao.delete(self.URL_API + "transactions/" + str(idLancamento))
