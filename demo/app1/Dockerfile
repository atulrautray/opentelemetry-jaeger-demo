FROM python:3.7-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN opentelemetry-bootstrap -a install
EXPOSE 5000
CMD ["opentelemetry-instrument", "--traces_exporter", "otlp_proto_grpc", "--metrics_exporter", "none","--service_name", "app1","--exporter_otlp_endpoint", "jaeger:4317", "--exporter_otlp_insecure", "true", "python", "app1.py"]