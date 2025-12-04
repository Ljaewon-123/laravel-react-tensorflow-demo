FROM python:3.10-slim

WORKDIR /app

# 필요한 라이브러리 설치
COPY ai/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY ai/ .

# uvicorn 으로 FastAPI 서버 실행
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]
