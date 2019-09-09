import collections
from six import iteritems


def mapping_extend(original, *updates):
    """Extend a deeply nested dictionary with values from another dict.
    Somewhat mirrors Javascript's Object.extend.
    Items from `original` will be overridden IN PLACE with items from each dict
    in `updates`. Sequence objects will be extended"""

    for update in updates:
        for k, v in iteritems(update):
            if isinstance(v, collections.Mapping):
                r = mapping_extend(original.get(k, {}), v)
                original[k] = r
            elif isinstance(v, collections.Sequence):
                if k not in original:
                    original[k] = []
                original[k].extend(v)
            else:
                original[k] = update[k]
    return original
