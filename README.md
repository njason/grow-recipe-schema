# Grow Recipe Schema

XML data format to represent grow recipes for plants. Designed for controlled-environment agriculture.

## High-level overview
- [presentation](https://www.youtube.com/watch?v=Zhoeu7jPA-w)
- [slides](https://njason.github.io/grow-recipe-schema/presentation)

[Documentation](https://grow-recipe-schema.readthedocs.io)

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

### Using xmllint

To validate a grow recipe against the schema, run the following xmllint command in the repository root directory:

`xmllint --schema grow-recipe.xsd <path to the recipe XML file>`

## Development

If you make any changes to the schema, you need to verify that all examples and documentations complies to the current state of the schema. To test that all example recipe files in this repository validate against the schema, run this command:

`$ find . -name "*.xml" | xargs xmllint --schema grow-recipe.xsd --noout`

### Documentation

Documentation is stored in the `docs` directory in [reStructuredText](http://docutils.sourceforge.net/rst.html) format and built using [Sphinx](http://www.sphinx-doc.org). To build the documentation, you first need to install Sphinx. To install Sphinx using [pip](https://pip.pypa.io/en/stable/), run:

`pip install -U Sphinx sphinx_rtd_theme`

To build the documentation, run the following command in the repository root:

`sphinx-build -b html docs docs/build`

To view the built documentation, open a browser to `docs/build/index.html`
