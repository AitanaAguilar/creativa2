FROM node:24-slim

WORKDIR /opt/microservices
COPY bookinfo/src/ratings/package.json /opt/microservices/
COPY bookinfo/src/ratings/ratings.js /opt/microservices/

ENV APP_VERSION=v1

RUN npm install --omit=dev

EXPOSE 9080
CMD ["node", "/opt/microservices/ratings.js", "9080"]
