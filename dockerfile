FROM cypress/browsers:node-22.17.1-chrome-138.0.7204.157-1-ff-140.0.4-edge-138.0.3351.83-1
WORKDIR /e2e
COPY package.json package-lock.json* ./
RUN npm ci
COPY . .
ENTRYPOINT ["npx", "cypress", "run"]