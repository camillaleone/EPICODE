-- create table
CREATE TABLE Aeroporto (
  Nome TEXT (20) NOT NULL,
  Citta TEXT (20) NOT NULL,
  Nazione TEXT (30) NOT NULL,
  NumPiste INTEGER (100) NULL);


INSERT INTO Aeroporto (Nome,Citta,Nazione,NumPiste) VALUES   
('Fiumicino','Roma','Italia',10),
('Schiphol','Amsterdam','Paesi Bassi',50),
('Atatürk','Istanbul','Turchia',24),
('Gatwick','Londra','Regno Unito',32),
('Pearson','Toronto','Canada',NULL),
('Guglielmo Marconi','Bologna','Italia',7),
('Charles de Gaulle','Parigi','Francia',NULL),
('Narita','Tokyo','Giappone',78),
('Dubai International','Dubai','Emirati Arabi Uniti',100),
('Pasquale Liberi','Pescara','Italia',2),
('Sandro Pertini','Torino','Italia',NULL);

CREATE TABLE Volo (
    IdVolo VARCHAR (50) PRIMARY KEY,
    GiornoSett VARCHAR (50) NOT NULL,
    CittaPart TEXT (50) NOT NULL,
    OraPart TIME NOT NULL,
    CittaArr TEXT(40) NOT NULL,
    OraArr TIME NOT NULL,
    TipoAereo VARCHAR (50) NOT NULL);

INSERT INTO Volo (IdVolo,GiornoSett,CittaPart,OraPart,CittaArr,OraArr,TipoAereo) VALUES
('AZ274','Lunedì','Roma','10:30','Dubai','12:40','Boeing 777'),
('CS264', 'Martedì', 'New York', '12:00', 'Tokyo', '16:45', 'Boeing 777'),
('ZZ763', 'Mercoledì', 'Torino', '09:30', 'Bologna', '15:15', 'Boeing 747'),
('OK504', 'Giovedì', 'Sydney', '14:45', 'Città del Messico', '21:00', 'Airbus A380'),
('XZ589', 'Venerdì', 'Parigi', '11:15', 'Roma', '13:45', 'Boeing 737'),
('VB676', 'Sabato', 'Toronto', '17:30', 'Berlino', '20:00', 'Airbus A330'),
('RB467', 'Domenica', 'Dubai', '18:45', 'New York', '23:30', 'Boeing 787'),
('HA564', 'Lunedì', 'Berlino', '07:00', 'Londra', '08:45', 'Airbus A319'),
('GH989', 'Martedì', 'Torino', '22:00', 'Sydney', '04:30', 'Boeing 767'),
('YY010', 'Mercoledì', 'Tokyo', '19:30', 'Bologna', '22:15', 'Airbus A350');

CREATE TABLE Aereo (
    TipoAereo VARCHAR (50) NOT NULL,
    NumPasseggeri INTEGER (50) NOT NULL,
    QtaMerci INTEGER (255) NOT NULL);

INSERT INTO Aereo (TipoAereo, NumPasseggeri, QtaMerci) VALUES
    ('Airbus A320', 150, 255),
    ('Boeing 777', 300, 100),
    ('Boeing 747', 400, 150),
    ('Airbus A380', 500, 200),
    ('Boeing 737', 120, 300),
    ('Airbus A330', 250, 87),
    ('Boeing 787', 200, 60),
    ('Airbus A319', 130, 41),
    ('Boeing 767', 180, 70),
    ('Airbus A350', 220, 98);

-- Le città con un aeroporto di cui non è noto il numero di piste
SELECT Citta FROM Aeroporto WHERE NumPiste IS NULL;

-- I tipi di aereo usati nei voli che partono da Torino
SELECT TipoAereo FROM Volo WHERE CittaPart='Torino';

-- Le città da cui partono voli diretti a Bologna
SELECT CittaPart FROM Volo WHERE CittaArr='Bologna';

-- Le città da cui parte e arriva il volo con codice AZ274
SELECT CittaPart, CittaArr FROM Volo WHERE IdVolo='AZ274'
