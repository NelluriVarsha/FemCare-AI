def predict_pcos(
    irregular_periods,
    acne,
    hair_loss,
    weight_gain,
    mood_swings
):

    score = 0

    if irregular_periods == "Yes":
        score += 2

    if acne == "Yes":
        score += 1

    if hair_loss == "Yes":
        score += 1

    if weight_gain == "Yes":
        score += 1

    if mood_swings == "Yes":
        score += 1

    if score >= 4:
        return "High Risk"

    elif score >= 2:
        return "Moderate Risk"

    else:
        return "Low Risk"