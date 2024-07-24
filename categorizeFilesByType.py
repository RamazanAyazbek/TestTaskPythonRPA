# Привет.
import os
from pathlib import Path
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

root_path = str(Path(__file__).resolve().parents[1])


def categorize_files_by_type(root_path: str) -> dict:
    dict1 = {}
    try:
        logging.info(f"Начинаем категоризацию корневого пути: {root_path}")

        if not os.path.exists(root_path):
            raise FileNotFoundError(f"Путь '{root_path}' не существует.")
        if not os.path.isdir(root_path):
            raise NotADirectoryError(f"Путь '{root_path}' не является каталогом.")

        for root, dirs, files in os.walk(root_path):
            logging.info(f"В процессе каталог: {root}")
            for file in files:
                # Проверка наличия расширения у файла
                if file.rfind('.') != -1:
                    # Извлечение расширения файла (включая точку)
                    extend = file[file.rfind('.'):]
                else:
                    # Если у файла нет расширения, используем пустую строку
                    extend = ''
                key = extend  # Ключом будет расширение файла
                value = os.path.join(root, file)  # Полный путь к файлу
                # Добавление пути к файлу в словарь по ключу (расширению)
                dict1.setdefault(key, []).append(value)

                # Логирование процесса добавления файла в словарь
                logging.debug(f"Добавлен файл: {value} ключ: {key}")

        logging.info("Классификация завершена. Подготовка вывода.")
        
        
        # возвращать результат функции на формате словарь
        return dict1

        # Компактно вывести на консоль (здесь возвращает на формате str)
        # return json.dumps(dict1, indent=4, ensure_ascii=False)

    except (FileNotFoundError, NotADirectoryError) as e:
        logging.error(f"Возникла ошибка: {e}")
        return str(e)
    except Exception as e:
        logging.error(f"Неизвестная ошибка: {e}")
        return f"Неизвестная ошибка: {e}"



print(categorize_files_by_type(root_path))




