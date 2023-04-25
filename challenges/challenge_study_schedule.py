def study_schedule(permanence_period, target_time):
    counter = 0

    if not isinstance(target_time, int) or not isinstance(
        permanence_period, list
    ):
        return None

    for i in permanence_period:
        if not isinstance(i[0], int) or not isinstance(i[1], int):
            return None
        if i[0] <= target_time <= i[1]:
            counter += 1

    return counter
