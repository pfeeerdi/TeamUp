# Stage 1
# FROM node:10-alpine as build-step
# RUN mkdir -p /app
# WORKDIR /app
# COPY package.json /app
# RUN npm install
# COPY . /app
# RUN npm run build --prod --localize

# Stage 2
FROM nginx:1.17.1-alpine
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-step /dist /usr/share/nginx/html/

# docker build -t frontend .
# docker run -p 80:80 frontend
# docker login registry.gitlab.com/Ronho1/coin-2-gether -u [gitlab_username] -p [gitlab_token]
# docker build -t registry.gitlab.com/ronho1/coin-2-gether/frontend .
# docker push registry.gitlab.com/ronho1/coin-2-gether/frontend