#!/usr/bin/env python3
"""module docs for filtered_logger.py"""

import logging
import os
import re
import mysql.connector
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    The filter_datum function takes in a list of fields, a redaction string,
    a message string and a separator. It returns the message with all instances
    of the fields replaced by the redaction.

    :param fields:List[str]: Specify the fields that are to be redacted
    :param redaction:str: Replace the fields that are to be redacted
    :param message:str: Pass in the message that is to be filtered
    :param separator:str: Separate the fields in the message
    :return: A string with the message and separator
    """
    for key in fields:
        pattern = key + r'(.*?)' + separator  # all chars btw key & sep
        replacement = key + '=' + redaction + separator
        message = re.sub(pattern, replacement, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter incoming records using `filter_datum`"""
        # convert record logger obj to string with
        # logging.Formatter.format() method
        mesg = super(RedactingFormatter, self).format(record)
        # print(mesg)
        return filter_datum(self.fields, self.REDACTION, mesg, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    The get_logger function creates a logger object that can be used to log
    messages.
    The function returns the logger object.

    :return: A logger object
    """
    # METHOD-1: using getLogger
    # logger = logging.getLogger("user_data")
    # logger.setLevel(logging.INFO)

    # OR using the class itself
    logger = logging.Logger("user_data", logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.propagate = False  # ancestors shld not get events from dz
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    creates a mysql db connection
    """
    user = os.getenv('PERSONAL_DATA_DB_USERNAME') or "root"
    passwd = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ""
    host = os.getenv('PERSONAL_DATA_DB_HOST') or "localhost"
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    conn = mysql.connector.connect(user=user,
                                   password=passwd,
                                   host=host,
                                   database=db_name)
    return conn


def main():
    """
    main entry point
    """
    db = get_db()
    logger = get_logger()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = cursor.column_names
    for row in cursor:
        message = "".join("{}={}; ".format(k, v) for k, v in zip(fields, row))
        logger.info(message.strip())
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
