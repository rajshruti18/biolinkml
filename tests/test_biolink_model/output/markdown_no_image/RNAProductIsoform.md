
# Type: RNA product isoform


Represents a protein that is a specific isoform of the canonical or reference RNA

URI: [biolink:RNAProductIsoform](https://w3id.org/biolink/vocab/RNAProductIsoform)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[GeneProductIsoform],[RNAProductIsoform&#124;name(i):symbol_type;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;category(i):iri_type%20%2B]uses%20-.->[GeneProductIsoform],[RNAProduct]^-[RNAProductIsoform],[RNAProduct])

## Parents

 *  is_a: [RNAProduct](RNAProduct.md)

## Uses Mixins

 *  mixin: [GeneProductIsoform](GeneProductIsoform.md) - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.

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
