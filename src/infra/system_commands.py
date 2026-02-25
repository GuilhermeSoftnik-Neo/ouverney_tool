try:
    from .base_command import Comando
except:
    from base_command import Comando

class MemTest(Comando):
    def __init__(self, nome = "Teste de Memória", desc = "Agendar teste de memória RAM"):
        super().__init__(nome, desc)

    def executar(self):
        self.system("mdsched.exe", True)

class AbrirPropriedadesDoSistema(Comando):
    def __init__(self, nome="Propriedades do Sistema", desc="Abre o painel de propriedades do sistema e da sua máquina."):
        super().__init__(nome, desc)
    
    def executar(self):
        self.system('msinfo32')