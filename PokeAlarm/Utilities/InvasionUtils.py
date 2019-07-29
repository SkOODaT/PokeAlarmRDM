from glob import glob
import json

from PokeAlarm.Utils import get_path


def get_invasion_id(invasion_name):
    try:
        name = unicode(invasion_name).lower()
        if not hasattr(get_invasion_id, 'ids'):
            get_invasion_id.ids = {}
            files = glob(get_path('locales/*.json'))
            for file_ in files:
                with open(file_, 'r') as f:
                    j = json.loads(f.read())
                    j = j['invasion_types']
                    for id_ in j:
                        nm = j[id_].lower()
                        get_invasion_id.ids[nm] = int(id_)
        if name in get_invasion_id.ids:
            return get_invasion_id.ids[name]
        else:
            return int(name)  # try as an integer
    except ValueError:
        raise ValueError("Unable to interpret `{}` as a valid "
                         " invasion name or id.".format(lure_name))