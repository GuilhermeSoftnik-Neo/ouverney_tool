from abc import ABC, abstractmethod
from subprocess import run, CalledProcessError
from shlex import split
from logging import info, error


class Comando(ABC):
    __slots__ = ["nome", "desc", "requires_admin"]

    def __init__(self, nome="Nome do Comando",
                 desc="Descrição"):
        self.nome = nome
        self.desc = desc

    @abstractmethod
    def executar(self):
        "Um comando precisa implementar o método 'executar'!"

    def banner(self) -> str:
        "Retorna uma linha formatada pré-fabricada."
        return f"{self.nome} - {self.desc}"

    def system(self, command_list: list | str, shell=False):

        def processar(comando):
            info(f"Comando ao Windows: ${comando}")

            try:
                run(split(comando), shell=shell).check_returncode()

            except CalledProcessError:
                error(f'"{comando}" não pôde ser processado pelo Windows.')

            except Exception as erro:
                error(f"Um erro desconhecido ocorreu: {erro}")

        (
            [processar(c) for c in command_list]
            if isinstance(command_list, list)
            else processar(command_list)
        )

    def pedir_confirmacao_do_usuario(self, mensagem) -> bool:
        while True:
            try:
                return input(mensagem).lower() in ["", "s", "y"]
            except KeyboardInterrupt:
                print("Cancelando.")
                return False


if __name__ == "__main__":

    class TesteComando(Comando):
        def executar(self):
            print("Charizard atacou!")

    teste = TesteComando("Charizard", "Queima malwares com o fogo do Python ardente!")

    # region Dec
    titulo = "Nome - Descrição"

    print(titulo, len(titulo) * "_", sep="\n")

    print(teste.banner())

    confirmacao = teste.pedir_confirmacao_do_usuario("O Charizard deve atacar? [S/n]")
    if confirmacao:
        teste.executar()
    else:
        print("oh...")

    print("Outro teste.")
    tt = TesteComando()
    print(tt.banner())
