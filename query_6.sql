-- Select all planes and show the air force they belonged to
SELECT JetModel.Name, AirForce.Name
FROM OperatedBy
INNER JOIN JetModel ON OperatedBy.ModelID = JetModel.ModelID
INNER JOIN AirForce ON OperatedBy.AirForceID = AirForce.AirForceID;