import PublicDataReader as pdr

# 기본 정보 : 서비스키, 작동 확인
serviceKey = "9ecpeezQSUTszUGp2DXRz0XXvI%2F9M9Mur9w37hx5SxnF4Mp4KU7AKD58GPNKC27p3VliAviyX6ofK3%2FAnVz17A%3D%3D"
ts = pdr.Transaction(serviceKey, debug=True)

# 지역, 월별 데이터 프레임 만들기
prod = "아파트"
trans = "매매"
sigunguCode = "41135"
yearMonth = "202110"

df = ts.read_data(prod, trans, sigunguCode, yearMonth)
df.to_excel('result_202110.xlsx')