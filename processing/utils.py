import pandas as pd
import matplotlib.pyplot as plt

def concat_two_dfs(df_list):
    df = pd.concat(df_list,
                   axis=0)
    df = df.reset_index(drop=True)
    return df

def standard_plot(pd_dataframe):
    # print(pd_dataframe['Date'])
    plt.figure(figsize=(12, 6), dpi=100)
    plt.plot(pd_dataframe['Date'],
             pd_dataframe['US dollar'])
    plt.xlabel('Date')
    plt.xlabel('Rates')
    plt.grid()
    plt.show()


def concat_n_dfs(df_list):
    if len(df_list) == 2:
        return concat_two_dfs(df_list)
    else:
        df_0_1 = df_list[0:2]
        df_cat = concat_two_dfs(df_0_1)
        for df_follow in df_list[2:]:
            df_cat = concat_two_dfs([df_cat, df_follow])
        return df_cat

