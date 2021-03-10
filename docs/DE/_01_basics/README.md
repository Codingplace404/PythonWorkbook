# Basic Aufgaben
In dieser Aufgabenkategorie werden ein paar Basisskills abgefragt.
- Funktionen
- Objektorientierte Programmierung (insbesondere die Vererbung)
- Kontrollstrukturen
- Der Modulo Operator ;-)

## Vorbereitung
Zur Bearbeitung der Aufgaben benötigst du folgende Pakete:
- pytest
- pytest-flake8

Füge sie bitte deiner Virtuellen Entwicklungsumgebung hinzu.

## Akzeptanz
Die Aufgaben gelten als Erfolgreich wenn du keine Fehler beim folgenden
Befehl erhältst:
```
pytest tests/tests_01_basics/
pytest --flake8
```

Nicht Erschrecken. Bei der ersten Ausführung bekommst du 38 failed, 5 passed
Tests. Deine Aufgabe ist es nach und nach alle ans laufen zu kriegen.

Die Programmierung sollte komplett in englisch erfolgen (dies wird nicht
geprüft) und sie sollte den PEP8 Standards entsprechen (dies kann geprüft
werden.)

## Aufgaben
Die Basics teilen sich in folgende Aufgabenblöcke:
- Funktionen (in `tasks/_01_basics/functions.py`)
- Klassen (in `tasks/_01_basics/classes.py`)

Diese sind getrennt voneinander zu bearbeiten. Sie teilen sich keinerlei
Abhängigkeiten.

Beachte bitte dass du zusätzliche Pakete installieren darfst, aber
nicht musst. Die erforderlichen Imports befinden sich in der
Standardbibliothek von Python.

Die folgenden Aufgabenbeschreibungen sind optional. Anhand der verwendeten
Docstrings an den Funktionen und Klassen sollte die Aufgabe ersichtlich sein.

### Funktionen `functions.py`
Im Folgenden eine Auflistung der Funktionen die erstellt werden sollen.

#### Zahl ist Gerade oder ungerade `is_even_number`
Die Funktion `is_even_number` bestimmt ob ein _Integer_ eine gerade
oder ungerade Zahl ist. Die Funktion gibt ein `True` zurück wenn sie es ist
und ein `False` wenn sie ungerade ist.

Bei falscher Eingabe (z.B. eines Floats oder Strings) gibt die Funktion ein
`False` zurück.

#### Filter `low_or_highpass_filter`
Die Funktion `low_or_highpass_filter` filtert eine Liste so, dass
entweder zu große oder zu kleine Werte entfernt werden. Sie bekommt dabei
folgende Parameter:
- `values` Liste von Ergebnissen die gefiltert werden sollen. Die Liste
    beeinhaltet dabei nur Zahlen (Floats und / oder Integer)
- `treshhold` Wert der bestimmt welcher Wert die maximalen- bzw minimalen
    Grenze angibt. Die Variable kann Float oder Integer sein.
- `type_` Entweder `lowpass` oder `highpass`. Hier wird bestimmt welcher Art
    der Filter angehören soll

Folgende Fehler werden Berücksichtigt:
- `type_` ist weder `lowpass` noch `highpass`. Es wird ein `TypeError` 
    geworfen
- ein Wert in der Liste ist kein Float oder Integer. Es wird ein
    `ValueError` geworfen
- `treshhold` ist weder Float noch Integer. Es wird ein `ValueError`
    geworfen

#### Bekomme Dateien aus einem Verzeichnis `get_files_from_directory`
Die Funktion gibt eine Liste der Namen von Dateien mit einem bestimmten Suffix
eines bestimmten Verzeichnisses zurück. Sie bekommt dabei folgende Parameter:
- `suffix` Dateiendung
- `directory_path` Pfad zum Verzeichnis

Für den Fall dass das Verzeichnis nicht existiert, gibt die Funktion eine
leere Liste zurück.

_Tipp_ zur Bearbeitung dieser Aufgabe eignen sich u.U. das `pathlib` oder
das `os` Modul der Standardbibliothek von Python.

#### Generiere eine zufällige Zeichenkette `generate_random_string`
Die Funktion generiert eine zufällige Zeichenkette beliebiger Länge aus
Zahlen, Buchstaben und Sonderzeichen und gibt diese zurück. Sie bekommt dabei
folgende Parameter:
- `string_length` gewünschte Länge der Zeichekette

_Tipp_ zur Bearbeitung dieser Aufgabe eignen sich u.U. das `string` sowie
das `random` Modul der Standardbibliothek von Python.


#### Bestimme die Anzahl der Monate `get_number_of_days_in_month`
Die Funktion gibt die Anzahl der Tage eines bestimmten Monats in einem
bestimmten Jahr zurück. Sie bekommt dabei folgende Parameter:
- `month` der Monat der betrachtet wird als Integer. Dabei entspricht der
    Monat Januar dem Wert 1 und Dezember den Wert 12
- `year` das Jahr welches in Zusammenhang mit dem Monat betrachtet wird.

Die Funktion gibt den Wert -1 zurück, wenn der Wert des Monats unzulässig
ist (z.B. -2 oder 15).

_Tipp_ zur Bearbeitung dieser Aufgabe eignen sich u.U. das `datetime`
Modul der Standardbibliothek von Python.

#### Bestimme den Endzeitpunkt `next_time_calculator`
Die Funktion bestimmt anhand einer Dauer und einem Startzeitpunkt den
entsprechenden Endzeitpunkt. Betrachtet werden nur ganze Uhrzeiten zwischen
0 und 24 (inklusive, exklusive). Die Dauer wird auch ganzzahlig betrachtet.
Die Funktion bekommt dabei folgende Parameter:
- `hour` der Startzeitpunkt als volle Stunde (z.B. 0, 3, 12, 14)
- `duration` die Dauer in Stunden als ganze Zahl (darf auch größer als 24 sein)

Folgende Fehler werden berücksichtigt:
- `hour` ist nicht im Bereich 0 bis 24 (inklusive, exklusive). Es wird ein
    `ValueError` geworfen.
- `duration` oder `hour` sind falsch typisiert. Es wird ein `TypeError`
    geworfen.


#### Bestimme Fibonacci Zahlen `get_fibonacci_numbers`
Die Funktion gibt eine Liste an Fibonacci Zahlen zurück. Eine Fibonacci Folge
sieht wie folgt aus:
```
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
```
Die ersten beiden Werte einer Fibonacci Folge entsprechen in diesem Beispiel
den Werten 1 und 1. Die Anderen Werte sind jeweils das Ergebnis aus der
Addition der voherigen Werte
```
2 = 1 + 1
3 = 2 + 1
5 = 3 + 2
8 = 5 + 3
11 = 8 + 5
...
```
Dabei wird der Funktion der folgende Parameter übergeben:
- `counts` Anzahl der gewünschten Werte der Fibonacci Folge.


### Klassen `classes.py`
Im Folgenden eine Auflistung der Funktionen die erstellt werden sollen.

Bei diesen Aufgaben gibt es eine kleine zum warm werden (das Rechteck),
sowie eine größere bei der du einen kleinen Bestellprozess programmierst.

#### Das Rechteck `Rectangle`
**Initialisierung `__init__`**

Das Rechteck wird mit den Seitenlängen a und b initialisiert. Der
`__init__` bekommt dabei von außen folgende Parameter:
- `a` Seitenlänge a
- `b` Seitenlänge b

**Hinweis:** Bevor du mit den weiteren Aufgabe fohrtfährst prüfe bitte ob dein
Initialisator entsprechend der Akzeptanzkriterien korrekt ist.
```
pytest tests/tests_01_basics/test_01_basics_classes.py::test_rectangle_init
```

**Flächenberechnung `get_area`**

Die Funktion bestimmt den Flächeninhalt des gegebenen Rechteckobjekts. Sie
bekommt dabei keine weiteren Parameter von außen.

**Umfangberechnung `get_scope`**

Die Funktion bestimmt den Umfang des gegebenen Rechteckobjekts. Sie
bekommt dabei keine weiteren Parameter von außen.


#### Die Bestellung

Die Folgenden Aufgaben sind Teil eines Großen Ganzen. Es geht final darum
Artikel einer Bestellung zuzuordnen (im speziellen TShirts und Filme) und
dabei zu prüfen ob eine Altersverifizierung notwendig ist, sowie diverser
anderer kleinigkeiten.

**Grundartikel Klasse `BaseArticle`**

Diese Klasse beschreibt einen Artikel allgemein. Ein Artikel wird dabei durch
die Eigenschaften Titel, Herstellungskosten, UVP und Verkaufspreis beschrieben.

Zudem gibt es die Möglichkeiten den Gewinn eines Artikels zu bestimmen und
die Überprüfung der Notwendigkeit einer zwingenden Altersverifizierung.

**Initialisierung `__init__`**

Der Basisartikel wird mit den Eigenschaften Titel, Herstellungskosten,
UVP und Verkaufspreis initialisiert. Der `__init__` bekommt dabei von außen 
folgende Parameter:
- `title` Titel des Artikels
- `manufacturing_costs` Herstellungskosten des Artikels
- `recommended_price` Unverbindliche Preisempfehlung
- `price` Tatsächlicher Verkaufspreis

**Hinweis:** Bevor du mit den weiteren Aufgabe fohrtfährst prüfe bitte ob dein
Initialisator entsprechend der Akzeptanzkriterien korrekt ist.
```
pytest tests/tests_01_basics/test_01_basics_classes.py::test_base_article_init
```


**Altersverifizierung erforderlich? `age_verification_is_required`**

Die Funktion prüft ob der Artikel Altersverifizierungspflichtig ist. Die
Entscheidung hier ist Standardmäßig für alle Artikel `False`


**Bestimme den Gewinn `get_revenue`**

Die Funktion bestimmt den Gewinn eines einzelnen Produkts. Der Gewinn
entspricht dabei allgemein Verkaufspreis abzüglich Herstellungskosten.


**TShirt `TShirtArticle`**

Diese Klasse ist ein Spezialfall der Basisartikel. Betrachtet werden hier
insbesondere TShirts mit den zusätzlichen Eigenschaften Größe und Marke.

Die Eigenschaften der Basisartikel bleiben in dieser Klasse aber auch
erhalten.

**Initialisierung `__init__`**

Das TShirt wird mit den Eigenschaften Titel, Herstellungskosten, UVP, 
Verkaufspreis, Größe und Marke initialisiert. Der `__init__` bekommt dabei von 
außen folgende Parameter:
- `title` Titel des Artikels
- `manufacturing_costs` Herstellungskosten des Artikels
- `recommended_price` Unverbindliche Preisempfehlung
- `price` Tatsächlicher Verkaufspreis
- `size` Größe des TShirts. Erlaubt sind hier die Werte
    xs, s, m, l, xl, xxl
- `brand` Marke des TShirts

Folgende Fehler werden berücksichtigt:
- `size` entspricht einem nicht erlaubten Wert (z.B. xxxxl). Es wird ein
    `ValueError` geworfen.


**Film `FilmArticle`**

Ein Film ist ein Spezialfall der Basisartikel. Betrachtet werden hier neben
den normalen Eigenschaften zusätzlich Typ des Films, Altersbeschränkung und
der Cast des Films.

Weiter wird hier die Bestimmung zur zwingenden Altersüberprüfung angepasst.

**Initialisierung `__init__`**

Der Film wird mit den Eigenschaften Titel, Herstellungskosten, UVP,
Verkaufspreis, Typ, Altersbeschränkung und Cast initialisiert. Der `__init__`
bekommt dabei von außen folgende Parameter:
- `title` Titel des Artikels
- `manufacturing_costs` Herstellungskosten des Artikels
- `recommended_price` Unverbindliche Preisempfehlung
- `price` Tatsächlicher Verkaufspreis
- `type_` Typ des Films. Erlaubt sind hier die Werte dvd, bluray, 4k
- `age_restriction` Altersbeschränkung des Films. Erlaubt sind die Werte
    0, 6, 12, 16, 18
- `cast` Die Filmbesetzung

Folgende Fehler werden berücksichtigt:
- `type_` entspricht einem nicht erlaubten Wert (z.B. vod). Es wird ein
    `TypeError` geworfen.
- `age_restriction` entspricht einem nicht erlaubten Wert (z.B. 21). Es wird
    ein `ValueError` geworfen.

**Hinweis:** Bevor du mit den weiteren Aufgabe fohrtfährst prüfe bitte ob dein
Initialisator entsprechend der Akzeptanzkriterien korrekt ist.
```
pytest tests/tests_01_basics/test_01_basics_classes.py::TestFilmArticleInit
```


**Altersverifizierung erforderlich? `age_verification_is_required`**

Die Funktion gibt an ob eine Altersüberprüfung erforderlich ist. Eine
Überprüfung ist erforderlich wenn die Altersberschränkung nicht 0 ist.


**Bestellter Artikel `OrderObject`**
Dies ist im weitesten Sinne eine Hilfsklasse um die Bestellung einfacher
verwalten zu können. Sie besteht aus dem Artikel und der Anzahl der gekauften
Artikel.

**Initialisierung `__init__`**

Der bestellte Artikel wird mit den Eigenschaften Artikel und Anzahl
initialisiert. Dazu werden der dem `__init__` von außen folgende Parameter
übergeben:
- `article` der Artikel in der Bestellung
- `quantity` die Anzahl dieses einen Artikel in der Bestellung. Darf nicht
    kleiner als 0 sein.

Folgende Fehler werden berücksichtigt:
- `quantity` ist kleiner als 0. Es wird ein `ValueError` geworfen

**Hinweis:** Bevor du mit den weiteren Aufgabe fohrtfährst prüfe bitte ob dein
Initialisator entsprechend der Akzeptanzkriterien korrekt ist.
```
pytest tests/tests_01_basics/test_01_basics_classes.py::TestOrderObjectInit
```

**Bestellung `Order`**
Diese Klasse beschreibt (stark vereinfacht) eine Bestellung. Ihre
Eigenschaften sind eine Liste an bestellten Artikeln sowie die Lieferadresse.

Zusätzlich enthalt die Bestellung die Information ob eine Altersüberprüfung
erforderlich ist und was der Gesamtpreis der Bestellung ist.

**Initialisierung `__init__`**

Die Bestellung wird mit den Eigenschaften Bestellte Artikel sowie
Lieferadresse initialisiert. Die Parameter von außen sind dabei:
- `ordered_objects` Liste an bestellter Objekte
- `shipping_address` Lieferadresse

**Hinweis:** Bevor du mit den weiteren Aufgabe fohrtfährst prüfe bitte ob dein
Initialisator entsprechend der Akzeptanzkriterien korrekt ist.
```
pytest tests/tests_01_basics/test_01_basics_classes.py::test_order_init
```

**Altersverifizierung erforderlich? `age_verification_is_required`**

Die Funktion gibt an ob eine Altersüberprüfung erforderlich ist. Eine
Überprüfung ist erforderlich wenn die Altersberschränkung nicht 0 ist.

**Bestimme den Gesamtpreis `get_price`**

Die Funktion bestimmt den Gesamten Einkaufspreis aller Artikel im Warenkorb.

#### Akzeptanzkriterien
**`is_even_number`**

1. Eine gerade Zahl wird als gerade identifiziert
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestIsEvenNumber::test_number_is_even
```

2. Eine ungerade Zahl wird als ungerade identifiziert
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestIsEvenNumber::test_number_is_not_even
```

3. Die Funktion gibt bei einem falschen Datentypen ein `False` zurück
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestIsEvenNumber::test_wrong_number_type
```

Sollten alle Tests erfolgreich sein, so teste die komplette Aufgabe um sicher
zu gehen dass du bei fortlaufender Arbeit nicht rückwirkend Fehler produziert
hast:
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestIsEvenNumber
```

Die Aufgabe gilt als abgeschlossen wenn `TestIsEvenNumber` komplett
erfolgreich ist.


**`low_or_highpass_filter`**

1. Lowpass Filter filtert Werte größer oder gleich des Treshholds raus
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestLowOrHighpassFilter::test_lowpass_filter
```

2. Highpass Filter filtert Werte kleiner oder gleich des Treshholds raus
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestLowOrHighpassFilter::test_highpass_filter
```

3. Werfe Fehler wenn Wert `type_` unzulässig
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestLowOrHighpassFilter::test_type_error_if_type_is_not_highpass_or_lowpass
```

4. Werfe Fehler wenn Datentyp `treshhold` unzulässig
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestLowOrHighpassFilter::test_value_error_if_treshhold_has_wrong_type
```

5. Werfe Fehler wenn ein falscher Datentyp in `values` ist
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestLowOrHighpassFilter::test_value_error_if_single_value_has_wrong_type
```

Sollten alle Tests erfolgreich sein, so teste die komplette Aufgabe um sicher
zu gehen dass du bei fortlaufender Arbeit nicht rückwirkend Fehler produziert
hast:
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestLowOrHighpassFilter
```

Die Aufgabe gilt als abgeschlossen wenn `TestLowOrHighpassFilter` komplett
erfolgreich ist.


**`get_files_from_directory`**

1. Bekomme Dateien eines bestimmten Suffix aus einem existierenden Verzeichnis
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestGetPythonFilesFromDirectory::test_get_python_files_from_directory
```

2. Bekomme eine Leere Liste aus einem existierenden Verzeichnis in dem keine
    Dateien des gewünschten Sufix' existieren:
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestGetPythonFilesFromDirectory::test_get_empty_list_of_files_from_directory
```

3. Bekomme eine leere Liste wenn das Verzeichnis nicht existiert
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestGetPythonFilesFromDirectory::test_get_python_files_from_directory
```

Die Aufgabe gilt als abgeschlossen wenn `TestGetPythonFilesFromDirectory`
komplett erfolgreich ist.


**`generate_random_string`**

1. Erstelle einen Random String beliebiger Länge:
```
pytest tests/tests_01_basics/test_01_basics_functions.py::test_generate_random_string
```

Die Aufgabe gilt als abgeschlossen sobald Punkt 1 abgeschlossen ist.
Aktuell wird nicht überprüft aus welchen Zeichenketten der String besteht.


**`get_number_of_days_in_month`**

1. Die Anzahl der Tage eines Monats wird zuverlässig berechnet
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestGetNumbersOfDaysInMonth::test_get_number_of_days_in_month
```

2. Es wird eine negativer Wert von der Funktion zurück gegeben wenn der
    angegebene Monat nicht valide ist:
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestGetNumbersOfDaysInMonth::test_returns_negative_value_for_invalid_month
```

Die Aufgabe gilt als abgeschlossen wenn `TestGetNumbersOfDaysInMonth`
komplett erfolgreich ist.

**`next_time_calculator`**

1. Der Endzeitpunkt wird für den selben Tag zuverlässig bestimmt
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestNextTimeCalculator::test_next_time_calculator_within_same_day
```

2. Der Endzeitpunkt wird im Falle eines einzelnen Überlaufs zuverlässig
    bestimmt
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestNextTimeCalculator::test_next_time_calculator_with_overlap_day_less_than_24_hours
```

3. Der Endzeitpunkt wird für mehrere Überläufe bestimmt
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestNextTimeCalculator::test_next_time_calculator_with_overlap_day_more_than_24_hours
```

4. Es wird ein Fehler geworfen wenn der Startpunkt einen zu großen Wert hat
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestNextTimeCalculator::test_raise_value_error_if_hour_is_out_of_range_positive_number
```

5. Es wird ein Fehler geworfen wenn der Startpunkt negativ ist
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestNextTimeCalculator::test_raise_value_error_if_hour_is_out_of_range_negative_number
```

6. Es wird ein Fehler geworfen wnn der Startpunkt falsch typisiert ist
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestNextTimeCalculator::test_raise_type_error_if_hour_is_wrong_type
```

7. Es wird ein Fehler geworfen wnn die Dauer falsch typisiert ist
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestNextTimeCalculator::test_raise_type_error_if_duration_is_wrong_type
```

Die Aufgabe gilt als abgeschlossen wenn `TestNextTimeCalculator`
komplett erfolgreich ist.


**`get_fibonacci_numbers`**

1. Es wird eine korrekte Liste der Länge 1 bestimmt
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestFibonacciNumbers::test_fibonacci_numbers_count_1
```

2. Es wird eine korrekte Liste der Länge 2 bestimmt
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestFibonacciNumbers::test_fibonacci_numbers_count_2
```

3. Es wird eine korrekte Liste der Länge 3 bestimmt
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestFibonacciNumbers::test_fibonacci_numbers_count_3
```

4. Es wird eine korrekte Liste der Länge n bestimmt:
```
pytest tests/tests_01_basics/test_01_basics_functions.py::TestFibonacciNumbers::test_fibonacci_numbers_count_10
```

Die Aufgabe gilt als abgeschlossen wenn `TestFibonacciNumbers`
komplett erfolgreich ist.

