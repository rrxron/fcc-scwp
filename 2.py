def add_time(start, duration, startDayOfWeek = ""):
    # build our initial values
    start_time, start_mode = start.split(" ")
    start_hr, start_min = start_time.split(":")
    duration_hr, duration_min = duration.split(":")

    # convert start_hr to 24hr format first
    if (start_mode == "PM"):
        start_hr = 12 + int(start_hr)

    # prepare initial values for calculation
    start_hr = int(start_hr)
    start_min = int(start_min)
    duration_hr = int(duration_hr)
    duration_min = int(duration_min)

    # add duration_min and update start_hr
    if duration_min < 60:
        for x in range(1, duration_min+1):
            start_min += 1
            if (start_min > 59):
                start_min = 0
                start_hr +=1

        duration_min = 0 # duration_min has been used up

    start_day = 0 # accumulate days depending on start_* and duration_*

    accumulated_hour_for_one_day = 0

    #update start_hr
    while (start_hr > 23):
        if (start_hr > 23):
            start_hr -= 24
            accumulated_hour_for_one_day += 24
        if (accumulated_hour_for_one_day >= 24):
            start_day+=1
            accumulated_hour_for_one_day = 0
        else:
            accumulated_hour_for_one_day+=1

    if (accumulated_hour_for_one_day == 1 and start_day == 0):
        start_day+=1

    # update start_hr according to duration_hr
    for x in range(0, duration_hr):
        start_hr+= 1

    # update start_day again
    while (start_hr > 23):
        start_hr -= 24
        start_day +=1

    duration_hr = 0 # duration_hr has been used up

    # reformat return values
    strHr = start_hr - 12 if start_hr > 12 else "12" \
            if start_hr == 0 else start_hr
    strMin = "0"+ str(start_min) if start_min < 10 else start_min
    strMode = "PM" if start_hr >= 12 else "AM"

    strNextDay = " (next day)" if start_day >= 1 else ""
    if (start_day > 1):
        strNextDay = f" ({start_day} days later)"

    # calculate: ", day"
    strDayOfWeek = ""
    if (startDayOfWeek != ""):
        startDayOfWeek = startDayOfWeek.lower().capitalize()
        daysOfWeek = {0:"Monday", 1:"Tuesday", 2:"Wednesday",
                      3:"Thursday", 4:"Friday", 5:"Saturday",
                      6:"Sunday"}

        startingDayIndex = 0

        # determine starting day for looping
        for i in daysOfWeek.items():
            if (i[1] == startDayOfWeek):
                startingDayIndex = i[0]
                break

        # loop on accumulated start_day
        for i in range(start_day):
            startingDayIndex+=1
            if startingDayIndex > 6:
                startingDayIndex = 0

        # build strDayOfWeek
        for i in daysOfWeek.items():
            if (i[0]) == startingDayIndex:
                strDayOfWeek = f", {i[1]}"
                break

    return f"{strHr}:{strMin} {strMode}{strDayOfWeek}{strNextDay}"