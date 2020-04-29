#!/usr/bin/env python3
from pl_curve import check_columns
import pandas as pd


def test_check_columns_correct():
    '''
    Tests check_columns correctly checks items summing to 1.0 returns true
    '''

    df = pd.DataFrame([0.1, 0.9])
    assert check_columns(df)


def test_check_columns_incorrect():
    df = pd.DataFrame([0.1, 0.8])
    assert check_columns(df) is False
