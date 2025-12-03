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

print(f"훈련 데이터: {len(x_train)}개")
print(f"테스트 데이터: {len(x_test)}개")
print(f"첫 번째 리뷰 길이: {len(x_train[0])}단어")
print(f"첫 번째 리뷰 레이블: {'긍정' if y_train[0] == 1 else '부정'}")

# ==================== 2. 데이터 전처리 ====================
print("\n[2단계] 데이터 전처리 중...")

# 패딩: 모든 리뷰를 같은 길이로 맞춤
x_train = keras.preprocessing.sequence.pad_sequences(
    x_train, 
    maxlen=MAX_LENGTH,
    padding='post',      # 뒤에 0 추가
    truncating='post'    # 길면 뒤에서 자르기
)

x_test = keras.preprocessing.sequence.pad_sequences(
    x_test,
    maxlen=MAX_LENGTH,
    padding='post',
    truncating='post'
)

print(f"전처리 후 shape: {x_train.shape}")

# ==================== 3. 모델 구축 ====================
print("\n[3단계] 모델 구축 중...")

model = keras.Sequential([
    # Embedding: 단어 ID → 벡터로 변환
    keras.layers.Embedding(
        input_dim=VOCAB_SIZE,
        output_dim=EMBEDDING_DIM,
        input_length=MAX_LENGTH,
        name='embedding'
    ),
    
    # GlobalAveragePooling: 모든 단어 벡터의 평균
    keras.layers.GlobalAveragePooling1D(name='pooling'),
    
    # Dense: 패턴 학습
    keras.layers.Dense(16, activation='relu', name='hidden'),
    
    # Dropout: 과적합 방지
    keras.layers.Dropout(0.5, name='dropout'),
    
    # 출력층: 0(부정) ~ 1(긍정)
    keras.layers.Dense(1, activation='sigmoid', name='output')
], name='sentiment_model')

# 모델 컴파일
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 모델 구조 출력
model.summary()

# ==================== 4. 모델 학습 ====================
print("\n[4단계] 모델 학습 시작...")

history = model.fit(
    x_train, y_train,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    validation_split=0.2,  # 훈련 데이터의 20%를 검증용으로
    verbose=1
)

# ==================== 5. 모델 평가 ====================
print("\n[5단계] 모델 평가 중...")

test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"\n테스트 정확도: {test_accuracy*100:.2f}%")
print(f"테스트 손실: {test_loss:.4f}")

# ==================== 6. 모델 저장 ====================
print("\n[6단계] 모델 저장 중...")

# 모델 저장
model.save('sentiment_model.h5')
print("✓ 모델 저장 완료: sentiment_model.h5")

# 단어 인덱스 저장 (나중에 예측할 때 필요)
word_index = keras.datasets.imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# 처음 100개 단어만 저장 (전체는 너무 큼)
word_dict = {k: v for k, v in list(word_index.items())[:100]}
with open('word_index.json', 'w', encoding='utf-8') as f:
    json.dump(word_dict, f, ensure_ascii=False, indent=2)
print("✓ 단어 사전 저장 완료: word_index.json")

# ==================== 7. 예측 테스트 ====================
print("\n[7단계] 예측 테스트...")

def decode_review(encoded_review):
    """숫자로 된 리뷰를 원래 텍스트로 변환"""
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

def predict_sentiment(model, review_text, word_index):
    """새로운 리뷰의 감정 예측"""
    # 텍스트를 숫자로 변환
    words = review_text.lower().split()
    encoded = [word_index.get(word, 0) + 3 for word in words]
    
    # 패딩
    padded = keras.preprocessing.sequence.pad_sequences(
        [encoded], 
        maxlen=MAX_LENGTH,
        padding='post'
    )
    
    # 예측
    prediction = model.predict(padded, verbose=0)[0][0]
    
    return prediction

# 테스트 리뷰 몇 개 예측해보기
test_indices = [0, 100, 200]
print("\n" + "="*60)
print("샘플 예측 결과:")
print("="*60)

for idx in test_indices:
    review = decode_review(x_test[idx])
    actual = "긍정" if y_test[idx] == 1 else "부정"
    
    prediction = model.predict(x_test[idx:idx+1], verbose=0)[0][0]
    predicted = "긍정" if prediction > 0.5 else "부정"
    
    print(f"\n리뷰 #{idx}")
    print(f"내용: {review[:100]}...")
    print(f"실제: {actual} | 예측: {predicted} (확률: {prediction:.2%})")
    print(f"{'✓ 정답' if actual == predicted else '✗ 오답'}")

# ==================== 8. 학습 곡선 시각화 준비 ====================
print("\n[8단계] 학습 결과 요약...")

print("\n에포크별 정확도:")
for epoch, (train_acc, val_acc) in enumerate(zip(
    history.history['accuracy'], 
    history.history['val_accuracy']
), 1):
    print(f"Epoch {epoch:2d}: 훈련 {train_acc:.4f} | 검증 {val_acc:.4f}")

print("\n" + "="*60)
print("학습 완료! 🎉")
print("="*60)
print(f"최종 테스트 정확도: {test_accuracy*100:.2f}%")
print(f"저장된 파일:")
print(f"  - sentiment_model.h5 (모델)")
print(f"  - word_index.json (단어 사전)")
print("\n다음 단계: 이 모델을 웹 서비스로 만들어보세요!")

