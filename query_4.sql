-- Show pilots and air force and country
SELECT Pilot.Name, AirForce.Name, Country.Name
FROM Pilot
INNER JOIN AirForce ON Pilot.AirForceID = AirForce.AirForceID
INNER JOIN Country ON AirForce.CountryID = Country.CountryID;