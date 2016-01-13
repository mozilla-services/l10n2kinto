from kinto_client import Client
from kinto_client.exceptions import KintoException

from .base import Records
from .id_generator import create_id


class KintoRecords(Records):
    def _load(self):
        self.client = Client(server_url=self.options['server'],
                             auth=self.options['auth'],
                             bucket=self.options['bucket_name'],
                             collection=self.options['collection_name'])

        # Create bucket
        try:
            self.client.create_bucket()
        except KintoException as e:
            if e.response.status_code != 412:
                raise e
        try:
            self.client.create_collection(
                permissions=self.options['permissions'])
        except KintoException as e:
            if e.response.status_code != 412:
                raise e

        return [self._kinto2rec(rec) for rec in
                self.client.get_records()]

    def _kinto2rec(self, record):
        return record

    def delete(self, data):
        self.client.delete_record(data['id'])

    def create(self, data):
        if 'id' not in data:
            data['id'] = create_id(data)
        rec = self.client.create_record(data)
        return rec
