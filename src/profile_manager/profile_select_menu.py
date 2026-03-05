BANNER = """
-- Escolha o perfil para executar suas ações.
[Escreva o nome do perfil ou digite seu número]

Perfis:
{}
________
-->> """

def create_options_menu(options_dict):
    string = ""

    for num, dict_data in enumerate(options_dict.items()):
        key = dict_data[0]
        values = dict_data[1]
        string += f" {num} - {key}: {values}\n"

    return BANNER.format(string)

def show_menu(options_dict):
    while True:
        answer = input(BANNER)
        available_options = options_dict.keys()

        if answer in available_options:
            key = answer

        elif (answer.isnumeric()
            and int(answer) in range(len(available_options))):
            key = tuple(available_options)[int(answer)]

        else:
            continue

        return options_dict[key]


if __name__ == '__main__':
    dicto = {
        "Manutenção": [1,2],
        "Limpeza": [11,84],
        "Amenic Fixing": [6,1,5,1]
    }

    BANNER = create_options_menu(dicto)
    # print("You choosed:",show_menu(dicto))