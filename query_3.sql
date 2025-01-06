-- Show the name of the manufacturer, the name of the jet model, and the headquarters of the manufacturer
SELECT Manufacturer.Name, JetModel.Name, Manufacturer.Headquarters 
FROM JetModel 
INNER JOIN Manufacturer 
ON JetModel.ManufacturerID = Manufacturer.ManufacturerID;