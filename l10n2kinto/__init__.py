import logging

COMMAND = 25
logging.addLevelName(COMMAND, 'COMMAND')

logger = logging.getLogger("l10n2kinto")
logging.basicConfig(level=COMMAND, format="%(message)s")
