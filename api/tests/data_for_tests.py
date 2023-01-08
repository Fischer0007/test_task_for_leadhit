# for positive test

PARAMETRS1 = "?atr_1=2023-01-07&atr_2=+7 900 600 99 99&atr_3=test_email1@gmail.com&atr_4=Hello World!&atr_5=" \
             "Hello World!2&atr_6=Hello World!3&atr_7=+7 900 600 99 99&atr_8=2023-01-06&atr_9=" \
             "test_email2@gmail.com&atr_10=Test text for query"

PARAMETRS2 = "?atr_1=2023-01-07&atr_2=+7 900 600 99 99&atr_3=test_email1@gmail.com&atr_4=Hello World!&atr_5=" \
             "Hello World!2&atr_6=Hello World!3&atr_7=+7 900 600 99 99&atr_8=2023-01-06&atr_9=test_email2@gmail.com"

PARAMETRS3 = "?atr_1=2023-01-07&atr_2=+7 900 600 99 99&atr_3=test_email1@gmail.com&atr_4=Hello World!&atr_5=" \
             "Hello World!2&atr_6=Hello World!3&atr_7=+7 900 600 99 99&atr_8=2023-01-06"

PARAMETRS4 = "?atr_1=2023-01-07&atr_2=+7 900 600 99 99&atr_3=test_email1@gmail.com&atr_4=Hello World!&atr_5=" \
             "Hello World!2&atr_6=Hello World!3&atr_7=+7 900 600 99 99"

PARAMETRS5 = "?atr_1=2023-01-07&atr_2=+7 900 600 99 99&atr_3=test_email1@gmail.com&atr_4=Hello World!&atr_5=" \
             "Hello World!2&atr_6=Hello World!3"

PARAMETRS6 = "?atr_1=2023-01-07&atr_2=+7 900 600 99 99&atr_3=test_email1@gmail.com&atr_4=Hello World!&atr_5=" \
             "HelloWorld!"

PARAMETRS7 = "?atr_1=2023-01-07&atr_2=+7 900 600 99 99&atr_3=test_email1@gmail.com&atr_4=Hello World!"

PARAMETRS8 = "?atr_1=2023-01-07&atr_2=+7 900 600 99 99&atr_3=test_email1@gmail.com&atr_4=Hello, World! Good Bay!"

RES = "MyForm"


# for negative test

PARAMETRS9 = "?atr_1=07.01.2023&atr_2=7-900-600-99-99&atr_3=test_email@gmail..com&atr_4=!@%23$%^%26*()ABCDEFabcdef"

PARAMETRS10 = "?atr_1=07-01-2023&atr_2=7-(900)-600-99-99&atr_3=test_email1@@gmail.com&atr_4=!@%23$%^%26*()ABCDEFabcdef"

PARAMETRS11 = "?atr_1=07.01.2023&atr_2=7-900-600-99-99&atr_3=test_email@gmail..com&atr_4=+79006009999&atr_5=" \
              "8(900)6009999&atr_6=+790060099990&atr_7=8-900-600-99-99&atr_8=test_email@@gmail..com&atr_9=" \
              "test_email@gmail com&atr_10=07-01-2023"

PARAMETRS12 = "?atr_1=200082252225&atr_2=+7  900600 99 99&atr_3=test_email@gmail..com&atr_4=+79006009999tel&atr_5=" \
              "2023.01.07&atr_6=+7-900-600-99-99&atr_7=07.01.23&atr_8=тестовый_email@gmail.com&atr_9=" \
              "test--email@gmail=com&atr_10=07/01/2023"


RESPONSE1 = {
    "atr_1": "FIELD_TYPE",
    "atr_2": "FIELD_TYPE",
    "atr_3": "FIELD_TYPE",
    "atr_4": "FIELD_TYPE"
}

RESPONSE2 = {
    "atr_1": "FIELD_TYPE",
    "atr_2": "FIELD_TYPE",
    "atr_3": "FIELD_TYPE",
    "atr_4": "FIELD_TYPE"
}

RESPONSE3 = {
    "atr_1": "FIELD_TYPE",
    "atr_10": "FIELD_TYPE",
    "atr_2": "FIELD_TYPE",
    "atr_3": "FIELD_TYPE",
    "atr_4": "FIELD_TYPE",
    "atr_5": "FIELD_TYPE",
    "atr_6": "FIELD_TYPE",
    "atr_7": "FIELD_TYPE",
    "atr_8": "FIELD_TYPE",
    "atr_9": "FIELD_TYPE"
}

RESPONSE4 = {
    "atr_1": "FIELD_TYPE",
    "atr_10": "FIELD_TYPE",
    "atr_2": "FIELD_TYPE",
    "atr_3": "FIELD_TYPE",
    "atr_4": "FIELD_TYPE",
    "atr_5": "FIELD_TYPE",
    "atr_6": "FIELD_TYPE",
    "atr_7": "FIELD_TYPE",
    "atr_8": "FIELD_TYPE",
    "atr_9": "FIELD_TYPE"
}
