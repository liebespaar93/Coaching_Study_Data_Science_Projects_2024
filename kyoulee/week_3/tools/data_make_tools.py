#!/usr/bin/env python
# coding: utf-8

from .base_setting import *
from .font_style import *

def data_make_bool(
    df: pandas.core.frame.DataFrame, columns: list[str], value_true: list[any]
):
    """
    ### param
    df: pandas.core.frame.DataFrame
    columns: list[str]
    value_true: list[any]
    ### return
    new_df: pandas.core.frame.DataFrame
    ### brief
    데이터를 boolean 변경하는 함수
    """
    print(fg.LMAGENTA, "🚀 make values bool" + fg.RESET, sep="")
    if len(columns) != len(value_true):
        print(
            fg.LRED + "arg is diff len\n" + fg.RESET,
            "columns" + fg.GREEN + "[" + str(len(columns)) + "]" + fg.RESET,
            " != ",
            "value_true" + fg.GREEN + "[" + str(len(value_true)) + "]" + fg.RESET,
            sep="",
        )
    new_df = df.copy(deep=True)
    for idx, column in enumerate(columns):
        new_df[column] = (new_df[column] == value_true[idx]).astype(bool)
    print(fg.LGREEN, "OK", sep="")
    return new_df


def data_make_number(
    df: pandas.core.frame.DataFrame, columns: list[str], value_index: list[list[any]]
):
    """
    ### param
    df: pandas.core.frame.DataFrame
    columns: list[str]
    value_index: list[list[any]]
    ### return
    new_df: pandas.core.frame.DataFrame
    ### brief
    데이터를 number 변경하는 함수
    """
    print(fg.LMAGENTA, "🚀 make values number" + fg.RESET, sep="")
    if len(columns) != len(value_index):
        print(
            fg.LRED + "arg is diff len\n" + fg.RESET,
            "columns" + fg.GREEN + "[" + str(len(columns)) + "]" + fg.RESET,
            " != ",
            "value_index" + fg.GREEN + "[" + str(len(value_index)) + "]" + fg.RESET,
            sep="",
        )
    new_df = df.copy(deep=True)
    for column_idx, column in enumerate(columns):
        for value_idx, value in enumerate(value_index[column_idx]):
            new_df[column] = new_df[column].replace(value, value_idx)
        try:
            new_df[column] = new_df[column].astype(float)
        except:
            print(fg.LRED + "some value is not catched" + fg.RESET)
            return df
    print(fg.LGREEN, "OK", sep="")
    return new_df
