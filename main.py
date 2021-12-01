from End_Of_Game import EndOfGame, Query

def main():

    ###### mimic end of game #####
    ### will make sure these variable names match rest of main script ###
    player_name = 'chloe'
    game_character = 'batman'
    end_result = 'Got too drunk!'



    ### this saves the game by creating time stamp for when the game finishes then converts to string ###
    finish = EndOfGame()
    game_time_string = finish.save()

    ### sends all the queries to check if player exists, if not then sends player info, then sends game info
    # then updates the total number of plays for the player ###
    database_queries = Query()
    database_queries.send_all_queries(player_name, game_character, game_time_string, end_result)


if __name__=='__main__':
    main()


