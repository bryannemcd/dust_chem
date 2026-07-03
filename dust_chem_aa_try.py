import numpy as np
# ----------------------------
# atomic masses (amu)
# ----------------------------

ATOMIC_MASS = {
    "H": 1.008,
    "He": 4.003,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "Ne": 20.180,
    "Mg": 24.305,
    "Si": 28.085,
    "Fe": 55.845,
}


def mass_fraction_to_uclchem(
    element_mass_fraction,
    hydrogen_mass_fraction,
    atomic_mass
):
    """
    Convert TNG mass fraction
        M_element / M_total

    to UCLCHEM abundance

        n_element / n_H
    """
# convertes TNG abundances to UCLCHEM format
    return (
        element_mass_fraction / atomic_mass
    ) / (
        hydrogen_mass_fraction / ATOMIC_MASS["H"]
    )
#example
#carbon = mass_fraction_to_uclchem(C_mass, H_mass, 12.011)

# ----------------------------
# Initial parameter grids
# ----------------------------

density_grid = np.array([])

gas_temperature_grid = np.array([])

dust_temperature_grid = np.array([])

av_grid = np.array([])

carbon_grid = np.array([])
#Will decide on grid points so I will leave the arrays empty for now.
#carbon_grid = np.array([
   # mass_fraction_to_uclchem(0.0005, H_mass_fraction, 12.011),
    #mass_fraction_to_uclchem(0.0015, H_mass_fraction, 12.011),
   #mass_fraction_to_uclchem(0.0030, H_mass_fraction, 12.011)
#])