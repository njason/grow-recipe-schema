Getting Started
===============

Say you are given an instruction to keep the air temperature above 65℉. This is how you can translate this requirement into a grow recipe:

.. literalinclude:: code/getting-started/example1.xml
   :language: xml

Notice the conversion from Fahrenheit to Celsius. All metrics defined in a grow recipe are standardized to SI_. A complete list of metric types and their units can be found in :doc:`metrics`.

Next, say you are now given a second instruction keep the air temperature between 75℉ and 85℉ during flowering. You can add this second instruction into you existing recipe:

.. literalinclude:: code/getting-started/example2.xml
   :language: xml

.. _SI: https://en.wikipedia.org/wiki/International_System_of_Units
