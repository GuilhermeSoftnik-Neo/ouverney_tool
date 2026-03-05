import logging, pathlib, json

PROFILE_FILE = pathlib.Path(__file__).resolve().parent / "profiles.json"
PROMPT_TEMPLATE = "-- {} {}:\n|o-->> {}: "
CREATE_NEW_PROF_PROMPT = PROMPT_TEMPLATE.format(
    "Qual o nome do perfil?", "[Para melhor identificação]", "Nome")
CREATE_NEW_PROF_SEQUENCE_PROMPT = PROMPT_TEMPLATE.format(
    "Qual a repetição a ser seguida?", "[Pode repetir. Separe por vírgula]",
    "Sequência"
)

#region Tools
def sequence_treatment(seq: str):
    parts = seq.replace(' ', '').split(",")
    result = []
    for part in parts:
        if part.isnumeric():
            result.append(int(part))
        continue
    return result

def secure_execute(func):
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        
        except json.decoder.JSONDecodeError as e:
            logging.error(f"Erro ao decodificar json, erro de sintaxe - {e}")

        except Exception as e:
            logging.error(f"Um erro desconhecido ocorreu: {e}")

    return wrapper
#endregion

#region Real Functions
@secure_execute
def load_profiles() -> dict | str:
    with open(PROFILE_FILE, 'r') as file:
        return json.load(file)

@secure_execute
def save_profile(data: dict = {}):
    with open(PROFILE_FILE, 'w') as file:
        json.dump(data, file)

@secure_execute
def create_new_profile():

    while True:
        name = input(CREATE_NEW_PROF_PROMPT).capitalize()
        sequence = input(CREATE_NEW_PROF_SEQUENCE_PROMPT)
        sequence = sequence_treatment(sequence)
        break

    logging.info("Perfil criado com sucesso!")
    return {name: sequence}
#endregion



if __name__ == '__main__':
    logging.basicConfig(format="[%(funcName)s] %(message)s")

    # Load
    profiles = load_profiles() or "Sem perfis salvos!"
    print(profiles)

    # Creation
    profile = create_new_profile()
    print(profile)

    # Save
    save_profile(profile)