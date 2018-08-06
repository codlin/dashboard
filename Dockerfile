
# build stage vue.js
FROM node:8.11.3
LABEL Name=dashboard-frontend Version=0.0.1

ENV REFRESHED_AT 2018-08-01
ENV http_proxy http://135.245.48.34:8000
ENV https_proxy http://135.245.48.34:8000

ENV NODE_ENV development

WORKDIR /app
COPY frontend/package.json ./
RUN rm -rf node_modules && npm install --save
COPY frontend ./
RUN npm run build

# Nginx
FROM nginx:1.13.12-alpine
COPY --from=0 /app/dist /usr/share/nginx/html
COPY nginx/conf/default.conf /etc/nginx/conf.d/
COPY nginx/conf/nginx.* /etc/ssl/
EXPOSE 80
EXPOSE 443

ENV http_proxy ""
ENV https_proxy ""
