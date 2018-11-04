import numpy as np

F = 96485.33289  # Faraday's constant (Coulombs per Mole)
R = 8.314  # ideal gas constant (Joules per Mole)
ZERO_C = 273.15  # celsius to Kelvin offset


def calc_v_rev(c_in, c_ex, tmpr, z):
    """
    Calculate reversal potential from intra and extra-cellular ion concentrations.
    
    See
    http://www.physiologyweb.com/lecture_notes/resting_membrane_potential/resting_membrane_potential_nernst_equilibrium_potential.html
    for details.
    """
    
    scale_factor = R*(tmpr+ZERO_C)/(F*z)
    v_rev = scale_factor * np.log(c_ex/c_in)

    return v_rev
