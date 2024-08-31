user_data = {}


def get_initial_message():
    return "Hi! Please provide your weight in kilograms."


def handle_message(message):
    global user_data

    if 'weight' not in user_data:
        try:
            user_data['weight'] = float(message)
            return "Great! Now, please provide your height in centimeters."
        except ValueError:
            return "Invalid weight format. Please provide your weight in kilograms (e.g., 70)."
    elif 'height' not in user_data:
        try:
            user_data['height'] = float(message)
            bmi = calculate_bmi(user_data['weight'], user_data['height'])
            user_data.clear() 
            return f"Your BMI is {bmi:.2f}. This is considered {bmi_category(bmi)}."
        except ValueError:
            return "Invalid height format. Please provide your height in centimeters (e.g., 175)."
    else:
        return "I'm sorry, I didn't understand that. Please start over."


def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal weight"
    elif 25 <= bmi < 29.9:
        return "overweight"
    else:
        return "obese"


