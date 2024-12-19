FROM node:20
WORKDIR /app_frontend/frontend

COPY /frontend_Project/docker/node/package.json /app_frontend/frontend/package.json
RUN npm install

COPY /frontend_Project/frontend/src /app_frontend/frontend/src/
COPY /frontend_Project/frontend/public /app_frontend/frontend/public/

CMD ["npm", "start"]


