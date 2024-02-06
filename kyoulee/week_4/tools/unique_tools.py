#!/usr/bin/env python
# coding: utf-8

from .base_setting import *
from .font_style import *

def show_unique(df: pandas.core.frame.DataFrame):
    """
    ### param
    df: pandas.core.frame.DataFrame
    data: str = ""
    ### return
    None
    ### brief
    데이터 프레임의 유니크 벨류를 보는 함수
    """
    print(fg.LMAGENTA, "🚀 unique values" + fg.RESET, sep="")
    for column in df.columns:
        print(
            fg.LYELLOW + df[column].name,
            fg.GREEN + " [" + str(df[column].nunique()) + "]",
            fg.LBLUE + "{" + str(df[column].dtype) + "}" ,
            fg.RESET,
            " : ",
            sorted(df[column].unique()),
            sep="",
        )
    print(fg.LGREEN, "OK", sep="")