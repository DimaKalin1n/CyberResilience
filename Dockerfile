FROM python
COPY ./requirements.txt /CYBERRESILIENCE/requirements.txt
WORKDIR /CYBERRESILIENCE
RUN pip install -r requirements.txt
COPY . /CYBERRESILIENCE
ENTRYPOINT ["python"]
CMD ["main.py"]
