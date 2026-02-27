from collections import OrderedDict


class Restaurant():

    WEEKDAYS = [
        'Sun',
        'Mon',
        'Tue',
        'Wed',
        'Thu',
        'Fri',
        'Sat',
    ]

    def __init__(self, *opening_hours):
        grouped_hours = self.group_opening_hours(opening_hours)
        self.pretty_openning_hours = []
        for opening_hour, indexes in grouped_hours.items():
            weekdays = self.prettify_weekdays(indexes)
            self.pretty_openning_hours.append(
                '{}: {}'.format(weekdays, opening_hour))

        # # group day with the opening hours
        # # [('Mon', '9-17'), ('Tue', '10-15'), ...]
        # self.opening_hours = zip(
        #     self.WEEKDAYS,
        #     [opening_hour.to_string() for opening_hour in opening_hours]
        # )

    def group_opening_hours(self, opening_hours):
        grouped = OrderedDict()
        for index, opening_hour in enumerate(opening_hours):
            key = opening_hour.to_string()
            if key in grouped:
                grouped[key].append(index)
            else:
                grouped[key] = [index]
        return grouped

    @classmethod
    def prettify_weekdays(self, indexes):
        # Step 1: divide indexes into groups
        groups = []
        previous_index = None
        for index in indexes:
            if not groups:
                groups.append([index])
                continue
            previous = groups[-1]
            if previous[-1] == index - 1:
                previous.append(index)
            else:
                groups.append([index])

        # Step 2: replace indexes with weekdays.
        prettified = []
        for group in groups:
            if group[0] == group[-1]:
                prettified.append(self.WEEKDAYS[group[0]])
            else:
                interval = '{} - {}'.format(
                    self.WEEKDAYS[group[0]],
                    self.WEEKDAYS[group[-1]],
                )
                prettified.append(interval)

        return ', '.join(prettified)


    def get_opening_hours(self):
        return ', '.join(self.pretty_openning_hours)


class OpeningHour():

    def __init__(self, opening_hour, closing_hour):
        self.opening_hour = opening_hour
        self.closing_hour = closing_hour

    def to_string(self):
        return "{}-{}".format(self.opening_hour, self.closing_hour)



restaurant = Restaurant(
    OpeningHour(8, 16),  # Sunday
    OpeningHour(8, 17),  # Monday
    OpeningHour(8, 17),  # Tuesday
    OpeningHour(8, 17),  # Wednesday
    OpeningHour(8, 16),  # Thursday
    OpeningHour(8, 16),  # Friday
    OpeningHour(8, 16),  # Saturday
)

print restaurant.get_opening_hours()

