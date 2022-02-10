# Team 2 (IBMazing)

Classifying Objects as Rocks or Mines Given Sonar Data 

Dataset from https://archive.ics.uci.edu/ml/datasets/Connectionist+Bench+(Sonar,+Mines+vs.+Rocks)

Main idea: In order to classify the above data using quantum kernel estimation, we need to reduce the dimensionality of the dataset. We compare two methods for doing so: principal component analysis and autoencoding.

Results: For a single repetition of the ZZ feature map (built into Qiskit), the autoencoder-compressed data led to a better classification accuracy than the PCA-compressed data (when reducing the dimensionality from sixty features down to five). For a larger number of repetitions, by contrast, it was the the PCA-compressed data that performed better. Results can be found in the QKE_Implementation notebook.
         


Required packages are listed in requirements.txt.
