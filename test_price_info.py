import price_info as price

def test_total_cost_shopping():
    correct_result = 46.75
    actual_result = price.total_cost_shopping()

    assert (correct_result == actual_result)

def test_cost_of_fruit():
    test_fruit = "orange"
    test_quantity = 15

    correct_result = 21

    actual_result = price.cost_of_fruits(test_fruit, test_quantity)

    assert (actual_result == correct_result)
    