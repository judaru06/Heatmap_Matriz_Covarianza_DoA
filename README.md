# Heatmap_Covariance_Matrix_DoA
Creating grayscale heatmaps for DoA estimation
# SCIENTIFIC COMPUTING

Std. Juan David Rojas Usuga

## Project Overview

This project aims to analyze complex matrices extracted from RF signals using different angles. Several statistical analyses and visualizations are performed to better understand the data. The project is organized in several folders containing scripts and data needed to run the analyses.

## Project Setup

1. **Clone Repository**:
   ````bash
   git clone <repository URL>.
   cd <repository name>

2. Install Dependencies:
Python 3.x is required. To install the dependencies, run:
   ````bash
      pip install -r requirements.txt
   
## Running the Analysis
   Example code:
   test/Test_Heatmap_Matrix_Covariance_DoA.py.

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
