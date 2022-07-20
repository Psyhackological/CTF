import re


def cezar(what, move):
    done = ""
    for char in what:
        ascii_num = ord(char)
        ascii_num += move
        while ascii_num > 126:
            ascii_num -= 95
        while ascii_num < 32:
            ascii_num += 95
        done += chr(ascii_num)

    return done


k1 = "/<V5;)j}j6\\<Y)8><\\9Fbu,Hy4ONC}pxP\"4st12wn`?@O$6BgQo7i#gtD|s>3lf="
k2 = "2m{y!\"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0."
k1_list = []
k2_list = []
for i in range(-100, 101):
    k1_list.append(f"{i} {cezar(k1, i)}")
    k2_list.append(f"{i} {cezar(k2, i)}")

pattern = "[A-Za-z]{3,}{{1}[^ ]{3,}}{1}"
matched = []
k1_match = re.findall(pattern, str(k1_list))
k2_match = re.findall(pattern, str(k2_list))

matched.append(k1_match)
matched.append(k2_match)

for m in matched:
    print(m)
