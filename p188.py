# 文字列の部分取得（スライス構文[開始：終了：ステップ]）

title = "あいうえおかきくけこ"

print(title[2])
print(title[2:5])
print(title[2:])
print(title[:5])
print(title)
print(title[:])  # titleそのまんまと同じ
print(title[::2])
print(title[-1])  # 最後から取得したいときは－１から
