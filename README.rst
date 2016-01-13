==========
l10n2kinto
==========

Take a l10n.js property file and create a Kinto collections that let's
people sync the file translation.


Usage
=====

.. code-block::

    l10n2kinto --host https://kinto.dev.mozaws.net/v1 \
               --auth user \
               --bucket loop-client \
               --collection fr \
               --in l10n/fr/*.properties

It will open all properties file in the fr directory and create a new
translation record for each entry:

.. code-block::

    {
        "id": "8cf933da-2224-fc06-f12c-d5d4ed4ac778",
        "last_modified": 1452701470453,
        "key": "chat_textbox_placeholder",
        "value": "Écrivez ici…"
    }
