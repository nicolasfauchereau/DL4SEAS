## Notes about Transfer Learning

# Inputs and Outputs

1. The test notebook inputs the SST anomalies near the central pacific and outputs the NZ seven station
series temperature anomally. 

2. The notebook reads the ERSST sst anomalies from NOAA, and the seven station series.

3. The idea of this notebook is to explain more variability in NZ temperature record from non-local climate drivers.
e.g  are there other relevant features in the central pacific that are relevant to NZ climate.


## Challenges with Transfer Learning

1. It appears that both instances of inputs and outputs for the ResNET50 model are very sensitive to
preprocessing. 
2. I'm having some significant issues with mappings. For example, the ResNET models are not able to properly map the outputs 
to the same valid range as the temperature anomalies - which is indicates that it is not learning properly
3. Note, that all the other layers are frozen in the model aside from the final dense layers. 

4. I've had some success while training my own custom CNN, which is relatively shallow.  