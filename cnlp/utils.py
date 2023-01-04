import importlib as imlib


def imp(m, frm=None):
    """Dynamic function of module importation 

    Args:
        m (str): The name of module which will be imported.
        _from (str): The name of module which will be the source of importation.

    Return:
        mixed: An instance of the imported module.

    Raises:
        AttributeError: if the `frm` module has not attribut named `m`.
        ModuleNotFoundError: if the module named `frm.m` is not found.
    """
    complete_module = ""
    try:
        if frm is not None: 
            complete_module = f"{frm}.{m}"
            mdl = imlib.import_module(frm)
            if hasattr(mdl, m):
                return getattr(mdl, m)
            else:
                raise AttributeError("{} is not defined".format(m))
        else:
            complete_module = m
            return imlib.import_module(complete_module)
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "[ \033[91mIMPORTATION ERROR\033[0m ] " + str(e)\
            + f"\n\033[91m>>> {complete_module}\033[0m")
    except AttributeError as e:
        raise AttributeError(
            "[ \033[91mATTRIBUTE ERROR\033[0m ] " + str(e)\
            + f"\n\033[91m>>> {complete_module}\033[0m")

