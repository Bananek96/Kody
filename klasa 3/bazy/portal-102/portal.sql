DROP TABLE IF EXISTS kraje;
CREATE TABLE kraje(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    kraj VARCHAR(50) NOT NULL CHECK (kraj <> '')
);

DROP TABLE IF EXISTS uzytkownicy;
CREATE TABLE uzytkownicy(
    id_uzytkownika INTEGER PRIMARY KEY AUTO_INCREMENT,
    imie VARCHAR(30) NOT NULL CHECK (imie <> ''),
    nazwisko VARCHAR(50) NOT NULL CHECK (nazwisko <> ''),
    id_kraj INTEGER,
    plec CHAR(2),
    FOREIGN KEY (id_kraj) REFERENCES kraje(id) ON DELETE SET NULL
);

DROP TABLE IF EXISTS zdjecia;
CREATE TABLE zdjecia(
    id_zdjecia INTEGER PRIMARY KEY AUTO_INCREMENT,
    data_dodania DATE NOT NULL,
    id_uzytkownika INTEGER,
    szerokosc INTEGER DEFAULT 0,
    wysokosc INTEGER DEFAULT 0,
    FOREIGN KEY (id_uzytkownika) REFERENCES uzytkownicy(id_uzytkownika) ON DELETE SET NULL
);

DROP TABLE IF EXISTS znajomosci;
CREATE TABLE znajomosci(
    znajomy_1 INTEGER,
    znajomy_2 INTEGER,
    data DATE NOT NULL,
    FOREIGN KEY (znajomy_1) REFERENCES uzytkownicy(id_uzytkownika) ON DELETE CASCADE,
    FOREIGN KEY (znajomy_2) REFERENCES uzytkownicy(id_uzytkownika) ON DELETE CASCADE,
    PRIMARY KEY (znajomy_1, znajomy_2)
);
