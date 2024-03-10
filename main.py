from codigo.bytebank import Funcionario

#lucas = Funcionario('Lucas Carvalho', '13/02/2000', 1000)


#print (lucas.idade())

def teste_idade():
    funcionario_teste1 = Funcionario("Teste",'13/03/2000', 1111)
    print(f'Teste = {funcionario_teste1.idade()}')
    funcionario_teste2 = Funcionario("Teste",'13/03/1999', 1111)
    print(f'Teste = {funcionario_teste2.idade()}')
    funcionario_teste3 = Funcionario("Teste",'01/12/1999', 1111)
    print(f'Teste = {funcionario_teste3.idade()}')

teste_idade()

#test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000()