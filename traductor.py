# hoy vamos a hacer un traductor en python con visual studio code

from translate import Translator

translator = Translator(from_lang='spanish', to_lang='english')

txt = input('que deceas traducir? ')

res = translator.translate(txt)

print(res)