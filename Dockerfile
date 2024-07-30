FROM python
EXPOSE 5432/tcp
ADD . .
RUN python3 -m pip install -r requirements.txt
CMD ["fastapi", "dev", "--host", "0.0.0.0", "--port", "5432", "main.py"]

