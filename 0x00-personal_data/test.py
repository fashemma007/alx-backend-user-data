#!venv/bin/python

# create a logger that logs each level in a different format
import logging
import sys

logger = logging.Logger('classy_logs', logging.DEBUG)
# create a console handler set to ERROR level
con_err = logging.StreamHandler(sys.stderr)
con_err.setLevel(logging.ERROR)

con_err_fmt = logging.Formatter(
    fmt="{levelname}::{message} {asctime}", style="{", datefmt="%d/%m/%Y %H:%M:%S")

con_err.setFormatter(con_err_fmt)

logger.addHandler(con_err)
# create a console handler set to ERROR level
con_deb = logging.StreamHandler(sys.stdout)
con_deb.setLevel(logging.DEBUG)

con_deb_fmt = logging.Formatter(
    fmt="{asctime} {name} {message} {levelname}", style="{", datefmt="%d/%m/%Y %H:%M:%S")

con_deb.setFormatter(con_deb_fmt)

logger.addHandler(con_deb)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
