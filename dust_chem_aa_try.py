import numpy as np
import uclchem
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
#carbon = mass_fraction_to_uclchem(C_mass, H_mass, 12.011) (though this is only one abundance)

# ----------------------------
#Defining H_mass_fraction values 
#----------------------------
H_low = 0.56
H_mid = 0.72
H_high = 0.76
# ----------------------------
# Initial parameter grids
# ----------------------------

density_grid = np.array([-1, 3, 9.5])  # log10(n_H / cm^-3)

gas_temperature_grid = np.array([2.5, 6.0, 9.0])  # log10(T_gas / K)

fneutral_grid = np.array([0.0, 0.06, 1.0])  # f_neutral

carbon_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_high, ATOMIC_MASS["C"]),
    mass_fraction_to_uclchem(10**(-7), H_mid, ATOMIC_MASS["C"]),
    mass_fraction_to_uclchem(10**(-2), H_low, ATOMIC_MASS["C"])
])

hydrogen_grid = np.array([1, 1, 1])
#n_H/n_H should = 1 so
helium_grid = np.array([
    mass_fraction_to_uclchem(0.24, H_high, ATOMIC_MASS["He"]),
    mass_fraction_to_uclchem(0.26, H_mid, ATOMIC_MASS["He"]),
    mass_fraction_to_uclchem(0.30, H_low, ATOMIC_MASS["He"])
])

nitrogen_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_high, ATOMIC_MASS["N"]),
    mass_fraction_to_uclchem(10**(-5), H_mid, ATOMIC_MASS["N"]),
    mass_fraction_to_uclchem(10**(-2), H_low, ATOMIC_MASS["N"])
])

oxygen_grid = np.array([
    mass_fraction_to_uclchem(10**(-9), H_high, ATOMIC_MASS["O"]),
    mass_fraction_to_uclchem(10**(-5), H_mid, ATOMIC_MASS["O"]),
    mass_fraction_to_uclchem(10**(-1.5), H_low, ATOMIC_MASS["O"])
])

neon_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_high, ATOMIC_MASS["Ne"]),
    mass_fraction_to_uclchem(10**(-5), H_mid, ATOMIC_MASS["Ne"]),
    mass_fraction_to_uclchem(10**(-2), H_low, ATOMIC_MASS["Ne"])
])

magnesium_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_high, ATOMIC_MASS["Mg"]),
    mass_fraction_to_uclchem(10**(-5), H_mid, ATOMIC_MASS["Mg"]),
    mass_fraction_to_uclchem(10**(-2), H_low, ATOMIC_MASS["Mg"])
])

silicon_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_high, ATOMIC_MASS["Si"]),
    mass_fraction_to_uclchem(10**(-5), H_mid, ATOMIC_MASS["Si"]),
    mass_fraction_to_uclchem(10**(-2), H_low, ATOMIC_MASS["Si"])
])

iron_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_high, ATOMIC_MASS["Fe"]),
    mass_fraction_to_uclchem(10**(-5), H_mid, ATOMIC_MASS["Fe"]),
    mass_fraction_to_uclchem(10**(-2), H_low, ATOMIC_MASS["Fe"])
])
#values for low, mid, and high are approximations and NOT accurate to the TNG histograms.
#carbon_grid = np.array([
   # mass_fraction_to_uclchem(C_low, H_high, 12.011),
    #mass_fraction_to_uclchem(C_mid, H_mid, 12.011),
   #mass_fraction_to_uclchem(C_high, H_low, 12.011)
#])
#missing other_grid, z_grid, metallicity_grid, and other elements. I will need to define those as well.

mg_test = mass_fraction_to_uclchem(
    10**(-5),
    H_mid,
    ATOMIC_MASS["Mg"]
)

print("Converted Mg abundance:", mg_test)