import numpy as np
import pandas as pd
import uclchem

from abundances import mass_fraction_to_uclchem, ATOMIC_MASS

sample_file = "/projects/dust_chem/sample_data/particle_sample.csv"

particles = pd.read_csv(sample_file)

print(particles.columns)
print(particles.head())
print("Number of particles:", len(particles))

# Pick first particle
particle = particles.iloc[0]

print("\nFIRST PARTICLE:")  
print(particle)


# --------------------------------
# Convert density for UCLCHEM
# --------------------------------

HUBBLE_h = 0.6774

MSUN_G = 1.98847e33
KPC_CM = 3.085677581e21
M_H_G = 1.6735575e-24

rho_code = float(particle["density_code_units"])
X_H = float(particle["metal_H_mass_fraction"])

# TNG density -> Msun/kpc^3
rho_msun_kpc3 = rho_code * 1.0e10 * HUBBLE_h**2

# Msun/kpc^3 -> g/cm^3
rho_g_cm3 = (
    rho_msun_kpc3
    * MSUN_G
    / KPC_CM**3
)

# Mass density -> hydrogen nuclei/cm^3
n_H = rho_g_cm3 * X_H / M_H_G

print("\nDENSITY CONVERSION")
print("Original TNG density:", rho_code)
print("Density [Msun/kpc^3]:", rho_msun_kpc3)
print("Density [g/cm^3]:", rho_g_cm3)
print("UCLCHEM n_H [cm^-3]:", n_H)

X_H = float(particle["metal_H_mass_fraction"])

C_uclchem = mass_fraction_to_uclchem(
    float(particle["metal_C_mass_fraction"]),
    X_H,
    ATOMIC_MASS["C"]
)

O_uclchem = mass_fraction_to_uclchem(
    float(particle["metal_O_mass_fraction"]),
    X_H,
    ATOMIC_MASS["O"]

)

Mg_uclchem = mass_fraction_to_uclchem(
    float(particle["metal_Mg_mass_fraction"]),
    X_H,
    ATOMIC_MASS["Mg"]
)

He_uclchem = mass_fraction_to_uclchem(
    float(particle["metal_He_mass_fraction"]),
    X_H,
    ATOMIC_MASS["He"]
)

N_uclchem = mass_fraction_to_uclchem(
    float(particle["metal_N_mass_fraction"]),
    X_H,
    ATOMIC_MASS["N"]
)       

Si_uclchem = mass_fraction_to_uclchem(
    float(particle["metal_Si_mass_fraction"]),
    X_H,
    ATOMIC_MASS["Si"]
)

H_uclchem = 1.0

print("\nUCLCHEM ELEMENTAL ABUNDANCES")
print("C/H:", C_uclchem)
print("O/H:", O_uclchem)
print("Mg/H:", Mg_uclchem)
print("He/H:", He_uclchem)
print("N/H:", N_uclchem)
print("Si/H:", Si_uclchem)
print("H/H:", H_uclchem)


# Build UCLCHEM parameter dictionary for this particle
param_dict = {
    "fh": 1.0,
    "fhe": He_uclchem,
    "fc": C_uclchem,
    "fn": N_uclchem,
    "fo": O_uclchem,
    "fmg": Mg_uclchem,
    "fsi": Si_uclchem,
}

print("\nPARAMETERS TO SEND TO UCLCHEM")
for key, value in param_dict.items():
    print(f"{key}: {value}")