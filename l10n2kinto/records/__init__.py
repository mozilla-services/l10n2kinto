from .base import Records
from .l10n import L10nRecords
from .kinto import KintoRecords

__all__ = ('same_record', 'Records', 'L10nRecords', 'KintoRecords')


def same_record(fields, one, two):
    for key in fields:
        if one.get(key) != two.get(key):
            return False
    return True
