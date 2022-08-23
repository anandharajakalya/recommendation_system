from basic.i_o_functions import *
from sklearn.preprocessing import MinMaxScaler
import numpy as np


def general_proprocessing(data):
    """
    Process the data for recommendation
    :param data: dataframe
    :return: filtered transaction data, items
    """

    #Remove gifts thats are not bought by many customers
    sig_gifts = data.groupby(['Description']).agg({'Description': 'count'}).rename(columns={'Description' : 'customercount'}).reset_index()

    #filter gifts that is bought by atleast 50 customers
    sig_gifts = sig_gifts[sig_gifts['customercount'] >= 50]
    gifts = sig_gifts[['Description']]

    #Merge with the main dataset to get gifts with the list of customer who bought it
    filtered_data = data.merge(sig_gifts, on='Description', how='left')
    filtered_data = filtered_data[filtered_data['customercount'].notna()]

    #Derive ratings to identify how much a user likes a specific item
    ratings_data = filtered_data.groupby(['CustomerID','Description']).agg({'Description': 'count'}).rename(columns={'Description' : 'Ratings'}).reset_index()

    #normalize ratings field
    ratings_data['Ratings'] = MinMaxScaler().fit_transform(np.array(ratings_data['Ratings']).reshape(-1,1))

    return ratings_data, gifts

def build_user_user_matrix(data):
    """
    Specific user based preprocessing steps
    :param data: dataframe
    :return:
    """

    #Build user*user matrix
    data = data.pivot_table(index='CustomerID', columns='Description', values='Ratings')

    #replace NaN values with 0
    data = data.fillna(0)
    return data
