import generate_porosity_dataset as gpd

# POROSITY PREDICTION
# Collect PORHE & PORFLU As Output, RHOB & NPHI As Input
# Note: ASDJ10 does not have a RHOB data. So just skip for this specific well
gpd.execute()