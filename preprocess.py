from datetime import datetime
import pandas as pd
import numpy as np

full_to_abbr = {
  'Atlanta Hawks': 'ATL',
  'Boston Celtics': 'BOS',
  'Brooklyn Nets': 'BKN',
  'Charlotte Hornets': 'CHA',
  'Chicago Bulls': 'CHI',
  'Cleveland Cavaliers': 'CLE',
  'Dallas Mavericks': 'DAL',
  'Denver Nuggets': 'DEN',
  'Detroit Pistons': 'DET',
  'Golden State Warriors': 'GSW',
  'Houston Rockets': 'HOU',
  'Indiana Pacers': 'IND',
  'Los Angeles Clippers': 'LAC',
  'Los Angeles Lakers': 'LAC',
  'Memphis Grizzlies': 'MEM',
  'Miami Heat': 'MIA',
  'Milwaukee Bucks': 'MIL',
  'Minnesota Timberwolves': 'MIN',
  'New Orleans Pelicans': 'NOP',
  'New York Knicks': 'NYK',
  'Oklahoma City Thunder': 'OKC',
  'Orlando Magic': 'ORL',
  'Philadelphia 76ers': 'PHI',
  'Phoenix Suns': 'PHO',
  'Portland Trail Blazers': 'POR',
  'Sacramento Kings': 'SAC',
  'San Antonio Spurs': 'SAS',
  'Toronto Raptors': 'TOR',
  'Utah Jazz': 'UTA',
  'Washington Wizards': 'WAS'
}

def process_schedule():
  df = pd.read_csv('data/schedules/2019-2022.csv')

  clean_date = []
  home_win = []
  home_loss = []
  margin = []

  for row in df.itertuples():
    d = row[1].split(" ")[1:]
    d = " ".join(d)
    clean_date.append(datetime.strptime(d, '%b %d %Y').strftime('%Y-%m-%d'))
    
    if int(row[3]) > int(row[5]):
      home_loss.append(1)
      home_win.append(0)
    else:
      home_loss.append(0)
      home_win.append(1)
      
    margin.append(int(row[5]) - int(row[3]))
    
    
  df['date'] = clean_date
  df['pt_diff'] = margin
  df['home_win'] = home_win
  df['home_loss'] = home_loss

  df.to_csv('data/schedules/2019-2022_clean.csv')
  
def process_odds():
  df = pd.read_csv('data/odds/2019-2022.csv')
  df2 = pd.DataFrame()
  
  home = []
  away = []
  home_total = []
  away_total = []
  home_ml = []
  away_ml = []
  
  for row in df.itertuples():
    if row.Index % 2 == 0:
      away.append(row.Team)
      away_ml.append(row.ML)
      away_total.append(row.Final)
    else:
      home.append(row.Team)
      home_ml.append(row.ML)
      home_total.append(row.Final)
  
  df2['home'] = home
  df2['away'] = away
  df2['home_total'] = home_total
  df2['home_ml'] = home_ml
  df2['away_total'] = away_total
  df2['away_ml'] = away_ml
  
  df2.to_csv('data/odds/2019-2022_clean.csv')
    
if __name__ == '__main__':
  process_odds()