import pandas as pd

yr_from = 1933
yr_to = 2004

for n in range(yr_from, yr_to):
    # This season was cancelled
    if n == 2005:
        continue
    scoring_table = pd.read_html(f'https://www.hockey-reference.com/teams/DET/{n}.html', match='PIM',
                                 header=0, skiprows=1)[0]
    scoring_table['Player'] = scoring_table['Player'].str.replace('*', '', regex=False)
    scoring_table.drop(scoring_table.index[-1], inplace=True)
    scoring_table.to_csv('../datasets/scoring_reg_season_' + str(n) + '.csv')
