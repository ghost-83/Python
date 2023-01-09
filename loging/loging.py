import logging


def log():
    logging.basicConfig(format="[%(asctime)s] %(filename)s[LINE:%(lineon)d %(levelname)-8s %(message)s",
                        level=logging.INFO)

    return logging
