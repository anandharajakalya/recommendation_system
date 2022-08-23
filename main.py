from basic.i_o_functions import *
from basic.datapreprocessing import *
from colloborative_filtering_user_based.core.algorithm import  *
from definitions import TYPE_OF_RECOMMENDATION


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # read the data
    purchase_history = read_csv("data/purchase_history.csv")

    #basic_dataprocessing
    transaction_data, itemlist = general_proprocessing(purchase_history)

    if TYPE_OF_RECOMMENDATION == "USER_BASED":
        #build user matrix
        user_user_matrix = build_user_user_matrix(transaction_data)

        #find similar users
        choose_userid = 12346.0
        find_similar_users = similar_users(choose_userid, user_user_matrix)

        #make 5 gift recommendations for the choosen user
        recommendations = recommend_item(choose_userid, find_similar_users, user_user_matrix, itemlist)

        print ("User based recommendations: ")

        for item in recommendations['Description'].tolist():
            print (item)



