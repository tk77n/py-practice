# 文字列の種類判定（英語、数字、空白など）真偽値を返す
s1 = "abc123"

print(s1.isalnum())  # 英語alと数字numでalnum
# 広く数字を認めたいならisnumericが使える


# 全角数字や漢数字を半角数字に⇒unicodedataモジュールのdigit/numeric関数
import unicodedata

print(unicodedata.digit("５"))  # int型5にする
print(unicodedata.digit("５"))  # float型5にする
print(unicodedata.numeric("五"))  # 漢数字行ける
print(unicodedata.numeric("五"))  # 漢数字行ける


# 識別子が予約済みかを確認（str.isidentifier()かkeywordモジュールのiskeyword関数）
import keyword

id1 = "tiff"
id2 = "if-else"
id3 = "if"
id4 = "id1"

print(id1.isidentifier())  # 変数名とか関数名として使っていいのかを判断できる
print(id2.isidentifier())  # false
print(keyword.iskeyword(id1))
print(keyword.iskeyword(id3))
print(keyword.iskeyword(id4))  # id1は使ってるからfalseになる
