from loguru import logger


def load(filepath):
    """Loads data from filepath to the database"""
    try:
        with open(filepath) as file_:
            return [line.strip() for line in file_.readlines()]
    except FileNotFoundError as e:
        logger.error(str(e))
        raise e
