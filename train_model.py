# 감정 분석 모델 - IMDB 영화 리뷰
# 필요한 라이브러리: pip install tensorflow numpy

import tensorflow as tf
from tensorflow import keras
import numpy as np
import json

print("TensorFlow 버전:", tf.__version__)

# ==================== 설정 ====================
VOCAB_SIZE = 10000      # 사용할 단어 개수
MAX_LENGTH = 200        # 리뷰 최대 길이
EMBEDDING_DIM = 16      # 단어 벡터 차원
EPOCHS = 10             # 학습 반복 횟수
BATCH_SIZE = 512        # 배치 크기

# ==================== 1. 데이터 로드 ====================
print("\n[1단계] 데이터 로딩 중...")
(x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(
    num_words=VOCAB_SIZE
)

