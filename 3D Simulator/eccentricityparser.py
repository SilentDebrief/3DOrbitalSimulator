import math

def distance(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)

def angle(x, y):
    return math.atan2(y, x)

def detect_orbits(data):
    orbits = []
    current_orbit = []
    prev_angle = None
    total_angle = 0

    for point in data:
        x, y, _ = point
        current_angle = angle(x, y)
        
        if prev_angle is not None:
            if prev_angle < -math.pi/2 and current_angle > math.pi/2:
                angle_diff = (current_angle - prev_angle) - 2*math.pi
            elif prev_angle > math.pi/2 and current_angle < -math.pi/2:
                angle_diff = (current_angle - prev_angle) + 2*math.pi
            else:
                angle_diff = current_angle - prev_angle
            
            total_angle += angle_diff

            if total_angle >= 2*math.pi:
                orbits.append(current_orbit)
                current_orbit = []
                total_angle = 0

        current_orbit.append(point)
        prev_angle = current_angle

    if current_orbit:
        orbits.append(current_orbit)

    return orbits

def calculate_eccentricity(orbit):
    apoapsis = max(orbit, key=lambda p: distance(*p))
    periapsis = min(orbit, key=lambda p: distance(*p))

    ra = distance(*apoapsis)
    rp = distance(*periapsis)
    a = (ra + rp) / 2
    c = (ra - rp) / 2

    e = c / a

    return e, apoapsis, periapsis, a, c

def read_planet_data(filename):
    planet_data = {}
    current_planet = None
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                current_planet = None
            elif current_planet is None:
                current_planet = line
                planet_data[current_planet] = []
            elif line != "Position History (x, y, z)":
                x, y, z = map(float, line.split(','))
                planet_data[current_planet].append((x, y, z))
    
    return planet_data

# Read data from file
planet_data = read_planet_data("planet_positions.txt")

# Process each planet's data
for planet, data in planet_data.items():
    print(f"\nAnalyzing orbits for {planet}")
    orbits = detect_orbits(data)

    print(f"Number of detected orbits: {len(orbits)}")

    for i, orbit in enumerate(orbits, 1):
        e, apoapsis, periapsis, a, c = calculate_eccentricity(orbit)
        print(f"\nOrbit {i}:")
        print(f"  Number of points: {len(orbit)}")
        print(f"  Apoapsis: {apoapsis}")
        print(f"  Periapsis: {periapsis}")
        print(f"  Semi-major axis (a): {a:.6f}")
        print(f"  Center to focus distance (c): {c:.6f}")
        print(f"  Eccentricity: {e:.6f}")

    # Print eccentricity of the last complete orbit
    if orbits:
        last_complete_orbit = orbits[-1]
        e, _, _, _, _ = calculate_eccentricity(last_complete_orbit)
        print(f"\nEccentricity of the last complete orbit for {planet}: {e:.6f}")
    else:
        print(f"\nNo complete orbits detected for {planet}")