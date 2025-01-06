-- Select planes that are faster than 2 Mach or were introduced after 1980
SELECT Name, IntroductionYear, MaxSpeed FROM JetModel WHERE MaxSpeed > 2450 OR IntroductionYear > 1980