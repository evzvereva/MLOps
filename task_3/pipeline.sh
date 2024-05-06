#!/bin/bash

# Инициализация переменной для хранения python-скриптов
scripts=('data_creation.py' 'model_preprocessing.py' 'model_preparation.py')

# Цикл для последовательного запуска python-скриптов
for script in "${scripts[@]}"; do
  echo "Запуск скрипта $script..."
  python $script
done