import pandas as pd
import os
import matplotlib.pyplot as plt

file_path = os.path.abspath('/Users/rohansingh/VSCode/2ndYear/data science/ACC_HW/acc_players-2324F.csv')

df = pd.read_csv(file_path, skiprows=1, index_col=False)

df = df[df['Player'].notna()]
df = df[df['Player'] != 'Player']

df.reset_index(drop=True, inplace=True)

# Total points scored by all players
total_points = df['PTS'].sum()
print(f"Total points scored by all players: {total_points}")

# Player with the most minutes
max_mp = df['MP'].max()
player_max_mp = df[df['MP'] == max_mp]['Player'].values[0]
print(f"Player with the most minutes: {player_max_mp} ({max_mp} minutes)")

# Top 5 players by total rebounds
top_5_rebounds = df[['Player', 'TRB']].sort_values(by='TRB', ascending=False).head(5)
print("Top 5 players by total rebounds:")
print(top_5_rebounds)

# Players with more than 500 minutes
df_over_500 = df[df['MP'] > 500]
print(df_over_500)

# Player with the highest assists
max_ast = df_over_500['AST'].max()
player_max_ast = df_over_500[df_over_500['AST'] == max_ast]['Player'].values[0]
print(f"Player with the highest assists: {player_max_ast} ({max_ast} assists)")

# Top 3 Assist Leaders
top_3_assists = df_over_500[['Player', 'AST']].sort_values(by='AST', ascending=False).head(3)
print("Top 3 Assist Leaders:")
print(top_3_assists)

# Top 3 Shot Block Leaders
top_3_blocks = df_over_500[['Player', 'BLK']].sort_values(by='BLK', ascending=False).head(3)
print("Top 3 Shot Blockers:")
print(top_3_blocks)

# Total points by school
points_by_school = df.groupby('School')['PTS'].sum().reset_index()
print("Total points by school:")
print(points_by_school)

# Total assists by school
assists_by_school = df.groupby('School')['AST'].sum().reset_index()
print("Total assists by school:")
print(assists_by_school)

# Top 3 schools by total points
top_3_schools = points_by_school.sort_values(by='PTS', ascending=False).head(3)
print("Top 3 schools by total points:")
print(top_3_schools)


# Plotting the top 5 players by total points scored
top_5_scorers = df[['Player', 'PTS']].sort_values(by='PTS', ascending=False).head(5)
plt.figure(figsize=(10, 6))
plt.bar(top_5_scorers['Player'], top_5_scorers['PTS'], color='blue')
plt.xlabel('Player')
plt.ylabel('Total Points')
plt.title('Top 5 Players by Total Points Scored')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Correlation between Field Goal Percentage (FG%) and Win Shares (WS)
df_corr = df.dropna(subset=['FG%', 'WS'])

plt.figure(figsize=(8, 6))
plt.scatter(df_corr['FG%'], df_corr['WS'], color='green')
plt.xlabel('Field Goal Percentage (FG%)')
plt.ylabel('Win Shares (WS)')
plt.title('Correlation between FG% and WS')
plt.show()

correlation = df_corr['FG%'].corr(df_corr['WS'])
print(f"Correlation coefficient between FG% and WS: {correlation}")
