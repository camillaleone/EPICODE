CREATE TABLE Dipendente (
    ID INT PRIMARY KEY,
    Nome VARCHAR(255),
    Cognome VARCHAR(255),
    Email VARCHAR(255),
    NumeroTelefono VARCHAR(255),
    Data_Assunzione DATE,
    ID_lavoro INT, 
    Salario DECIMAL(10, 2),  
    ID_Manager INT,
    ID_dipartimento INT);
 
    INSERT INTO Dipendente (ID, Nome, Cognome, Email, NumeroTelefono, Data_Assunzione, ID_lavoro, Salario, ID_manager, ID_dipartimento) VALUES
    (001, 'Antonio', 'Rossi', 'antonio.rossi1@email.com', '0853254967', '2023-06-18', 1, 50000.00, NULL, 93),
    (002, 'Mario', 'Biondi', 'mario.biondi2@email.com', '085382193', '2023-02-01', 4, 60000.00, 1, 93),
    (003, 'Luca', 'Verdi', 'luca.verdi3@email.com', '0854321987', '2023-08-10', 2, 55000.00, 1, NULL),
    (004, 'Giulia', 'Neri', 'giulia.neri4@email.com', '0853987654', '2023-06-25', 3, 48000.00, 2, 94),
    (005, 'Francesca', 'Gialli', 'francesca.gialli5@email.com', '0853765482', '2023-01-15', 1, 52000.00, NULL, 92),
    (006, 'Marco', 'Blu', 'marco.blu6@email.com', '0853147852', '2023-03-20', 2, 48000.00, 3, 91),
    (007, 'Sara', 'Rosa', 'sara.rosa7@email.com', '0853987654', '2023-07-05', 3, 55000.00, 2, 96),
    (008, 'Alessio', 'Verde', 'alessio.verde8@email.com', '0853265478', '2023-04-12', 4, 60000.00, 1, 93),
    (009, 'Chiara', 'Marrone', 'chiara.marrone9@email.com', '0853817265', '2023-11-30', 1, 53000.00, NULL, 97),
    (010, 'Giovanni', 'Arancio', 'giovanni.arancio10@email.com', '0853987654', '2023-09-08', 2, 49000.00, 3, 96),
    (011, 'Elena', 'Viola', 'elena.viola11@email.com', '0853987654', '2023-06-02', 3, 51000.00, 1, 95),
    (012, 'Davide', 'Gris', 'davide.gris12@email.com', '0853987654', '2023-08-14', 4, 58000.00, NULL, 92),
    (013, 'Roberta', 'Celeste', 'roberta.celeste13@email.com', '0853987654', '2023-02-28', 1, 54000.00, NULL, 96),
    (014, 'Simone', 'Rame', 'simone.rame14@email.com', '0853987654', '2023-10-10', 2, 47000.00, 3, 97),
    (015, 'Laura', 'Oro', 'laura.oro15@email.com', '0853987654', '2023-06-07', 3, 59000.00, NULL, 92);

CREATE TABLE Dipartimento (
    ID_dipartimento INT PRIMARY KEY,
    Nome_dip VARCHAR(255),
    ID_manager INT,
    ID_location INT
    );

INSERT INTO Dipartimento (ID_dipartimento, Nome_dip, ID_manager, ID_location) VALUES
    (90, 'Vendite', 2, 021),
    (91, 'Amministrazione', 3, 022),
    (92, 'Finanze', 1, 023),
    (93, 'Produzione', 1, 024),
    (94, 'Marketing', 2, 021),
    (95, 'Sviluppo', 1, 022),
    (96, 'Logistica', 6, 023),
    (97, 'Assistenza Clienti', 2, 020);

-- Visualizzare la data di assunzione dei manager e i loro id appartenenti al dipartimento ’Amministrazione’ nel formato Nome mese, giorno, anno
SELECT DATE_FORMAT (Data_assunzione,'%m/%d/%Y') AS Data_Assunzione_Manager , Dipendente.ID
FROM Dipendente 
JOIN Dipartimento ON Dipartimento.ID_manager = Dipendente.ID_manager
WHERE Dipartimento.Nome_dip = 'Amministrazione';

-- Visualizzare il nome e il cognome dei dipendenti assunti nel mese di Giugno
SELECT Nome, Cognome
FROM Dipendente
WHERE Data_Assunzione=06;