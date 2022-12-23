from collections import Counter
import sys


def write_binary(text):
    s_result = ''
    a_1 = ''
    for i in range(len(text)):
        a_1 += text[i]
        if (i + 1) % 8 == 0:
            s_result += ''.join(int(a_1, 2).to_bytes(1, "big"))
            a_1 = ''
        elif (i + 1) == len(text):
            s_result += ''.join(int(a_1, 2).to_bytes(1, "big"))
    return s_result


def encode(input_file, output_file):
    s_bin = ''
    outp = open(f'{output_file}', 'w', encoding='UTF-8')
    inp = open(f'{input_file}', 'r', encoding='UTF-8')

    def dict(string):  # Создаем закодированный словарь из строки

        arr = Counter(string)  # Создаем словарь из строки
        vertexes = [[el, arr[el], [], []] for el in arr]

        while len(vertexes) > 1:
            vertexes.sort(key=lambda x: x[1])
            x1 = vertexes.pop(0)
            x2 = vertexes.pop(0)
            new = [x1[0] + x2[0], x1[1] + x2[1], x1, x2]
            vertexes.append(new)

        codes = {}

        def search(paht, vertex):
            if len(vertex[2]) > 1:
                search(paht + "0", vertex[2])

            if len(vertex[3]) > 0:
                search(paht + "1", vertex[3])

            else:
                codes[vertex[0]] = paht
                return

        search("", vertexes[0])
        return codes

    text =
    a_1 = ' '
    while a_1 != '':
        a_1 = inp.readline()
        text += a_1

    codes_n = dict(text)

    len_codes_b = len(codes_n)
    outp.write(str(len_codes_b).encode("UTF-8"))

    for i in text:
        s_bin += codes_n.get(i)  # Пробегаем по строке и кодируем ее

    for i in codes_n:
        if i == '\n':
            outp.write(i+' '.encode("UTF-8"))
            outp.write(int(str(codes_n.get(i)), 2).to_bytes(1, "big"))
            outp.write("\n".encode("UTF-8"))
        else:
            outp.write((i+' ').encode("UTF-8"))
            outp.write(int(str(codes_n.get(i)), 2).to_bytes(1, "big"))
            outp.write("\n".encode("UTF-8"))
    a = write_binary(s_bin)
    outp.write(a)  # Записываем в файл закодированную строку

    inp.close()
    outp.close()


def decode(input_file, output_file):
    inp = open(f'{input_file}', 'r')
    outp = open(f'{output_file}', 'wb')

    codes = {}
    string_row = ''
    row = inp.readline()
    len_codes = int(row)
    str_result = ''
    string_result = ''
    s = ''
    for i in range(len_codes):  # Записываем словарь для декодирования
        row = inp.readline()
        if row[0] == ' ':
            row = row.split()[0]
            codes.update({row: ' '})
        elif row[:2] == '/n':
            row = row.split()
            codes.update({row[1]: '\n'})
        else:
            a, b = map(str, row.split())
            codes.update({b: a})

    len_last = 0
    a_1 = ' '
    string_row = ''
    while a_1 != '':
        a_1 = inp.readline()
        string_row += a_1
    outp.write()
    array_row = []
    '''for i in range(len(string_row)-1):
        a_2 += string_row[i]
        if string_row[i+1] == ' ':
            array_row.append(a_2)
            a_2 = ''
        elif string_row[i+1] != ' ':
            pass'''
    ''' for ii in range(len(string_row)): # Проходимся по строке и декодируем ее в бинарник
        try:
            row_s = str(bin(ord(string_row[ii])))[2:]
        except:pass
        if ii == len(string_row)-1:
            len_last = int(string_row[ii][:1])
            row_s = str(bin(ord(string_row[ii][1:])))[2:]
            if len(row_s) != len_last and len_last != 0:
                    row_s = row_s[::-1]
                    for i in range(len_last-len(row_s)):
                        row_s += '0'
                    row_s = row_s[::-1]
            str_result += row_s
        elif len(row_s)%8 != 0:
            row_s = row_s[::-1]
            for i in range(8-len(row_s)):
                row_s += '0'
            row_s = row_s[::-1]
            str_result += row_s
        else:
            str_result += row_s
    for ii in str_result: # Проходимся по строке и декодируем ее
        s += ii
        if s in codes:
            string_result += codes.get(s)
            s = ''
    outp.write(string_result) # Записываем в файл декодированную строку
    '''
    outp.close()


encode('r.txt', '2.txt')
# decode('2.txt','3.txt')


'''if len(sys.argv) < 4:
    raise "Not enough arguments"
else:
    method = sys.argv[1]
    in_path = sys.argv[2]
    out_path = sys.argv[3]
if method == '--encode':
    encode(in_path,out_path)
elif method == '--decode':
    decode(in_path,out_path)'''
