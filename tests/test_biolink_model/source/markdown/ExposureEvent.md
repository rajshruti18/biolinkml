
# Type: exposure event


A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

URI: [biolink:ExposureEvent](https://w3id.org/biolink/vocab/ExposureEvent)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[DiseaseToExposureAssociation]-%20object%201..1>\[ExposureEvent|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[ExposureEventToPhenotypicFeatureAssociation]-%20subject%201..1>\[ExposureEvent],%20\[ExposureEvent]^-\[Treatment],%20\[ExposureEvent]^-\[ChemicalExposure],%20\[BiologicalEntity]^-\[ExposureEvent])

## Parents

 *  is_a: [biological entity](biological entity.md)

## Children

 * [chemical exposure](chemical exposure.md) - A chemical exposure is an intake of a particular chemical substance
 * [treatment](treatment.md) - A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'

## Referenced by class

 *  **[disease to exposure association](disease to exposure association.md)** *[disease to exposure association➞object](disease_to_exposure_association_object.md)*  <sub>REQ</sub>  **[exposure event](exposure event.md)**
 *  **[exposure event to phenotypic feature association](exposure event to phenotypic feature association.md)** *[exposure event to phenotypic feature association➞subject](exposure_event_to_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[exposure event](exposure event.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](type/IdentifierType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](type/LabelType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](type/IriType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [has receptor](has_receptor.md)  <sub>OPT</sub>
    * Description: the organism or organism part being exposed
    * range: [organismal entity](organismal entity.md)
 * [has route](has_route.md)  <sub>OPT</sub>
    * Description: the process that results in the stressor coming into direct contact with the receptor
    * range: [String](type/String.md)
 * [has stressor](has_stressor.md)  <sub>OPT</sub>
    * Description: the process or entity that the receptor is being exposed to
    * range: [String](type/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | environment |
|  | | exposure |
|  | | experimental condition |
| **Mappings:** | | SIO:000955 |
