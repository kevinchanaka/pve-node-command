FROM python:3.9-slim
COPY requirements.txt /app/
WORKDIR /app
RUN addgroup --gid 1000 app-user && \
    adduser --system --uid 1000 --gid 1000 app-user && \
    pip install -r requirements.txt 
USER app-user
COPY --chown=app-user script.py /app/

ENV API_HOST="" \
    NODE_NAME="" \
    TOKEN_USER="" \
    TOKEN_NAME="" \
    TOKEN_VALUE="" \
    COMMAND=shutdown

CMD python script.py