import sys
from nba_api.stats.endpoints import boxscoretraditionalv2


def print_box_score(game_id, start_period, end_period):
    # Acquire data frame
    box_score = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_id, start_period=start_period, end_period=end_period)
    data_frame = box_score.data_sets[0].get_data_frame()

    # Massage data
    del data_frame['GAME_ID']
    del data_frame['TEAM_ID']
    del data_frame['PLAYER_ID']

    # Separate by teams
    teams = data_frame[['TEAM_ABBREVIATION', 'TEAM_CITY']].drop_duplicates().reindex()
    team_1 = teams.iloc[0]
    team_2 = teams.iloc[1]

    team_1_data = data_frame.where(data_frame['TEAM_ABBREVIATION'] == team_1['TEAM_ABBREVIATION']).dropna()
    del team_1_data['TEAM_ABBREVIATION']
    del team_1_data['TEAM_CITY']

    team_2_data = data_frame.where(data_frame['TEAM_ABBREVIATION'] == team_2['TEAM_ABBREVIATION']).dropna()
    del team_2_data['TEAM_ABBREVIATION']
    del team_2_data['TEAM_CITY']

    # Display data
    print(f"{team_1['TEAM_CITY']}'s box score from period {start_period} to period {end_period}")
    print(team_1_data.to_string(index=False))

    print()

    print(f"{team_2['TEAM_CITY']}'s box score from period {start_period} to period {end_period}")
    print(team_2_data.to_string(index=False))


if __name__ == "__main__":
    game_id = sys.argv[1]
    start_period = sys.argv[2]
    end_period = sys.argv[3]

    print_box_score(game_id, start_period, end_period)


