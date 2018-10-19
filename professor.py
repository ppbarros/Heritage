from funcionario import Funcionario
class Professor(Funcionario):
    def __init__(self, nome, cpf, idade, matricula, salario, setor, curso):
        super().__init__(nome, cpf, idade, matricula, salario, setor)
        self.curso = curso

    def __str__(self):
        return f'''{super().__str__()}
Curso: {self.curso}'''