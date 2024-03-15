# Thyroid Disease Data Analysis

This project is about an analysis of a thyroid disease dataset using Python.

- [Thyroid Disease Data Analysis](#thyroid-disease-data-analysis)
  - [Dataset Information](#dataset-information)
    - [Source](#source)
    - [Description of the variables](#description-of-the-variables)
  - [Analysis Information](#analysis-information)
    - [Technical specifications](#technical-specifications)
    - [Analysis methods](#analysis-methods)
    - [Data cleaning](#data-cleaning)
  - [Results](#results)
    - [Principal Component Analysis](#principal-component-analysis)
    - [Hierarchical Clustering Analysis](#hierarchical-clustering-analysis)
  - [Conclusions](#conclusions)

## Dataset Information

### Source

The data source is from the platform Kaggle, and the specified dataset can be found [here](https://www.kaggle.com/datasets/emmanuelfwerr/thyroid-disease-data). The dataset was specifically given out as part of the 'Thyroid Disease Awareness Month' (that being January) in $2022$.

The data itself was donated by the [Garvan Institute of Medical Research](https://www.garvan.org.au/) to the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/102/thyroid+disease), based on coverage from the $31^{st} \text{ of December } 1986$ till the $1^{st} \text{ of January } 1987$.

### Description of the variables

The dataset contains **9172 observations** and 31 variables, but only 12 were used for analysis.

They are (in order):

1. age - age of the patient (int)
2. sex - sex patient identifies (str)
3. on_thyroxine - whether patient is on thyroxine (bool)
4. on antithyroid meds - whether patient is on antithyroid meds (bool)
5. pregnant - whether patient is pregnant (bool)
6. thyroid_surgery - whether patient has undergone thyroid surgery (bool)
7. I131_treatment - whether patient is undergoing I131 treatment (bool)
8. query_hypothyroid - whether patient has hypothyroid (bool)
9. query_hyperthyroid - whether patient has hyperthyroid (bool)
10. lithium - whether patient takes lithium (bool)
11. goitre - whether patient has goitre (bool)
12. tumor - whether patient has tumor (bool)

## Analysis Information

### Technical specifications

The analysis was done using Python, and the main libraries used were `pandas`, `numpy` and `matplotlib`.

The code is split into two py files that corespond to the two main analysis methods use, namely `mainPCA.py` and `mainHCA.py`. These two files, aside from running the algorithms, also contain a reference to another two python scripts that clean the data and prepare it for analysis, namely `/util/datasetPCA.py` and `/util/datasetPCA.py`.

The raw dataset file can be found in `/dataIN/thyroid_dataset_raw.csv`.

### Analysis methods

The analysis was done using two main methods, namely **Principal Component Analysis (PCA)** and **Hierarchical Clustering Analysis (HCA)**.

I have chosen these two methods because they are both **unsupervised learning methods**, and they are both used for **dimensionality reduction** and **data visualization** respectively.

### Data cleaning

For both analysis methods, I turned the **boolean variables** into `0` and `1` along with the identifiers for *Male* and *Female*. Then, I replaced the missing values by taking a mean of the respective observation and following it up by standardising the data.

The only missing values that weren't replaced were the gender, for which I have decided it would be best to drop since there was no way of estimating a value for them. For the hierarchical clustering analysis, the variables were also grouped by age.

## Results

### Principal Component Analysis

### Hierarchical Clustering Analysis

## Conclusions
