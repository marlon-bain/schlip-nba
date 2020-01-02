# schlip-nba
Get period-level box scores for NBA games

`python3 main.py [game ID] [start period] (optionally, [end period])`

Where the period is given by one of: 1, 2, 3, 4. 

e.g. `python3 main.py 0021900504 3`

```
Orlando's box score in period 3
        PLAYER_NAME START_POSITION COMMENT    MIN  FGM  FGA  FG_PCT  FG3M  FG3A  FG3_PCT  FTM  FTA  FT_PCT  OREB  DREB  REB  AST  STL  BLK   TO   PF   PTS  PLUS_MINUS
         Wes Iwundu              F           9:20  1.0  3.0   0.333   0.0   1.0    0.000  2.0  2.0   1.000   0.0   1.0  1.0  1.0  1.0  0.0  1.0  2.0   4.0        10.0
     Nikola Vucevic              C          11:14  4.0  7.0   0.571   1.0   3.0    0.333  1.0  2.0   0.500   0.0   6.0  6.0  0.0  1.0  0.0  1.0  0.0  10.0         8.0
      Evan Fournier              G           9:44  2.0  5.0   0.400   0.0   1.0    0.000  2.0  3.0   0.667   0.0   1.0  1.0  0.0  1.0  0.0  0.0  1.0   6.0         4.0
     Markelle Fultz              G           7:04  2.0  5.0   0.400   1.0   2.0    0.500  1.0  2.0   0.500   0.0   0.0  0.0  3.0  1.0  0.0  1.0  0.0   6.0         7.0
    Amile Jefferson                          4:48  0.0  0.0   0.000   0.0   0.0    0.000  0.0  0.0   0.000   2.0   2.0  4.0  1.0  0.0  0.0  0.0  0.0   0.0         9.0
      Terrence Ross                          4:56  1.0  1.0   1.000   0.0   0.0    0.000  0.0  0.0   0.000   0.0   0.0  0.0  0.0  0.0  1.0  0.0  0.0   2.0         0.0
 Melvin Frazier Jr.                          4:32  0.0  1.0   0.000   0.0   0.0    0.000  0.0  0.0   0.000   0.0   0.0  0.0  0.0  0.0  0.0  0.0  1.0   0.0         1.0
      D.J. Augustin                          4:56  1.0  1.0   1.000   0.0   0.0    0.000  1.0  1.0   1.000   0.0   0.0  0.0  2.0  0.0  0.0  0.0  0.0   3.0         0.0
           Mo Bamba                          0:46  0.0  0.0   0.000   0.0   0.0    0.000  0.0  0.0   0.000   0.0   0.0  0.0  0.0  0.0  0.0  0.0  1.0   0.0        -1.0
         Khem Birch                          2:40  0.0  0.0   0.000   0.0   0.0    0.000  1.0  2.0   0.500   0.0   0.0  0.0  0.0  0.0  0.0  0.0  0.0   1.0        -3.0

Washington's box score in period 3
        PLAYER_NAME START_POSITION COMMENT    MIN  FGM  FGA  FG_PCT  FG3M  FG3A  FG3_PCT  FTM  FTA  FT_PCT  OREB  DREB  REB  AST  STL  BLK   TO   PF   PTS  PLUS_MINUS
         Wes Iwundu              F           9:20  1.0  3.0   0.333   0.0   1.0    0.000  2.0  2.0   1.000   0.0   1.0  1.0  1.0  1.0  0.0  1.0  2.0   4.0        10.0
     Nikola Vucevic              C          11:14  4.0  7.0   0.571   1.0   3.0    0.333  1.0  2.0   0.500   0.0   6.0  6.0  0.0  1.0  0.0  1.0  0.0  10.0         8.0
      Evan Fournier              G           9:44  2.0  5.0   0.400   0.0   1.0    0.000  2.0  3.0   0.667   0.0   1.0  1.0  0.0  1.0  0.0  0.0  1.0   6.0         4.0
     Markelle Fultz              G           7:04  2.0  5.0   0.400   1.0   2.0    0.500  1.0  2.0   0.500   0.0   0.0  0.0  3.0  1.0  0.0  1.0  0.0   6.0         7.0
    Amile Jefferson                          4:48  0.0  0.0   0.000   0.0   0.0    0.000  0.0  0.0   0.000   2.0   2.0  4.0  1.0  0.0  0.0  0.0  0.0   0.0         9.0
      Terrence Ross                          4:56  1.0  1.0   1.000   0.0   0.0    0.000  0.0  0.0   0.000   0.0   0.0  0.0  0.0  0.0  1.0  0.0  0.0   2.0         0.0
 Melvin Frazier Jr.                          4:32  0.0  1.0   0.000   0.0   0.0    0.000  0.0  0.0   0.000   0.0   0.0  0.0  0.0  0.0  0.0  0.0  1.0   0.0         1.0
      D.J. Augustin                          4:56  1.0  1.0   1.000   0.0   0.0    0.000  1.0  1.0   1.000   0.0   0.0  0.0  2.0  0.0  0.0  0.0  0.0   3.0         0.0
           Mo Bamba                          0:46  0.0  0.0   0.000   0.0   0.0    0.000  0.0  0.0   0.000   0.0   0.0  0.0  0.0  0.0  0.0  0.0  1.0   0.0        -1.0
         Khem Birch                          2:40  0.0  0.0   0.000   0.0   0.0    0.000  1.0  2.0   0.500   0.0   0.0  0.0  0.0  0.0  0.0  0.0  0.0   1.0        -3.0

```

# install

Python3 is required. Clone this repo. `pip3 install -r requirements.txt` from within the repo.
