Quick-start
===========

Although the structure of the recipes is strictly defined, all data is optional. An extreme example used to prove this point would be a completely empty recipe.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>

    <recipe>
    </recipe>

The minimum required structure is the XML document declaration and the root recipe element to pass Schema validation. The flexibility to specify as much or little data as desired allows for growers at any skill level to utilize the Growth Recipe Standard. For example, a novice grower whose only defined recipe rule is to maintain a constant air temperature between 18℃  and 24℃  would have his recipe look as such:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>

    <recipe>

      <default>
        <air>
          <temperature min=”18” max=”24” />
        </air>
      <default>

    </recipe>

The `default` node is a special node under the `root` node recipe because it is used to define cycles and metrics which are fallback throughout the grow. The `default` stage should be used primarily to alleviate the need to specify redundant data within the various stages of a grow. Any cycle or metric defined in the `default` stage should be overridden by any matching cycles or metrics defined in other stages. For example, imagine our novice grower has learned that his seeds will germinate faster if the air temperature is increased. The novice grower's recipe might evolve into something like:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>

    <recipe>
    
      <default>
        <air>
          <temperature min=”18” max=”24” />
        </air>
      <default>
        
      <germination>
        <air>
          <temperature min=”26” max=”32” />
        </air>
      </germination>

    </recipe>

Metrics can also be defined in periods within a cycle which can be used to represent different periods of a day. Let's say our novice grower has learned that his plants react positively to dropping the temperature for a certain period of the day. The grower’s recipe might evolve into something like:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>

    <recipe>

      <default>
        <!-- 24 hours -->
        <cycle duration=”86400”>

          <!-- Day Time, 18 hours -->
          <period duration=”64800”>
            <air>
              <temperature min=”18” max=”24” />
            </air>
          </period>

          <!-- Night Time, 6 hours -->
          <period duration=”21600”>
            <air>
              <temperature min=”15” max=”17” />
            </air>
          </period>
          
        </cycle>
      </default>
      
      <germination>
        <air>
          <temperature min=”26” max=”32” />
        </air>
      </germination>

    </recipe>

This example also demonstrates metric and cycle definition specificity. The most specific metric and cycle definitions should always be used at any given time in a grow. Metric and cycle definitions within the current stage should always take priority to ones defined in the default stage. Also, metric definitions defined within the current stage cycle period should take priority over metric definitions defined within the current stage, but outside of the stage cycle. Here is a list of priority when choosing the specificity of a metric definition at a given time from highest to lowest:

1. Current stage, current stage cycle period
2. Current stage outside of stage cycle
3. Default, current cycle period
4. Default, outside of default cycle
