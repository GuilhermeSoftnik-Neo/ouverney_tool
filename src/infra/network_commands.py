try:
    from .base_command import Comando
except:
    from base_command import Comando

class ReiniciarRede(Comando):
    def __init__(self, nome="Reiniciar Rede", desc="Reinicia a rede da sua máquina, reiniciando dados e renovando conexões (Não apaga dados e nem senhas de redes wi-fi)."):
        super().__init__(nome, desc)

    def executar(self):
        comandos = [
            "ipconfig /flushdns",
            "netsh winsock reset",
            "netsh int ip reset" ]

        self.system(comandos)
        print("Atenção: Um reinício será necessário para surtir completamente efeito.")
