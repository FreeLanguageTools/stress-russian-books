# coding=utf-8
import spacy

from russian_dictionary import RussianDictionary

nlp = spacy.load('ru_core_news_sm')
string = "Твои слова ничего не значат."
#string = "Шарик улетел от Максима."
#string = "Он говорил о дворе"

test = """
Эшонай всегда говорила сестре, что за следующим холмом, несомненно, ждет нечто чудесное. И вот настал день, когда Эшонай взошла на холм и обнаружила… человеков.
Она воображала себе человеков темными, бесформенными чудовищами, какими те представали в песнях. Они же оказались поразительными, причудливыми созданиями. В их речах не было различимого ритма. Их одежда была ярче панциря, но вот отращивать собственную броню они не умели. А еще так боялись бурь, что даже во время путешествий прятались внутри повозок.
Самое же примечательное — у них была всего одна форма.
Сперва она предположила, что человеки, должно быть, забыли свои формы, в точности как слушатели когда-то. Благодаря этому они мгновенно подружились.
Теперь, больше года спустя, Эшонай помогала разгружать барабаны с телеги, напевая в ритме благоговения. Слушатели преодолели большое расстояние, чтобы увидеть родину человеков, и с каждым шагом ее потрясение росло. Оно достигло пика здесь, в великолепном дворце, посреди невероятного города под названием Холинар.
Просторное помещение для разгрузки располагалось в западной части дворца. Оно было таким большим, что две сотни слушателей, набившиеся сюда по прибытии, не заполнили его целиком. Большинство слушателей не могли посетить пир наверху — там при свидетелях заключался договор между двумя народами, — но алети все равно позаботились об отдыхе для них, предоставив всем собравшимся горы еды и питья.
Она выбралась из телеги и огляделась, гудя в ритме возбуждения. Говоря Венли о своем желании нарисовать карту мира, Эшонай воображала открытия, связанные с природой. Каньоны и холмы, леса и лейты, переполненные жизнью. На самом же деле в непосредственной близости от них существовало… все это. Дожидалось, пока кто-то его обнаружит.
Вместе с новыми слушателями.
"""
doc = nlp(string)
#spacy.displacy.serve(doc, style='dep')
rd = RussianDictionary()

for token in doc:
    print(token.text)
    print(token.pos_)
    print(token.morph.to_dict())
    rd.get_stressed_word_and_set_yo(token.text, token.morph)