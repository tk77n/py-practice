# 文字列内に”ある文字列”があるかのインデックスを検索（find/rfindメソッド）
# 後ろの位置引数で検索開始インデックスと終了インデックスをかける
msg = "にわにはにわにわとりがいる"

print(msg.find("にわ"))
print(msg.rfind("にわ"))
print(msg.find("にも"))  # ないときは戻り値-1


# 探したい文字列がなかったときに例外を返す（index/rindexメソッド）
print(msg.index("にわ"))
print(msg.index("にも"))  # ValueError: substring not found


# 部分文字列の登場回数をカウントする（countメソッド）
print(msg.count("にわ"))
print(msg.count("にも"))  # なければ0
