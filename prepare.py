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
    return df
