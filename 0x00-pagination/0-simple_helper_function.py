#!/usr/bin/env python3
"""
function that calculates start and end index
based on the given pagination parameters
return a tuple of size 2 containing start and index
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    calculate start and end index
    return tuple
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
