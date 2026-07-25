import numpy as np
import uclchem

mg_abundance = 5.760131660152233e-7

time_array = np.array([
    1.0,
    1000.0,
    2000.0,
    3000.0,
])

density_array = np.array([
    1111.0,
    2222.0,
    3333.0,
    4444.0,
])

gas_temperature_array = np.array([
    11.0,
    22.0,
    33.0,
    44.0,
])

dust_temperature_array = np.array([
    10.0,
    20.0,
    30.0,
    40.0,
])

zeta_array = np.array([
    1.1,
    1.2,
    1.3,
    1.4,
])

radfield_array = np.array([
    2.1,
    2.2,
    2.3,
    2.4,
])

# This must come after time_array is defined.
param_dict = {
    "fmg": mg_abundance,
    "finaltime": 3000.0001,
    "finalDens": 5000.0,
}

print("PARAMETERS SENT TO UCLCHEM")
for key, value in param_dict.items():
    print(f"{key}: {value}")

result = uclchem.model.postprocess(
    param_dict=param_dict,
    return_dataframe=True,
    return_rates=False,
    time_array=time_array,
    density_array=density_array,
    gas_temperature_array=gas_temperature_array,
    dust_temperature_array=dust_temperature_array,
    zeta_array=zeta_array,
    radfield_array=radfield_array,
)

physical_arrays = {
    "density_array": density_array,
    "gas_temperature_array": gas_temperature_array,
    "dust_temperature_array": dust_temperature_array,
    "zeta_array": zeta_array,
    "radfield_array": radfield_array,
}
#input validation for the arrays to ensure they are one-dimensional, finite, and strictly increasing. Also checks that the physical parameter arrays have the same shape as the time array and contain no negative values.
time_array = np.asarray(time_array, dtype=float)

if time_array.ndim != 1:
    raise ValueError("time_array must be one-dimensional")

if not np.all(np.isfinite(time_array)):
    raise ValueError("time_array contains NaN or infinite values")

if not np.all(np.diff(time_array) > 0):
    raise ValueError("time_array must be strictly increasing")

for name, values in physical_arrays.items():
    values = np.asarray(values, dtype=float)

    if values.shape != time_array.shape:
        raise ValueError(
            f"{name} has shape {values.shape}, "
            f"but time_array has shape {time_array.shape}"
        )

    if not np.all(np.isfinite(values)):
        raise ValueError(f"{name} contains NaN or infinite values")

    if np.any(values < 0):
        raise ValueError(f"{name} contains negative values")


#next part of the code is to unpack the result and print the outputs, simplifying the terminal output for easier reading and analysis.
physics_df, chemistry_df, rates_df, abundance_start, success_flag = result

print("\nSUCCESS FLAG")
print(success_flag)

print("\nPHYSICS OUTPUT")
print(physics_df.to_string(index=False))

print("\nOUTPUT SHAPES")
print("Physics:", physics_df.shape)
print("Chemistry:", chemistry_df.shape)
print("Rates:", None if rates_df is None else rates_df.shape)
print("Starting chemistry:", abundance_start.shape)
mg_columns = [
    name
    for name in chemistry_df.columns
    if "MG" in name.upper()
]

print("\nMAGNESIUM SPECIES")
print(mg_columns)

print("\nFINAL MAGNESIUM ABUNDANCES")
print(
    chemistry_df.iloc[-1][mg_columns]
    .sort_values(ascending=False)
    .to_string()
)

print("Number of returned objects:", len(result))

for index, item in enumerate(result):
    print(index, type(item))

    print("test")