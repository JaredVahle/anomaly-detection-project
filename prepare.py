import pandas as pd
import numpy as np


def clean_cohort_data(df):
    df['datetime'] = df.date + ' ' + df.time
    df['datetime'] = pd.to_datetime(df['datetime'])
    df = df.set_index('datetime')
    df['program_name'] = df.program_id.replace({1:'PHP Full Stack Web Development',2:'Java Full Stack Web Development',3:'Data Science',4:'Front End Web Development'})
    df['program_subdomain'] = df.program_id.replace({1:'php',2:'java',3:'ds',4:'fe'})
    df.drop(columns = ['date','time','deleted_at','program_id','id'],inplace = True)
    df.rename(columns = {'name':'cohort_name'},inplace = True)
    dictionary = {'Bash':61,'Hyperion':58,'Darden':59,'Florence':137,'Jupiter':62}
    df['cohort_id'].fillna(df['cohort_name'].map(dictionary), inplace=True)
    df = df.astype({"cohort_id": int})
    df['count_helper'] = 1
    df['split_path'] = df['path'].str.split('/')
    return df

def remove_empty_paths(df):
    df = df[df.path != '/']
    return df
