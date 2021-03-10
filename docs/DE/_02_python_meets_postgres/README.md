# Python <3 Postgres Aufgaben
In dieser Kategorie werden erweiterte Skills abgefragt. Dazu zählen
insbesondere
- Objektorientierte Programmierung
- oberflächliche SQL Kenntnisse (es genügen schon `CREATE TABLE`, 
    `DELETE TABLE` und `INSERT ROW`)

Ziel ist es ein kleines ORM Modul inkl. Model für Postgres zu schreiben.


## Vorbereitung
Zur Bearbeitung der Aufgaben benötigst du folgende Pakete:
- pytest
- pytest-flake8
- psycopg2-binary
- python-dotenv

Zum Start der Anwendung sollte eine Postgres Instanz laufen. Solltest du
Postgres nicht bei dir installiert haben, empfehle ich dir die Gelegenheit
zu nutzen und dir Docker und Docker Compose zu installieren.

Anschließend führe folgenden Befehl aus:
```
docker-compose -f tasks/_02_python_meets_postgres/docker-compose.yml up -d
```
Es wird nun eine Postgres Instanz gestartet:
- `PORT=54320`
- `POSTGRES_USER=postgres`
- `POSTGRES_PASSWORD=postgres`
- `POSTGRES_DB=sampledb`

Erstelle dir eine Datei `.env` durch folgenden Befehl:
```
cp tasks/_02_python_meets_postgres/.env.example tasks/_02_python_meets_postgres/.env
```

Update die Umgebungsvariablen in der `.env` Datei mit deinen Postgres
Zugangsdaten.

Um zu prüfen ob das Setup erfolgreich ist und du mit der eigentlichen Aufgabe
starten kannst, führe bitte folgende Befehle aus:

1. Prüfe ob die `.env` File Ordnungsgemäß erstellt wurde
```
pytest tests/tests_02_python_meets_postgres/test_orm.py::test_env_file_exists
```

2. Prüfe ob die Postgres Datenbank unter den angegebenen Parametern erreichbar
    ist
```
pytest tests/tests_02_python_meets_postgres/test_orm.py::test_postgres_connection
```

## Akzeptanz
Die Aufgaben gelten als Erfolgreich wenn du keine Fehler beim folgenden
Befehl erhältst:
```
pytest tests/tests_02_python_meets_postgres
pytest --flake8
```

Nicht Erschrecken. Bei der ersten Ausführung bekommst du 8 failed, 2 passed
und 5 errors Tests. Deine Aufgabe ist es nach und nach alle ans laufen zu
kriegen.

Die Programmierung sollte komplett in englisch erfolgen (dies wird nicht
geprüft) und sie sollte den PEP8 Standards entsprechen (dies kann geprüft
werden.)

## Aufgaben

Zur Bearbeitung dieser Aufgaben öffne die Datei
`tasks/_02_python_meets_postgres/orm.py`

Es wird ein oberflächlies ORM programmiert. Dabei wird sich auf
- die Erstellung einer Tabelle
- das Löschen einer Tabelle
- das Schreiben einzelner Reihen in eine Tabelle
- das Schreiben vieler Reihen in eine Tabelle
beschränkt.

Zusätzlich wird ein kleines Model programmiert. Das erleichtert es eine
Tabelle zu erstellen oder in eine Tabelle zu schreiben.


### Spalte `Column`
Die Klasse erleichtert die Handhabung einer einzelnen Spalte. Sie enthält
Informationen über Datentyp, Spaltenbezeichnung sowie Primary Key ja / nein.

**Initialisierung `__init__`**

Die Klasse `Column` wird mit den Eigenschaften Spaltenbezeichnung, Spaltentyp,
Primary Key initialisiert. Sie bekommt dabei folgende Parameter:
- `name` Spaltenbezeichnung
- `type_` Spaltentyp. Erlaubt sind int, serial, decimal und varchar
- `primary_key` Info darüber ob Spalte ein Primary Key ist

Folgende Fehler werden berücksichtigt:
- `type_` ist nicht ein nicht erlaubter Wert (z.B. timestamp). Es wird ein
    `KeyError` geworfen


**Hinweis:** Bevor du mit den weiteren Aufgabe fohrtfährst prüfe bitte ob dein
Initialisator entsprechend der Akzeptanzkriterien korrekt ist.
```
pytest tests/tests_02_python_meets_postgres/test_orm.py::TestColumnInit
```

**Lese Spalte `__str__`**

Es wird eine formatierte Ausgabe für die Klasse der Spalte erzeugt. Der 
Returnwert entspricht hier `NAME TYPE_ [PRIMARY KEY]`

### Pythonmodel `Model`

Es wird ein Pythonmodel erstellt, welches im ORM leichter zu handhaben ist
als einzelne Werte. Es hat dabei die Eigenschaften des Tabellennamen sowie
eine Liste der einzelnen Spalten.

**Initialisierung `__init__`**

Die Klasse `Model` wird mit den Eigenschaften des Tabellennamen und einer
Liste der einzelnen Spalten initialisiert. Es wird aktuell lediglich ein
Primary Key pro Model unterstützt. Die Klasse bekommt dabei folgende
Parameter von außen:
- `table_name` Name der Tabelle
- `columns` Liste der Spalten

Folgende Fehler werden berücksichtigt:
- `columns` enthält mehr als ein Primary Key. Es wird ein `ValueError`
    geworfen


**Hinweis:** Bevor du mit den weiteren Aufgabe fohrtfährst prüfe bitte ob dein
Initialisator entsprechend der Akzeptanzkriterien korrekt ist.
```
pytest tests/tests_02_python_meets_postgres/test_orm.py::TestModelInit
```

### `PostgresConnector`

Diese Klasse Kommuniziert direkt mit der Postgres Datenbank. Hier (und nur
hier!) werden SQL Statements ausgeführt.

**Initialisierung `__init__`**

Die Klasse initialisiert einen Datenbankconnector und einen Datenbankcursor.
Sie bekommt dazu folgende Parameter von außen:
- `**configs` Zur Verbindung notwendige Parameter (z.B. host, port, usw.)

**Hinweis:** Bevor du mit den weiteren Aufgabe fohrtfährst prüfe bitte ob dein
Initialisator entsprechend der Akzeptanzkriterien korrekt ist.
```
pytest tests/tests_02_python_meets_postgres/test_orm.py::test_postgres_connector_init
```

**Erstelle eine Tabelle `create_table`**

Die Methode erstellt eine Tabelle. Sie bekommt dabei folgende Parameter:
- `table_name` Tabellenname der Tabelle die erstellt werden soll.
- `columns` Spalten die erstellt werden sollen. Beachte bitte: Die Spalten
    sind eine Liste aus der zuvor erstellten `Columns` Klasse.

**Lösche eine Tabelle `drop_table`**

Diese Methode Löscht eine Tabelle. Sie bekommt dabei folgende Parameter:
- `table_name` Tabellenname der Tabelle die entfernt werden soll.

**Einzelner Reiheninput `single_row_insert`**

Diese Methode schreibt eine Reihe in eine Tabelle. Sie bekommt dabei folgende
Parameter übergeben:
- `table_name` Tabellenname der Tabelle die geschrieben werden soll.
- `columns` Spalten die zum schreiben beachtet werden sollen. Beachte bitte: 
    Die Spalten sind eine Liste aus der zuvor erstellten `Columns` Klasse.
- `row` Werte die in die Tabelle geschrieben werden sollen.

**Mehrere Reiheninputs `bulk_row_insert`**

Hier wird nicht nur eine Reihe, sondern gleich mehrere in die Datenbank
geschrieben. Es werdem dabei folgende Parameter übergeben:
- `table_name` Tabellenname der Tabelle die geschrieben werden soll.
- `columns` Spalten die zum schreiben beachtet werden sollen. Beachte bitte: 
    Die Spalten sind eine Liste aus der zuvor erstellten `Columns` Klasse.
- `rows` Reihen deren Werte die in die Tabelle geschrieben werden sollen.

__Tipp__ Guck' dir die Methode `cursor.executemany()` in der Dokumentation
von psycopg2 an. In den meisten Stackoverflow Hinweisen zu dem Thema wird
genau diese verwendet. Doch sie hat einen Nachteil der in der Dokumentation
deutlich wird. Mich hat dieser Nachteil im wahrsten Sinne des Wortes viel
Zeit gekostet ...

### `PostgresManager`

Diese Klasse verbindet die `PostgresConnector` Klasse und die `Model` Klasse.

**Initialisierung `__init__`**

Die Klasse initialisiert den Connector sowie das Model. Sie bekommt dabei
folgende Parameter von außen:
- `connector` PostgresConnector Objekt
- `model` Modelobjekt

**Hinweis:** Bevor du mit den weiteren Aufgabe fohrtfährst prüfe bitte ob dein
Initialisator entsprechend der Akzeptanzkriterien korrekt ist.
```
pytest tests/tests_02_python_meets_postgres/test_orm.py::test_postgres_manager_init
```

**Migriere das Model in die Datenbank `migrate`**

Diese Methode erstellt das Model in der Datenbank.

**Schreibe eine einzelne Reihe in die Datenbank `insert`**

Diese Methode schreibt eine einzelne Reihe in die Datenbank. Dafür bekommt
sie folgende Parameter von außen übergeben:
- `row` Werte die in die Tabelle geschrieben werden sollen.

**Schreibe viele Reihen in die Datenbank `bulk_insert`**

Diese Methode schreibt viele Reihen in die Datenbank. Dafür bekommt sie
folgende Parameter von außen übergeben:
- `rows` Reihen deren Werte die in die Tabelle geschrieben werden sollen.
