"""Introduction
~~~~~~~~~~~~~~~

The :mod:`libraw` package contains low-level CTYPES_ based APIs for interfacing
with LibRaw_ by LibRaw, LLC.

While this library can be used on its own to access the full functionality of
LibRaw and develop raw photos, we recommend using the higher-level :mod:`rawkit`
module, which provides a more pythonic interface to LibRaw.

Currently, the following API versions of LibRaw are supported (note that these
are API versions, not the package versions which you download, eg. API 10 is
LibRaw 16):

  - {}

.. _CTYPES: https://docs.python.org/3/library/ctypes.html
.. _LibRaw: http://www.libraw.org
"""

from libraw.library import __supported_versions__

__doc__ = __doc__.format('\n  - '.join(__supported_versions__()))
