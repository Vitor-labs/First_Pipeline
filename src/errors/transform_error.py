"""
This module defines the TransformError class, which is a
custom exception used for handling errors related to
transform operations.
"""
class TransformError(Exception):
    """
    Custom exception class for errors encountered during 
    data transformation.

    Args:
        message (str): The error message explaining the
        cause of the exception.

    Attributes:
        message (str): The error message explaining the
        cause of the exception.
        error_type (str): The type of error, which is set
        to 'ExtractError'.
    """
    def __init__(self, message:str)->None:
        """
        Initializes a new instance of the TransformError
        class.

        Args:
            message (str): The error message explaining the
            cause of the exception.
        """
        super().__init__(message)
        self.message=message
        self.error_type='TransformError'
