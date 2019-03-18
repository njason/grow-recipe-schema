# Grow Recipe Schema

XML data format to represent grow recipes for plants. Designed for controlled-environment agriculture.

## High-level overview
- [presentation](https://www.youtube.com/watch?v=Zhoeu7jPA-w)
- [slides](https://njason.github.io/grow-recipe-schema/presentation)

[Google XML styling guide](https://google.github.io/styleguide/xmlstyle.html)

**Units Key:**

see http://unitsofmeasure.org/ucum.html

## SDKs
 - [Python](https://github.com/njason/grow-recipe-python)

## Schema validation

The XML Schema Definition file in this repository, `grow-recipe.xsd`, can be used to validate recipe XML files. There are many ways to validate an XML file against a schema. There are many free XML validator web apps that can be found with a search engine. There is also a CLI tool, [xmllint](http://xmlsoft.org/xmllint.html).

### Install xmllint

#### Debian
`$ apt install libxml2-utils`

#### Windows via [Chocolatey](https://chocolatey.org/)
`C:\ choco install xsltproc`

#### macOS
pre-installed
