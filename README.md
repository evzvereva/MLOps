## Практические задания MLOps

<details><summary><b>task_1</b></summary>

Цель: из "подручных средств" создать простейший конвейер для автоматизации работы с моделью машинного обучения. Отдельные этапы конвейера машинного обучения описываются в разных python-скриптах, которые потом соединяются с помощью bash-скрипта.

Для удобства развертывания иммется файл "requirements.txt", содержащий перечень необходимых пактов, подлежащих установке.

Установка необходимых пакетов осуществляется из корневого каталога "MLOps_one_task/" командой в терминале ```pip install -r requirements.txt```.

Этапы контейнера для автоматизации работы с моделью машинного обучения:
1. data_creation.py позволяет создать случайный набор данных пациентов с их показателями. В результаты данные разделены на тестовую и обучающую выборку, сохраняются файлы в директории train и test.
    - в качестве целевой переменной выбран признак "status" - где 0 - не выжил пациент, 1 - выжил
    - остальные признаки: пульс, давление, температура, возраст и id пациента
    - добавлены шумы в признаки: temperature и pressure
2. model_preprocessing.py выполняет предобработку данных с помощью sklearn.preprocessing.StandardScaler.
3. model_preparation.py создает и обучает модель машинного обучения RandomForestClassifier на построенных данных из папки «train».
4. model_testing.py проверяет модель машинного обучения на построенных данных из папки «test».
5. pipeline.sh последовательно запускает все python-скрипты. Для запуска введите команду в терминале из корневого каталога ```./task_1/pipeline.sh```.

Результаты на обучающей выборке:
```
Accuracy: 0.9833333333333333
Classification Report:
               precision    recall  f1-score   support

           0       0.98      0.99      0.99       243
           1       0.99      0.97      0.98       177

    accuracy                           0.98       420
   macro avg       0.98      0.98      0.98       420
weighted avg       0.98      0.98      0.98       420
```

Результаты на тестовой выборке:
```
Accuracy: 0.9688888888888889
Classification Report:
               precision    recall  f1-score   support

           0       0.96      0.98      0.97       511
           1       0.98      0.95      0.96       389

    accuracy                           0.97       900
   macro avg       0.97      0.97      0.97       900
weighted avg       0.97      0.97      0.97       900
```
</details>

<details><summary><b>task_2</b></summary>

Этапы контейнера для автоматизации работы с моделью машинного обучения:
1. data_creation.py позволяет создать случайный набор данных пациентов с их показателями. В результаты данные разделены на тестовую и обучающую выборку, сохраняются файлы в директории train и test.
    - в качестве целевой переменной выбран признак "status" - где 0 - не выжил пациент, 1 - выжил
    - остальные признаки: пульс, давление, температура, возраст и id пациента
    - добавлены шумы в признаки: temperature и pressure
2. model_preprocessing.py выполняет предобработку данных с помощью sklearn.preprocessing.StandardScaler.
3. model_preparation.py создает и обучает модель машинного обучения RandomForestClassifier на построенных данных из папки «train».
4. model_testing.py проверяет модель машинного обучения на построенных данных из папки «test».
5. Jenkinsfile позволяет позволяет автоматически создать процесс сборки pipeline. На этом этапе производится создание виртуального окружения, его активация, установка зависимостей, запуск скриптов python пункты 1-4.
</details>

<details><summary><b>task_3</b></summary>

Этапы контейнера для автоматизации работы с моделью машинного обучения:
1. data_creation.py позволяет создать случайный набор данных пациентов с их показателями. В результаты данные разделены на тестовую и обучающую выборку, сохраняются файлы в директории train и test.
    - в качестве целевой переменной выбран признак "status" - где 0 - не выжил пациент, 1 - выжил
    - остальные признаки: пульс, давление, температура, возраст и id пациента
    - добавлены шумы в признаки: temperature и pressure
2. model_preprocessing.py выполняет предобработку данных с помощью sklearn.preprocessing.StandardScaler.
3. model_preparation.py создает и обучает модель машинного обучения RandomForestClassifier на построенных данных из папки «train».
4. model_testing.py проверяет модель машинного обучения на построенных данных из папки «test».
5. pipeline.sh последовательно запускает все python-скрипты. Для запуска введите команду в терминале из корневого каталога.
6. model_testing.py позволяет пользователю загрузить файл .csv c тестовыми данными через веб-приложение Streamlit и получить прогноз.

В Dockerfile содержится описание процесса создания образа Docker для запуска приложения на Streamlit, используя Python 3.12.2 в минимальной версии образа (python:3.12.2-slim).
docker-compose.yml описывает конфигурацию для запуска сервиса с использованием Docker Compose.

Для сборки и запуска понадобится выполнить команды находясь в директории /task_3:
```commandline
docker-compose build
docker-compose up
```
Или из [репозитория](https://hub.docker.com/r/evzvereva/task_3) hub.docker.com выполнить команду:
```commandline
docker pull evzvereva/task_3
```
</details>

<details><summary><b>task_4</b></summary>

В директории datasets:
1. titanic.py позволяет получить данные о пассажирах «Титаника» и сохранить в файл titanic.csv.
2. update_nan_age_titanic.py создает новую версию датасета, в котором пропущенные (nan) значения в поле "Age" будут заполнены средним значением.
3. one_hot_encod_sex_titanic.py создает новый признак "Sex_enc" с использованием one-hot-encoding для строкового признака "Пол" (“Sex”)
4. Техническая информация:
   - Коммиты:
   ```
   (.venv) evzvereva@Ubuntu:~/PycharmProjects/MLOps$ git log --oneline
   7b40171 (HEAD -> task_4) Update task_4/datasets.dvc
   cf27d54 Add new column "Sex_enc"
   753986a Update git add task_4/datasets.dvc
   bc95a22 Add replace value nan in column "Age" on mean
   e92fb1a Google Disk was added as remote datasets folder
   a6d7e7c Put datasets under control
   75d2028 Add load data titanic
   16b9e1d Init dvc
   ```
   - Переключение между версиями и сохранение изменений на примере следующего коммита
   ```
   git checkout bc95a22
   dvc pull -r datasets  
   ```
   - Возвращение к актуальной версии:
   ```
   git checkout task_4
   dvc pull -r datasets
   ```
</details>