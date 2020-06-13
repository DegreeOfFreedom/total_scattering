# total_scattering

## Usage  

The scripts in this repository are not intended to work out of the box for any given total scattering experiment.  
Neither are they the most efficient for that purpose. In fact they could be improved greatly with only little effort.  
The purpose of these scripts is to demonstrate how the raw intensities from the data folder were evaluated to represent the scattering functions **S(q)** for each sample in the results section of the master thesis "Evaluation of the diffuse X-Ray scattering on Alkali-Borate Glasses".  
As such, included in this repository are scrips for:  
- All calibrations performed in section 2.3
- Preparation and normalization of gathered intensities and calculation of scattering factors as described in 2.5.1
- Calculation of the scattering function with the output being a text-file of the data-points and a plot of the function
- Calculation of the sample thickness  

A complete set of the raw data is also provided. Furthermore a modified script where **S(q)** is calculated with the trapezoid thickness-correction is included as well. The simulations used in section 3 are not included.  
The scripts are written on the basis of Python version 2.7, and require the following external packages:  
- Numpy
- Scipy
- Matplotlib
- Sympy
- Natsort
- Scikit-learn  

The main script, "auswerter.py", goes through all the steps mentioned above, except for the calibration. It requires a configuration file in which the location of the angle-specific intensity-profiles is specified. The other parameters included in this file are the output-paths for the data-points and plot, the name of the sample, the name of the required module to calculate the sample-specific averaged scattering factors, the concentrations in at.% for the atoms comprising the sample, the intensities **I0**  and  **I** for thickness correction, the length of the input array and finally the normalization coefficient **N**.  
The script requires only the location of the configuration files for execution.  
The remaining calibration scripts handle calculation pertaining to the detector energy and absorption linearity, as well as the beam profile. The relevant data for our measurements is already provided within them. The beam profile script calculates the FWHM according to the methods laid out in section 2.3.3.
