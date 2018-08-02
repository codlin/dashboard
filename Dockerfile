
# build stage vue.js
FROM node:8.11.3
LABEL Name=dashboard-frontend Version=0.0.1

ENV http_proxy http://135.245.48.34:8000
ENV https_proxy http://135.245.48.34:8000

ENV NODE_ENV production

WORKDIR /app
COPY frontend/package*.json ./
COPY frontend .
RUN ls -l /app && npm install
RUN npm run build

# Nginx
FROM nginx:1.13.12-alpine as production-stage
COPY --from=0 /app/dist /usr/share/nginx/html
COPY nginx/conf/default.conf /etc/nginx/conf.d/
COPY nginx/conf/nginx.* /etc/ssl/
EXPOSE 80
EXPOSE 443

ENV http_proxy ""
ENV https_proxy ""
