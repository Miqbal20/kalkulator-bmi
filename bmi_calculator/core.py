def calculate_bmi(weight_kg, height_cm):
    """
    Calculate the Body Mass Index (BMI).
    """
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def get_bmi_category(bmi):
    """
    Return the BMI category based on the calculated BMI score.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 22.9:
        return "Normal weight"
    elif 23.0 <= bmi <= 24.9:
        return "Overweight"
    elif 25.0 <= bmi <= 29.9:
        return "Obesity Class I"
    else:
        return "Obesity Class II"
