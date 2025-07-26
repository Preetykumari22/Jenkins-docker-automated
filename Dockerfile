FROM redhat/ubi8
RUN dnf install python3 -y
RUN pip3 install flask
COPY sms.py /sms.py
CMD ["python3", "/sms.py"]
