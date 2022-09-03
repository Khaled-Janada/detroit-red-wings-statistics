import pandas as pd

yr_from = 1933
yr_to = 2023

for n in range(yr_from, yr_to):
    scoring_table = pd.read_html('https://www.hockey-reference.com/teams/DET/1933.html', match='PIM',
                                 header=0, skiprows=1, index_col='Rk')[0]
    scoring_table['Player'] = scoring_table['Player'].str.replace('*', '', regex=False)
    scoring_table.to_csv('../datasets/scoring_reg_season_' + str(n) + '.csv')
