from pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, cpf, idade, matricula, curso, semestre):
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.curso = curso
        self.semestre = semestre

    def __str__(self):
        return f'''{super().__str__()}
Matrícula: {self.matricula}
Curso: {self.curso}
Semestre: {self.semestre}'''
