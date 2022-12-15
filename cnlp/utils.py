import importlib as imlib


def imp(m, frm=None):
    """ 
    Dynamic function of module importation 
    :param:
        m       [str] name of module which will be imported.
        _from   [str] name of module which will be the source of importation
    :return:
        An instance of the imported module.
    """
    x = "";
    try:
        if frm is not None: 
            x = f"{frm}.{m}";
            mdl = imlib.import_module(frm);
            if hasattr(mdl, m):
                return getattr(mdl, m);
            else:
                raise AttributeError("{} is not defined".format(m))
        else: 
            x = m;
            return imlib.import_module(x);
    except ModuleNotFoundError as e:
        raise Exception("[ \033[91mIMPORTATION ERROR\033[0m ] " + str(e) + f"\n\033[91m>>> {x}\033[0m");
    except AttributeError as e:
        raise Exception("[ \033[91mATTRIBUTE ERROR\033[0m ] " + str(e) + f"\n\033[91m>>> {x}\033[0m");

