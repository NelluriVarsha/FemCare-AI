def calculate_health_score(
    sleep_hours,
    water_intake,
    exercise_minutes,
    stress_level
):

    score = 0

    # Sleep Score
    if sleep_hours >= 8:
        score += 20
    elif sleep_hours >= 6:
        score += 15
    else:
        score += 5

    # Water Score
    if water_intake >= 3:
        score += 20
    elif water_intake >= 2:
        score += 15
    else:
        score += 5

    # Exercise Score
    if exercise_minutes >= 30:
        score += 30
    elif exercise_minutes >= 15:
        score += 20
    else:
        score += 10

    # Stress Score
    if stress_level <= 3:
        score += 30
    elif stress_level <= 6:
        score += 20
    else:
        score += 10

    return score