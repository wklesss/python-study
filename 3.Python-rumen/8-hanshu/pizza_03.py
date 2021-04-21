def make_pizza(size, *topings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + " inch pizza with the following toppings:")
    for topping in topings:
        print("- " + topping)
    