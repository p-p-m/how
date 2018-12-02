from collections import defaultdict


def groupingDishes(dishes):
    result = defaultdict(list)
    for dish in dishes:
        food = dish[0]
        ingredients = dish[1:]
        for ingredient in ingredients:
            result[ingredient].append(food)

    result = {key: value for key, value in result.items() if len(value) > 1}
    return [
        [ingredient] + sorted(result[ingredient])
        for ingredient in sorted(result.keys())
    ]


dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
          ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
          ["Quesadilla", "Chicken", "Cheese", "Sauce"],
          ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]


expected_result = [["Cheese", "Quesadilla", "Sandwich"],
                   ["Salad", "Salad", "Sandwich"],
                   ["Sauce", "Pizza", "Quesadilla", "Salad"],
                   ["Tomato", "Pizza", "Salad", "Sandwich"]]


assert expected_result == groupingDishes(dishes), groupingDishes(dishes)
