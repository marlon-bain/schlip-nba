# schlip-nba
Get period-level box scores for NBA games

`python3 main.py [game ID] [start period] [end period]`

Where the period is given by one of: 1, 2, 3, 4. 

e.g. ` python3 main.py 0021900504 1 4`

```
Orlando's box score from period 1 to period 4
        PLAYER_NAME START_POSITION COMMENT    MIN  FGM   FGA  FG_PCT  FG3M  FG3A  FG3_PCT  FTM   FTA  FT_PCT  OREB  DREB   REB  AST  STL  BLK   TO   PF   PTS  PLUS_MINUS
         Wes Iwundu              F          22:01  4.0   7.0   0.571   0.0   1.0    0.000  2.0   2.0   1.000   1.0   5.0   6.0  1.0  1.0  0.0  1.0  3.0  10.0        13.0
     Jonathan Isaac              F           2:03  1.0   2.0   0.500   0.0   0.0    0.000  0.0   0.0   0.000   1.0   0.0   1.0  0.0  1.0  0.0  0.0  0.0   2.0         0.0
     Nikola Vucevic              C          30:31  8.0  20.0   0.400   3.0   6.0    0.500  1.0   2.0   0.500   2.0  10.0  12.0  2.0  1.0  0.0  1.0  2.0  20.0        18.0
      Evan Fournier              G          37:35  7.0  16.0   0.438   2.0   6.0    0.333  2.0   3.0   0.667   0.0   4.0   4.0  0.0  2.0  1.0  4.0  4.0  18.0        16.0
     Markelle Fultz              G          22:21  6.0  12.0   0.500   1.0   3.0    0.333  3.0   4.0   0.750   1.0   3.0   4.0  8.0  2.0  0.0  1.0  3.0  16.0        20.0
    Amile Jefferson                         13:04  0.0   1.0   0.000   0.0   0.0    0.000  2.0   4.0   0.500   2.0   4.0   6.0  2.0  0.0  1.0  0.0  0.0   2.0        13.0
      Terrence Ross                         24:22  6.0  10.0   0.600   3.0   6.0    0.500  0.0   0.0   0.000   0.0   0.0   0.0  0.0  1.0  1.0  1.0  1.0  15.0         3.0
 Melvin Frazier Jr.                         12:41  0.0   2.0   0.000   0.0   1.0    0.000  0.0   0.0   0.000   0.0   0.0   0.0  0.0  1.0  1.0  0.0  4.0   0.0         3.0
      D.J. Augustin                         31:25  7.0  15.0   0.467   2.0   6.0    0.333  9.0  10.0   0.900   0.0   3.0   3.0  9.0  2.0  0.0  1.0  2.0  25.0         8.0
           Mo Bamba                         15:13  3.0   6.0   0.500   1.0   3.0    0.333  0.0   0.0   0.000   0.0   6.0   6.0  1.0  0.0  1.0  0.0  2.0   7.0         4.0
         Khem Birch                         26:28  3.0   3.0   1.000   0.0   0.0    0.000  1.0   2.0   0.500   4.0   6.0  10.0  2.0  0.0  1.0  0.0  0.0   7.0         8.0
       Josh Magette                          2:16  0.0   1.0   0.000   0.0   0.0    0.000  0.0   0.0   0.000   0.0   0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0        -1.0

Washington's box score from period 1 to period 4
        PLAYER_NAME START_POSITION COMMENT    MIN  FGM   FGA  FG_PCT  FG3M  FG3A  FG3_PCT  FTM   FTA  FT_PCT  OREB  DREB   REB  AST  STL  BLK   TO   PF   PTS  PLUS_MINUS
       Bradley Beal              F          30:17  8.0  20.0   0.400   2.0   8.0    0.250  9.0  10.0   0.900   1.0   3.0   4.0  5.0  0.0  0.0  2.0  2.0  27.0       -20.0
 Johnathan Williams              F          12:03  1.0   1.0   1.000   0.0   0.0    0.000  0.0   0.0   0.000   1.0   5.0   6.0  1.0  0.0  1.0  0.0  0.0   2.0       -16.0
        Ian Mahinmi              C          19:38  1.0   2.0   0.500   0.0   0.0    0.000  0.0   0.0   0.000   0.0   2.0   2.0  0.0  0.0  2.0  2.0  2.0   2.0       -22.0
     Gary Payton II              G           9:46  2.0   5.0   0.400   0.0   1.0    0.000  0.0   0.0   0.000   0.0   3.0   3.0  0.0  0.0  0.0  1.0  3.0   4.0        -9.0
      Isaiah Thomas              G          19:13  3.0  10.0   0.300   1.0   4.0    0.250  2.0   2.0   1.000   0.0   0.0   0.0  1.0  1.0  0.0  2.0  2.0   9.0       -16.0
     Troy Brown Jr.                         28:18  5.0  12.0   0.417   1.0   2.0    0.500  3.0   4.0   0.750   2.0   5.0   7.0  1.0  1.0  0.0  2.0  1.0  14.0        -9.0
       Jordan McRae                         31:05  4.0  12.0   0.333   2.0   6.0    0.333  5.0   6.0   0.833   0.0   7.0   7.0  1.0  1.0  0.0  2.0  0.0  15.0        -8.0
   Anzejs Pasecniks                         23:49  2.0   8.0   0.250   0.0   1.0    0.000  0.0   0.0   0.000   3.0   7.0  10.0  3.0  0.0  0.0  1.0  5.0   4.0         4.0
          Ish Smith                         28:27  4.0  10.0   0.400   1.0   4.0    0.250  1.0   2.0   0.500   1.0   4.0   5.0  3.0  1.0  0.0  0.0  2.0  10.0        -7.0
   Garrison Mathews                         17:02  2.0   4.0   0.500   1.0   3.0    0.333  5.0   5.0   1.000   1.0   0.0   1.0  1.0  0.0  0.0  1.0  3.0  10.0         0.0
        Isaac Bonga                         12:40  1.0   1.0   1.000   1.0   1.0    1.000  1.0   2.0   0.500   0.0   1.0   1.0  1.0  1.0  1.0  0.0  3.0   4.0        -4.0
  Admiral Schofield                          3:51  0.0   1.0   0.000   0.0   1.0    0.000  0.0   0.0   0.000   0.0   0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0         1.0
    Justin Robinson                          3:51  0.0   1.0   0.000   0.0   0.0    0.000  0.0   0.0   0.000   0.0   0.0   0.0  1.0  0.0  0.0  0.0  0.0   0.0         1.0
```

# install

Python3 is required. Clone this repo. `pip3 install -r requirements.txt` from within the repo.
