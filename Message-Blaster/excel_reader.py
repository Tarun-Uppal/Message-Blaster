import pandas as pd
import os

def read_file(contacts_path):
    data = pd.read_excel (contacts_path) 
    df = pd.DataFrame(data, columns= ['Name', 'Number'])
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
        contacts[i] = str(df.loc[i].Name)
        numbers[i] = int(df.loc[i].Number)
    
    return (contacts, numbers)

