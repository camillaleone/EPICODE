-- 1. Trova il totale delle vendite per ogni mese
SELECT MONTH(DataTransazione) AS mese,
SUM(QuantitaAcquistata) AS TotaleVendite
FROM transazioni 
GROUP BY mese;

-- 2. Identifica i tre prodotti più venduti e la loro quantità venduta.
SELECT NomeProdotto, t.ProdottoID,
SUM(QuantitaAcquistata) AS QuantitàVenduta
FROM transazioni t
JOIN prodotti p ON t.ProdottoID=p.ProdottoID
GROUP BY NomeProdotto, t.ProdottoID
ORDER BY QuantitàVenduta DESC
LIMIT 3;

-- 3. Trova il cliente che ha effettuato il maggior numero di acquisti.
SELECT c.NomeCliente,t.ClienteID,
SUM(t.QuantitaAcquistata) AS NumeroAcquisti
FROM transazioni t
JOIN clienti c ON c.ClienteID = t.ClienteID
GROUP BY c.NomeCliente, t.ClienteID
ORDER BY NumeroAcquisti DESC
LIMIT 1;

-- 4. Calcola il valore medio di ogni transazione. *NON USIAMO IMPORTO TRANSAZIONE MA PREZZO*QUANTITA
SELECT MONTH(DataTransazione) AS Mese,p.Categoria,
SUM(QuantitaAcquistata*Prezzo)/COUNT(t.ProdottoID) AS ValoreMedio
FROM transazioni t
JOIN prodotti p ON p.ProdottoID = t.ProdottoID
GROUP BY MONTH(DataTransazione),p.Categoria
ORDER BY MONTH(DataTransazione);

-- 5. Determina la categoria di prodotto con il maggior numero di vendite.
SELECT p.Categoria,
SUM(t.QuantitaAcquistata) AS TotaleVendite
FROM transazioni t
JOIN prodotti p ON p.ProdottoID=t.ProdottoID 
GROUP BY p.Categoria
ORDER BY TotaleVendite DESC
LIMIT 1;

-- 6. Identifica il cliente con il maggior valore totale di acquisti.
SELECT t.ClienteID, 
SUM(QuantitaAcquistata*Prezzo) AS TotaleValoreSpeso
FROM transazioni t
JOIN prodotti p ON p.ProdottoID=t.ProdottoID
GROUP BY t.ClienteID
ORDER BY TotaleValoreSpeso DESC
LIMIT 1;

-- 7. Calcola la percentuale di spedizioni con "Consegna Riuscita".
SELECT
(COUNT(CASE WHEN StatusConsegna = 'Consegna Riuscita' THEN 1 END) / COUNT(*)) * 100 AS PercentualeConsegnaRiuscita
FROM spedizioni;

-- 8. Trova il prodotto con la recensione media più alta.
SELECT r.ProductID, AVG(Rating) AS MediaPiùAlta, COUNT(Rating) AS Recensioni
FROM recensioni r
JOIN prodotti p ON p.ProdottoID=r.ProductID
GROUP BY r.ProductID
ORDER BY MediaPiùAlta DESC, Recensioni DESC 
LIMIT 1;

-- 9. Calcola la variazione percentuale nelle vendite rispetto al mese precedente.
SELECT MONTH(DataTransazione) as Mese, 
YEAR(DataTransazione) as Anno,
SUM(QuantitaAcquistata*Prezzo) AS TotaleVenditeMese,
((SUM(QuantitaAcquistata*Prezzo) - LAG(SUM(QuantitaAcquistata*Prezzo), 1, 0) OVER(ORDER BY MONTH(DataTransazione))) / LAG(SUM(QuantitaAcquistata*Prezzo), 1, 0) OVER(ORDER BY MONTH(DataTransazione))) AS VariazioneVenditePercentuale
FROM transazioni t
JOIN prodotti p on p.ProdottoID =t.ProdottoID
GROUP BY 
MONTH(DataTransazione), 
YEAR(DataTransazione);

-- 10. Determina la quantità media disponibile per categoria di prodotto.
SELECT Categoria, AVG(QuantitaDisponibile-QuantitaAcquistata) AS QuantitaMediaDisponibile
FROM prodotti p
JOIN transazioni t ON t.ProdottoID=p.ProdottoID
GROUP BY Categoria;

-- 11. Trova il metodo di spedizione più utilizzato.
SELECT MetodoSpedizione, COUNT(MetodoSpedizione) AS NumeroSpedizioni
FROM spedizioni
GROUP BY MetodoSpedizione
ORDER BY MetodoSpedizione DESC;

-- 12. Calcola il numero medio di clienti registrati al mese.
SELECT AVG(clienti) AS Media, SUM(CLIENTI) AS Clienti, COUNT(Mesi) AS Mesi
FROM(
SELECT MONTH(DataRegistrazione) AS Mesi, YEAR(DataRegistrazione) AS Anno, COUNT(ClienteID) AS Clienti
FROM clienti
GROUP BY MONTH(DataRegistrazione), YEAR(DataRegistrazione)) CONTEGGIO;

-- 13. Identifica i prodotti con una quantità disponibile inferiore alla media.
WITH QuantitaDopoTransazioni AS (
    SELECT prodotti.NomeProdotto,
           (prodotti.QuantitaDisponibile - coalesce(SUM(transazioni.QuantitaAcquistata), 0)) AS QuantitaDopoTransazioni
    FROM prodotti 
    LEFT JOIN transazioni ON prodotti.ProdottoID = transazioni.ProdottoID
    GROUP BY prodotti.ProdottoID, prodotti.QuantitaDisponibile, prodotti.NomeProdotto)
SELECT NomeProdotto, QuantitaDopoTransazioni
FROM QuantitaDopoTransazioni
WHERE QuantitaDopoTransazioni < (SELECT AVG(QuantitaDopoTransazioni) FROM QuantitaDopoTransazioni)
ORDER BY QuantitaDopoTransazioni;

-- 14. Per ogni cliente, elenca i prodotti acquistati e il totale speso.
SELECT c.NomeCliente, c.ClienteID, p.ProdottoID, t.QuantitaAcquistata,
SUM(p.Prezzo*t.QuantitaAcquistata) AS TotaleSpeso
FROM clienti c
JOIN transazioni t ON c.ClienteID = t.ClienteID
JOIN prodotti p ON t.ProdottoID = p.ProdottoID
GROUP BY c.NomeCliente, c.ClienteID,p.ProdottoID,t.QuantitaAcquistata
ORDER BY c.NomeCliente, c.ClienteID DESC, p.ProdottoID, t.QuantitaAcquistata;

-- 15. Identifica il mese con il maggior importo totale delle vendite.
SELECT MONTH (DataTransazione) AS Mese,
SUM(p.Prezzo*t.QuantitaAcquistata) AS ImportoTotale
FROM transazioni t
JOIN prodotti p ON t.ProdottoID=p.ProdottoID
GROUP BY Mese
ORDER BY ImportoTotale DESC
LIMIT 1;

-- 16. Trova la quantità totale di prodotti disponibili in magazzino.
WITH QuantitaDopoOrdini AS (
    SELECT p.ProdottoID, 
           (p.QuantitaDisponibile - COALESCE(SUM(t.QuantitaAcquistata), 0)) AS QuantitaDisponibileDopoOrdini
    FROM prodotti p 
    LEFT JOIN transazioni t ON p.ProdottoID = t.ProdottoID
    GROUP BY p.ProdottoID, p.QuantitaDisponibile
)
SELECT SUM(QuantitaDisponibileDopoOrdini) AS Quantita_Tot_Disponibile_Dopo_Ordini
FROM QuantitaDopoOrdini
ORDER BY Quantita_Tot_Disponibile_Dopo_Ordini;


-- 17. : Identifica i clienti che non hanno effettuato alcun acquisto.
SELECT c.NomeCliente
FROM clienti c
LEFT JOIN transazioni t ON c.ClienteID = t.ClienteID
WHERE t.ClienteID IS NULL
GROUP BY c.NomeCliente;

-- 18: Calcola il totale delle vendite per ogni anno.
SELECT YEAR (DataTransazione) AS Anno,
SUM(p.Prezzo*t.QuantitaAcquistata) AS ImportoTotaleAnnuo
FROM transazioni t
JOIN prodotti p ON t.ProdottoID=p.ProdottoID
GROUP BY Anno
ORDER BY ImportoTotaleAnnuo;

-- 19: Trova la percentuale di spedizioni con "In Consegna" rispetto al totale.
SELECT (COUNT(CASE WHEN StatusConsegna = 'In Consegna' THEN 1 END) * 100) / COUNT(*) AS PercentualeInConsegna
FROM spedizioni;

-- +++ 20 - I 5 prodotti più redditizi.
SELECT p.Categoria, p.NomeProdotto, 
SUM(Prezzo) AS RicavoTotale
FROM prodotti p
GROUP BY p.Categoria, p.NomeProdotto
ORDER BY RicavoTotale DESC
LIMIT 5;

-- +++ 21 - Quali prodotti vendono meglio in determinati periodi dell’anno?
SELECT ProdottoID, DATE_FORMAT(DataTransazione, '%Y-%m') AS Mese, SUM(QuantitaAcquistata) as VenditeTotali
FROM Transazioni
GROUP BY ProdottoID, Mese
ORDER BY VenditeTotali DESC
LIMIT 10;

-- +++ 22 - Categoria con recensioni più alte e categoria con recensioni più basse.
SELECT Categoria, AVG(Rating) AS MediaRecensioni
FROM Prodotti p
JOIN Recensioni r ON p.ProdottoID = r.ProductID
GROUP BY Categoria
ORDER BY MediaRecensioni DESC, Categoria;


-- AGGIUNTIVA Seleziona i primi 3 clienti che hanno il prezzo medio di acquisto più alto in ogni categoria di prodotto.
SELECT c.ClienteID, p.Categoria, AVG(t.QuantitaAcquistata * p.Prezzo) AS PrezzoMedioAcquisto
FROM transazioni t
JOIN clienti c ON t.ClienteID = c.ClienteID
JOIN prodotti p ON t.ProdottoID = p.ProdottoID
GROUP BY c.ClienteID, p.Categoria
ORDER BY PrezzoMedioAcquisto DESC
LIMIT 3;