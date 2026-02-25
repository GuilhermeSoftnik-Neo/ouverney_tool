from importlib.util import spec_from_file_location
from importlib.util import module_from_spec
from logging import error, warning
from typing import Generator
from pathlib import Path
from os import listdir
from inspect import getmembers, isclass, isabstract


this_folder = Path(__file__).resolve().parent.absolute()


def get_pyfiles_in_the_folder(folder: str | Path = this_folder) -> Generator:
    try:
        return filter(
            lambda x: (
                x
                if (
                    Path(folder / x).is_file()
                    and x.endswith(".py")
                    and not x.startswith("_")
                )
                else None
            ),
            listdir(folder),
        )

    except Exception as e:
        error(f"Não foi possível pegar arquivos .py na pasta {folder}. Motivo:", e)


def import_all_modules_of_got_pyfiles(
    py_files: list | Generator, folder: Path | str = this_folder
) -> list:
    modules = []

    for file in py_files:
        spec = spec_from_file_location(
            f"src.infra.{file.replace(".py", "")}", folder / file
        )
        module = module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            modules.append(module)

        except FileNotFoundError:
            warning(
                f"Arquivo não encontrado: {file} - Recomenda-se checar, a fim de evitar o comportamento indesejado do programa"
            )
            continue

        except AttributeError as e:
            error(f"O loader do especificador {spec.name} está vazio!")
            raise e

        except ModuleNotFoundError as e:
            error(f"Erro crítico! O módulo {module} não existe.")

        except Exception as e:
            error(
                "Erro desconhecido na Infraestrutura!",
                e,
            )
            raise e

    return modules


def extract_Comando_objects_from_a_module(module) -> list:
    result = []

    for _, obj in getmembers(module, lambda x: isclass(x) and not isabstract(x)):
        if hasattr(obj, "executar"):
            result.append(obj)

    return result
