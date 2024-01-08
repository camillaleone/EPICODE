-- creo tabella vendite che include ID transazione,categoria del prodotto,costo a cui si è venduto e lo sconto applicato.
CREATE TABLE VENDITE (
  ID_transazione INT PRIMARY KEY,
  Categoria_prodotto VARCHAR (255) NOT NULL,
  Costo DECIMAL (10,2) NOT NULL,
  Sconto_applicato VARCHAR (10)
);


-- creo tabella dettagli vendite include ID transazione, la data della transazione dell’acquisto e la quantità.
CREATE TABLE Dettagli_vendite (
  ID_transazione INT,
  Data_transazione DATE,
  Quantità INT,
  FOREIGN KEY (ID_transazione) REFERENCES VENDITE (ID_transazione)
);


-- inserimento dati in entrambe le tabelle
INSERT INTO VENDITE (ID_transazione,Categoria_prodotto,Costo,Sconto_applicato) VALUES 
  (1, 'Anello', 499.99, '50%'),
  (2, 'Anello', 79.99, '10%'),
  (3, 'Collana', 29.99, '2%'),
  (4, 'Orologio', 149.50, '55%'),
  (5, 'Bracciale', 699.99, '15%'),
  (6, 'Orecchini', 49.95, '90%'),
  (7, 'Anello', 99.75, '12%'),
  (8, 'Bracciale', 19.99, '3%'),
  (9, 'Orologio', 899.99, '20%'),
  (10, 'Orecchini', 199.50, '60%'),
  (11, 'Collana', 599.99, '25%'),
  (12, 'Anello', 89.99, '5%'),
  (13, 'Bracciale', 39.99, '8%'),
  (14, 'Orologio', 169.50, '40%'),
  (15, 'Orecchini', 799.99, '10%'),
  (16, 'Collana', 59.95, '0%'),
  (17, 'Anello', 119.75, '15%'),
  (18, 'Bracciale', 24.99, '7%'),
  (19, 'Orologio', 999.99, '30%'),
  (20, 'Orecchini', 229.50, '50%'),
  (21, 'Collana', 699.99, '20%'),
  (22, 'Anello', 69.99, '15%'),
  (23, 'Bracciale', 19.99, '2%'),
  (24, 'Orologio', 129.50, '25%'),
  (25, 'Orecchini', 899.99, '18%'),
  (26, 'Collana', 54.95, '5%'),
  (27, 'Anello', 89.75, '10%'),
  (28, 'Bracciale', 14.99, '3%'),
  (29, 'Orologio', 1099.99, '35%'),
  (30, 'Orecchini', 249.50, '55%'),
  (31, 'Collana', 799.99, '22%'),
  (32, 'Anello', 79.99, '80%'),
  (33, 'Bracciale', 24.99, '4%'),
  (34, 'Orologio', 139.50, '30%'),
  (35, 'Orecchini', 999.99, '25%'),
  (36, 'Collana', 64.95, '3%'),
  (37, 'Anello', 109.75, '18%'),
  (38, 'Bracciale', 17.99, '5%'),
  (39, 'Orologio', 1199.99, '40%'),
  (40, 'Orecchini', 279.50, '60%'),
  (41, 'Collana', 649.99, '15%'),
  (42, 'Anello', 49.99, '5%'),
  (43, 'Bracciale', 19.99, '2%'),
  (44, 'Orologio', 89.50, '20%'),
  (45, 'Orecchini', 899.99, '70%'),
  (46, 'Collana', 39.95, '0%'),
  (47, 'Anello', 79.75, '12%'),
  (48, 'Bracciale', 12.99, '3%'),
  (49, 'Orologio', 1099.99, '58%'),
  (50, 'Orecchini', 199.50, '30%');


INSERT INTO Dettagli_vendite (ID_transazione, Data_transazione, Quantità) VALUES
  (1, '2023-08-01', 2),
  (7, '2023-09-28', 3),
  (4, '2023-08-01', 1),
  (4, '2023-12-25', 4),
  (5, '2023-05-21', 1),
  (6, '2024-01-06', 2),
  (7, '2023-09-07', 3),
  (8, '2023-03-25', 5),
  (9, '2023-07-10', 1),
  (10, '2023-09-10', 2),
  (50, '2023-08-01', 1),
  (12, '2023-09-28', 2),
  (13, '2023-08-01', 3),
  (14, '2024-01-04', 2),
  (1, '2023-12-25', 1),
  (3, '2024-01-06', 4),
  (17, '2023-09-07', 2),
  (18, '2023-03-25', 3),
  (19, '2023-12-25', 1),
  (20, '2023-09-10', 2),
  (21, '2023-08-01', 3),
  (5, '2023-09-28', 2),
  (23, '2023-08-01', 1),
  (22, '2024-01-04', 2),
  (25, '2023-05-21', 2),
  (33, '2023-12-25', 1),
  (27, '2023-09-07', 3),
  (48, '2023-03-25', 1),
  (29, '2023-07-10', 2),
  (22, '2023-12-25', 3),
  (47, '2023-08-01', 2),
  (8, '2023-09-28', 3),
  (33, '2023-08-01', 1),
  (34, '2024-01-04', 4),
  (35, '2023-05-21', 2),
  (48, '2023-12-25', 1),
  (3, '2023-09-07', 3),
  (38, '2023-03-25', 2),
  (41, '2023-07-10', 1),
  (5, '2023-04-10', 2),
  (41, '2023-08-01', 3),
  (4, '2023-09-28', 2),
  (45, '2023-08-01', 1),
  (8, '2024-01-04', 2),
  (45, '2023-05-21', 2),
  (6, '2023-12-25', 1),
  (47, '2023-09-07', 3),
  (5, '2023-03-25', 1),
  (39, '2023-04-10', 2),
  (9, '2023-09-10', 3);


-- 3.Vendite avvenute in una specifica data, Natale 2023-12-25.
SELECT V.*
FROM VENDITE V
JOIN Dettagli_vendite DV ON V.ID_transazione=DV.ID_transazione
WHERE Data_transazione='2023-12-25';

-- 3.Elenco delle vendite con sconti maggiori del 50%.                                
SELECT *
FROM VENDITE V 
WHERE Sconto_applicato BETWEEN 50 AND 100;
 
-- 4.Calcola il totale delle vendite (costo) per categoria. Anello, Bracciale, Collana, Orologio, Orecchini.
SELECT Categoria_prodotto, SUM(Costo) AS Costo_Totale
FROM VENDITE
GROUP BY Categoria_prodotto;

-- 4.Trova il numero totale di prodotti venduti per ogni categoria.
SELECT Categoria_prodotto, SUM(Quantità) AS Num_Totale_Prodotti_x_Categoria
FROM Dettagli_vendite DV
JOIN VENDITE V WHERE DV.ID_transazione=V.ID_transazione
GROUP BY Categoria_prodotto;

-- 5.Seleziona le vendite dell'ultimo trimestre. Gennaio-Marzo-Aprile, mi darà solo gennaio.
SELECT V.ID_transazione, V.Categoria_prodotto
FROM VENDITE AS V JOIN Dettagli_vendite AS DV ON V.ID_transazione = DV.ID_transazione
WHERE QUARTER(Data_transazione) = QUARTER(CURRENT_DATE) AND YEAR(DV.Data_transazione) = YEAR(CURRENT_DATE);

-- 5. Raggruppa le vendite per mese e calcola il totale delle vendite per ogni mese.
SELECT MONTH(Data_transazione) AS Mese, 
SUM(Costo) AS Totale_Vendite_Mensili
FROM VENDITE V
JOIN Dettagli_vendite DV ON V.ID_transazione = DV.ID_transazione
GROUP BY Mese;

-- 7. Trova la categoria con lo sconto medio più alto.
SELECT Categoria_prodotto, AVG(Sconto_applicato) AS ScontoMedio
FROM VENDITE
GROUP BY Categoria_prodotto
ORDER BY ScontoMedio DESC
LIMIT 1;

-- 8. Confronta le vendite mese per mese per vedere l'incremento o il decremento delle vendite. Calcola l’incremento o decremento mese per mese
SELECT Anno,Mese,Totale_Vendite,
LAG(Totale_Vendite) OVER (ORDER BY Anno, Mese) AS Vendite_Mese_Precedente,
CASE WHEN LAG(Totale_Vendite) OVER (ORDER BY Anno, Mese) IS NULL THEN NULL
ELSE Totale_Vendite - LAG(Totale_Vendite) OVER (ORDER BY Anno, Mese)
END AS Incremento_Decremento
FROM (SELECT YEAR(Data_transazione) AS Anno, MONTH(Data_transazione) AS Mese,
SUM(Costo) AS Totale_Vendite
FROM VENDITE V
JOIN Dettagli_vendite DV ON V.ID_transazione = DV.ID_transazione
GROUP BY Anno, Mese) AS Vendite_Mese_Per_Mese
ORDER BY Anno, Mese;

-- 9. Confronta le vendite totali in diverse stagioni. 
SELECT CASE
WHEN MONTH(Data_transazione) BETWEEN 3 AND 5 THEN 'Primavera'
WHEN MONTH(Data_transazione) BETWEEN 6 AND 8 THEN 'Estate'
WHEN MONTH(Data_transazione) BETWEEN 9 AND 11 THEN 'Autunno'
ELSE 'Inverno'
END AS Stagione,
SUM(Costo) AS Totale_Vendite
FROM VENDITE V
JOIN Dettagli_vendite DV ON V.ID_transazione = DV.ID_transazione
GROUP BY Stagione;

-- 10. Clienti fedeli. Creo tabella clienti con i campi IDCliente, IDVendita, ID_transazione (per collegare alle altre tabelle).TOP 5 Clienti con maggior numero acquisti.
-- AGGIUNGO: Ai top 5 clienti offro sconto 50% sul prossimo acquisto, dal 6 al 10 40% di sconto, 11 a 20 30% di sconto.
CREATE TABLE Clienti (
  ID_Cliente VARCHAR(255) PRIMARY KEY,
  ID_Vendita INT,
  FOREIGN KEY (ID_Vendita) REFERENCES VENDITE (ID_transazione)
);

INSERT INTO Clienti (ID_Cliente, ID_Vendita) VALUES
  ('A1', 1),
  ('A2', 2),
  ('A3', 3),
  ('A4', 4),
  ('A5', 5),
  ('B6', 6),
  ('B7', 7),
  ('B8', 22),
  ('B9', 9),
  ('B10', 45),
  ('C11', 11),
  ('C12', 12),
  ('C13', 13),
  ('C14', 14),
  ('C15', 10),
  ('C16', 16),
  ('C17', 17),
  ('C18', 50),
  ('C19', 19),
  ('C20', 20);

-- query su i top 5 clienti
SELECT Clienti.ID_Cliente, COUNT(Clienti.ID_Vendita) AS Numero_Acquisti
FROM Clienti 
JOIN VENDITE ON Clienti.ID_Vendita = VENDITE.ID_transazione
JOIN Dettagli_vendite ON VENDITE.ID_transazione = Dettagli_vendite.ID_transazione
GROUP BY Clienti.ID_Cliente
ORDER BY Numero_Acquisti DESC
LIMIT 5;

-- sconti per clienti TOP - NON FINITO PER FINE TEMPO
SELECT C.ID_Cliente,
COUNT(C.ID_Vendita) AS Numero_Acquisti,
CASE
WHEN COUNT(C.ID_Vendita) >= 5 THEN 'Sconto del 50%'
WHEN COUNT(C.ID_Vendita) >= 10 THEN 'Sconto del 40%'
WHEN COUNT(C.ID_Vendita) >= 20 THEN 'Sconto del 30%'
END AS Tipo_Sconto
FROM Clienti AS C
JOIN VENDITE AS V ON C.ID_Vendita = V.ID_transazione
GROUP BY C.ID_Cliente
ORDER BY Numero_Acquisti ASC;