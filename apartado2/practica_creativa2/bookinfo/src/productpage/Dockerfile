FROM python:3.9-slim

WORKDIR /opt/productpage

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
 && pip install --no-cache-dir --no-deps -r requirements.txt \
 && pip install --no-cache-dir Flask-Bootstrap==3.3.7.1

COPY . .

EXPOSE 8080
CMD ["python", "productpage_monolith.py", "8080"]
