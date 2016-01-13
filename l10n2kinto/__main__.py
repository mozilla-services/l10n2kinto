# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse
import getpass
import logging
import os

from l10n2kinto import logger, COMMAND
from l10n2kinto.synchronize import synchronize

COLLECTION_PERMISSIONS = {'read': ["system.Everyone"]}
DEFAULT_KINTO_SERVER = 'http://localhost:8888/v1'
DEFAULT_USER_NAME = 'admin'


def main(args=None):
    parser = argparse.ArgumentParser(description='Take properties files and '
                                     'sync them with a Kinto collection.')

    parser.add_argument('-s', '--host', help='Kinto Server',
                        type=str, default=DEFAULT_KINTO_SERVER)

    parser.add_argument('-u', '--auth', help='BasicAuth user:pass',
                        type=str, default=DEFAULT_USER_NAME)

    parser.add_argument('-b', '--bucket',
                        help='Bucket name, usually the app name',
                        type=str)

    parser.add_argument('-c', '--collection',
                        help='Collection name, usually the locale code',
                        type=str)

    parser.add_argument('files', metavar='N', type=str, nargs='+',
                        help='A list of properties file for the locale.')

    parser.add_argument('--verbose', '-v',
                        help='Display status',
                        dest='verbose',
                        action='store_true')

    args = vars(parser.parse_args(args=args))

    verbose = args['verbose']

    if verbose:
        logger.setLevel(logging.INFO)

    files = []
    for f in args['files']:
        if os.path.exists(f):
            files.append(os.path.abspath(f))
            logger.log(COMMAND, '%s: ✓' % os.path.abspath(f))
        else:
            logger.error('%s: ✗' % os.path.abspath(f))

    auth = args.get('auth')

    if auth:
        # Ask for the user password if needed
        auth = tuple(auth.split(':', 1))
        if len(auth) < 2:
            email = auth[0]
            password = getpass.getpass('Please enter a password for %s: '
                                       % email)
            auth = (email, password)

    synchronize(files,
                kinto_options={
                    'server': args['host'],
                    'bucket_name': args['bucket'],
                    'collection_name': args['collection'],
                    'auth': auth,
                    'permissions': COLLECTION_PERMISSIONS
                })


if __name__ == '__main__':  # pragma: nocover
    main()
