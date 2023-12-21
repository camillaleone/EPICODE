
CREATE TABLE DISCO (
    NroSerie INT PRIMARY KEY,
    TitoloAlbum VARCHAR(255),
    Anno INT,
    Prezzo DECIMAL (10,2));

INSERT INTO DISCO (NroSerie,TitoloAlbum,Anno,Prezzo) VALUES
    (001,'Amore',1999,15.99),
    (002,'Pace',NULL,20.99),
    (003,'Natale',2010,15.99),
    (004,'Atmosfera',NULL,25.99),
    (005,'Errore',2020,9.99);

CREATE TABLE CONTIENE (
    NroSerieDisco INT,
    CodiceReg INT PRIMARY KEY,
    NroProg INT,
    FOREIGN KEY (NroSerieDisco) REFERENCES DISCO(NroSerie)
    );

INSERT INTO CONTIENE (NroSerieDisco, CodiceReg, NroProg) VALUES
    (001, 111,1),
    (002, 213,2),
    (003, 132,1),
    (004, 122,1),
    (005, 133,2);

CREATE TABLE ESECUZIONE (
    CodiceReg INT,
    TitoloCanz VARCHAR(255) PRIMARY KEY,
    Anno INT,
    FOREIGN KEY (CodiceReg) REFERENCES CONTIENE (CodiceReg)
    );

INSERT INTO ESECUZIONE (CodiceReg, TitoloCanz,Anno) VALUES
    (111, 'Amore1', 1999),
    (213, 'Pace2', NULL),
    (132, 'Natale3', 2010),
    (122, 'Atmosfera4', NULL),
    (133, 'Errore5', 2020);

CREATE TABLE AUTORE (
    Nome VARCHAR (255) PRIMARY KEY,
    TitoloCanzone VARCHAR (255),
    FOREIGN KEY (TitoloCanzone) REFERENCES ESECUZIONE(TitoloCanz)
    );

INSERT INTO AUTORE (Nome,TitoloCanzone) VALUES
    ('Mario Biondi','Amore1'),
    ('Giulia Rossi','Pace2'),
    ('Dando','Natale3'),
    ('Damiano','Atmosfera4'),
    ('Francesca Marroni','Errore5');

CREATE TABLE CANTANTE (
    NomeCantante VARCHAR (255) PRIMARY KEY,
    CodiceReg INT,
    FOREIGN KEY (CodiceReg) REFERENCES ESECUZIONE(CodiceReg)
    );

INSERT INTO CANTANTE (NomeCantante, CodiceReg) VALUES
    ('Mario Biondi', 111),
    ('Giulia Rossi', 213),
    ('Dando', 132),
    ('Damiano', 122),
    ('Jayjay', 133);

-- I cantautori (persone che hanno cantato e scritto la stessa canzone) il cui nome inizia per 'D’;
SELECT Nome Cantautore
FROM CANTANTE
JOIN AUTORE ON CANTANTE.NomeCantante=AUTORE.Nome
WHERE NomeCantante LIKE 'D%';

-- I titoli dei dischi che contengono canzoni di cui non si conosce l'anno di registrazione;
SELECT  TitoloAlbum
FROM DISCO 
JOIN CONTIENE ON DISCO.NroSerie=CONTIENE.NroSerieDisco
JOIN ESECUZIONE ON CONTIENE.CodiceReg=ESECUZIONE.CodiceReg
WHERE ESECUZIONE.Anno IS NULL;


