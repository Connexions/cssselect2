# coding: utf8

import re

from tinycss2 import serialize

from . import ext_utils as ex


def _match(selector):
    "Callback for match pseudoClass."
    regex = serialize(selector.arguments)
    trim = '\"\''
    if regex[0] in trim and regex[0] == regex[-1]:
        regex = regex[1:-1]
    else:
        regex = re.sub(r'(?<!\\)[\\]', '', regex)
    return ('(re.search("%s", ex.textstring(el)) is not None)' % regex)


extensions = {'pseudoClass': {'match': {'callback': _match,
                                        'modules': {'re': re,
                                                    'ex': ex}
                                        },
                              'pass': {'callback': lambda s: '1'},
                              'deferred': {'callback': lambda s: '1'},
                              }
              }
