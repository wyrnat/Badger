from pkg_resources import get_distribution
try:
    from ..factory import BADGER_PLUGIN_ROOT, BADGER_EXTENSIONS
except:
    BADGER_PLUGIN_ROOT = None
    BADGER_EXTENSIONS = None
try:
    from ..db import BADGER_DB_ROOT
except:
    BADGER_DB_ROOT = None
try:
    from ..logbook import BADGER_LOGBOOK_ROOT
except:
    BADGER_LOGBOOK_ROOT = None
try:
    from ..archive import BADGER_RUN_ROOT
except:
    BADGER_RUN_ROOT = None
from ..utils import yprint


def show_info(args):
    if args.gui:
        from ..gui import launch_gui

        launch_gui()
    else:
        info = {
            'name': 'Badger the optimizer',
            'version': get_distribution('badger-opt').version,
            'plugin root': BADGER_PLUGIN_ROOT,
            'database root': BADGER_DB_ROOT,
            'logbook root': BADGER_LOGBOOK_ROOT,
            'run root': BADGER_RUN_ROOT,
        }

        if BADGER_EXTENSIONS:
            extensions = list(BADGER_EXTENSIONS.keys())
            if extensions:
                info['extensions'] = extensions

        yprint(info)
        # print(f'Badger the optimizer')
        # print('====================')
        # print(f'version      : {version}')
        # print(f'plugins root : {BADGER_PLUGIN_ROOT}')
