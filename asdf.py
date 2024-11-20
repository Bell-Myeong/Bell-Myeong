from hanspell import spell_checker

text = "서율 날씨 좋네요."
result = spell_checker.check(text)

# 교정된 텍스트 출력
print("교정된 텍스트:", result.checked)
