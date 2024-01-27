#!/usr/bin/env python
# coding: utf-8

from .base_setting import *
from .font_style import *

def show_distplot(df: pandas.core.frame.DataFrame, cols: list[str], size: int = 3, x_size: int = 20, y_size: int = 20):
    if size < 1:
        return
    
    row_size = len(cols) // size + int(len(cols) / size > len(cols) // size)
    fig, axes = plt.subplots(nrows=row_size, ncols=size, figsize=(x_size, y_size))

    if row_size == 1:
        for i, column in enumerate(cols):
            col = i % size
            sns.distplot(df[column], ax=axes[col])
            sns.distplot(df[column], ax=axes[col])
    else:
        for i, column in enumerate(cols):
            row = i // size
            col = i % size
            sns.distplot(df[column], ax=axes[row][col])
            sns.distplot(df[column], ax=axes[row][col])

def show_boxplot(
    df: pandas.core.frame.DataFrame,
    cols: list[str],
    size: int = 3,
    x: str = "",
    hue: str = "",
    x_size: int = 20,
    y_size: int = 20,
):
    if size < 1:
        return
    row_size = len(cols) // size + int(len(cols) / size > len(cols) // size)
    fig, axes = plt.subplots(nrows=row_size, ncols=size, figsize=(x_size, y_size))

    if row_size == 1:
        for i, column in enumerate(cols):
            col = i % size
            sns.boxplot(df, x=x, y=column, hue=hue, ax=axes[col])
    else:
        for i, column in enumerate(cols):
            row = i // size
            col = i % size
            sns.boxplot(df, x=x, y=column, hue=hue, ax=axes[row][col])

def show_countplot(
    df: pandas.core.frame.DataFrame,
    cols: list[str],
    size: int = 3,
    hue: str = "",
    x_size: int = 20,
    y_size: int = 20,
):
    if size < 1:
        return
    row_size = len(cols) // size + int(len(cols) / size > len(cols) // size)
    fig, axes = plt.subplots(nrows=row_size, ncols=size, figsize=(x_size, y_size))

    if row_size == 1:
        for i, column in enumerate(cols):
            col = i % size
            sns.countplot(df, x=column, hue=hue, ax=axes[col])
    else:
        for i, column in enumerate(cols):
            row = i // size
            col = i % size
            sns.countplot(df, x=column, hue=hue, ax=axes[row][col])