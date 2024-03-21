#Calculate num of tie and total points

number_of_games_played = int(input("Enter number_of_games_played - "))
number_of_games_WON = int(input("Enter number_of_games_WON - "))
number_of_games_LOSS = number_of_games_played -number_of_games_WON

Won_points = 4*number_of_games_WON

total_tied = number_of_games_played-number_of_games_WON
tie_points = 2*total_tied

if number_of_games_WON==number_of_games_LOSS:
    print( "Toatl total_tied and total_tied = ",total_tied,":", tie_points)
else:
    print("Total won points" , Won_points)

print("Congratulations for Playing in this Game")


