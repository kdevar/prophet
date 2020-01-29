FROM safakcirag/fbprophet:latest

WORKDIR /app/src

COPY ./src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./

