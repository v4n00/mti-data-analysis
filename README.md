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

The dataset contains **9172 observations** and **31 variables**, but **only 14 variables** were used for analysis.

They are (in order):

1. age - age of the patient *(int)*
2. sex - sex patient identifies *(str)*
3. on_thyroxine - whether patient is on thyroxine *(bool)*
4. on antithyroid meds - whether patient is on antithyroid meds *(bool)*
5. sick - whether patient is sick *(bool)*
6. pregnant - whether patient is pregnant *(bool)*
7. thyroid_surgery - whether patient has undergone thyroid surgery *(bool)*
8. I131_treatment - whether patient is undergoing I131 treatment *(bool)*
9. query_hypothyroid - whether patient has hypothyroid *(bool)*
10. query_hyperthyroid - whether patient has hyperthyroid *(bool)*
11. lithium - whether patient takes lithium *(bool)*
12. goitre - whether patient had goitre *(bool)*
13. tumor - whether patient had a tumor *(bool)*
14. psych - whether patient psychiatric problems *(bool)*

## Analysis Information

### Technical specifications

- The analysis was done using Python, and the main libraries used were `pandas`, `numpy` and `matplotlib`.

- The code is split into two py files that corespond to the two main analysis methods use, namely `mainPCA.py` and `mainHCA.py`. These two files, aside from running the algorithms, also contain a reference to another two python scripts that clean the data and prepare it for analysis, namely `/util/datasetPCA.py` and `/util/datasetPCA.py`.

- The raw dataset file can be found in `/dataIN/thyroid_dataset_raw.csv`.

### Analysis methods

- The analysis was done using two main methods, namely **Principal Component Analysis (PCA)** and **Hierarchical Clustering Analysis (HCA)**.

- I have chosen these two methods because they are both **unsupervised learning methods**, and they are both used for **dimensionality reduction** and **data visualization** respectively.

### Data cleaning

- For both analysis methods, I turned the **boolean variables** into `0` and `1` along with the identifiers for *Male* and *Female*. Then, I replaced the missing values by taking a mean of the respective observation and following it up by standardising the data.

- The only missing values that weren't replaced were the gender, for which I have decided it would be best to drop since there was no way of estimating a value for them. For the hierarchical clustering analysis, the variables were also grouped by age.

## Results

### Principal Component Analysis

This analysis is used more for understanding the data more than dimensionality reduction, and it is used to find the most important features of the dataset.

![PCA scree plot of variations](/dataOUT/PCA/principal_components.png)

- The scree plot illustrates the variance explained by the principal components, and it shows that the **first seven components are the most important**. As the scree plot progresses from `C1` to `C7`, the variance explained by each component decreases.

- Although this pattern continues, we can observe an interesting case, where the *sixth component* (`C6`) is **slightly above** the red horizontal line of 1.0 (which represents **Kaiser’s criterion**, signaling which components to keep) and the *seventh component* (`C7`) is also on the same level.

- This weird case sparked the interest for a second analysis to investigate what is happening with the data, especially for the the *seventh component* (`C7`).

![PCA factor loadings](/dataOUT/PCA/factor_loadings.png)

The factor loadings plot shows the relationship between the variables and the principal components. **The following results that follow are my own interpretations and should not be taken at face value**:

1. **Component 1** - this component explains a notable correlation between `sex` and `psych`, probably presenting the fact that **thyroid diseases manifest differently on the two genders** and that they can also **affect the mental health** of the patient;

2. **Component 2** - this component shows a strong correlation between `thyroxine`, `query_hypothyroid` and `pregnant`. Pregnancy increases the demand for thyroid hormones, and it can also lead to hypothyroidism, while thyroxine is a hormone that is used to treat hypothyroidism. In a nutshell, if a woman has **insufficient thyroxine production before becoming pregnant**, or if her body cannot increase thyroxine production adequately during pregnancy, **she may develop hypothyroidism**;

3. **Component 3** - this component shows an easily interpretable conclusion, the correlation between `on_antithyroid_meds` and `query_hyperthyroid` makes sense, since **antithyroid medications are used to treat hyperthyroidism**. The correlation between goitre and tumor is weirdly logical, since **goitre can be mistaken for thyroid cancer**;

4. **Component 4** - this component shows a correlation between `psych` and `lithium`, which is totally accurate since **lithium is used to treat psychiatric problems like bipolar disorder**. This components links up with the next component;

5. **Component 5** - this component shows a weird correlation between `goitre` and `lithium`, which can suggest that **lithium can affect thyroid function** and thus cause abnomarlities in the thyroid gland. This is also backed by a study that can be found [here](https://www.uptodate.com/contents/lithium-and-the-thyroid);

6. **Component 6** - this component is not really linked with anything, showing only a strong correlation with only `thyroid_surgery`, which makes sense for patients that already have thyroid problems;

7. **Component 7** - this component is very interesting, since it shows a very strong correlation with `age`, indicating that there might be some underlying **age-related thyroid problems**.

### Hierarchical Clustering Analysis

This analysis is used to cluster the data into groups based on the age of the patients, starting from $10$ all the way up to $64$.

![HCA dendogram](/dataOUT/HCA/hierarchical_classification.png)

The dendogram shows the clustering of the ages, and it is clear that there are **three main clusters that represent different stages in life**. The red line represents the **optimal number of clusters**, that being 3. The clusters are as follows:

1. **Cluster 1 / Puberty** (ages $11$ - $15$) - this cluster indicates the prevalence of thyroid problems that occur during puberty, which is a understandable due to the **hormonal changes that happen during this developmental period**;

2. **Cluster 2 / Adulthood** (ages $22$ - $40$) - this cluster indicates the prevalence of thyroid problems that occur during the childbearing years for women, which is also another common occurrence due to the **hormonal changes that happen during pregnancy**;

3. **Cluster 3 / Middle age** (ages $40$ - $60$) - this cluster indicates the prevalence of thyroid problems that occur during middle age, which is a common occurrence due to the **hormonal changes that happen during this period, especially for women**. This cluster can be further broken down into 2 more clusters, showing ages below 50 and above 50.

An **interesting outlier** is the age of $21$, which is situated between the first and second cluster, and can be interpreted as a **transition period** between puberty and adulthood.

## Conclusions

The analysis of this dataset has shown that there are **several factors that can influence the development of thyroid diseases**, like gender, psychiatric problems or medications and that they can also be linked with the **different stages of life**.

As people go through life, from being young to getting older, the risk and type of thyroid problems can change, and it is important to be aware of these changes and to take necessary precautions.
