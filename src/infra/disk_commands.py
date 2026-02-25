try:
    from . import base_command
except:
    import base_command

class VerificacaoDeDisco(base_command.Comando):
    def __init__(self):
        self.nome = "Verificação de Disco"
        self.desc = "Corrige os erros do disco rígido."

    def executar(self):
        self.system("chkdsk C: /f")

class ChecagemDoSistema():
    def __init__(self):
        self.nome = "Checagem do Sistema"
        self.desc = " Verifica a integridade de todos os arquivos do sistema protegidos e repara os arquivos com problemas quando possível."

    def executar(self):
        self.system("sfc /scannow")

class AnalisarNecessidadeDeFragmentacao(base_command.Comando):
    def __init__(
        self,
        nome="Analisar necessidade de desfragmentação.",
        desc="Analisa o seu disco e diz se é necessário ou não desfragmentar.",
    ):
        super().__init__(nome, desc)

    def executar(self):
        self.system("defrag C: /A /U")
        return super().executar()


class DesfragmentarDisco(base_command.Comando):
    def __init__(
        self,
        nome="Desfragmentar Disco (HDD) / Otimizar Slabs (SSD)",
        desc="Ele identifica se o seu disco é um HD ou SSD e faz a limpeza certa para deixar o Windows mais rápido, sem riscos para os seus arquivos.",
    ):
        super().__init__(nome, desc)

    def executar(self):
        conf = self.pedir_confirmacao_do_usuario(
            """
Desfragmentar o disco pode levar MUITO tempo.
Você poderá usar o computador normalmente, mas é recomendado que não desligue até que seja concluído o processo. Prosseguir? [S/n] >> """
        )

        if conf:
            self.system("defrag C: /O /U")
            self.system("defrag C: /B /U")
        else:
            print("Entendido. Operação cancelada.")


class DiagnosticarWindows(base_command.Comando):
    def __init__(self):
        self.nome = "Diagnosticar saúde do sistema"
        self.desc = "Executa Dism Scanhealth para realizar um diagnóstico do sistema. Note que diagnosticar primeiro é fundamental antes de corrigir, pois o diagnóstico revela e aponta falhas e corrupções novas."

    def executar(self):
        conf = self.pedir_confirmacao_do_usuario(
            "Realizar diagnóstico? Pode demorar um bocado mas é recomendado [S/n] "
        )

        if conf:
            self.system("dism /online /cleanup-image /scanhealth")
        else:
            print("Diagnóstico cancelado.")


class RestaurarSaude(base_command.Comando):
    def __init__(self):
        self.nome = "Restaurar saúde do sistema"
        self.desc = "O /Restorehealth vai buscar arquivos saudáveis (geralmente via Windows Update) para substituir os que estão corrompidos ou faltando."

    def executar(self):
        conf = self.pedir_confirmacao_do_usuario(
            "Restaurar saúde? Pode levar muitas horas. [S/n] "
        )

        if conf:
            self.system("dism /online /cleanup-image /Restorehealth")
        else:
            print("Entendido. A Restauração de Saúde não será feita.")
