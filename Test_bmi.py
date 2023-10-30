import DevOps_Lab_2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.7, 70)
    correct_result = 0

    assert(result == correct_result)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.7, 73)
    correct_result = 1

    assert (result == correct_result)


def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.7, 50)
    correct_result = -1

    assert (result == correct_result)

