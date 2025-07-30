import csv
import os
from typing import Optional
from app.config import Config
from app.exceptions import (
    NoDataAvailableError,
    TooMuchDataError,
    WordLengthError
)


def get_basic_words_path(filename: str = 'basic_words.csv') -> Optional[str]:
    current_path = os.path.dirname(__file__)
    root_path = os.path.dirname(current_path)
    root_path_listdir = os.listdir(root_path)
    try:
        if filename not in root_path_listdir:
            raise NoDataAvailableError(
                f'Файл {filename} отсутствует '
                f'в выбранной директории "{root_path}"'
            )
    except NoDataAvailableError as e:
        print(f'Возникла ошибка: {e}')
    else:
        basic_words_path = os.path.join(root_path, filename)
        return basic_words_path


def basic_words_parser(path: str) -> Optional[list]:
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        basic_words_list = list(reader)
        try:
            for row in basic_words_list:
                if ('' in row) or (len(row) < 2):
                    raise NoDataAvailableError(
                        f'Отсутствует одно или оба слова {row}'
                    )
                elif len(row) > 2:
                    raise TooMuchDataError(
                        f'Найдены лишние слова {row}'
                    )
                elif len(row[0]) > 50 or len(row[1]) > 50:
                    raise WordLengthError(
                        f'Одно из слов больше допустимой длины в 50 символов'
                    )
        except NoDataAvailableError as e:
            print(
                f'Возникла ошибка в строке '
                f'{basic_words_list.index(row) + 1}: {e}'
            )
        except TooMuchDataError as e:
            print(
                f'Возникла ошибка в строке '
                f'{basic_words_list.index(row) + 1}: {e}'
            )
        except WordLengthError as e:
            print(
                f'Возникла ошибка в строке '
                f'{basic_words_list.index(row) + 1}: {e}'
            )
        else:
            return basic_words_list[1::]
