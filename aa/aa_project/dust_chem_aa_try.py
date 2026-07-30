import numpy as np
import uclchem  
from abundances import abundance_dict

density_grid = np.array([-1, 3, 9.5])  # log10(n_H / cm^-3)

gas_temperature_grid = np.array([2.5, 6.0, 9.0])  # log10(T_gas / K)

fneutral_grid = np.array([0.0, 0.06, 1.0])  # f_neutral

#missing other_grid, z_grid, metallicity_grid, and other elements. I will need to define those as well.

mg_test = mass_fraction_to_uclchem(
    10**(-5),
    H_mid,
    ATOMIC_MASS["Mg"]
)

print("Converted Mg abundance:", mg_test)

MID = 1

param_dict = {
    parameter: float(values[MID])
    for parameter, values in abundance_dict.items()
}

param_dict["finaldens"] = 5000.0
