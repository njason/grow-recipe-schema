Metrics
=======

Metrics are broken down into three topics: Air, Light, and Water. Each metric contains a min and max acceptable value. The smaller the difference between the min and max of a metric, the more strictly it should be regulated. The absence of a metric should indicate that the metric should not be tracked. If a certain metric is supposed to not appear, it should be explicitly defined with a min and max of zero.

Air
---

=================== ===============================
Name                Unit
=================== ===============================
`temperature`       ℃
`relative-humidity` %
`co2`               mg/m\ :sup:`3` (a ppm converter_.)
=================== ===============================

Water
-----

=============================== =============
Name                            Unit
=============================== =============
`temperature`                   ℃
`electro-conductivity`          mS/cm
`dissolved-oxygen`              mg/L (a ppm converter_.)
`oxidizing-reduction-potential` mV
`hardness`                      mg/L
`ph`                            pH
`vpd`                           kPa
`bicarbonate`                   mg/L
`nitrogen`                      mg/L 
`potassium`                     mg/L
`calcium`                       mg/L
`magnesium`                     mg/L
`sulfer`                        mg/L
`iron`                          mg/L
`copper`                        mg/L
`zinc`                          mg/L
`manganese`                     mg/L
`sodium`                        mg/L
`boron`                         mg/L
`chlorine`                      mg/L
`silicon`                       mg/L
`iron-chelates`                 mg/L
`sodium-chloride`               mg/L
=============================== =============

Light
-----
Light metrics are separated into one or more bands. A band is defined as an upper and lower wavelength (nanometers) within the electromagnetic spectrum. A band can also be defined as a specific Color Temperature, determining the warmness or coolness of white light, using Kelvin (K) as units of measure. Within a band a light intensity is defined with the usual min and max values. Light intensity is represented in PPFD (µmol/m\ :sup:`2`\ /s)


.. _converter: http://www.lenntech.com/calculators/ppm/converter-parts-per-million.htm
