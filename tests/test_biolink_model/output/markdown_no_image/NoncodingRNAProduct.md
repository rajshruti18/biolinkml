
# Type: noncoding RNA product




URI: [biolink:NoncodingRNAProduct](https://w3id.org/biolink/vocab/NoncodingRNAProduct)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[NoncodingRNAProduct&#124;name(i):symbol_type;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;category(i):iri_type%20%2B]^-[MicroRNA],[RNAProduct]^-[NoncodingRNAProduct],[MicroRNA],[RNAProduct])

## Parents

 *  is_a: [RNAProduct](RNAProduct.md)

## Children

 * [MicroRNA](MicroRNA.md)

## Referenced by class


## Attributes


### Inherited from RNA product:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal)
 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [macromolecular machine➞name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SIO:001235 |

