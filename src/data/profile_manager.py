import json
import pathlib
import logging
from treatments import is_sequence_valid, fix_sequence

PROFILE_FILE = pathlib.Path(__file__).resolve().parent / "profiles.json"

# Warnings
NO_DATA_WARNING = "Sem dados para salvar..."
NO_PROFILES_FOUND = "Nenhum perfil foi encontrado... Hora de criar um!"

# Infos
SAVE_SUCCESS = "Perfil salvo com sucesso!"

# Input Prompts
CREATING_PROFILE_PROMPT = (
    "- Qual nome deseja dar para este perfil [Para facilitar a identificação]?\n|__>> "
)
CREATING_PROFILE_COMMANDS_PROMPT = (
    "- Qual a sequência EXATA que deseja salvar, mestre?\n|__>> "
)
DELETING_PROFILE_PROMPT = (
    "\n- Digite o número da opção que deseja excluir [99 para Cancelar]\n|__>> "
)


def secure_func(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except FileNotFoundError as e:
            logging.error(f"Arquivo não encontrado, motivo: {e}")
            raise e

        except json.JSONDecodeError as e:
            logging.error(f"Erro ao decodificar JSON, motivo: {e}")
            raise e

        except Exception as e:
            logging.error(f"Um erro desconhecido ocorreu! Motivo: {e}")
            raise e

    return wrapper


# region Basic Functions
@secure_func
def load() -> dict | None:
    try:
        with open(PROFILE_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(NO_PROFILES_FOUND)
        logging.warning(NO_PROFILES_FOUND)
        return None


@secure_func
def save(data={}) -> None:
    if not data:
        print(NO_DATA_WARNING)
        logging.warning(NO_DATA_WARNING)
        return

    with open(PROFILE_FILE, "w") as file:
        json.dump(data, file)
        print(SAVE_SUCCESS)
        logging.info(SAVE_SUCCESS)


# endregion


@secure_func
def create_new_profile(existing_profiles = {}):
    print("-- Criação de Perfil")

    final_data = {}

    if existing_profiles:
        final_data.update(existing_profiles)
        print("\n\nAviso: Usar o mesmo nome de um perfil já criado, o atualizará!\n")
        print("Perfis:")
        print("-------")
        for key, val in existing_profiles.items():
            print(f"{key} = {val}")

    profile_name = input(CREATING_PROFILE_PROMPT)

    while True:
        commands = input(CREATING_PROFILE_COMMANDS_PROMPT)
        commands = commands.replace(" ", "").split(",")
        commands = fix_sequence(commands)

        if not is_sequence_valid(commands):
            print("Por favor, tente novamente...")
            continue
        else:
            answer = input("Tem certeza dessa sequência? [S/n] >> ").lower()
            if not answer in ["", "s", "y"]:
                continue
            break

    final_data.update({profile_name: commands})

    save(final_data)


@secure_func
def delete_profile(existing_profiles) -> dict:
    print("* --- Exclusão de Perfis\n")

    for index, dict_info in enumerate(existing_profiles.items()):
        key = dict_info[0]
        value = dict_info[1]
        print(f'[{index}] - "{key}" contém {value}')

    answer = input(DELETING_PROFILE_PROMPT)

    return dict


@secure_func
def edit_profile():
    json


if __name__ == "__main__":
    # old_data = load()  # Returns None
    # data = {0: [1, 4, 2], "Bentoo": [1, 4, 5]}
    # save(data)  # Write new profiles

    # Testing profile funcs

    create_new_profile(load())
