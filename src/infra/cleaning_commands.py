try:
    from .base_command import Comando
except:
    from base_command import Comando


class ConfigurarCleanMGR(Comando):
    def __init__(
        self,
        nome="Configurar CleanMGR",
        desc="Abre as configurações do Gerenciador de Limpeza no perfil 1.",
    ):
        super().__init__(nome, desc)

    def executar(self):
        self.system("cleanmgr.exe /sageset:1 /d c:", True)


class ExecutarCleanMGR(Comando):
    def __init__(
        self,
        nome="Executar CleanMGR no Perfil 1",
        desc="Executa o Gerenciador de Limpeza configurado com base nas configurações de Configurar CleanMGR",
    ):
        super().__init__(nome, desc)

    def executar(self):
        conf = self.pedir_confirmacao_do_usuario(
            """
O CleanMGR pode demorar uns bons minutos dependendo das configurações.
Tem certeza que quer executar a limpeza? [S/n] >>> """
        )
        self.system("cleanmgr.exe /sagerun:1 /d c:", True) if conf else print("Limpeza cancelada.")
        
