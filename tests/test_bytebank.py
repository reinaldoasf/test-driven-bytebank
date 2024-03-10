from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_24(self):
        # Given
        entrada = '13/03/2000'
        esperado = 24
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        # When
        resultado = funcionario_teste.idade()

        # Then
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' #Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000',1111)

        resultado = lucas.sobrenome() #when

        assert resultado == esperado #Then