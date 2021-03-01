#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
txt="\x65"

txt = "最近都忙些啥?還有在上班嗎?"

x = txt.encode()

print(x)

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())


txt = "50800"

x = txt.isdigit()

print(x)

txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)

txt = "565543"

x = txt.isnumeric()

print(x)