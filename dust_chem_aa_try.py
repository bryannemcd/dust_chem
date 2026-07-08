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
#carbon = mass_fraction_to_uclchem(C_mass, H_mass, 12.011) (though this is only one abundance)

# ----------------------------
#Defining H_mass_fraction values 
#----------------------------
H_mass_fraction = 0.7381 #from TNG100-1, z=
# ----------------------------
# Initial parameter grids
# ----------------------------

density_grid = np.array([-1, 3, 9.5])  # log10(n_H / cm^-3)

gas_temperature_grid = np.array([2.5, 6.0, 9.0])  # log10(T_gas / K)

fneutral_grid = np.array([0.0, 0.06, 1.0])  # f_neutral

carbon_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_mass_fraction, ATOMIC_MASS["C"]),
    mass_fraction_to_uclchem(10**(-7), H_mass_fraction, ATOMIC_MASS["C"]),
    mass_fraction_to_uclchem(10**(-2), H_mass_fraction, ATOMIC_MASS["C"])
])

hydrogen_grid = np.array([
    mass_fraction_to_uclchem(0.60, H_mass_fraction, ATOMIC_MASS["H"]),
    mass_fraction_to_uclchem(0.7381, H_mass_fraction, ATOMIC_MASS["H"]),
    mass_fraction_to_uclchem(0.75, H_mass_fraction, ATOMIC_MASS["H"])
])
#I used the same value of the H_mass_fraction for the H_mid range since its the same meaning
helium_grid = np.array([
    mass_fraction_to_uclchem(0.24, H_mass_fraction, ATOMIC_MASS["He"]),
    mass_fraction_to_uclchem(0.26, H_mass_fraction, ATOMIC_MASS["He"]),
    mass_fraction_to_uclchem(0.30, H_mass_fraction, ATOMIC_MASS["He"])
])

nitrogen_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_mass_fraction, ATOMIC_MASS["N"]),
    mass_fraction_to_uclchem(10**(-5), H_mass_fraction, ATOMIC_MASS["N"]),
    mass_fraction_to_uclchem(10**(-2), H_mass_fraction, ATOMIC_MASS["N"])
])

oxygen_grid = np.array([
    mass_fraction_to_uclchem(10**(-9), H_mass_fraction, ATOMIC_MASS["O"]),
    mass_fraction_to_uclchem(10**(-5), H_mass_fraction, ATOMIC_MASS["O"]),
    mass_fraction_to_uclchem(10**(-1.5), H_mass_fraction, ATOMIC_MASS["O"])
])

neon_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_mass_fraction, ATOMIC_MASS["Ne"]),
    mass_fraction_to_uclchem(10**(-5), H_mass_fraction, ATOMIC_MASS["Ne"]),
    mass_fraction_to_uclchem(10**(-2), H_mass_fraction, ATOMIC_MASS["Ne"])
])

magnesium_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_mass_fraction, ATOMIC_MASS["Mg"]),
    mass_fraction_to_uclchem(10**(-5), H_mass_fraction, ATOMIC_MASS["Mg"]),
    mass_fraction_to_uclchem(10**(-2), H_mass_fraction, ATOMIC_MASS["Mg"])
])

silicon_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_mass_fraction, ATOMIC_MASS["Si"]),
    mass_fraction_to_uclchem(10**(-5), H_mass_fraction, ATOMIC_MASS["Si"]),
    mass_fraction_to_uclchem(10**(-2), H_mass_fraction, ATOMIC_MASS["Si"])
])

iron_grid = np.array([
    mass_fraction_to_uclchem(10**(-10), H_mass_fraction, ATOMIC_MASS["Fe"]),
    mass_fraction_to_uclchem(10**(-5), H_mass_fraction, ATOMIC_MASS["Fe"]),
    mass_fraction_to_uclchem(10**(-2), H_mass_fraction, ATOMIC_MASS["Fe"])
])
#values for low, mid, and high are approximations and NOT accurate to the TNG histograms.
#carbon_grid = np.array([
   # mass_fraction_to_uclchem(C_low, H_mass_fraction, 12.011),
    #mass_fraction_to_uclchem(C_mid, H_mass_fraction, 12.011),
   #mass_fraction_to_uclchem(C_high, H_mass_fraction, 12.011)
#])
#missing other_grid, z_grid, metallicity_grid, and other elements. I will need to define those as well.