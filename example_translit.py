def translit(text: str):
    return text.replace("іє", 'ie') \
        .replace("Іє", 'Ie') \
        .replace("ія", 'ia') \
        .replace("Ія", 'Ia') \
        .replace("зг", 'zgh') \
        .replace("Зг", 'Zgh') \
        .replace("ьо", 'io') \
        .replace("а", 'a') \
        .replace("б", 'b') \
        .replace("в", 'v') \
        .replace("г", 'h') \
        .replace("ґ", 'g') \
        .replace("д", 'd') \
        .replace("е", 'e') \
        .replace("є", 'ie') \
        .replace("ж", 'zh') \
        .replace("з", 'z') \
        .replace("и", 'y') \
        .replace("і", 'i') \
        .replace("ї", 'i') \
        .replace("й", 'i') \
        .replace("к", 'k') \
        .replace("л", 'l') \
        .replace("м", 'm') \
        .replace("н", 'n') \
        .replace("о", 'o') \
        .replace("п", 'p') \
        .replace("р", 'r') \
        .replace("с", 's') \
        .replace("т", 't') \
        .replace("у", 'u') \
        .replace("ф", 'f') \
        .replace("х", 'kh') \
        .replace("ц", 'ts') \
        .replace("ч", 'ch') \
        .replace("ш", 'sh') \
        .replace("щ", 'sch') \
        .replace("ь", '') \
        .replace("ю", 'iu') \
        .replace("я", 'ia') \
        .replace("А", 'A') \
        .replace("Б", 'B') \
        .replace("В", 'V') \
        .replace("Г", 'H') \
        .replace("Ґ", 'G') \
        .replace("Д", 'D') \
        .replace("Е", 'E') \
        .replace("Є", 'Ie') \
        .replace("Ж", 'Zh') \
        .replace("З", 'Z') \
        .replace("И", 'Y') \
        .replace("І", 'I') \
        .replace("Ї", 'I') \
        .replace("Й", 'I') \
        .replace("К", 'K') \
        .replace("Л", 'L') \
        .replace("М", 'M') \
        .replace("Н", 'N') \
        .replace("О", 'O') \
        .replace("П", 'P') \
        .replace("Р", 'R') \
        .replace("С", 'S') \
        .replace("Т", 'T') \
        .replace("У", 'U') \
        .replace("Ф", 'F') \
        .replace("Х", 'Kh') \
        .replace("Ц", 'Ts') \
        .replace("Ч", 'Ch') \
        .replace("Ш", 'Sh') \
        .replace("Щ", 'Sch') \
        .replace("Ь", '') \
        .replace("Ю", 'Iu') \
        .replace("Я", 'Ia')



if __name__ == '__main__':
    print(translit("Ірпінь"))

# function translit(input) {
#         input = input || '';
#
#         return input
#             .replace(/іє/g, 'ie') // Exception
#             .replace(/Іє/g, 'Ie') // Exception
#             .replace(/ія/g, 'ia') // Exception
#             .replace(/Ія/g, 'Ia') // Exception
#             .replace(/зг/g, 'zgh') // Exception
#             .replace(/Зг/g, 'Zgh') // Exception
#             .replace(/ьо/g, 'io') // Exception
#             .replace(/а/g, 'a')
#             .replace(/б/g, 'b')
#             .replace(/в/g, 'v')
#             .replace(/г/g, 'h')
#             .replace(/ґ/g, 'g')
#             .replace(/д/g, 'd')
#             .replace(/е/g, 'e')
#             .replace(/(^|\s)є/g, '$1ye')
#             .replace(/є/g, 'ie')
#             .replace(/ж/g, 'zh')
#             .replace(/з/g, 'z')
#             .replace(/и/g, 'y')
#             .replace(/і/g, 'i')
#             .replace(/(^|\s)ї/g, '$1yi')
#             .replace(/ї/g, 'i')
#             .replace(/(^|\s)й/g, '$1y')
#             .replace(/й/g, 'i')
#             .replace(/к/g, 'k')
#             .replace(/л/g, 'l')
#             .replace(/м/g, 'm')
#             .replace(/н/g, 'n')
#             .replace(/о/g, 'o')
#             .replace(/п/g, 'p')
#             .replace(/р/g, 'r')
#             .replace(/с/g, 's')
#             .replace(/т/g, 't')
#             .replace(/у/g, 'u')
#             .replace(/ф/g, 'f')
#             .replace(/х/g, 'kh')
#             .replace(/ц/g, 'ts')
#             .replace(/ч/g, 'ch')
#             .replace(/ш/g, 'sh')
#             .replace(/щ/g, 'sch')
#             .replace(/ь/g, '')
#             .replace(/(^|\s)ю/g, '$1yu')
#             .replace(/ю/g, 'iu')
#             .replace(/(^|\s)я/g, '$1ya')
#             .replace(/я/g, 'ia')
#             .replace(/А/g, 'A')
#             .replace(/Б/g, 'B')
#             .replace(/В/g, 'V')
#             .replace(/Г/g, 'H')
#             .replace(/Ґ/g, 'G')
#             .replace(/Д/g, 'D')
#             .replace(/Е/g, 'E')
#             .replace(/(^|\s)Є/g, '$1Ye')
#             .replace(/Є/g, 'Ie')
#             .replace(/Ж/g, 'Zh')
#             .replace(/З/g, 'Z')
#             .replace(/И/g, 'Y')
#             .replace(/І/g, 'I')
#             .replace(/(^|\s)Ї/g, '$1Yi')
#             .replace(/Ї/g, 'I')
#             .replace(/(^|\s)Й/g, '$1Y')
#             .replace(/Й/g, 'I')
#             .replace(/К/g, 'K')
#             .replace(/Л/g, 'L')
#             .replace(/М/g, 'M')
#             .replace(/Н/g, 'N')
#             .replace(/О/g, 'O')
#             .replace(/П/g, 'P')
#             .replace(/Р/g, 'R')
#             .replace(/С/g, 'S')
#             .replace(/Т/g, 'T')
#             .replace(/У/g, 'U')
#             .replace(/Ф/g, 'F')
#             .replace(/Х/g, 'Kh')
#             .replace(/Ц/g, 'Ts')
#             .replace(/Ч/g, 'Ch')
#             .replace(/Ш/g, 'Sh')
#             .replace(/Щ/g, 'Sch')
#             .replace(/Ь/g, '')
#             .replace(/(^|\s)Ю/g, '$1Yu')
#             .replace(/Ю/g, 'Iu')
#             .replace(/(^|\s)Я/g, '$1Ya')
#             .replace(/Я/g, 'Ia')
#             .replace(/'/g, '')
#             .replace(/’/g, '');
#     }
# });
#
