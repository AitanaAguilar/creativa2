FROM python:3.9-slim

WORKDIR /opt/microservices

COPY bookinfo/src/productpage/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bookinfo/src/productpage/ .

ENV TEAM_ID=unknown
ENV APP_OWNER=unknown

EXPOSE 8080
CMD ["python", "productpage.py", "8080"]
