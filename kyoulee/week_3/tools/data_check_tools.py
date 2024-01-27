#!/usr/bin/env python
# coding: utf-8

from .base_setting import *
from .font_style import *

def data_check_null(df: pandas.core.frame.DataFrame) -> int:
    """
    ### param
    df: pandas.core.frame.DataFrame
    ### return
    null_count : int
    ### brief
    DataFrame 안에 null갯수를 확인하는 함수 입니다
    """
    print(fg.LMAGENTA, "🚀 NULL Check", fg.RESET, sep="")
    if df.isnull().sum().sum():
        print(
            fg.LYELLOW,
            df.isnull().sum(),
            "\n",
            fg.LRED,
            "Total : ",
            df.isnull().sum().sum(),
            fg.RESET,
            sep="",
        )
    else:
        print(fg.LGREEN, "OK", fg.RESET, sep="")
    return df.isnull().sum().sum()


def data_check_object(df: pandas.core.frame.DataFrame, data=""):
    """
    ### param
    df: pandas.core.frame.DataFrame
    data: str = ""
    ### return
    None
    ### brief
    양측 공백을 제거하고 특정 문자를 찾는 함수 입니다.
    """
    df_object = df.select_dtypes(["object"])
    isclear = True
    print(fg.LMAGENTA, "🚀 '" + data + "' Check" + fg.RESET, sep="")
    for column in df_object.columns:
        if np.where(df_object[column].str.strip() == data)[0].size:
            isclear = False
            print(
                fg.LYELLOW + df_object[column].name + fg.RESET,
                " : ",
                np.where(df_object[column].str.strip() == data),
                sep="",
            )
    print(fg.LGREEN, "OK", sep="") if isclear else print(fg.LRED, "Not Clear", sep="")
