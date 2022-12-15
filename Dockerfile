FROM python:3.8
USER root
RUN mkdir /app
COPY . /app/
WORKDIR  /app/
RUN ppip3 install -r requirements.txt
ENV AIRFLOW_HOME = "/app/airflow"
ENV AIRFLOW__CORE__ENABLE_IMPORT_TIMEOUT = 1000
ENV AIRFLOW__CORE__ENABLE_XCOM_PICKLING = True
RUN airflow db init
RUN airflow users create -e kashyapabhishek22@gmail.com -f Abhishek -l Kashyap -p admin -r Admin -u admin
RUN chmod 777 start.sh
RUN apt update -y && apt install awscli -y
ENTRYPOINT
CMD ["start.sh"]