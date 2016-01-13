class Records(object):
    def __init__(self, options=None):
        if options is None:
            self.options = {}
        else:
            self.options = options
        self.records = self._load()

    def _load(self):
        raise NotImplementedError()

    def find(self, id):
        for rec in self.records:
            if rec['id'] == id:
                return rec
