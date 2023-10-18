#pip3 install translate

#don't keep your file name as translate.py
#bullshit error for some reason

from translate import Translator
t = Translator(to_lang="hi")
translation = t.translate("Hey there my name is")
print(translation)
