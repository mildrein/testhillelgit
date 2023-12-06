
def to_inches(length_cm):
    if length_cm < 0:
        return round(length_cm, 2)

    inches = length_cm / 2.54  # 1 см = 2.54 дюйми
    return round(inches, 2)

if __name__ == "__main__":
    try:
        length_cm = float(input("Введіть довжину в сантиметрах: "))
        result = to_inches(length_cm)
        print(f"{length_cm} см = {result} дюймів")
    except ValueError:
        print("Будь ласка, введіть коректне числове значення.")
