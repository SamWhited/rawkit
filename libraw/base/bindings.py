""":mod:`libraw.bindings` --- Low-level LibRaw bindings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :class:`libraw.bindings` module handles linking against the LibRaw binary.
"""

from ctypes import *  # noqa

from libraw.library import __api_version__
from libraw.library import __library__


class LibRaw(CDLL):

    """
    A :class:`ctypes.CDLL` that links against `libraw.so` (or the equivalent on
    your platform).
    """

    def __init__(self):  # pragma: no cover
        try:
            super(LibRaw, self).__init__(__library__)
        except (ImportError, AttributeError, OSError, IOError):
            raise ImportError('Error loading LibRaw!')

    @property
    def version_number(self):
        """
        A numeric representation of the version of LibRaw which we have linked
        against in ``(Major, Minor, Patch)`` form. eg. ::

            (0, 16, 1)

        Returns:
            3 tuple: The version number
        """
        raise NotImplementedError

    @property
    def version(self):
        """
        A string representation of the version of LibRaw which we have linked
        against. eg. ::

            "0.16.1-Release"

        Returns:
            str: The version
        """
        raise NotImplementedError

    @property
    def api_version(self):
        """
        API version of LibRaw

        Returns:
            int: API version
        """
        return __api_version__
