# name=input("enter your name:")
# print(f"Good afternoon Mr. {name}")

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","nishanth").replace("<|Date|>","January 31 2025"))

greeting="Hello good morning  guys"
print(greeting.find('  '))
print(greeting.replace("  "," "))
