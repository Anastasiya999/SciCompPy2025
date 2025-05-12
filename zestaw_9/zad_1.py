# Plot functions sin(x), cos(x), and exp(-x) in a range [0,10] in the same figure.
# Colors are red, green, and blue, respectively.
# Lines are solid, dashed, and dotted, respectively. Add a legend.

import numpy as np
import matplotlib.pyplot as plt


def plot_functions(x, sin_style=None, cos_style=None, exp_style=None, figsize=(8, 5)):
    x = np.array(x) 

    default_styles = {
        'sin': {'color': 'r', 'linestyle': '-'},
        'cos': {'color': 'g', 'linestyle': '--'},
        'exp': {'color': 'b', 'linestyle': ':'}
    }

    # Use provided styles or defaults
    sin_style = sin_style or default_styles['sin']
    cos_style = cos_style or default_styles['cos']
    exp_style = exp_style or default_styles['exp']

    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_exp = np.exp(-x)

    plt.figure(figsize=figsize)

    plt.plot(x, y_sin, label='sin(x)', **sin_style)
    plt.plot(x, y_cos, label='cos(x)', **cos_style)
    plt.plot(x, y_exp, label='exp(-x)', **exp_style)

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of sin(x), cos(x), and exp(-x)')

    plt.grid(True)
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    x = np.linspace(0, 10, 1000)
    plot_functions(
        x,
        sin_style={'color': 'r', 'linestyle': '-'},
        cos_style={'color': 'g', 'linestyle': '--'},
        exp_style={'color': 'b', 'linestyle': ':'}, figsize=(10, 6)
    )

