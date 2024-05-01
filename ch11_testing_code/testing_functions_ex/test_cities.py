from Python_crash_course.ch11_testing_code.testing_functions_ex.city_functions import get_formatted_city

def test_city_country():
    """ Do city and country names such as 'santiago' and 'chile' work?"""
    formatted_city = get_formatted_city("santiago","chile")
    assert formatted_city == "Santiago, Chile"

def test_city_country_population():
    """Do city, country and population data work?"""
    formatted_city_popoulation = get_formatted_city("santiago", "chile", "500000")
    assert formatted_city_popoulation == "Santiago, Chile - population 500000"