from collections import namedtuple


ExtractContract=namedtuple(
    "ExtractContract", 
    '''
        raw_info
        extract_date
    '''
)

"""
A named tuple representing the contract for extracting data.
Args:
    raw_info: The raw information to be extracted.
    extract_date: The date of extraction.
"""
