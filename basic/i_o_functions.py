import pandas as pd

#iofiles
def read_csv(path_to_data):
    """
    read a comma seperated file into pandas dataframe
    path_to_data: location of the csvfile to be read
    :return: read output
    """
    data = pd.read_csv(path_to_data, encoding='unicode_escape')
    return data