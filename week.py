my_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def modify_week(week):
    # print(week[1], week[2], week[3], week[4], week[5], week[6], week[0])
    # print(my_week[1:7])
    week.append(week.pop(0))
    return week
    print(week)


modify_week(my_week)


