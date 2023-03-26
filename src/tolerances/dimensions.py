import typing
from abc import ABC, abstractmethod

import numpy as np


class Dimension(ABC):

    @property
    @abstractmethod
    def basic(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def upper_tol(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def lower_tol(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def lower_limit(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def upper_limit(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def midpoint(self) -> float:
        raise NotImplementedError

    @property
    def tolerance(self) -> float:
        '''Returns the range between the limits.'''
        return self.upper_tol+self.lower_tol

    @abstractmethod
    def sample(self) -> float:
        raise NotImplementedError


class SimpleDimension(Dimension):
    def __init__(self, basic: float, upper_tol: float, lower_tol: float,
                 sample: typing.Optional[typing.Callable[[], float]] = None) -> None:
        '''Constructor for dimension.'''
        # Checks on inputs
        if basic < 0:
            raise ValueError('Basic dimension must be positive.')
        if upper_tol < 0 or lower_tol < 0:
            raise ValueError('Tolerances must be positive.')

        # Assign
        self._basic = basic
        self._upper_tol = upper_tol
        self._lower_tol = lower_tol

        # If no sampling function is defined, assume gaussian
        if sample is None:
            self._sample = lambda: np.random.normal(
                self.midpoint, self.tolerance/8)
        else:
            self._sample = sample

    @property
    def basic(self) -> float:
        return self._basic

    @property
    def upper_tol(self) -> float:
        return self._upper_tol

    @property
    def lower_tol(self) -> float:
        return self._lower_tol

    @property
    def lower_limit(self) -> float:
        '''Returns the lower limit for the dimension.'''
        return self.basic-self.lower_tol

    @property
    def upper_limit(self) -> float:
        '''Returns the upper limit for the dimension.'''
        return self.basic+self.upper_tol

    @property
    def midpoint(self) -> float:
        '''Returns the midpoint between the upper and lower limit.
        This is not nescessarily the same as the basic dimension, i.e., in the case
        of an assymetrical upper and lower tolerance.
        '''
        return self.lower_limit + ((self.upper_tol+self.lower_tol)/2)

    def sample(self) -> float:
        return self.sample()


class DerivedDimension(Dimension):
    def __init__(self, uppers: typing.List[Dimension], lowers: typing.List[Dimension]) -> None:
        self._uppers = uppers
        self._lowers = lowers

    @property
    def basic(self) -> float:
        u = sum([dim.basic for dim in self._uppers])
        l = sum([dim.basic for dim in self._lowers])
        return u - l
    
    @property
    def upper_tol(self) -> float:
        u = sum([dim.upper_tol for dim in self._uppers])
        l = sum([dim.lower_tol for dim in self._lowers])
        return u - l
    
    @property
    def lower_tol(self) -> float:
        u = sum([dim.lower_tol for dim in self._uppers])
        l = sum([dim.upper_tol for dim in self._lowers])
        return u - l
    
    @property
    def upper_limit(self) -> float:
        u = sum([dim.upper_limit for dim in self._uppers])
        l = sum([dim.lower_limit for dim in self._lowers])
        return u - l
    
    @property
    def lower_limit(self) -> float:
        u = sum([dim.lower_limit for dim in self._uppers])
        l = sum([dim.upper_limit for dim in self._lowers])
        return u - l
    
    @property
    def midpoint(self) -> float:
        u = sum([dim.midpoint for dim in self._uppers])
        l = sum([dim.midpoint for dim in self._lowers])
        return u - l
    
    def sample(self) -> float:
        u = sum([dim.sample() for dim in self._uppers])
        l = sum([dim.sample() for dim in self._lowers])
        return u - l
    

