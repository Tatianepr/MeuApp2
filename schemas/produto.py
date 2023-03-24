# pydantic - framework para geração de documentação das APIs
# serve também para validar requisições enviadas
from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

from schemas import ComentarioSchema

# aqui está exemplificado o uso de schemas para definir um formato de uma requisição.

class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
        define um modelo de dados e como será comunicado com o cliente
    """
    id: int = 1
    nome: str = "Banana Prata"
    quantidade: Optional[int] = 12
    valor: float = 12.50


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Uva"


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "valor": produto.valor,
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    nome: str = "Banana Prata"
    quantidade: Optional[int] = 12
    valor: float = 12.50
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "valor": produto.valor,
        "total_cometarios": len(produto.comentarios),
        "comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }
