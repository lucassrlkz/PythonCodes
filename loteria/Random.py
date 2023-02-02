from mypackage.FuncaoLoteria import FuncaoLoteria


if __name__ == '__main__':
    tipo_loteria = str(
        input('qual tipo de loteria (megasena, lotofacil) :'))

    qtde = int(
        input('quantidade de jogos: '))

    funcao_loteria = FuncaoLoteria(qtde)
    loteria = funcao_loteria.loteria

    if tipo_loteria in loteria:
        funcao_loteria.printer()
        loteria.get(tipo_loteria)()
    