try:
    from . import base_command
except:
    import base_command


class AjustarAparenciaParaPerformance(base_command.Comando):
    def __init__(self):
        self.nome = "Opções de Desempenho"
        self.desc = "Abre Opções de Desempenho para permitir ativar ou desativar recursos gráficos para equilibrar aparência e performance (Pode trocar quando quiser)."

    def executar(self):
        self.system("SystemPropertiesPerformance.exe", True)