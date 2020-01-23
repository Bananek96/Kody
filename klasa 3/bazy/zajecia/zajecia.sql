DROP TABLE IF EXISTS osoby;
CREATE TABLE osoby(
    id_osoby INTEGER PRIMARY KEY AUTO_INCREMENT,
    nazwisko VARCHAR(50) NOT NULL CHECK (nazwisko <> ''),
    imie VARCHAR(30) NOT NULL CHECK (imie <> ''),
    plec CHAR(2)
);

DROP TABLE IF EXISTS obiekty;
CREATE TABLE obiekty(
    id_obiektu INTEGER PRIMARY KEY AUTO_INCREMENT,
    nazwa VARCHAR(50) NOT NULL CHECK (nazwa <> '')
);


DROP TABLE IF EXISTS zajecia;
CREATE TABLE zajecia(
    id_zajec INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_obiektu INTEGER,
    zajecia VARCHAR(30) NOT NULL CHECK (zajecia <> ''),
    cena INTEGER DEFAULT 0,
    FOREIGN KEY (id_obiektu) REFERENCES obiekty(id_obiektu) ON DELETE CASCADE
);

DROP TABLE IF EXISTS wejscia;
CREATE TABLE wejscia(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_osoby INTEGER,
    data DATE NOT NULL,
    id_zajec INTEGER,
    FOREIGN KEY (id_osoby) REFERENCES osoby(id_osoby) ON DELETE CASCADE,
    FOREIGN KEY (id_zajec) REFERENCES zajecia(id_zajec) ON DELETE CASCADE
);
