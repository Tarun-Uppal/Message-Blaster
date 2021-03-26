import pandas as pd
import os

def read_file(contacts_path):
    data = pd.read_excel (contacts_path) 
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
            numbers[i] = int(df.loc[i].Number)
        except ValueError as e:
            return None
    
    return (contacts, numbers)