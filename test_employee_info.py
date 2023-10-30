import employee_info as emp

dictionary = emp.employee_data


def test_get_employees_by_age_range():
    correct_result = [dictionary[5]]

    actual_result = emp.get_employees_by_age_range(39,41)

    assert (actual_result == correct_result)


def test_calculate_average_salary():
    correct_result = 361000 / 6

    actual_result = emp.calculate_average_salary()

    assert (actual_result == correct_result)


def test_get_employees_by_dept():
    correct_result = [dictionary[3], dictionary[4]]

    actual_result = emp.get_employees_by_dept("Engineering")

    assert (actual_result == correct_result)

