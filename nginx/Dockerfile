# Nginx
FROM nginx:1.13.12-alpine as production-stage

ENV REFRESHED_AT 2018-08-01
ENV http_proxy http://135.245.48.34:8000
ENV https_proxy http://135.245.48.34:8000

RUN rm /etc/nginx/conf.d/default.conf
COPY conf/default.conf /etc/nginx/conf.d/
COPY conf/nginx.* /etc/ssl/
EXPOSE 80
EXPOSE 443

ENV http_proxy ""
ENV https_proxy ""

CMD ["nginx", "-g", "daemon off;"]
