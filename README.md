
# organizze-banker  
  Python Wrapper para a API do aplicativo Organizze  
  
  
# Descrição  
Este wrapper foi elaborado como um projeto pessoal para facilitar o uso da API do Organizze, meu principal software de gestão das finanças. Espero que também possa ajudar outros, mas sejam pacientes, sou iniciante em programação Python e atualmente é apenas um hobby.

Aceito sugestões de melhoria, mas peço que o objetivo de cada alteração seja explicado, porque estou em processo de aprendizado.

Este wrapper foi desenvolvido utilizando PyCharm e a SDK Python 3.9.2

# Requisitos e Instalação
*Em elaboração*

> Obs: Aceito dicas na identificação dos requisitos e como preencher melhor esta seção

**Pacotes:**
 - idna
 - urllib3
 - chardet
 - certifi
 - requests

# Como usar
Todos os métodos atualmente estão contidos dentro de uma única classe **Banker**, a ser instanciada e cujo objeto será o núcleo de todas as consultas seguintes.

Parâmetros:
--- **email** da conta Organizze
--- **chave de API** gerada em https://app.organizze.com.br/configuracoes/api-keys
--- **autor** (*opcional*) - é enviado junto com o email de login para formar o User-Agent da conexão remota, que a Organizze pede num formato específico para **facilitar** sua identificação (*impedir é impossível já que a identificação do usuário já é realizada pelos email/chave da API*)

**Exemplo:**

    from banker import Banker
     
    email = "meuemail@provedor.com"
    chave_api = "3f7e4dc07e5a77d09e9ae2892d2611832f220bf4"
    autor = "Anderson"
    
    conn = Banker(email, chave_api, autor)
após isso, basta invocar os métodos programados diretamente do objeto de conexão

    contas = conn.getContas()
    for i, c in enumerate(contas):  
	    print(f'[{i}] => {c}')

# Métodos  

## Usuários
> *Obs: não é vista funcionalidade de gestão de usuários dentro do Organizze ou sua API, portanto considero que é um esqueleto já montado para eventual implementação futura. Dessa forma, hoje as funções de busca de usuários ou detalhamento retornam praticamente o mesmo resultado.*

### getUsuarios()
Busca os usuários associados à sua conta
 --- retorno: **lista** contendos **dicts** com cada usuário

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### getUsuario( idUsuario )
Traz detalhamento de um usuário específico
--- retorno: **dict** com dados de um usuário

**Parâmetros obrigatórios:**
> * idUsuario(int) -> define qual o ID do usuário a ser retornado

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

## Contas
### getContas()

Busca as contas (Corrente, Investimento, etc...) cadastradas no sistema
 --- retorno: **lista** contendos **dicts** com cada conta

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### getConta( idConta )

Traz detalhamento de uma conta específica
--- retorno: **dict** com dados de uma conta

**Parâmetros obrigatórios:**
> * idConta(int) -> define qual o ID da conta a ser retornada

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### addConta( JSON_params )

Cria uma nova conta

**Parâmetros obrigatórios:**
> * JSON_params(dict) -> dicionário com parâmetros para criação de uma nova conta
> *Obs: determinar o que diferencia uma conta corrente, investimento e outro

#### Parâmetros de input (JSON)
> *Obs: campos JSON de input serem incluídos aqui*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### updConta( idConta , JSON_params )

Atualiza dados de uma conta existente

**Parâmetros obrigatórios:**
> * idConta(int) -> define qual o ID da conta a ser atualizada
> * JSON_params(dict) -> dicionário com parâmetros/dados alvo de atualização

#### Parâmetros de input (JSON)
> *Obs: campos JSON de input serem incluídos aqui*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### delConta( idConta )

Remove uma conta existente, realizando efeito cascata em todos os lançamento associados àquela conta

**Parâmetros obrigatórios:**
> * idConta(int) -> define qual o ID da conta a ser removida

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

## Metas
### getMetas()
### getMetas(ano)
### getMetas(ano, mes)

Busca as metas cadastradas no sistema
 --- retorno: **lista** contendos **dicts** com cada meta

**Parâmetros opcionais:**
> * ano (int) -> define qual o ano buscado
> * mes (int) -> define qual o mês buscado no ano definido anteriormente
>
> Obs1: na ausência de parâmetros, é usado como padrão o ano e mês atual
> Obs2: caso apenas ANO seja definido, as metas do ano inteiro serão retornadas
> Obs3: não é possível definir apenas MES, sem definição de um ANO.

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

## Categorias
### getCategorias()

Busca as categorias cadastradas no sistema
 --- retorno: **lista** contendos **dicts** com cada categoria

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### getCategoria( idCategoria )

Traz detalhamento de uma categoria específica
--- retorno: **dict** com dados de uma categoria

**Parâmetros obrigatórios:**
> * idCategoria(int) -> define qual o ID da categoria a ser retornada

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### addCategoria( JSON_params )

Cria uma nova categoria

**Parâmetros obrigatórios:**
> * JSON_params(dict) -> dicionário com parâmetros/dados da nova categoria

#### Parâmetros de input (JSON)
> *Obs: campos JSON de input serem incluídos aqui*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### updCategoria( idCategoria , JSON_params )

Atualiza dados de uma categoria existente

**Parâmetros obrigatórios:**
> * idCategoria(int) -> define qual o ID da categoria a ser atualizada
> * JSON_params(dict) -> dicionário com parâmetros/dados alvo de atualização

#### Parâmetros de input (JSON)
> *Obs: campos JSON de input serem incluídos aqui*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### delCategoria( idCategoria , idNovaCategoria )

Remove uma categoria existente, realizando efeito cascata em todos os classificados naquela categoria.

**Parâmetros obrigatórios:**
> * idCategoria(int) -> define qual o ID da categoria a ser removida

**Parâmetros opcionais:**
> * idNovaCategoria (int) -> indicação de qual o ID de nova categoria para onde serão migrados os lançamentos que estavam classificados como a categoria removida. Padrão: categoria OUTROS

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

## Cartões de Crédito
### getCartoesCredito()

Busca os cartões de crédito cadastrados no sistema
 --- retorno: **lista** contendos **dicts** com cada cartão de crédito

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### getCartaoCredito( idCartao )

Traz detalhamento de um cartão de crédito específico
--- retorno: **dict** com dados de um cartão de crédito

**Parâmetros obrigatórios:**
> * idCartao(int) -> define qual o ID do cartão de crédito a ser retornado

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### addCartaoCredito( JSON_params )

Cria um novo cartão de crédito

**Parâmetros obrigatórios:**
> * JSON_params(dict) -> dicionário com parâmetros/dados do novo cartão de crédito

#### Parâmetros de input (JSON)
> *Obs: campos JSON de input serem incluídos aqui*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### updCartaoCredito( idCartao , JSON_params )

Atualiza dados de um cartão de crédito existente

**Parâmetros obrigatórios:**
> * idCartao(int) -> define qual o ID do cartão de crédito a ser atualizado
> * JSON_params(dict) -> dicionário com parâmetros/dados alvo de atualização

#### Parâmetros de input (JSON)
> *Obs: campos JSON de input serem incluídos aqui*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### delCartaoCredito( idCartao )

Remove uma conta existente, realizando efeito cascata em todos os lançamento associados àquele cartão de crédito

**Parâmetros obrigatórios:**
> * idCartao(int) -> define qual o ID do cartão de crédito a ser removido

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

## Faturas de Cartões

### getFaturasCartao( idCartao )

Busca as faturas de um cartão de crédito cadastrado no sistema
 --- retorno: **lista** contendos **dicts** com cada fatura

**Parâmetros obrigatórios:**
> * idCartao(int) -> define qual o ID do cartão de crédito cujas faturas serão retornadas

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### getFaturaCartao( idCartao , idFatura )

Traz detalhamento de uma fatura específica
--- retorno: **dict** com dados de uma fatura

**Parâmetros obrigatórios:**
> * idCartao(int) -> define qual o ID do cartão de crédito referente à fatura consultada
> * idFatura(int) -> define qual o ID da fatura a ser retornada

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### getPagamentosFatura( idCartao , idFatura )

Busca os pagamentos de faturas cadastrados no sistema
 --- retorno: **lista** contendos **dicts** com cada pagamento de fatura

**Parâmetros obrigatórios:**
> * idCartao(int) -> define qual o ID do cartão de crédito referente à fatura consultada
> * idFatura(int) -> define qual o ID da fatura cujos pagamentos serão retornados

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

## Lançamentos
### getLancamentos()
### getLancamentos(dataInicio)
### getLancamentos(dataInicio, dataFim)

Busca os lançamentos cadastrados no sistema
 --- retorno: **lista** contendos **dicts** com cada lançamento

**Parâmetros opcionais:**
> * dataInicio (string) -> Data no formato "AAAA-MM-DD" definindo o período inicial da busca de lançamentos
> * dataFim (string) -> Data no formato "AAAA-MM-DD" definindo o período final da busca de lançamentos
>
> *Obs1: No caso de não serem definidos parâmetros, serão retornados lançamentos do mês atual*
> *Obs2: Caso se deseje definir apenas uma data fim, basta não tocar no parâmetro dataInicio ou definí-lo como None, que este será ignorado*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### getLancamento( idLancamento )

Traz detalhamento de um lançamento específico
--- retorno: **dict** com dados de um lançamento

**Parâmetros obrigatórios:**
> * idLancamento(int) -> define qual o ID do lançamento a ser retornado

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### addLancamento( JSON_params )

Cria um novo lançamento único

**Parâmetros obrigatórios:**
> * JSON_params(dict) -> dicionário com parâmetros/dados do novo lançamento único

#### Parâmetros de input (JSON)
> *Obs: campos JSON de input serem incluídos aqui*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### addLancamentoFixo( JSON_params , periodicidade )

Cria um novo lançamento recorrente fixo

**Parâmetros obrigatórios:**
> * JSON_params(dict) -> dicionário com parâmetros/dados do novo lançamento recorrente fixo
> * periodicidade(str) -> determina se o lançamento é de recorrência 'semanal', 'bissemanal', 'mensal', 'bimestral', 'trimestral', 'semestral' ou 'anual'

#### Parâmetros de input (JSON)
> *Obs: campos JSON de input serem incluídos aqui*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### addLancamentoParcelado( JSON_params , periodicidade , parcelas )

Cria um novo lançamento parcelado

**Parâmetros obrigatórios:**
> * JSON_params(dict) -> dicionário com parâmetros/dados do novo lançamento recorrente fixo
> * periodicidade(str) -> determina se o lançamento tem intervalo 'semanal', 'bissemanal', 'mensal', 'bimestral', 'trimestral', 'semestral' ou 'anual'
> * parcelas(int) -> determina por quantos períodos o lançamento ocorrerá

#### Parâmetros de input (JSON)
> *Obs: campos JSON de input serem incluídos aqui*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### updLancamento( idLancamento , JSON_params , atualizaFuturos , atualizaTodos )

Atualiza dados de um lançamento existente

**Parâmetros obrigatórios:**
> * idLancamento(int) -> define qual o ID do lançamento a ser atualizado
> * JSON_params(dict) -> dicionário com parâmetros/dados alvo de atualização

**Parâmetros opcionais:**
> * atualizaFuturos (bool) -> define que lançamentos FUTUROS (se existirem) associados àquele lançamento também serão atualizados. Padrão: FALSE
> * atualizaTodos (bool) -> define que TODOS os lançamentos associados àquele lançamento também serão atualizados. Padrão: FALSE
>
> *Obs: se o parâmetro de atualização de todos estiver ativado, este irá sobrepor o de apenas lançamentos futuros*

#### Parâmetros de input (JSON)
> *Obs: campos JSON de input serem incluídos aqui*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*

### delLancamento( idLancamento , apagaFuturos , apagaTodos )

Remove um lançamento existente, realizando efeito cascata em todos os lançamento associados àquela conta

**Parâmetros obrigatórios:**
> * idLancamento(int) -> define qual o ID do lançamento a ser removido

**Parâmetros opcionais:**
> * apagaFuturos (bool) -> define que lançamentos FUTUROS (se existirem) associados àquele lançamento também serão removidos. Padrão: FALSE
> * apagaTodos (bool) -> define que TODOS os lançamentos associados àquele lançamento também serão removidos. Padrão: FALSE
>
> *Obs: se o parâmetro de remoção de todos estiver ativado, este irá sobrepor o de apenas lançamentos futuros*

#### Exemplo de dados retornados:
> *Obs: exemplo de retorno JSON a ser incluído aqui*
  
# Planejado para o futuro
* Desmembramento em classes por contexto (Ex: Lançamentos, Metas, Categorias, etc...)
* Transferências (que são simplesmente '*lançamentos mais complexos*'
* Métodos especiais para automatização de tarefas e _housekeeping_
* Documentação mais decente (ex: exemplos, detalhes dos possíveis inputs, JSONs retornados, etc.)
* Publicação no PyPi

# Referências
* [Organizze API docs](https://github.com/organizze/api-doc)
* [organizze-client](https://github.com/lucrib/organizze-client/) (*fonte de inspiração para iniciar este wrapper. Obrigado [Lucas Ribeiro](https://github.com/lucrib)!*)
* [PyCharm](https://www.jetbrains.com/pt-br/pycharm/)
* [Python SDK 3.9.2](https://www.python.org/downloads/release/python-392/)