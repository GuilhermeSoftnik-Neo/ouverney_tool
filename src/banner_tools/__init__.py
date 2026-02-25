import os, textwrap


def print_comandos_banner(comandos: list | tuple, comandos_banner: str) -> list[str]:
    """Imprime o banner formatado com cada opção
    sendo um Comando e o que ele é e faz.

    Retorna opções disponíveis."""

    available_options = []
    options = ""
    TOTAL_LINE_SIZE = 100
    NAME_COLUMN_SIZE = 55
    DESC_COLUMN_SIZE = TOTAL_LINE_SIZE - NAME_COLUMN_SIZE



    for num, com in enumerate(comandos):
        prefixo = f"{num} - {com.nome}:"
        left_column = prefixo.ljust(NAME_COLUMN_SIZE)
        desc_lines = textwrap.wrap(com.desc, DESC_COLUMN_SIZE)

        options += f"{left_column}{desc_lines.pop(0)}\n"
        
        for line in desc_lines:
            options += " " * NAME_COLUMN_SIZE + line + '\n'

        available_options.append(str(num))
        
        options += '\n'


    print(comandos_banner.format(options))
    return available_options

def clear():
    """Limpa a saída do terminal.

    Atalho para: os.system("cls")"""
    os.system("cls")


translation_dict = {
    0: "Não. (Manual, espera confirmação manual a cada comando)",
    1: "Sim. (Automático, avança sem pedir confirmação)",
}
convert_boolean_to_message = lambda boolean: translation_dict[int(boolean)]
