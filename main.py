# main.py

from cricket_points import calculate_batting_points, calculate_bowling_points

players = [
    {'name': 'Virat Kohli', 'runs': 83, 'balls_faced': 70, 'boundaries': {'fours': 7, 'sixes': 0}, 'wickets': 0, 'economy_rate': 0, 'catches': 1, 'stumpings': 0, 'run_outs': 0},
    {'name': 'du Plessis', 'runs': 94, 'balls_faced': 92, 'boundaries': {'fours': 10, 'sixes': 1}, 'wickets': 0, 'economy_rate': 0, 'catches': 0, 'stumpings': 0, 'run_outs': 1},
    {'name': 'Bhuvneshwar Kumar', 'runs': 0, 'balls_faced': 0, 'boundaries': {'fours': 0, 'sixes': 0}, 'wickets': 4, 'economy_rate': 4.2, 'catches': 0, 'stumpings': 0, 'run_outs': 0},
    {'name': 'Yuzvendra Chahal', 'runs': 3, 'balls_faced': 10, 'boundaries': {'fours': 0, 'sixes': 0}, 'wickets': 3, 'economy_rate': 3.8, 'catches': 0, 'stumpings': 0, 'run_outs': 0},
    {'name': 'Kuldeep Yadav', 'runs': 17, 'balls_faced': 20, 'boundaries': {'fours': 2, 'sixes': 0}, 'wickets': 2, 'economy_rate': 5.1, 'catches': 0, 'stumpings': 0, 'run_outs': 0}
]

for player in players:
    batting_points = calculate_batting_points(player['runs'], player['balls_faced'], player['boundaries'])
    bowling_points = calculate_bowling_points(player['wickets'], player['economy_rate'])
    total_points = batting_points + bowling_points

    player['batting_points'] = batting_points
    player['bowling_points'] = bowling_points
    player['total_points'] = total_points

top_player = max(players, key=lambda x: x['total_points'])
print(f"Top Player: {top_player['name']} ({top_player['total_points']} points)")
