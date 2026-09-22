# DURF Position Paper - Draft

_Alastair Dunning and Maurice Vanderfeesten, September 2026_

## Dutch Science and the Role of Libraries

Netherlands scientific output is one of the most productive in the world. In terms of its impact, [the Netherlands ranks 72% higher than the global average](https://assets.ctfassets.net/zlnfaxb2lcqx/01Hzv33cwHLycsbtTCv2QK/cff31c51400a0b3c58a34b439fd15758/Nederland-als-wetenschapsland-2024.pdf). The [NWO summarised](https://www.nwo.nl/en/future-proofing-the-netherlands-as-a-knowledge-hub) that "The Netherlands is a global leader in knowledge and innovation. Dutch science is of high quality and excels in international cooperation".

Much of that reputation is anchored in impact of the publications. [According to OpenAIRE, the research institutes of the Netherlands produce over 127,000 articles per year.](https://monitor.openaire.eu/dashboard/netherlands/research-output/publications/all) From so called _high impact journals_ to a mass of subject-specific journals, scientists at Dutch research organisations demonstrate their quality and impact through sharing and publishing the outputs of their research.

Managing these outputs, therefore, is of crucial importance. Libraries have an essential role to play in their management, curation, dissemination and preservation. The pre-Internet role of libraries was simply purchasers of research content from publishers. This is now different. With the onset of CRIS systems, research information and specifically institutional repositories, researchers are a key actor in the very infrastructure that makes research visible and usable.

That infrastructure that libraries support is still maturing. Since the early 2000s, Dutch universities and other research institutes have been building and managing a variety of repository and CRIS systems to manage these research outputs.

While progress has been rapid, it has been lacking in coherent coordination. Metadata, for example, is not created to a unified approach. Researchers struggle with access to paywalled literature. There are limited preservation options for non-traditional outputs. Repository and metadata staff face issues of duplication and lack of standardisation; bulk refinement, exporting and importing of metadata between universities is time-consuming. Staff lack efficient metadata tools and workflows thought through at a national level to reduce workload while improving content coverage.

Additional challenges now loom large. The rise of agentic AI offers both threats and opportunities to scholarly publications; the geopolitical environment threatens many of the international connections that underpinned infrastructures. Digital sovereignty, and greater trust in the reliability of partners, is paramount.

## Aim of this paper

This position paper is a call for university libraries to commit to working together so as to help develop an infrastructure for Dutch scientific output that is shared, mature and resilient.

It is based on the concept of a federation. It acknowledges that university libraries are of different sizes, serve varied communities and have access to different levels of technical skills. It acknowledges that universities use different systems to manage publications, which are all at different levels of sophistication. This makes the creation of a shared technical infrastructure difficult.

Therefore, the immediate focus of DURF, and this position paper, lies on the information chain that is supported by the various repositories and CRIS's, and can do so independent of technical choices that are made about these systems. DURF will create a shared approach for the policies concerning these systems - for metadata entry, for full text harvesting, for dissemination, and for long-term preservation. These are explained in more detail below:

1. Integrate systems under shared governance
2. Enable enriched metadata feedback via the OpenAIRE Graph
3. Increase full-text collection
4. Preserve output via the KB's e-Depot
5. Maximise discoverability through multiple channels, such as OpenAlex, Google and EOSC nodes
6. Provide a Dutch Portal as the outlet for curated research output

# The DURF Information Chain

![The DURF information ecosystem: repositories and CRIS systems feed a metadata harvester and validator (OpenAIRE PROVIDE), which populates the OpenAIRE Graph; from there, metadata is enriched (OpenAIRE Broker), made discoverable via the Netherlands Research Portal (OpenAIRE Connect), and preserved long-term via the KB e-Depot and URN resolver.](assets/durf-information-chain.svg)

## Systems and parties

The diagram above names systems: repositories, CRIS's, a harvester, a graph, a broker, a portal, an e-Depot, a resolver. Each has a distinct function in the chain. But a system cannot sign a position paper, hold a meeting, or make a pledge - only a party can. Every system in the diagram is operated by a party, and it is that party which takes on the obligations, and holds the rights, described throughout this paper.

| System | Function | Operated by |
| --- | --- | --- |
| Institutional repository / CRIS | Captures and holds an institution's own research output and its metadata | Each university library |
| Metadata harvester & validator (OpenAIRE PROVIDE) | Collects and checks records from repositories and CRIS's | OpenAIRE |
| OpenAIRE Graph | Aggregates, deduplicates and cross-references records nationally and internationally | OpenAIRE |
| Enrichment (OpenAIRE Broker) | Returns quality and enrichment signals to the source system | OpenAIRE |
| Netherlands Research Portal (OpenAIRE Connect) | Curated, national outlet for Dutch research output | OpenAIRE, on behalf of DURF |
| e-Depot | Long-term preservation of deposited files | KB (National Library of the Netherlands) |
| URN:NBN resolver | Keeps preserved files reliably citable and linkable | KB |
| Other research indexes (OpenAlex, Google, EOSC nodes) | External discovery channels | Parties outside DURF's own governance |

This resembles what [data mesh architecture](https://www.datamesh-architecture.com/) - the approach SURF's Open Research Information programme is also exploring, for the ORI DuckLake - calls a **data product**: a bundle of a pipeline, the data it produces and a description of what it offers, with an owner who is responsible for it. Applied here: each system above is a shared building block, but the commitments in this position paper belong to the party operating it, not to the system itself.

Bringing these parties together under one set of shared rules is what data mesh calls **federated governance**: rather than one central authority controlling every system, each party - a university library, OpenAIRE, the KB - agrees to a small set of common rules (a shared metadata standard, clear interfaces between systems, how disagreements get resolved), and is then responsible for meeting them within the system it operates. That is the shared governance theme 1, below, asks signees to commit to.

## 1. Integrate systems under shared governance

Bringing Dutch repositories, CRIS's, the harvester, the graph, the portal and the e-Depot together is bigger than agreeing a metadata standard - that belongs mostly under theme 2, below. This theme is about organising DURF as a [research commons](https://doi.org/10.5281/zenodo.21468732): metadata, full text and the infrastructure that carries them become resources that the signing parties manage, maintain and are accountable for together, as a community, rather than separately.

That takes more than good intentions. It takes the right legal structures - to share all fields of metadata openly, to capture and share full text, to jointly maintain and financially uphold the Netherlands Research Portal and OpenAIRE's services, and to commit to backing up content in the KB's e-Depot. It is these commitments, brought together across all six themes above, that this position paper asks its signees to make.

Therefore, the signees of the DURF Position Paper agree to:

* establish a National Membership Consortium (NaMeCo), giving Dutch institutions formal representation within OpenAIRE;
* draft and finalise formal agreements on roles and responsibilities between SURF, NaMeCo institutions, the KB, publishers and OpenAIRE;
* define a legal structure under which all fields of metadata are shared as CC0, so they can move freely between systems;
* create a governance framework covering all six themes, reviewed toward the end of the project to keep it sustainable beyond it;
* jointly fund the shared infrastructure - contributing to the licences that cover OpenAIRE's operating costs, shared among federation members - rather than leaving that cost to a single party;
* meet annually, at a National Symposium and General Assembly, to hold each other to these commitments.

### Outputs

* This position paper, developed and signed by the federation's signatories.
* A National Membership Consortium (NaMeCo), giving Dutch institutions formal representation within OpenAIRE.
* Formal agreements on roles and responsibilities between SURF, NaMeCo institutions, the KB, publishers and OpenAIRE.
* A legal structure for sharing all fields of metadata as CC0.
* A governance framework covering all six themes, reviewed and updated to ensure it is sustainable after the project ends.
* An annual National Symposium and General Assembly for federation members.

## 2. Enable enriched metadata feedback via the OpenAIRE Graph

High-quality metadata is a condition for a successful repository. Poor metadata can mean broken links or context-free content. It erodes trust, one of the most important values that university repositories should embody.

[OCLC Report on Metadata](https://www.helibtech.com/helibtech-viewpoints/the-strategic-pivot-from-collection-management-to-research-enablement-the-invisible-infrastructure-why-metadata-is-now-a-c-level-strategic-asset)

A metadata harvester and validator (OpenAIRE PROVIDE) collects records from institutional repositories and CRIS systems into the OpenAIRE Graph, where they are deduplicated, cross-referenced and enriched (OpenAIRE Broker) - with the results fed back to the originating repositories rather than disappearing into a one-way pipeline. Aggregation and dissemination of metadata and the related content also becomes much easier if each institute registering research output does so in a unified manner.

Therefore, the signees of the DURF Position Paper agree to:

* form a NL Research Information Content Board, through EduStandaard, to steward the shared metadata standard;
* develop an updated metadata application profile, translating the current NL-DIDL-MODS requirements to OpenAIRE's CERIF and DC guidelines;
* support repositories, CRIS systems and the KB's e-Depot in adopting that profile, and monitor compliance;
* monitor the use of core persistent identifiers (ROR, ORCID, DOI) and promote their local implementation;
* connect their repositories to the OpenAIRE Graph's enrichment feedback loop, and act on the signals it returns.

### Outputs

* A NL Research Information Content Board, formalised through EduStandaard.
* An updated metadata application profile, aligned with OpenAIRE's CERIF and DC guidelines.
* Each university library, as the party operating its repository/CRIS system, has adopted the updated metadata- and exchange-standards for high-quality research metadata that comply with international guidelines and meet national requirements.
* Monitoring of core PID (ROR, ORCID, DOI) usage, with shared compliance and best-practice reports.
* University libraries regularly harvesting their repository/CRIS content into, and receiving enriched metadata back from, the OpenAIRE Graph.

## 3. Increase full-text collection

Repositories are not just collections of metadata. The collection of the actual research output (whether article, conference paper, book chapter or other output) is also part of the repository's function. Collecting the full text serves various subsidiary purposes:

* it helps create corpora for use in text and data mining
* it provides a corpus for multiple AI uses
* it facilitates better aggregation and dissemination
* it underpins the university's mission to preserve its intellectual output in the long term
* perhaps most importantly, it allows for the upload and sharing of Green OA articles (particularly under NL's Taverne Agreement)

Despite this, there are various challenges to importing full-text of research output - different tools and methodologies (with varying levels of effectiveness). Too many article PDFs are still missing from repositories, and this can be much better.

Therefore, the signees of the DURF Position Paper agree to add full text to metadata records. They will first agree the detail of any full-text policy - for which records and to which level of completeness do we wish to achieve this aim. They will then use and implement the tools, methods and services developed in the DURF project to meet these agreed targets.

### Outputs

* Baseline metrics and a reporting system for full-text uptake.
* An inventory of existing tools and methods for full-text capture.
* A piloted, shareable full-text capture service - code and practices - ready to roll out ecosystem-wide.
* Measurable, ecosystem-wide improvement in full-text availability by the end of the project.

## 4. Preserve output via the KB's e-Depot

While university libraries have capacity to manage their research outputs, tasks related to the functional preservation of digital files are undertaken by the National Library of the Netherlands (KB). The KB's e-Depot service ensures that files remain accessible in the long term, that they are associated with the right metadata, and - in the event of any digital disaster - that there is also a safe copy of the deposited material. A persistent URN:NBN resolver, also maintained by the KB, keeps preserved files reliably citable and linkable over time. This gives the KB a unique role in relation to university repositories.

Signatories of the DURF Position Paper pledge that they will share their repository outputs with the e-Depot for the purposes of long-term preservation.

### Outputs

* A pull mechanism, partly via OpenAIRE, that brings metadata and full-text publications into the e-Depot.
* All Dutch CRIS and repository content archived and backed up at the KB's e-Depot.
* A monitoring system tracking the preservation status of publications and their metadata.
* A maintained, up-to-date URN:NBN resolver.

## 5. Maximise discoverability through multiple channels

> _Improving Open Access Discovery for Academic Library Users. Dublin, Ohio: OCLC Research. https://doi.org/10.25333/4xem-xr80._

Good metadata is only useful if it reaches researchers where they actually search. Dutch research output should be discoverable not only through institutional repositories, but through the channels researchers actually use: aggregators such as OpenAlex, general search engines such as Google (Scholar), and the network of EOSC nodes that connects European research infrastructure. Poor-quality metadata endangers findability across every one of these channels, which is why the standardisation and enrichment work above matters here too.

At the moment, universities do their best efforts, but without a standardised approach across these channels that leads to consistently high-quality discoverability.

Therefore, the signees of the DURF Position Paper agree to work towards a shared approach for maximising the discoverability of Dutch research output, across OpenAlex, Google, EOSC nodes and other relevant channels, building on the metadata and full-text work above.

### Outputs

* Mappings and best practices for the major indexes, improving the visibility of Dutch research output.
* DOI-minting for grey literature held in DURF repositories.
* A monitoring system tracking DURF content's visibility across the major indexes.

## 6. Provide a Dutch Portal as the outlet for curated research output

Alongside the many channels through which Dutch research output can be discovered, DURF partners also commit to the Netherlands Research Portal (built on OpenAIRE Connect) as the national, curated showcase of that output - a single outlet where the results of shared governance, enriched metadata and full-text collection come together for a Dutch and international audience.

Therefore, the signees of the DURF Position Paper agree to share their curated research output with the Netherlands Research Portal, and to support its role as DURF's public-facing outlet.

### Outputs

* A Netherlands Research Portal Steering Committee, with rotating NaMeCo membership.
* Regular stakeholder needs assessments, feeding development roadmaps aligned with OpenAIRE Connect.
* Quarterly portal updates, with a major version released annually.
* Single sign-on to OpenAIRE's PROVIDE, CONNECT and MONITOR services via SURFconext.
* All DURF signatories have their institutional research output represented, and kept up to date, on the Netherlands Research Portal.

# Rough Ideas and Notes

> _Position Paper does not have to be binding legally; it shows commitment from the library._
>
> _Other deals:_
>
> _Library recognises its role in a shared information chain. Library commits to playing a role in this chain and supporting the other stakeholders. It does this by means of:_
