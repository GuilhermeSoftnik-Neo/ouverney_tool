try:
    from .utils import *

except ImportError:
    from utils import *

except ModuleNotFoundError as e:
    print(
        "O módulo utils não pôde ser importado. Impossível prosseguir com infraestrutura danificada. Motivo:",
        e,
    )
    raise e


def get_every_obj_child_of_Comando():
    pyfiles = get_pyfiles_in_the_folder()
    modules = import_all_modules_of_got_pyfiles(pyfiles)

    comandos = []
    [
        comandos.extend(extract_Comando_objects_from_a_module(module))
        for module in modules
    ]

    return comandos


if __name__ == "__main__":
    comandos = get_every_obj_child_of_Comando()
    for c in comandos:
        print(c().nome)
    print(len(comandos), "subclasses de Comando encontradas.")
