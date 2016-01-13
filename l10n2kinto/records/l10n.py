import codecs
from six.moves.configparser import ConfigParser
from six import StringIO

from .base import Records
from .id_generator import create_id


class L10nRecords(Records):
    def _load(self):
        self.files = self.options

        config = ConfigParser()

        for filepath in self.files:
            with codecs.open(filepath, 'r', encoding='utf-8') as stream:
                fakefile = StringIO("[top]\n" + stream.read())
                config.readfp(fakefile)

        return [self._l10n2rec(key, config.get('top', key))
                for key in config.options('top')]

    def _l10n2rec(self, key, value):
        rec = {
            "id": create_id(key),
            "key": key,
            "value": value
        }

        return rec
