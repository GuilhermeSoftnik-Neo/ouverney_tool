from time import sleep
from src.app import setup_log
from src.app import ask_actions
from src.app import process_actions
from src.infra import get_every_obj_child_of_Comando
from src.banner_tools import clear
from src.banner_tools import print_comandos_banner
from src.banner_tools import convert_boolean_to_message as translate
from src.banner_tools.ascii_arts import BANNER
from src.banner_tools.ascii_arts import COMANDOS_BANNER

EXIT = 99

skip_asks = True
comandos = [i() for i in get_every_obj_child_of_Comando()]

clear()
setup_log()

main_options = [
    "Iniciar",
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

                if actions == EXIT:
                    break

                process_actions(
                    actions, available_actions, comandos, skip_asks)

                input(
                    "\n -- Todas as ações foram executadas. Pressione Enter para voltar ao menu --"
                )

        case "1":
            skip_asks = not skip_asks
            main_options[1] = f"Pular pedidos de confirmação: {translate(skip_asks)}"

        case "2" | "Sair" | "/exit" | "99":
            print("Bye!")
            break

        case _:
            clear()
            print("Ops! Essa opção não existe, colega!")
            sleep(1.5)


input("\n** Obrigado por usar Ouverney Tool! Pressione Enter para sair **")
