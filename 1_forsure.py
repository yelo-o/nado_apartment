# 1. 라이브러리 임포트하기
import PublicDataReader as pdr
print(pdr.__version__)

# 2. 공공데이터 포털 OpenAPI 인증키 복사하기
serviceKey = "9ecpeezQSUTszUGp2DXRz0XXvI%2F9M9Mur9w37hx5SxnF4Mp4KU7AKD58GPNKC27p3VliAviyX6ofK3%2FAnVz17A%3D%3D"
# serviceKey = "9ecpeezQSUTszUGp2DXRz0XXvI/9M9Mur9w37hx5SxnF4Mp4KU7AKD58GPNKC27p3VliAviyX6ofK3/AnVz17A=="

# 3. 국토교통부 실거래가 정보 조회 OpenAPI 세션 정의하기
# debug: True이면 모든 메시지 출력, False이면 오류 메시지만 출력 (기본값: False)
ts = pdr.Transaction(serviceKey, debug=True)
# print(ts)

# https://www.youtube.com/watch?v=31EX6TLao5g
#https://pypi.org/project/PublicDataReader/