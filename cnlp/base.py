import time
from . import LOG


class BaseAlgorithm:
    """ Basic algorithm structure to represents all algorithm of processing. """
    @property
    def name(self):
        """ Return the name given to this algorithm """
        if hasattr(self, '_name'): 
            return self._name;
        else:
            return self.classname();

    @property
    def results(self):
        """ Return the results producted by the algorithm. """
        raise NotImplementedError(
            "{BaseAlgorithm.results} Function must be implement in your subclass "
            f"{self.classname()}"
        );

    def classname(self):
        """ Return the class name of the current instance """
        return self.__class__.__name__;

    def _f_(self, *args, **kwargs):
        """
        Sub function called, when an algorithm is called by __call__ function. 
        This function is abstract, so must be defined on the subclass will be implemented.
        """
        raise NotImplementedError(
            "{BaseAlgorithm._f_} Function must be implement in your subclass "
            f"{self.classname()}"
        );

    def __call__(self, *args, **kwargs):
        """ 
        Function called, when an algorithm is called. This function is abstract, 
        so must be defined on the subclass will be implemented.
        """
        init = time.time();
        res  = self._f_(*args, **kwargs);
        LOG("Executed in %.3fsec." % (time.time() - init));
        return res;


