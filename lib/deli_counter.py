def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")


def line(katz_deli):
    if not katz_deli:
        return "The line is currently empty."

    current_line = "The line is currently:"
    for i, customer in enumerate(katz_deli, 1):
        current_line += f" {i}. {customer}"

    return current_line


def now_serving(katz_deli):
    if not katz_deli:
        return "There is nobody waiting to be served!"

    serving_customer = katz_deli.pop(0)
    return f"Currently serving {serving_customer}"
