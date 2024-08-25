import math

def eccentricityCalculator(linearVelocity): 
    linearVelocity = float(linearVelocity)
    G = 6.6743e-11
    marsMass = 6.39e23
    sunMass = 1.989e30
    r = 2.279e11
    energy = (0.5*marsMass*(math.pow(linearVelocity,2))) - ((G*marsMass*sunMass)/r)
    angularMomentum = marsMass*linearVelocity*r
    reducedMass = (marsMass*sunMass)/(marsMass+sunMass)
    param = -G*marsMass*sunMass
    fractionNumerator = (2*energy*(math.pow(angularMomentum,2)))
    fractionDenominator = reducedMass * (math.pow(param,2))
    eccentricity = math.sqrt(1 + (fractionNumerator/fractionDenominator))
    print(eccentricity)

eccentricityCalculator(3413.3)
eccentricityCalculator(6826.6)
eccentricityCalculator(10233.9)
eccentricityCalculator(13645.2)
eccentricityCalculator(17056.5)
eccentricityCalculator(20467.8)
eccentricityCalculator(23879.1)
eccentricityCalculator(27290.4)
eccentricityCalculator(30701.7)
eccentricityCalculator(34113.0)