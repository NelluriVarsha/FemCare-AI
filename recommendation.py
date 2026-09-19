def get_recommendations(
    health_score,
    pcos_risk
):

    recommendations = []

    if health_score < 60:
        recommendations.append(
            "Improve your daily lifestyle habits."
        )

    if health_score < 70:
        recommendations.append(
            "Increase physical activity and maintain a balanced diet."
        )

    if pcos_risk == "High Risk":

        recommendations.append(
            "Consult a gynecologist for PCOS screening."
        )

        recommendations.append(
            "Maintain a healthy weight and regular exercise routine."
        )

    elif pcos_risk == "Moderate Risk":

        recommendations.append(
            "Monitor menstrual cycles regularly."
        )

        recommendations.append(
            "Reduce stress and improve sleep quality."
        )

    else:

        recommendations.append(
            "Continue maintaining a healthy lifestyle."
        )

    return recommendations