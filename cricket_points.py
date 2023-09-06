# cricket_points.py

def calculate_batting_points(runs, balls_faced, boundaries):
    """
    Calculate fantasy points for a batsman based on runs, balls faced, and boundaries.

    :param runs: Total runs scored by the batsman.
    :param balls_faced: Total balls faced by the batsman.
    :param boundaries: A dictionary containing the count of fours and sixes.
    :return: Total fantasy points for batting performance.
    """
    points = runs // 2

    if runs >= 50:
        points += 5
    if runs >= 100:
        points += 10

    strike_rate = (runs / balls_faced) * 100

    if 80 <= strike_rate <= 100:
        points += 2
    elif strike_rate > 100:
        points += 4

    points += boundaries['fours'] + (boundaries['sixes'] * 2)
    
    return points

def calculate_bowling_points(wickets, economy_rate):
    """
    Calculate fantasy points for a bowler based on wickets taken and economy rate.

    :param wickets: Total wickets taken by the bowler.
    :param economy_rate: Economy rate of the bowler.
    :return: Total fantasy points for bowling performance.
    """
    points = wickets * 10

    if wickets >= 3:
        points += 5
    if wickets >= 5:
        points += 10

    if 3.5 <= economy_rate <= 4.5:
        points += 4
    elif 2 <= economy_rate < 3.5:
        points += 7
    elif economy_rate < 2:
        points += 10

    return points

def calculate_fielding_points(catches, stumpings, run_outs):
    """
    Calculate fantasy points for fielding performance based on catches, stumpings, and run-outs.

    :param catches: Number of catches taken.
    :param stumpings: Number of stumpings performed.
    :param run_outs: Number of run-outs executed.
    :return: Total fantasy points for fielding performance.
    """
    points = (catches + stumpings + run_outs) * 10
    return points
