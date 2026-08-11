"""
Sample a subset of particles to run with astrochemical codes
"""

import numpy as np
import h5py
import pandas as pd

k_b = 1.380649e-16 #erg/K       #1.3806448e-23 # J/K
m_H = 1.6726219e-24 # g

def energy_to_temp(u, mu, gamma_min_one =2/3):
    """
    Convert energy per unit mass to temperature using the equation of state.
    Parameters:
        u (float): Energy per unit mass in (km/s)^2 (code units)
        mu (float): Mean molecular weight
        gamma_min_one (float): Adiabatic index (default is 5/3 for monatomic gas) subtracted by 1 (to avoid repeat divisition)

    Returns:
        temp (float): Temperature in Kelvin
    """
    return u*mu*m_H*(gamma_min_one)/k_b #convert to Kelvin 


def mean_mol_weight(X, x_e):
    """
    Compute the mean molecular weight for a given partially-ionized composition.
    Assumption is made that contribution of metals is negligible
    
    Parameters:
        X (float): Hydrogen mass fraction
        x_e (float): Electron abundance (n_e/n_H)
    Returns:
        mu (float): Mean molecular weight
    """
    return 4/(1+3*X+4*X*x_e) #mean molecular weight for fully ionized gas

chunk=np.random.randint(0,200) #if went out to all 599 files, high chance of always pulling from outer fuzz
print(chunk)

with h5py.File(f"/projects/dust/data/TNG300_gas/snap99/snap_099.{chunk}.hdf5", "r") as f:
    gas=f["PartType0"]
    #print(gas.keys())
    density = gas["Density"][:]
    e_abundance=gas["ElectronAbundance"][:]
    metallicity=gas["GFM_Metallicity"][:]
    masses=gas["Masses"][:]
    neutral_H=gas["NeutralHydrogenAbundance"][:]
    metals=gas["GFM_Metals"][:]
    energy=gas["InternalEnergy"][:]

with h5py.File(f"/projects/dust/data/TNG300_gas/snap99/post_snap_099.{chunk}.hdf5", "r") as f:
    dust=f["M20_half"]
    dust_mass=dust['M_dust'][:]
    universal=f["Universal"]
    location=universal["location"][:]
    neutral_fraction=universal["f_neutral"][:]
    
    #print(dust.keys())
    #print(universal.keys())


data=pd.DataFrame()
data["density"]=density
data["masses"]=masses
data["metallicity"]=metallicity


data["neutral_fraction"]=neutral_fraction
data["neutral_H"]=neutral_H
data["e_abundance"]=e_abundance


species=['H', 'He', 'C', 'N', 'O', 'Ne', 'Mg', 'Si', 'Fe', 'other_metals']

for i in range(len(metals[0])):
    data[f"{species[i]}"]=metals[:,i]


mu=mean_mol_weight(data["H"], e_abundance)
data['gas_temp']=energy_to_temp(energy, mu)
data['dust_mass (estimate)']=dust_mass

data['location']=location

df=data.loc[data['location']!=3]

df.drop(columns=['location'], inplace=True)

from sklearn.cluster import MiniBatchKMeans
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler


sampling_columns = [
    "density",
    "gas_temp",
    "metallicity",
    "H",
]

sampling_df = (
    df[sampling_columns]
    .replace([np.inf, -np.inf], np.nan)
    .dropna()
)

sampling_df = sampling_df[
    (sampling_df["density"] > 0)
    & (sampling_df["gas_temp"] > 0)
    & (sampling_df["metallicity"] > 0)
    & (sampling_df["H"] > 0)
]

features = pd.DataFrame(
    {
        "log_density": np.log10(sampling_df["density"]),
        "log_gas_temp": np.log10(sampling_df["gas_temp"]),
        "log_metallicity": np.log10(sampling_df["metallicity"]),
        "H": sampling_df["H"],
    },
    index=sampling_df.index,
)

development_size = min(100_000, len(features))

development_features = features.sample(
    n=development_size,
    random_state=42,
)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(development_features)

n_representatives = 25

cluster_model = MiniBatchKMeans(
    n_clusters=n_representatives,
    batch_size=4096,
    random_state=42,
    n_init="auto",
)

cluster_model.fit(X_scaled)

nearest = NearestNeighbors(n_neighbors=1)
nearest.fit(X_scaled)

distances, positions = nearest.kneighbors(
    cluster_model.cluster_centers_
)

representative_indices = development_features.index[
    positions[:, 0]
]

representative_particles = df.loc[representative_indices].copy()
representative_particles["distance_to_cluster_center"] = distances[:, 0]

representative_particles.to_csv(
    "representative_particles_test.csv",
    index=True,
)

print(representative_particles)
print(f"Selected {len(representative_particles)} particles.")


""" 
UNITS: 
density: 10^10 M_sun / kpc^3
masses: 10^10 M_sun
metallicity: ratio of total mass of all elements heavier than helium to total mass of gas particle; 
    to convert to solar metallicity divide by 0.0127 
neutral_fraction: fraction of gas in neutral phase
dust_mass: 10^10 M_sun
"""