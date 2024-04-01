"""! @brief Miscellaneous useful methods
 @file utils.py
 @section authors Author(s)
  - Created by Nicolas Dufresne on 4/1/2024 .
"""

def mergeDicts(a:dict, b:dict):
    """!
    @brief Merges two dicts,
    in case there are the same keys, the values from
    the second dict overwrite the values in the first.

    This function is used to keep backwards compatibility
    with Python < 3.5 (where native methods exist for this)

    Parameters : 
        @param a : dict => The first dict
        @param b : dict => The second dict

    @return {dict} The new dict.
    """
    z = a.copy()   # start with keys and values of a
    z.update(b)    # modifies z with keys and values of b
    return z
