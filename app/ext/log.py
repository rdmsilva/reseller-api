import logging

from settings import LOG_LEVEL


def create_log():
    logger = logging.getLogger('reseller')
    logger.setLevel(LOG_LEVEL.upper())
    ch = logging.StreamHandler()
    ch.setLevel(LOG_LEVEL.upper())
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


logger = create_log()
