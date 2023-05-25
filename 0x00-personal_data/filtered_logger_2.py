#!/usr/bin/env python3
"""module docs for filtered_logger.py"""

import re
from typing import List


def to_dict(msg) -> dict:
    """takes nested k:v pairs and converts to dict"""
    return_dict = {}
    for item in msg:
        try:
            # [return_dict.update(item) for item in msg]
            item = item.split("=")
            return_dict[item[0]] = item[1]
        except Exception:
            pass
    return return_dict


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
    new_message_dict = to_dict(message.split(separator))
    # hide specified data
    for field in fields:
        pattern = new_message_dict[field]
        message = re.sub(pattern, redaction, message)
    return message
