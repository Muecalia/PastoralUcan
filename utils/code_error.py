from enum import Enum


class CodeError(Enum):
    
    # SUCCESS
    INSERT_SUCCESS = 1
    UPDATE_SUCCESS = 2
    DELETE_SUCCESS = 3
    LIST_SUCCESS = 4
    
    # ERROR
    INSERT_ERROR = -1
    UPDATE_ERROR = -2
    DELETE_ERROR = -3
    LIST_ERROR = -4
    NOT_FOUND = -5
    BAD_REQUEST = -6
    EXISTS = -7
    NULL = -8
    
    