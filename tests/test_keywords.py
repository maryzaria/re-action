import pandas as pd
import pytest

from main import find_sentence_with_key_word


df = pd.read_csv(f"../vacancies_with_code_word.csv")


@pytest.mark.parametrize("input_data, expected", [*zip(df['sentence'], df['key_word'])])
def test_1(input_data, expected):
    result = find_sentence_with_key_word(input_data)
    assert result == expected