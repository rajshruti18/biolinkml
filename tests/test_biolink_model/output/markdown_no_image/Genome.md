
# Type: genome


A genome is the sum of genetic material within a cell or virion.

URI: [biolink:Genome](https://w3id.org/biolink/vocab/Genome)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[GenomicEntity],[GenomicEntity]^-[Genome&#124;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;name(i):label_type;category(i):iri_type%20%2B])

## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Attributes


### Inherited from genomic entity:

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
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SO:0001026 |
|  | | SIO:000984 |
|  | | WD:Q7020 |

