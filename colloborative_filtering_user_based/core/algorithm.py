
from sklearn.metrics.pairwise import cosine_similarity
import operator
import pandas as pd


def similar_users(customer_id, matrix, k=3):
    """
    Find most similar users using cosine similarity
    :param customer_id: choosen user
    :param matrix: user-user matrix
    :param k: number of similar users
    :return:
    """
    # create a dataframe of just the current user
    user = matrix[matrix.index == customer_id]

    # and a df of all other users
    other_users = matrix[matrix.index != customer_id]

    # calc cosine similarity between user and each other user
    similarities = cosine_similarity(user, other_users)[0].tolist()

    # create list of indices of these users
    indices = other_users.index.tolist()

    # create key/values pairs of user index and their similarity
    index_similarity = dict(zip(indices, similarities))

    # sort by similarity
    index_similarity_sorted = sorted(index_similarity.items(), key=operator.itemgetter(1))
    index_similarity_sorted.reverse()

    # grab k users off the top
    top_users_similarities = index_similarity_sorted[:k]
    users = [u[0] for u in top_users_similarities]

    return users


# get the top 5 recommendations of gifts

def recommend_item(user_index, similar_user_indices, matrix, itemlist, items=5 ):
    # load vectors for similar users
    similar_users = matrix[matrix.index.isin(similar_user_indices)]
    # calc avg ratings across the 3 similar users
    similar_users = similar_users.mean(axis=0)
    # convert to dataframe so its easy to sort and filter
    similar_users_df = pd.DataFrame(similar_users, columns=['mean'])

    # get the gifts unpurchased by the current user
    # load vector for the current user
    user_df = matrix[matrix.index == user_index]
    # transpose it so its easier to filter
    user_df_transposed = user_df.transpose()
    # rename the column as 'rating'
    user_df_transposed.columns = ['rating']
    # remove any rows without a 0 value. gifts not purchased yet
    user_df_transposed = user_df_transposed[user_df_transposed['rating'] == 0]
    # generate a list of gifts the user has not purchased
    gifts_unpurchased = user_df_transposed.index.tolist()

    # filter avg ratings of similar users for only anime the current user has not seen
    similar_users_df_filtered = similar_users_df[similar_users_df.index.isin(gifts_unpurchased)]
    # order the dataframe
    similar_users_df_ordered = similar_users_df.sort_values(by=['mean'], ascending=False)
    # grab the top n gifts
    top_n_gifts = similar_users_df_ordered.head(items)
    top_n_gifts_indices = top_n_gifts.index.tolist()
    # lookup these gifts in the other dataframe to find names
    gifts_information = itemlist[itemlist['Description'].isin(top_n_gifts_indices)].reset_index(drop=True)

    return gifts_information #items
