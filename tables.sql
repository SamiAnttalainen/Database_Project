CREATE TABLE Country (
    CountryID INT NOT NULL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Region VARCHAR(100) NOT NULL,
    UNIQUE (Name)
);

CREATE TABLE Manufacturer (
    ManufacturerID INT NOT NULL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Headquarters VARCHAR(100) NOT NULL,
    EstablishedYear INT,
    CHECK (EstablishedYear >= 1890)
);

CREATE TABLE AirForce (
    AirForceID INT NOT NULL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    CountryID INT,
    Size INT,
    FOREIGN KEY (CountryID) REFERENCES Country(CountryID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Pilot (
    PilotID INT NOT NULL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Rank VARCHAR(100) NOT NULL,
    ExperienceYears INT,
    AirForceID INT,
    FOREIGN KEY (AirForceID) REFERENCES AirForce(AirForceID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE JetModel (
    ModelID INT NOT NULL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    IntroductionYear INT,
    MaxSpeed INT,
    Armament VARCHAR(100),
    ManufacturerID INT,
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturer(ManufacturerID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE INDEX idx_JetModelName ON JetModel(Name);

CREATE TABLE MissionType (
    MissionTypeID INT NOT NULL PRIMARY KEY,
    Description VARCHAR(100) DEFAULT 'No data given'
);

CREATE TABLE Missions (
    ModelID INT NOT NULL,
    MissionTypeID INT NOT NULL,
    PRIMARY KEY (ModelID, MissionTypeID),
    FOREIGN KEY (ModelID) REFERENCES JetModel(ModelID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (MissionTypeID) REFERENCES MissionType(MissionTypeID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE OperatedBy (
    ModelID INT NOT NULL,
    AirForceID INT NOT NULL,
    PRIMARY KEY (ModelID, AirForceID),
    FOREIGN KEY (ModelID) REFERENCES JetModel(ModelID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (AirForceID) REFERENCES AirForce(AirForceID) ON DELETE CASCADE ON UPDATE CASCADE
);