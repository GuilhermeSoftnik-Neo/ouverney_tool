from logging import info, error, warning



def ask_actions():
    """Pergunta ao usuário quais devem ser os
    comandos a serem executados respectivamente.

    Retorna uma lista de strings, onde cada string
    é numérica."""

    answer = input("--* O que o script deve executar? >> ")

    if answer == "99" or not input("Tem certeza? [S/n]") in ("s", "y", "", None):
        return 99

    else:
        answer = answer.replace(" ", "").split(",")
        actions = filter(lambda i: i if i.isnumeric() else None, answer)

        return actions


def process_actions(actions, available_options, comandos, skip_asks=False):
    """Itera sobre :actions:

    Se action for uma opção válida:
        Tenta executar Comando."""

    for action in actions:
        try:
            if (
                isinstance(action, str)
                and action in available_options
                and action.isnumeric()
            ):
                comando = comandos[int(action)]

                assert not isinstance(comando.nome, list)

                info(f"[EXECUTANDO] {comando.nome}")

                if skip_asks:
                    comando.pedir_confirmacao_do_usuario = lambda _: skip_asks

                comando.executar()
                info(f"{comando.nome} [SUCESSO]")

            else:
                warning(f"Ignorando: {action}, pois não é uma opção válida, meu jovem.")

        except AssertionError as e:
            warning(f"Ignorando: {comando.nome} é uma lista, rapaz.")
            raise e

        except Exception as e:
            error(f"{comando.nome} [FALHA]. Motivo: {e}")
