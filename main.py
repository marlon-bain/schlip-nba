import sys
from nba_api.stats.endpoints import boxscoretraditionalv2


def print_box_score(team_name, data, start_period, end_period):
    period_description = \
        f"in period {start_period}" \
        if start_period == end_period \
        else f"from period {start_period} to {end_period}"

    print(f"{team_name}'s box score {period_description}")
    print(data.to_string(index=False))

def print_box_score_for_game_and_periods(game_id, start_period, end_period):
    start_range = str((start_period - 1) * 7200)
    end_range = str(end_period * 7200)
    # Acquire data frame
    box_score = boxscoretraditionalv2.BoxScoreTraditionalV2(
        game_id=game_id,
        start_period=start_period,
        start_range=start_range,
        end_period=end_period,
        end_range=end_range,
        range_type="2"
    )
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
    print_box_score(team_1['TEAM_CITY'], team_1_data, start_period, end_period)
    print()
    print_box_score(team_2['TEAM_CITY'], team_1_data, start_period, end_period)



if __name__ == "__main__":
    game_id = sys.argv[1]
    start_period = int(sys.argv[2])
    end_period = int(sys.argv[3]) if len(sys.argv) == 4 else start_period

    if end_period < start_period:
        print("End period must be greater than or equal to start period")
        exit(1)

    print_box_score_for_game_and_periods(game_id, start_period, end_period)
