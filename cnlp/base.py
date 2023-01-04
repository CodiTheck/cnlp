"""Basic definition module of CNLP package.
"""
import time
from . import LOG


class BaseAlgorithm:
    """Basic algorithm structure to represents all algorithm of processing.
    """
    @property
    def name(self):
        """str: Return the name given to this algorithm. """
        if hasattr(self, '_name'): 
            return self._name
        else:
            return self.classname()

    @property
    def results(self):
        """str: Return the results producted by the algorithm. """
        raise NotImplementedError(
            "{BaseAlgorithm.results} Function must be implement"
            " in your subclass"
            f"{self.classname()}"
        )

    def classname(self):
        """Return the class name of the current instance 
        Returns:
            str: Class name.
        """
        return self.__class__.__name__

    def _f_(self, *args, **kwargs):
        """Definition of algorithm main function.

        Sub function called, when an algorithm is called by __call__ function. 
        This function is abstract, so must be defined on the subclass 
        will be implemented.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Additional keyword arguments.
        
        Raises:
            NotImplementedError: Function must be implement in your subclass.
        """
        raise NotImplementedError(
            "{BaseAlgorithm._f_} Function must be implement in your subclass "
            f"{self.classname()}"
        )

    def __call__(self, *args, **kwargs):
        """  Redefining of __call__ function.
        
        Function called, when an algorithm is called. This function is abstract, 
        so must be defined on the subclass will be implemented.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Additional keyword arguments.

        Raises:
            NotImplementedError: Function must be implement in your subclass.
        """
        init = time.time()
        res = self._f_(*args, **kwargs)
        LOG("Executed in %.3fsec." % (time.time() - init))
        return res


