#!/usr/bin/env python
# coding: utf-8

from .base_setting import *
from .font_style import *

def show_value_count(df: pandas.core.frame.DataFrame):
    """
    ### param
    df: pandas.core.frame.DataFrame
    ### return
    None
    ### brief
    데이터 벨류 비율을 보는 함수
    """
    print(fg.LMAGENTA, "🚀 show values count" + fg.RESET, sep="")
    fig, ax = plt.subplots(
        len(df.columns) // 2, 2, figsize=(16, len(df.columns) // 2 * 4)
    )
    for idx, column in enumerate(df.columns):
        sns.countplot(data=df, x=column, ax=ax[idx // 2, idx % 2])
    plt.show(fig)

