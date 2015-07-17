from ctypes import util
from importlib import import_module
import sys


__library__ = util.find_library('raw')

if __library__ is None:
    raise ImportError('Cannot find LibRaw on your system!')

__api_version__ = int(__library__.split('.')[-1])


def __load_module__(module_name):
    api_module = 'libraw.api_{api_version}'.format(api_version=__api_version__)
    versioned_module_name = module_name.replace('libraw', api_module)
    try:
        sys.modules[module_name] = import_module(versioned_module_name)
    except ImportError:
        raise ImportError(
            'Unsupported LibRaw version: {api_version}',
            api_version=__api_version__,
        )
