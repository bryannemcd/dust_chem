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
H_low = 0.56
H_mid = 0.72
H_high = 0.76
# ----------------------------
# Initial parameter grids
# ----------------------------

carbon_abundance = np.array([
    mass_fraction_to_uclchem(10**(-10), H_high, ATOMIC_MASS["C"]),
    mass_fraction_to_uclchem(10**(-7), H_mid, ATOMIC_MASS["C"]),
    mass_fraction_to_uclchem(10**(-2), H_low, ATOMIC_MASS["C"])
])

hydrogen_abundance = np.array([
    1, 1, 1
])
#n_H/n_H should = 1 so
helium_abundance = np.array([
    mass_fraction_to_uclchem(0.24, H_high, ATOMIC_MASS["He"]),
    mass_fraction_to_uclchem(0.26, H_mid, ATOMIC_MASS["He"]),
    mass_fraction_to_uclchem(0.30, H_low, ATOMIC_MASS["He"])
])

nitrogen_abundance = np.array([
    mass_fraction_to_uclchem(10**(-10), H_high, ATOMIC_MASS["N"]),
    mass_fraction_to_uclchem(10**(-5), H_mid, ATOMIC_MASS["N"]),
    mass_fraction_to_uclchem(10**(-2), H_low, ATOMIC_MASS["N"])
])

oxygen_abundance = np.array([
    mass_fraction_to_uclchem(10**(-9), H_high, ATOMIC_MASS["O"]),
    mass_fraction_to_uclchem(10**(-5), H_mid, ATOMIC_MASS["O"]),
    mass_fraction_to_uclchem(10**(-1.5), H_low, ATOMIC_MASS["O"])
])

neon_abundance = np.array([
    mass_fraction_to_uclchem(10**(-10), H_high, ATOMIC_MASS["Ne"]),
    mass_fraction_to_uclchem(10**(-5), H_mid, ATOMIC_MASS["Ne"]),
    mass_fraction_to_uclchem(10**(-2), H_low, ATOMIC_MASS["Ne"])
])

magnesium_abundance = np.array([
    mass_fraction_to_uclchem(10**(-10), H_high, ATOMIC_MASS["Mg"]),
    mass_fraction_to_uclchem(10**(-5), H_mid, ATOMIC_MASS["Mg"]),
    mass_fraction_to_uclchem(10**(-2), H_low, ATOMIC_MASS["Mg"])
])

silicon_abundance = np.array([
    mass_fraction_to_uclchem(10**(-10), H_high, ATOMIC_MASS["Si"]),
    mass_fraction_to_uclchem(10**(-5), H_mid, ATOMIC_MASS["Si"]),
    mass_fraction_to_uclchem(10**(-2), H_low, ATOMIC_MASS["Si"])
])

iron_abundance = np.array([
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

abundance_dict = {
    "fhe": helium_abundance,
    "fc": carbon_abundance,
    "fn": nitrogen_abundance,
    "fo": oxygen_abundance,
    "fmg": magnesium_abundance,
    #"fne": neon_abundance, removed for now
    "fsi": silicon_abundance,
    #"ffe": iron_abundance,
    "fh": hydrogen_abundance,
}

# Only parameters currently accepted by UCLCHEM
#abundance_dict = {
   # "fhe": he_abundance,
    #"fc": c_abundance,
   # "fn": n_abundance,
    #"fo": o_abundance,
   # "fs": s_abundance,
   # "fmg": mg_abundance,
   # "fsi": si_abundance,
   # "fcl": cl_abundance,
    #"fp": p_abundance,
    #"ff": f_abundance,
#}