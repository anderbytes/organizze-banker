
class Banker:
    import requests
    from requests.auth import HTTPBasicAuth
    from auxiliar import validaData, validaAno

    # Parametros oriundos da documentação da API da Organizze
    URL_API = "https://api.organizze.com.br/rest/v2"

    def __init__(self, email: str, token: str, autor: str = 'SemNome'):
        self.sessao = self.requests.Session()
        self.sessao.auth = self.HTTPBasicAuth(email, token)
        self.sessao.headers.update({'User-Agent': f'{autor} ({email})', 'Content-Type': 'application/json; charset=utf-8'})

    ## USUARIOS #################################################################
    def getUsuarios(self) -> list:
        return self.sessao.get(f'{self.URL_API}/users').json()

    def getUsuario(self, idUsuario: int) -> dict:
        return self.sessao.get(f'{self.URL_API}/users/{idUsuario}').json()

    ## CONTAS   #################################################################
    def getContas(self) -> list:
        return self.sessao.get(f'{self.URL_API}/accounts').json()

    def getConta(self, idConta: int) -> dict:
        return self.sessao.get(f'{self.URL_API}/accounts/{idConta}').json()

    def addConta(self, JSON_params: dict):
        self.sessao.post(f'{self.URL_API}/accounts', params=JSON_params)

    def updConta(self, idConta: int, JSON_params: dict):
        self.sessao.put(f'{self.URL_API}/accounts/{idConta}', params=JSON_params)

    def delConta(self, idConta: int):
        self.sessao.delete(f'{self.URL_API}/accounts/{idConta}')

    ## METAS    #################################################################
    def getMetas(self, ano: int = 0, mes: int = 0) -> list:
        parametros = ""
        if (ano > 0):
            self.validaAno(ano, 1900, 3000)
            parametros = f'{ano}'
            if (1 <= mes <= 12):
                parametros = f'{parametros}/{mes}'
        return self.sessao.get(f'{self.URL_API}/budgets/{parametros}').json()

    ## CATEGORIAS ###############################################################
    def getCategorias(self) -> list:
        return self.sessao.get(f'{self.URL_API}/categories').json()

    def getCategoria(self, idCategoria: int) -> dict:
        return self.sessao.get(f'{self.URL_API}/categories/{idCategoria}').json()

    def addCategoria(self, JSON_params: dict):
        self.sessao.post(f'{self.URL_API}/categories', params=JSON_params)

    def updCategoria(self, idCategoria: int, JSON_params: dict):
        self.sessao.put(f'{self.URL_API}/categories/{idCategoria}', params=JSON_params)

    def delCategoria(self, idCategoria: int, idNovaCategoria: int = None):
        if (idNovaCategoria is not None):
            self.sessao.delete(f'{self.URL_API}/categories/{idCategoria}', params={'replacement_id': idNovaCategoria})
        else:
            self.sessao.delete(f'{self.URL_API}/categories/{idCategoria}')

    ## CARTÕES DE CRÉDITO #######################################################
    def getCartoesCredito(self) -> list:
        return self.sessao.get(f'{self.URL_API}/credit_cards').json()

    def getCartaoCredito(self, idCartao: int) -> dict:
        return self.sessao.get(f'{self.URL_API}/credit_cards/{idCartao}').json()

    def addCartaoCredito(self, JSON_params: dict):
        self.sessao.post(f'{self.URL_API}/credit_cards', params=JSON_params)

    def updCartaoCredito(self, idCartao: int, JSON_params: dict):
        self.sessao.put(f'{self.URL_API}/credit_cards/{idCartao}', params=JSON_params)

    def delCartaoCredito(self, idCartao: int):
        self.sessao.delete(f'{self.URL_API}/credit_cards/{idCartao}')

    ## FATURAS DE CARTÕES DE CRÉDITO ###############################################
    def getFaturasCartao(self, idCartao: int) -> list:
        return self.sessao.get(f'{self.URL_API}/credit_cards/{idCartao}/invoices').json()

    def getFaturaCartao(self, idCartao: int, idFatura: int) -> dict:
        return self.sessao.get(f'{self.URL_API}/credit_cards/{idCartao}/invoices/{idFatura}').json()

    def getPagamentosFatura(self, idCartao: int, idFatura: int) -> list:
        return self.sessao.get(f'{self.URL_API}/credit_cards/{idCartao}/invoices/{idFatura}/payments').json()

    ## LANÇAMENTOS #################################################################
    def getLancamentos(self, dataInicio: str = None, dataFim: str = None) -> list:
        parametros = ""
        if (dataInicio is not None):
            self.validaData(dataInicio)
            parametros = f'&start_date={dataInicio}'
        if (dataFim is not None):
            self.validaData(dataFim)
            parametros = f'{parametros}&end_date={dataFim}'
        return self.sessao.get(f'{self.URL_API}/transactions', params=parametros).json()

    def getLancamento(self, idLancamento: int) -> dict:
        return self.sessao.get(f'{self.URL_API}/transactions/{idLancamento}').json()

    def addLancamento(self, JSON_params: dict):
        self.sessao.post(f'{self.URL_API}/transactions', params=JSON_params)

    def addLancamentoFixo(self, JSON_params: dict, periodicidade: str):
        # OPÇÕES DE PERIODICIDADE: ["weekly", "biweekly", "monthly",  "bimonthly", "trimonthly", "yearly"]
        # Cadê DAILY e SEMESTRAL (or SEMESTRIAL)
        periodos = {'diário': 'daily', 'semanal': 'weekly', 'bissemanal': 'biweekly', 'mensal': 'monthly',
                    'bimestral': 'bimonthly', 'trimestral': 'trimonthly', 'semestral': 'semesterly', 'anual': 'yearly'}

        JSON_params.update({"recurrence_attributes": {"periodicity": periodos[periodicidade]}})
        self.sessao.post(f'{self.URL_API}/transactions', params=JSON_params)

    def addLancamentoParcelado(self, JSON_params: dict, periodicidade: str, parcelas: int):
        # OPÇÕES DE PERIODICIDADE: ["weekly", "biweekly", "monthly",  "bimonthly", "trimonthly", "yearly"]
        # Cadê DAILY e SEMESTRAL (or SEMESTRIAL)
        periodos = {'diário': 'daily', 'semanal': 'weekly', 'bissemanal': 'biweekly', 'mensal': 'monthly', 'bimestral': 'bimonthly', 'trimestral': 'trimonthly', 'semestral': 'semesterly', 'anual': 'yearly'}
        periodicidade = periodos[periodicidade]

        if not (2 <= parcelas <= 480):
            raise ValueError("O número de parcelas é inválido (utilize um Nº entre 2 a 480)")
        JSON_params.update({"installments_attributes": {"periodicity": periodicidade, "total": parcelas}})
        self.sessao.post(f'{self.URL_API}/transactions', params=JSON_params)

    def updLancamento(self, idLancamento: int, JSON_params: dict, atualizaFuturos: bool = False, atualizaTodos: bool = False):
        if atualizaFuturos is True:
            JSON_params.update({"update_future": True})
        elif atualizaTodos is True:
            JSON_params.update({"update_all": True})
        self.sessao.put(f'{self.URL_API}/transactions/{idLancamento}', params=JSON_params)

    def delLancamento(self, idLancamento: int, apagaFuturos: bool = False, apagaTodos: bool = False):
        parametros = None
        if apagaFuturos is True:
            parametros = {"update_future": True}
        elif apagaTodos is True:
            parametros = {"update_all": True}
        self.sessao.delete(f'{self.URL_API}/transactions/{idLancamento}', params=parametros)
