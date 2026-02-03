FROM ruby:2.7.1-slim

WORKDIR /opt/microservices
COPY bookinfo/src/details/details.rb /opt/microservices/details.rb

ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

EXPOSE 7070
CMD ["ruby", "/opt/microservices/details.rb", "7070"]
