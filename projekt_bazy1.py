from sa3 import *




db1 = SqlAlchemyCreate('postgresql://maciek:password@localhost/moja_baza', "dostawca")
db1.sql_create_5col_cstr("id_producenta", Integer, "nazwa_producenta",
                         String, "adres_producenta", String, "nip_producenta", Integer, "data", String,
                         )

db2 = SqlAlchemyCreate('postgresql://maciek:password@localhost/moja_baza', "produkt")
db2.sql_create_9col_cstr("id_produktu", Integer, "nazwa_producenta",
                         String, "nazwa_produktu", String, "opis_produktu", String, "cena_netto", Integer,
                         "cena_brutto", Integer, "netto_sprzedaz", Integer, "brutto_sprzedaz", Integer,
                         "procent_vat_sprzedazy", Integer)

db3 = SqlAlchemyCreate('postgresql://maciek:password@localhost/moja_baza', "zamówienie")
db3.sql_create_4col_cstr("id_zamówienia", Integer, "id_klienta", Integer,
                         "id_produktu", Integer, "data_zamówienia", String)

db4 = SqlAlchemyCreate('postgresql://maciek:password@localhost/moja_baza', "klient")
db4.sql_create_5col_cstr_2("id_klienta", Integer, "id_zamówienia",
                           Integer, "imię", String, "nazwisko", String, "adres", String)

db5 = SqlAlchemyWrite('postgresql+psycopg2://maciek:password@localhost/moja_baza',
"""INSERT INTO dostawca(id_producenta, nazwa_producenta, adres_producenta, nip_producenta, data)
VALUES(:id_producenta, :nazwa_producenta, :adres_producenta, :nip_producenta,
:data)""")
data = ({"id_producenta": 1, "nazwa_producenta": "kopex",
         "adres_producenta": "Jara 21B Libiąż", "nip_producenta": "74859",
         "data": "2020-11-01"},
        {"id_producenta": 2, "nazwa_producenta": "Jarex",
         "adres_producenta": "Wola 2 Warszawa", "nip_producenta": "8939",
         "data": "2020-12-01"},
        {"id_producenta": 3, "nazwa_producenta": "Top_projekt",
         "adres_producenta": "Wolnego 4/8 Katowice", "nip_producenta": "6342",
         "data": "2014-12-22"},
        {"id_producenta": 4, "nazwa_producenta": "Bolex",
         "adres_producenta": "Walicka 23 Kraków", "nip_producenta": "9453",
         "data": "2017-03-04"})
db5.sql_write(data)

db6 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza', """INSERT INTO
produkt(id_produktu, nazwa_producenta, nazwa_produktu, opis_produktu, cena_netto,
cena_brutto, netto_sprzedaz, brutto_sprzedaz, procent_vat_sprzedazy)
VALUES(:id_produktu, :nazwa_producenta, :nazwa_produktu, :opis_produktu,
:cena_netto, :cena_brutto, :netto_sprzedaz, :brutto_sprzedaz,
:procent_VAT_sprzedazy)""")
data = ({"id_produktu": 1, "nazwa_producenta": "kopex",
         "nazwa_produktu": "Skarpety", "opis_produktu": "piękne, różowe",
         "cena_netto": 8, "cena_brutto": 9, "netto_sprzedaz": 10, "brutto_sprzedaz": 10,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 2, "nazwa_producenta": "kopex",
         "nazwa_produktu": "Podkolanówki", "opis_produktu": "dla dziewcząt",
         "cena_netto": 4, "cena_brutto": 5, "netto_sprzedaz": 6, "brutto_sprzedaz": 6,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 3, "nazwa_producenta": "kopex",
         "nazwa_produktu": "Czapeczka", "opis_produktu": "z pomponem",
         "cena_netto": 13, "cena_brutto": 16, "netto_sprzedaz": 19, "brutto_sprzedaz": 21,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 4, "nazwa_producenta": "kopex",
         "nazwa_produktu": "Rajstopy czarne", "opis_produktu": "z ładnymi wzorkami",
         "cena_netto": 12, "cena_brutto": 14, "netto_sprzedaz": 15, "brutto_sprzedaz": 15,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 5, "nazwa_producenta": "kopex",
         "nazwa_produktu": "Stringi", "opis_produktu": "Wąskie!",
         "cena_netto": 25, "cena_brutto": 33, "netto_sprzedaz": 45, "brutto_sprzedaz": 49,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 6, "nazwa_producenta": "Top_projekt",
         "nazwa_produktu": "Program do obsługi księgowości", "opis_produktu": "webowy",
         "cena_netto": 150, "cena_brutto": 175, "netto_sprzedaz": 250, "brutto_sprzedaz": 290,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 7, "nazwa_producenta": "Top_projekt",
         "nazwa_produktu": "Model Machine Learning", "opis_produktu": "ubogi",
         "cena_netto": 2, "cena_brutto": 3, "netto_sprzedaz": 4, "brutto_sprzedaz": 4,
         "procent_VAT_sprzedazy": 8},
        {"id_produktu": 8, "nazwa_producenta": "Top_projekt",
         "nazwa_produktu": "Analiza biznesowa", "opis_produktu": "zaawansowana",
         "cena_netto": 15000, "cena_brutto": 18500, "netto_sprzedaz": 20000,
         "brutto_sprzedaz": 20000, "procent_VAT_sprzedazy": 23},
        {"id_produktu": 9, "nazwa_producenta": "Top_projekt",
         "nazwa_produktu": "Szalik", "opis_produktu": "ręcznie wyszywany",
         "cena_netto": 20, "cena_brutto": 30, "netto_sprzedaz": 35, "brutto_sprzedaz": 40,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 10, "nazwa_producenta": "Jarex",
         "nazwa_produktu": "Bluza", "opis_produktu": "z kapturem, mroczna",
         "cena_netto": 120, "cena_brutto": 148, "netto_sprzedaz": 179,
         "brutto_sprzedaz": 199, "procent_VAT_sprzedazy": 23},
        {"id_produktu": 11, "nazwa_producenta": "Jarex",
         "nazwa_produktu": "Spodnie", "opis_produktu": "jeansowe, klimatyczne",
         "cena_netto": 130, "cena_brutto": 160,  "netto_sprzedaz": 200,
         "brutto_sprzedaz": 229, "procent_VAT_sprzedazy": 23},
        {"id_produktu": 12, "nazwa_producenta": "Jarex",
         "nazwa_produktu": "Koszulka", "opis_produktu": "t-shirt z pulp fiction",
         "cena_netto": 20, "cena_brutto": 33,  "netto_sprzedaz": 58, "brutto_sprzedaz": 79,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 13, "nazwa_producenta": "Jarex",
         "nazwa_produktu": "Spodenki", "opis_produktu": "krótkie dla dziewczyny",
         "cena_netto": 40, "cena_brutto": 56,  "netto_sprzedaz": 74, "brutto_sprzedaz": 89,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 14, "nazwa_producenta": "Jarex",
         "nazwa_produktu": "Sweterek", "opis_produktu": "czerwony",
         "cena_netto": 70, "cena_brutto": 90,  "netto_sprzedaz": 110, "brutto_sprzedaz": 139,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 15, "nazwa_producenta": "Jarex",
         "nazwa_produktu": "Piżama", "opis_produktu": "zwykła",
         "cena_netto": 15, "cena_brutto": 20,  "netto_sprzedaz": 25, "brutto_sprzedaz": 30,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 16, "nazwa_producenta": "Jarex",
         "nazwa_produktu": "Pullover", "opis_produktu": "coś to jest",
         "cena_netto": 20, "cena_brutto": 30, "netto_sprzedaz": 35, "brutto_sprzedaz": 40,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 17, "nazwa_producenta": "Jarex",
         "nazwa_produktu": "Koszula", "opis_produktu": "wyjściowa w kropki",
         "cena_netto": 40, "cena_brutto": 55,  "netto_sprzedaz": 75, "brutto_sprzedaz": 85,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 18, "nazwa_producenta": "Jarex",
         "nazwa_produktu": "Dresy", "opis_produktu": "różowe podomki",
         "cena_netto": 20, "cena_brutto": 33,  "netto_sprzedaz": 35, "brutto_sprzedaz": 44,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 19, "nazwa_producenta": "Jarex",
         "nazwa_produktu": "Gumka do włosów", "opis_produktu": "w czarne kropki",
         "cena_netto": 1, "cena_brutto": 2,  "netto_sprzedaz": 3, "brutto_sprzedaz": 3,
         "procent_VAT_sprzedazy": 23},
        {"id_produktu": 20, "nazwa_producenta": "Jarex",
         "nazwa_produktu": "Stanik", "opis_produktu": "sportowy, czarny",
         "cena_netto": 13, "cena_brutto": 15,  "netto_sprzedaz": 137, "brutto_sprzedaz": 149,
         "procent_VAT_sprzedazy": 23})
db6.sql_write(data)

db7 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza', """INSERT INTO
Zamówienie(id_zamówienia, id_produktu, id_klienta, data_zamówienia)
VALUES(:id_zamówienia, :id_produktu, :id_klienta, :data_zamówienia)""")
data = ({"id_zamówienia": 1, "id_produktu": 1,
         "id_klienta": 10, "data_zamówienia": "22-12-2020"},
        {"id_zamówienia": 2, "id_produktu": 12,
         "id_klienta": 9, "data_zamówienia": "03-03-2020"},
        {"id_zamówienia": 3, "id_produktu": 20,
         "id_klienta": 8, "data_zamówienia": "16-12-2020"},
        {"id_zamówienia": 4, "id_produktu": 5,
         "id_klienta": 7, "data_zamówienia": "04-06-2020"},
        {"id_zamówienia": 5, "id_produktu": 11,
         "id_klienta": 6, "data_zamówienia": "25-04-2020"},
        {"id_zamówienia": 6, "id_produktu": 5,
         "id_klienta": 5, "data_zamówienia": "03-06-2020"},
        {"id_zamówienia": 7, "id_produktu": 7,
         "id_klienta": 4, "data_zamówienia": "17-08-2020"},
        {"id_zamówienia": 8, "id_produktu": 3,
         "id_klienta": 3, "data_zamówienia": "21-10-2020"},
        {"id_zamówienia": 9, "id_produktu": 17,
         "id_klienta": 2, "data_zamówienia": "01-05-2020"},
        {"id_zamówienia": 10, "id_produktu": 12,
         "id_klienta": 1, "data_zamówienia": "22-09-2020"})
db7.sql_write(data)

db8 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza', """INSERT INTO
Klient(id_klienta, id_zamówienia, imię, nazwisko, adres)
VALUES(:id_klienta, :id_zamówienia, :imię, :nazwisko, :adres)""")
data = ({"id_klienta": 1, "id_zamówienia": 10, "imię": "Maciej",
        "nazwisko": "Nowicki", "adres": "Ul. Jabłonia 8/2 Malbork"},
         {"id_klienta": 2, "id_zamówienia": 9, "imię": "Robert",
         "nazwisko": "Marecki", "adres": "Ul. Hryszczata 12 Pilzno"},
         {"id_klienta": 3, "id_zamówienia": 8, "imię": "Magdalena",
         "nazwisko": "Moj", "adres": "Ul. Górki 1/2 Nowa Sól"},
         {"id_klienta": 4, "id_zamówienia": 7, "imię": "Kasia",
         "nazwisko": "Kalicka", "adres": "Al. Stanisławska 1 Kluczbork"},
         {"id_klienta": 5, "id_zamówienia": 6, "imię": "Wojciech",
         "nazwisko": "Wojerz", "adres": "Ul. Kalety 8/2 Warszawa"},
         {"id_klienta": 6, "id_zamówienia": 5, "imię": "Maciej",
         "nazwisko": "Nowak", "adres": "Ul. Ułańska 16/19 Katowice"},
         {"id_klienta": 7, "id_zamówienia": 4, "imię": "Patryk",
         "nazwisko": "Jakiś", "adres": "Ul. Więzienna 19/0 Warszawa"},
         {"id_klienta": 8, "id_zamówienia": 3, "imię": "Tomasz",
         "nazwisko": "Zawadzki", "adres": "Ul. Chrobrego 12/1 Katowice"},
         {"id_klienta": 9, "id_zamówienia": 2, "imię": "Jarosław",
         "nazwisko": "Kaszanka", "adres": "Ul. Mięsna 1 Bytom"},
         {"id_klienta": 10, "id_zamówienia": 1, "imię": "Eliza",
         "nazwisko": "Malicka", "adres": "Ul. Krucza 12 Zwardoń"})
db8.sql_write(data)

db9 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza', """ALTER TABLE zamówienie
ADD FOREIGN KEY (id_produktu) REFERENCES Produkt(id_produktu)""")
db9.sql_any()

db10 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza', """ALTER TABLE dostawca
ADD id_produktu Integer""")
db10.sql_any()

db11 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza', """ALTER TABLE dostawca
ADD FOREIGN KEY (id_produktu) REFERENCES Produkt(id_produktu)""")
db11.sql_any()

db12 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""select * from dostawca where id_producenta = 1""")
db12.sql_any_print()

db13 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"select * from produkt where nazwa_producenta = 'kopex' ORDER BY nazwa_produktu")
db13.sql_any_print()

db14 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"select AVG(cena_netto) from produkt where nazwa_producenta = 'kopex'")
db14.sql_any_print()

db15 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"select AVG(cena_netto) from produkt where nazwa_producenta = 'kopex'")
db15.sql_any_print()

db16 = SqlAlchemyCreate('postgresql://maciek:password@localhost/moja_baza', "tani_produkt")
db16.sql_create_9col_cstr("id_produktu", Integer, "nazwa_producenta",
                         String, "nazwa_produktu", String, "opis_produktu", String, "cena_netto", Integer,
                         "cena_brutto", Integer, "netto_sprzedaz", Integer, "brutto_sprzedaz", Integer,
                         "procent_vat_sprzedazy", Integer)

db17 = SqlAlchemyCreate('postgresql://maciek:password@localhost/moja_baza', "drogi_produkt")
db17.sql_create_9col_cstr("id_produktu", Integer, "nazwa_producenta",
                         String, "nazwa_produktu", String, "opis_produktu", String, "cena_netto", Integer,
                         "cena_brutto", Integer, "netto_sprzedaz", Integer, "brutto_sprzedaz", Integer,
                         "procent_vat_sprzedazy", Integer)


db18 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza', '''
select *
from produkt
left join public.tani_produkt ON produkt.id_produktu = tani_produkt.id_produktu
where produkt.cena_netto > 12.4
ORDER BY produkt.id_produktu
''')
db18.sql_any_print()

db19 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza', '''
select *
from produkt
Left JOIN public.drogi_produkt ON produkt.id_produktu = drogi_produkt.id_produktu
where produkt.cena_netto >= 12.4
ORDER BY produkt.id_produktu
''')
db19.sql_any_print()

db20 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
select nazwa_produktu from produkt
inner join zamówienie on produkt.id_produktu = zamówienie.id_produktu
limit 5
""")
db20.sql_any_print()

db21 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
select sum(cena_netto) from produkt
inner join zamówienie on produkt.id_produktu = zamówienie.id_produktu
limit 5
""")
db21.sql_any_print()

db22 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
select * from produkt
inner join zamówienie on produkt.id_produktu = zamówienie.id_produktu
limit 5
""")
db22.sql_any_print()

#nie wiem jak zadeklarować datę w słowniku przy tworzeniu tablicy w sqlalchemy.
#wskazanie stringa nie działa, a nie przypiszę trzech liczb do wartości w dict.
db23 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
alter table zamówienie
ADD data DATE
""")
db23.sql_any()

db24 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
update zamówienie
set data = '2011-11-02' where id_zamówienia = 1
""")
db24.sql_any()

db25 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
update zamówienie
set data = '2019-11-06' where id_zamówienia = 2
""")
db25.sql_any()

db26 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
update zamówienie
set data = '2021-03-26' where id_zamówienia = 3
""")
db26.sql_any()

db27 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
update zamówienie
set data = '2021-04-02' where id_zamówienia = 4
""")
db27.sql_any()

db28 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
update zamówienie
set data = '2020-12-21' where id_zamówienia = 5
""")
db28.sql_any()

db29 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
update zamówienie
set data = '2021-01-21' where id_zamówienia = 6
""")
db29.sql_any()

db30 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
update zamówienie
set data = '2018-10-01' where id_zamówienia = 7
""")
db30.sql_any()

db31 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
update zamówienie
set data = '2021-02-26' where id_zamówienia = 8
""")
db31.sql_any()

db32 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
update zamówienie
set data = '2021-01-26' where id_zamówienia = 9
""")
db32.sql_any()

db33 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
update zamówienie
set data = '2020-07-14' where id_zamówienia = 10
""")
db33.sql_any()

db34 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
select * from produkt
inner join zamówienie on produkt.id_produktu = zamówienie.id_produktu
order by data
""")
db34.sql_any_print()

db35 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
SELECT *
FROM produkt
WHERE id_produktu IS NULL OR nazwa_producenta IS NULL OR nazwa_produktu IS null OR opis_produktu IS NULL OR cena_netto IS null
OR cena_brutto IS null OR netto_sprzedaz IS NULL OR brutto_sprzedaz IS null OR procent_vat_sprzedazy IS NULL
""")
db35.sql_any_print()

db36 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
select * from produkt
inner join zamówienie on produkt.id_produktu = zamówienie.id_produktu
order by data
""")
db36.sql_any_print()

db37 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
select produkt.nazwa_produktu, produkt.cena_brutto, count(produkt.id_produktu) from produkt
inner join zamówienie on produkt.id_produktu = zamówienie.id_produktu
group by produkt.id_produktu, zamówienie.id_zamówienia
ORDER BY COUNT(produkt.id_produktu) desc
""")
db37.sql_any_print()


db38 = SqlAlchemyWrite('postgresql://maciek:password@localhost/moja_baza',
"""
select produkt.nazwa_produktu, produkt.cena_brutto, count(zamówienie.data) from produkt
inner join zamówienie on produkt.id_produktu = zamówienie.id_produktu
group by produkt.id_produktu, zamówienie.id_zamówienia
ORDER BY COUNT(zamówienie.data) desc
""")
db38.sql_any_print()
