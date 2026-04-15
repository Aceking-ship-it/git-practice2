print("hello git")
print("Change 1")

properties = [
    {"지역": "강남", "유형": "아파트", "거래": "매매", "가격": "10억", "연도": "2010년"},
    {"지역": "마포", "유형": "오피스텔", "거래": "전세", "가격": "5억", "연도": "2007년"},
    {"지역": "송파", "유형": "빌라", "거래": "월세", "가격": "500/50", "연도": "2000년"}
]

# 총 매물 수 출력
print(f"총 {len(properties)}대의 매물이 있습니다.")

# 각 매물 출력
for p in properties:
    print(f"{p['지역']} {p['유형']} {p['거래']} {p['가격']} {p['연도']}")


import os
print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더 입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더는 생성하였습니다.")

print(os.listdir)