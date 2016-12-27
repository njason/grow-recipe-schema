# plant-recipe-schema
Draft for AVF plant recipe standard

Run `$ ./validate.py <xmlfile>` on an XML file to check validation against schema

Run `$ ./redact.py <xmlfile>` to redact a recipe's sensitive data, but maintain the structure



**Units Key:**
http://unitsofmeasure.org/ucum.html
c: celcius
ppm: see [here](https://en.wikipedia.org/wiki/Parts-per_notation#SI-compliant_expressions "Wikipedia")
mv: milli volts



Metric to Unit Key:
water-temp: c
dissolved-oxygen: ppm
oxidizing-reduction-potential: mv
air-co2: ppm


***Stage abbreviations:***
- so: Sow
- g: Germination
- se: Seedling
- j: Juvenile
- a: Adult
- f: Flowering
- d: Dormant

**Metric abbreviations:**
- at: Air Temperature
- co2: CO2
- dli: Daily Light Integral
- p: Photoperiod
- ppf: Photosynthetic Photon Flux
- ppfd: Photosynthetic Photon Flux Density
- rh: Relative Humidity
- s: Spectrum
- wec: Water Electric Conductivity
- wdo: Water Dissolved Oxygen
- wph: Water pH
- wt: Water Temperature
