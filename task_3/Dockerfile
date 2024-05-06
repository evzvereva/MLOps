FROM python:3.12.2-slim

COPY . /app

WORKDIR /app

EXPOSE 8501

RUN pip install -r requirements.txt
RUN /bin/bash -c '/app/pipeline.sh'

CMD ["streamlit", "run", "streamlit.py", "--host", "172.17.0.6", "--port", "8501"]
