DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie(
    id_ucznia CHAR(8) PRIMARY KEY,
    imie VARCHAR(30) NOT NULL CHECK (imie <> ''),
    nazwisko VARCHAR(50) NOT NULL CHECK (nazwisko <> ''),
    klasa CHAR(5) DEFAULT ''
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty(
    id_przedmiot INTEGER PRIMARY KEY AUTO_INCREMENT,
    nazwa VARCHAR(60) NOT NULL CHECK (nazwa <> '')
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny(
    id_oceny INTEGER PRIMARY KEY AUTO_INCREMENT,
    data DATE NOT NULL,
    id_ucznia CHAR(8),
    id_przedmiot INTEGER,
    ocena DECIMAL(3, 2),
    FOREIGN KEY (id_ucznia) REFERENCES uczniowie(id_ucznia) ON DELETE CASCADE,
    FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id_przedmiot) ON DELETE SET NULL
);
