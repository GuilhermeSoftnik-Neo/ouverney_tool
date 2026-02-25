from time    import sleep
from pathlib import Path
from logging import INFO
from logging import basicConfig
from src.app import ask_actions
from src.app import process_actions
from src.app.ascii_arts import BANNER
from src.app.ascii_arts import COMANDOS_BANNER
from src.banner_tools import clear
from src.banner_tools import print_comandos_banner
from src.infra        import get_every_obj_child_of_Comando
from src.banner_tools import convert_boolean_to_message as translate


comandos = [i() for i in get_every_obj_child_of_Comando()]
LOG_FILE = Path(__file__).resolve().parent / "LOG.txt"
skip_asks = True


basicConfig(
    level=INFO,
    filemode="w",
    encoding="UTF-8",
    filename=LOG_FILE,
    datefmt="%H:%M:%S",
    format="%(asctime)s - [%(funcName)s]: %(message)s",
)

main_options = [
    "Iniciar",
    "TODO: Configurações c[]",
    "TODO: Ajuda c[]",
    f"Pular pedidos de confirmação: {translate(skip_asks)}",
    "Sair",
]


while True:
    options = ""

    clear()

    for num, opt in enumerate(main_options):
        options += f"    * [ - {num} - ] - {opt}\n"

    print(BANNER.format(options))

    answer = input("--> Digite a opção desejada >> ")

    match answer:
        case "0":
            while True:
                clear()
                available_actions = print_comandos_banner(comandos, COMANDOS_BANNER)

                actions = ask_actions()

                if actions == 99:
                    break

                process_actions(actions, available_actions, comandos, skip_asks)

                input(
                    "\n -- Todas as ações foram executadas. Pressione Enter para voltar ao menu --"
                )

            continue

        case "1":
            print("Ops! Isso ainda não está disponivel.")
            sleep(1.5)
            continue

        case "3":
            skip_asks = not skip_asks
            main_options[3] = f"Pular pedidos de confirmação: {translate(skip_asks)}"
            continue

        case "4" | "Sair" | "/exit":
            print("Bye!")

        case _:
            print("Ops! Essa opção não existe, colega!")
            sleep(1.5)
            continue

    break


input("\n** Obrigado por usar Ouverney Tool! Pressione Enter para sair **")
