# import from python libraries
import os
from attrdict import AttrDict

try:
    import magic
    MAGIC_IMPORTED = True
except ImportError:
    MAGIC_IMPORTED = False

try:
    import mimetypes
    MIMETYPES_IMPORTED = True
except ImportError:
    MIMETYPES_IMPORTED = False

def file_access_check(filepath, mode=os.R_OK, raise_exception=False):
    """ helper method to check file access"""
    if not filepath:
        raise AttributeError('missing file error')

    if (not os.path.exists(filepath) or
        not os.path.isfile(filepath) or
        not os.access(filepath, mode)):
            if raise_exception:
                raise AttributeError("'%' file access error" % filepath)
            return False

    return True

def reverse_attrdict(dict_data):
    """ helper method to recursivly convert dictionary to attrdict properties"""
    if not isinstance(dict_data, dict):
        return dict_data

    for key in list(dict_data.keys()):
        value = reverse_attrdict(dict_data.pop(key))
        key = key.replace('-', '_')
        dict_data[key] = AttrDict(value) if isinstance(value, dict) else value

    return dict_data

def deseralize(cls, input):
    """ helper method to deseralize json payload Veem Object"""
    return cls(**input) if isinstance(input, dict) else input

def extract_file_content_type(filename, buffer=None):
    """ helper method to extract file content type"""
    try:
        if MIMETYPES_IMPORTED:
            mimetype, encoding = mimetypes.guess_type(filename)
            return mimetype
        if mimetype is None and MAGIC_IMPORTED:
            if buffer:
                return magic.from_buffer(buffer, mime=True)
            return magic.from_file(filename, mime=True)
    except Exception:
        pass
    return "multipart/form-data"
