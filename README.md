# Deep Learning experiments for seasonal climate forecasting 

### content of the repository 

+ [dl4seas](https://github.com/nicolasfauchereau/DL4SEAS/tree/master/dl4seas): modules
	- **IO**: inputs / outputs, for now functions to create TF protobuf files from xarray datasets and a list of netcdf files
	- **NN**: custom layers to use in CNNs and DataGenerator Class 
	- **preprocessing**: for now only a `train_scaler` function using dask-ml or scikit-learn to train a Standard Scaler on xarray Dataset objects
	- **utils**: some utility functions 

+ [CNN](https://github.com/nicolasfauchereau/DL4SEAS/tree/master/CNN)

notebooks, scripts, outputs and figures for the core experiments building on Convolutional Neural Networks (incl. Auto-encoders)

+ [transfer_learning](https://github.com/nicolasfauchereau/DL4SEAS/tree/master/transfer_learning)

notebooks, scripts, outputs and figures for the experiments specifically building on pre-trained NN architectures (*Transfer Learning*)

+ [wide_and_deep](https://github.com/nicolasfauchereau/DL4SEAS/tree/master/wide_and_deep)

notebooks, scripts, outputs and figures for the experiments building on "wide and Deep"* architectures, which include auxiliary inputs representing the current state and / or the recent evolution of the climate system from observational sources. 

* Cheng, H.-T., and Coauthors, 2016: Wide & Deep Learning for Recommender Systems. arXiv:1606.07792 [cs, stat]s