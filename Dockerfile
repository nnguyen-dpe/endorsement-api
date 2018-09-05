FROM amaysim/serverless:1.27.1

WORKDIR /opt/app
RUN git clone https://github.com/nnguyen-dpe/endorsement-api.git
RUN cd endorsement-api && \
    pwd && \
    npm i --save-dev serverless-wsgi serverless-python-requirements serverless-offline && \
    pip3 install virtualenv && \
    virtualenv venv --python=python3 && \
    source venv/bin/activate && \
    pip install -r requirements.txt && \
    chmod a+x run.sh

EXPOSE 5000
ENTRYPOINT ["node"]
