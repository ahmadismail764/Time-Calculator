# def add_time(start, duration, curr_day="blank"):
#     noon_night = ["AM", "PM"]
#     week = [
#         "Sunday",
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#     ]
#     hours = start[:2]
#     minutes = start[3:5]
#     hourstoadd = duration[: duration.index(":")]
#     minutestoadd = duration[duration.index(":") + 1 :]
#     new_hours = int(hours) + int(hourstoadd)
#     new_minutes = int(minutes) + int(minutestoadd)
#     while new_minutes > 60:
#         new_hours += 1
#     #     new_minutes -= 60
#     # if len(start) > 7:
#     #     dayornight = start[5:]
def add_time(start_time, duration, starting_day=None):
    # Parse start time
    start_time_parts = start_time.split()
    start_hours, start_minutes = map(int, start_time_parts[0].split(":"))
    start_period = start_time_parts[1]

    if start_period == "PM":
        start_hours += 12

    # Parse duration
    duration_hours, duration_minutes = map(int, duration.split(":"))

    # Calculate total minutes
    total_minutes = (
        start_hours * 60 + start_minutes + duration_hours * 60 + duration_minutes
    )

    # Calculate new hours and minutes
    new_hours = total_minutes // 60
    new_minutes = total_minutes % 60

    # Determine period (AM/PM)
    if new_hours >= 24:
        days_passed = new_hours // 24
        new_hours %= 24
    else:
        days_passed = 0
    period = "AM" if new_hours < 12 else "PM"
    if new_hours > 12:
        new_hours -= 12

    # Format result
    new_time = f"{new_hours}:{new_minutes:02d} {period}"
    if starting_day:
        days_of_week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        starting_day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (starting_day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        if days_passed == 1:
            new_time += f", {new_day} (next day)"
        elif days_passed > 1:
            new_time += f", {new_day} ({days_passed} days later)"
    elif days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
