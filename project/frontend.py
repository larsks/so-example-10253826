from project.common import services


def a_method():
    calc = services.utils.Calculations()
    return calc.get_area()


if __name__ == "__main__":
    a_method()
