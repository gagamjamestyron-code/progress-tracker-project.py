all_workout_days = []

while True:
    day_name = input("\nWhat workout day is it? ")

    if day_name.lower() == "done":
        break

    workout_day = []

    while True:
        exercise_name = input(
            "Put your exercise (or type 'another' for a new day): "
        )

        if exercise_name.lower() == "another":
            break

        if exercise_name.lower() == "done":
            break

        sets = input("How many sets: ")
        weight = input("How heavy: ")
        reps = input("How many reps: ")

        exercise_dict = {
            "exercise": exercise_name,
            "sets": sets,
            "weight": weight,
            "reps": reps
        }

        workout_day.append(exercise_dict)

    day_dict = {
        "name": day_name,
        "exercises": workout_day
    }

    all_workout_days.append(day_dict)

print("\nWORKOUT SUMMARY")

for day in all_workout_days:
    print(f"\nWorkout for {day['name']}:")
    print("EXERCISE | SETS | WEIGHT | REPS")

    for index, exercise in enumerate(day["exercises"], start=1):
        print(
            f"{index}. {exercise['exercise']} | "
            f"{exercise['sets']} | {exercise['weight']} | {exercise['reps']}"
        )