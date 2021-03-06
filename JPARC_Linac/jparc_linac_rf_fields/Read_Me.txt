============== Preparations ======================
We have SuperFISH data for DTL,SDTL, and ACS cavities
in the JPARC_SuperFish_FIELD_DATA dir. We use the .FSO files
to extract the Ez(z) field distributions( actually only for z>0).

For ACS *.FSO data with Ez(z) are under the beta value names. The explanations
are in ./JPARC_SuperFish_FIELD_DATA/acs/ACSgeobeta.txt file.

We do not use the amplitude of the Ez(z) from *.FSO files. We use PyORBIT 
tracking data from file:
./base_rf_tracking_data/pyorbit_jparc_rf_gaps_ekin_in_out.dat
This file was generated by the PyORBIT script:
../jparc_linac_model/pyorbit_jparc_linac_energy_at_rf_gaps.py
This script used old XML file for J-PARC linac generated with Trace3D E0TL and
synchronous phase parameters for each gap. 

All calculations are performed by the PyORBIT 
jparc_ttf_and_ez_field_generator.py 
script. It also rewrites the XML J-PARC linac file replacing the fake TTF by the 
real polynomials.
jparc_linac_init.xml    ---->   jparc_linac_new.xml

The normalized Ez(z) functions are saved in the "axis_field" dir.







