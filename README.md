**Funktion:**  

Überträgt deutsche Schachnotation ins PGN Format.

**Beschreibung:**

Input kann über manuelle Eingabe, copy/paste oder durch drag&drop einer Textdatei in das obere Textfeld erfolgen.

Die Schaltfläche "Konvertieren" überträgt dann deutsche Notation ins PGN Format

Die Ausgabe erfolgt im zweiten Fenster.

Nach dem Betätigen der Schaltfläche "In Zwischenablage kopieren" kann man die PGN Daten in ein Dokument, Webseite oder Software seiner Wahl mittels der der üblichen Methoden einfügen. 
Die Schaltfläche "Auf Lichess.org analysieren" öffnet das Analyse-Tool der kostenfreien opensource 
Schachwebseite Lichess.org und fügt die PGN Daten ein, sodass man direkt mit der Auswertung des Spiels
beginnen kann.

**Wozu das ganze?**

Ich spiele regelmäßig mit meinem Vater Schach auf einer kleineren, deutschen Schachseite. Die Spiele erhält man, zumindest als nicht zahlender Kunde, nur in der deutschen Schachnotation.
Oft will ich Schlüsselmomente in den Partien im Nachhinein mittels eine Engine untersuchen, auf besagter Schachseite nicht möglich. 
Zum Glück gibt es Lichess.org, wo das kein Problem ist. Abgesehen davon das deren Analysetool kein deutsch spricht.
Klingt nach 'ner hübschen kleinen Aufgabe für ein Übungsprojekt.

Die Übersetzungslogik an sich war erstaunlich simpel und innerhalb von wenigen Minuten umgesetzt, was ein wenig enttäuschend war. Das Projekt an sich kann trotzdem als lehrreich gelten
weil ich ein paar Libraries ausprobieren konnte die ich bisher nicht genutzt hatte. Etwas praktische Erfahrung mit APIs sammeln hat sicher auch nicht geschadtet.

**TODO:**

Kommentare und Metadaten in der Notation ermöglichen <- erübrigt sich, Lichess.org/analyse ignoriert PGN Metadaten, Kommentare sowie mehr als ein Spiel pro PGN Datei.
