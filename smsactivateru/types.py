# -*- coding: utf-8 -*-


class SmsTypes:
    class Country:
        RU = '0'   # Россия (Russia)
        UA = '1'   # Украина (Ukraine)
        KZ = '2'   # Казахстан (Kazakhstan)
        CN = '3'   # Китай (China)
        PH = '4'   # Филиппины (Philippines)
        MM = '5'   # Мьянма (Myanmar)
        ID = '6'   # Индонезия (Indonesia)
        MY = '7'   # Малайзия (Malaysia)
        KE = '8'   # Кения (Kenya)
        TZ = '9'   # Танзания (Tanzania)
        VN = '10'  # Вьетнам (Vietnam)
        KG = '11'  # Кыргызстан (Kyrgyzstan)
        US = '12'  # США (USA)
        IL = '13'  # Израиль (Israel)
        HK = '14'  # Гонконг (Hong Kong)
        PL = '15'  # Польша (Poland)
        UK = '16'  # Великобритания (United Kingdom)
        MG = '17'  # Мадагаскар (Madagascar)
        CG = '18'  # Конго (Congo)
        NG = '17'  # Нигерия (Nigeria)
        MO = '17'  # Макао (Macau)

    class Status:
        Cancel = '-1'
        SmsSent = '1'
        OneMoreCode = '3'
        End = '6'
        AlreadyUsed = '8'


    class Operator:
        MTS = 'mts'
        Beeline = 'beeline'
        Megafon = 'megafon'
        TELE2 = 'tele2'