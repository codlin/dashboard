
# build stage vue.js
FROM node:9.11.1-alpine as vue-build-stage
LABEL Name=dashboard-frontend Version=0.0.1

ENV REFRESHED_AT 2018-08-01
ENV http_proxy http://135.245.48.34:8000
ENV https_proxy http://135.245.48.34:8000

ENV NODE_ENV production

WORKDIR /app
RUN npm install
RUN npm run build

# Nginx
FROM nginx:1.13.12-alpine as production-stage
COPY --from=vue-build-stage /app/dist /usr/share/nginx/html
COPY nginx/conf/default.conf /etc/nginx/conf.d/
COPY nginx/conf/nginx.* /etc/ssl/
EXPOSE 80
EXPOSE 443

ENV http_proxy ""
ENV https_proxy ""

CMD ["nginx", "-g", "daemon off;"]
