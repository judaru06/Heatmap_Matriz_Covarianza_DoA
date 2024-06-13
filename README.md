# Heatmap_Covariance_Matrix_DoA
Creating grayscale heatmaps for DoA estimation
# SCIENTIFIC COMPUTING

Std. Juan David Rojas Usuga

## Project Overview

This project aims to analyze complex matrices extracted from RF signals using different angles. Several statistical analyses and visualizations are performed to better understand the data. The project is organized in several folders containing scripts and data needed to run the analyses.

## Theoretical background:

Due to the digital transformation we are currently experiencing, the increase in data volumes and coverage, the challenges for 5G mobile networks are the increase in the number and variety of connected devices, the increase in user traffic, security and interference mitigation (Pastorino, 2005) in order to improve key performance indicators (KPIs) such as user throughput, accessibility, spectral efficiency, traffic capacity per area and density. As a primary option, new sites are added to address issues such as coverage, increasing connection capacity and increasing throughput per user, but at the same time new challenges arise in terms of signal interference, power consumption and spectrum saturation.

To help with these 5G problems, research has been carried out on beamforming techniques (Brilhante et al., 2023), which allow the generation of beams with main lobes at a desired angle, such as mobile phone users (UE), and generate nulls in the direction of interfering signals. In order to know where a transmitter is located, techniques for estimating the direction of arrival (DOA) have been researched, using methods such as sum and delay (Bartlett) and minimum variance with least distortion (Capon), which do not require knowledge of signal statistics, but give values that are different from the real value compared to the most popular techniques, such as multiple signal classification (MUSIC) and rotation invariance (ESPRIT), which provide an unbiased estimate of the incoming signals, but generally have a high degree of computational complexity, since accurate eigenvector estimation of both the signal subspace and the noise subspace is required (Chen and Gong, 2020).

Artificial Intelligence (AI) has become a valuable tool in several challenging domains and is being explored by researchers as a promising option to address practical problems in DoA prediction. These deep learning (DL) approaches outperform all conventional DOA estimation methods in terms of accuracy, making them a fundamental option in signal processing for advanced DOA estimation (Liu et al. 2018). Several models for DOA estimation using deep neural network (DNN) and Convolutional neural network (CNN) have been presented. Here, the DOA estimation task can be addressed by formulating classification (Fang et al., 2021; Z.-M. Liu et al., 2018) and regression (Cong et al., 2021) problems. In this method, the neural network processes a covariance matrix of the antenna outputs, which includes mutual coupling effects, to subsequently predict the DoA.  It should be noted that in (Fang et al., 2022) they process the covariance matrix as an image and then use a generative antagonistic network (GAN) to correct imperfections in the correlation matrix. The CNN is trained to perform regression by learning to map direction images, which are transformations of the spatial covariance matrix of the received signals, to the angular directions of the signal sources. In (Harkouss, 2021).

As can be seen the covariance matrix is a fundamental concept in signal processing and plays a fundamental role in DoA estimation to analyze the characteristics of the signals received by an array of antennas. In DoA estimation using CNN or DNN, the covariance matrix needs to be taken to a heat map image.

## Project Setup

1. **Clone Repository**:
   ````bash
   git clone <repository URL>.
   cd <repository name>

2. Install Dependencies:
Python 3.x is required. To install the dependencies, run:
   ````bash
      pip install -r requirements.txt
   
## The repository structure is as follows:
   ````bash
         C:.
         | .gitignore
         | output.txt
         | README.md
         | requirements.txt
         |
         +---data
         | datos_MUSIC_3.csv
         |
         +---results
         |
         +---srcs
         | Calculating_descriptive_statistics.py
         | Data_Organization_Conversion.py
         | Heatmap_Matriz_Covarianza_DoA.py
         |
         ---test
         Test_Heatmap_Matriz_Covarianza_DoA.py
  ````
## Running the Analysis
   Example code:
   ````
   test/Test_Heatmap_Matrix_Covariance_DoA.py.
   ````
## Methodology
* Data Loading: Data is loaded from CSV files.
* Data Conversion: Complex matrices in text format are converted into numerical matrices.
* Component Extraction: Real and imaginary parts of complex matrices are extracted.
* Statistical Analysis: Descriptive statistics such as mean, median, mode, standard deviation, etc. are calculated.
* Visualization: Heat maps are generated for the real and imaginary parts of the matrices.
  
## Summary of Results
Results show significant patterns in the complex matrices at different angles. Descriptive statistics provide a detailed view of the distribution of values in the matrices.

## Discussion
The results obtained allow the identification of patterns in RF signals that can be used to improve signal transmission and reception techniques. The visualizations help to better understand the data and to detect possible anomalies.

## Conclusions
This project demonstrates an effective methodology for the analysis of complex matrices in RF signals. The statistical analyses and visualizations provide valuable information that can be used in practical applications in the field of telecommunications.

## References:

* Brilhante, D. D. S., Manjarres, J. C., Moreira, R., De Oliveira Veiga, L., De Rezende, J. F., Müller, F., Klautau, A., Leonel Mendes, L., & P. De Figueiredo, F. A. (2023). A Literature Survey on AI-Aided Beamforming and Beam Management for 5G and 6G Systems. Sensors, 23(9), 4359. https://doi.org/10.3390/s23094359

* Pastorino, M. (2005). A Smart Antenna for the DOA Estimation of Impinging Signals and Passive Obstacle  Detection for Homeland Security. https://doi.org/10.1109/MSHS.2005.1502558

* Chen, M., Gong, Y., & Mao, X. (2020). Deep Neural Network for Estimation of Direction of Arrival With Antenna Array. IEEE ACCESS, 8, 140688-140698. https://doi.org/10.1109/ACCESS.2020.3012582

* Fang, W., Yu, D., Wang, X., Xi, Y., Cao, Z., Song, C., & Xu, Z. (2021). A Deep Learning Based Mutual Coupling Correction and DOA Estimation Algorithm. 2021 13th International Conference on Wireless Communications and Signal Processing (WCSP), 1-5. https://doi.org/10.1109/WCSP52459.2021.9613199

* Cong, J., Wang, X., Huang, M., & Wan, L. (2021). Robust DOA Estimation Method for MIMO Radar via Deep Neural Networks. IEEE Sensors Journal, 21(6), 7498-7507. https://doi.org/10.1109/JSEN.2020.3046291

* Fang, W., Cao, Z., Yu, D., Wang, X., Ma, Z., Lan, B., Song, C., & Xu, Z. (2022). A Lightweight Deep Learning-Based Algorithm for Array Imperfection Correction and DOA Estimation. Journal of Communications and Information Networks, 7(3), 296-308. https://doi.org/10.23919/JCIN.2022.9906943

* Harkouss, Y. (2021). Direction of arrival estimation in multipath environments using deep learning. International Journal of Communication Systems, 34(11). Scopus. https://doi.org/10.1002/dac.4882

* Bishop, C. M. (2006). Pattern recognition and machine learning. Springer.
