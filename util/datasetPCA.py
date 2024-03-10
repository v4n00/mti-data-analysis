import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

thyroid_df = pd.read_csv('./dataIn/thyroid_dataset_raw.csv')

categorical_bool_columns = thyroid_df.select_dtypes(include=['object', 'bool']).columns
label_encoders = {}

for col in categorical_bool_columns:
    if col not in ['patient_id', 'target']:
        le = LabelEncoder()
        thyroid_df[col] = le.fit_transform(thyroid_df[col].astype(str))
        label_encoders[col] = le

thyroid_df = thyroid_df[thyroid_df.columns.values[:-3]]

def replaceNAN(X):
    means = np.nanmean(X, axis=0)
    locs = np.where(np.isnan(X))
    X[locs] = means[locs[1]]
    return X

cols = thyroid_df.columns.values
th = replaceNAN(thyroid_df.values)
thyroid_df = pd.DataFrame(data=th, columns=cols)
thyroid_df.drop(['query_on_thyroxine', 'query_hypothyroid'], inplace=True, axis=1)

scaler = StandardScaler()
thyroid_df[thyroid_df.columns] = scaler.fit_transform(thyroid_df)

thyroid_df.to_csv('./dataIN/thyroid_dataset_pca.csv', index=False)