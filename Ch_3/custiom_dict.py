import collections

class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item

from types import MappingProxyType
# it can mutable only on d (dict)
# d_proxy is always read-only
# but d_proxy is dynamic: any changed in d is reflected!
d = {1:'A'}
d_porxy = MappingProxyType(d)
