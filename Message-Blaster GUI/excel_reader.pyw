import pandas as pd
import os
import re

def isValid(s):
    """
    validates the number
    """
    # casts the number into a string
    s = str(s)
    # stores the pattern
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    # validates the pattern and returns thue if it is valid otherwise false
    if (Pattern.match(s)) and len(s) == 12: 
        return True
    else:
        return False

def read_file(contacts_path):
    try:
        data = pd.read_excel (contacts_path) 
    except AssertionError:
        return None
    df = pd.DataFrame(data, columns=['Name', 'Number'])
    entries_count = 0
    while True:
        try:
            name = df.loc[entries_count].Name
        except KeyError as e:
            break
        entries_count += 1
        
    contacts = [None] * entries_count
    numbers = [None] * entries_count
    for i in range(entries_count):   
        if str(df.loc[i].Name) == 'nan':
            return None
        else:
            contacts[i] = str(df.loc[i].Name)
        try:
            if isValid(910000000000 + int(df.loc[i].Number)) == True:
                numbers[i] = int(df.loc[i].Number)
            else:
                return None
        except ValueError:
            return None
        
    
    return (contacts, numbers)