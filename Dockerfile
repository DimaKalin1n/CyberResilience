FROM python
COPY ./info.txt /CYBERRESILIENCE/info.txt
WORKDIR /CYBERRESILIENCE
RUN pip install -r info.txt
COPY . /CYBERRESILIENCE
ENTRYPOINT ["python"]
CMD ["main.py"]
