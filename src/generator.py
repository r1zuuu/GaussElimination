def generate_equations(number_of_equations):
    import numpy as np

    coefficients = np.random.randint(
        -10, 10, size=(number_of_equations, number_of_equations)
    )  # wspolczynniki generowanie
    constants = np.random.randint(
        -10, 10, size=(number_of_equations, 1)
    )  # generowanie wyrazów wolnych

    equations = []
    for i in range(number_of_equations):  # poradzkowanie
        equation = (
            " + ".join(
                f"{coefficients[i][j]}x{j+1}" for j in range(number_of_equations)
            )
            + f" = {constants[i][0]}"
        )
        equations.append(equation)

    return equations, coefficients, constants.flatten()
