from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .pyppeteer_pdf import save_pdf, get_args_kwargs, main, PyppdfError
