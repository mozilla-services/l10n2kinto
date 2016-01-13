import hashlib
import uuid
from six import text_type


def create_id(key):
    hash = hashlib.md5(key)
    return text_type(uuid.UUID(hash.hexdigest()))
