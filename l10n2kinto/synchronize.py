from kinto_client.exceptions import KintoException

from l10n2kinto import logger, COMMAND
from l10n2kinto.exceptions import SynchronizationError
from l10n2kinto.records import L10nRecords, KintoRecords, same_record

FIELDS = ('key', 'value')


def synchronize(files, kinto_options):
    logger.log(COMMAND, 'Working on %r' % kinto_options['server'])
    logger.debug('Reading data from files')
    l10n = L10nRecords(files)
    kinto = KintoRecords(kinto_options)
    to_delete = []
    to_update = []
    to_create = []

    logger.log(COMMAND, 'Syncing to %s/buckets/%s/collections/%s/records' % (
        kinto_options['server'].rstrip('/'),
        kinto_options['bucket_name'],
        kinto_options['collection_name']))

    # looking at kinto to list records
    # to delete or to update
    for record in kinto.records:
        l10n_rec = l10n.find(record['id'])
        if l10n_rec is None:
            to_delete.append(record)
        else:
            if not same_record(FIELDS, l10n_rec, record):
                to_update.append(l10n_rec)

    # new records ?
    for record in l10n.records:
        kinto_rec = kinto.find(record['id'])
        if not kinto_rec:
            to_create.append(record)

    logger.log(COMMAND, '- %d records to create.' % len(to_create))
    logger.log(COMMAND, '- %d records to update.' % len(to_update))
    logger.log(COMMAND, '- %d records to delete.' % len(to_delete))

    if len(to_delete) > 0:
        logger.log(COMMAND, 'You may want to delete the following keys:')

    for record in to_delete:
        logger.log(COMMAND, '- %s: %s=%s' % (record['id'],
                                     record['key'],
                                     record['value']))

        # XXX: Add an option to ask for deletion
        # try:
        #     kinto.delete(record)
        # except KintoException as e:
        #     raise SynchronizationError(e.response.content)

    for record in to_create + to_update:
        try:
            kinto.create(record)
        except KintoException as e:
            raise SynchronizationError(e.response.content)

    print('Done!')
