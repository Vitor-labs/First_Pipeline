"""
This module defines the ExtractError class, which is
a custom exception used for handling errors related
to extraction operations.
"""
class ExtractError(Exception):
    """
    Custom exception class for errors encountered during data extraction.

    Args:
        message (str): The error message explaining the cause of the exception.

    Attributes:
        message (str): The error message explaining the cause of the exception.
        error_type (str): The type of error, which is set to 'ExtractError'.
    """
    def __init__(self, message:str)->None:
        """
        Initializes a new instance of the ExtractError class.

        Args:
            message (str): The error message explaining the cause of the exception.
        """
        super().__init__(message)
        self.message=message
        self.error_type='ExtractError'
