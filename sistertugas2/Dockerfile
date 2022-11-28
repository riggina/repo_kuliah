FROM node:latest

RUN mkdir -p /src/repo_kuliah/sistetugas2

WORKDIR /src/repo_kuliah/sistetugas2

COPY package.json .

RUN npm install

COPY . .

EXPOSE 4000

CMD ["npm", "start"]

