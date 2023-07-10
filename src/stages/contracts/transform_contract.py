from collections import namedtuple

TransformContract=namedtuple(
    "TransformContract", 
    '''
        content
    '''
)

"""
A named tuple representing the contract for transforming data.
Args:
    content: The content to be transformed.
"""
