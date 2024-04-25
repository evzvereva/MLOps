#!/bin/bash

# Инициализация переменной для хранения python-скриптов
scripts=('task_1/data_creation.py' 'task_1/model_preprocessing.py' 'task_1/model_preparation.py' 'task_1/model_testing.py')

# Цикл для последовательного запуска python-скриптов
for script in "${scripts[@]}"; do
  echo "Запуск скрипта $script..."
  python $script
done