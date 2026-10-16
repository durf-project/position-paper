# DURF Position Paper - Draft

_Alastair Dunning (TU Delft), Maurice Vanderfeesten (VU Amsterdam), Simone Kortekaas (KB) and Hilde van Wijngaarde (VU Amsterdam), September 2026_

## Dutch Science and the Role of Libraries

Dutch science is among the most productive and influential in the world: its impact is 72% above the global average<sup><a href="#ref-1">1</a></sup>, and Dutch research institutes publish over 127,000 articles a year<sup><a href="#ref-2">2</a></sup>. Libraries have an essential role in managing, curating, disseminating and preserving that output, through the repositories and CRIS systems that Dutch universities and research institutes have been building since the early 2000s.

That infrastructure is still maturing. While progress has been rapid, it has been lacking in coherent coordination. Metadata, for example, is not created to a unified approach. Researchers struggle with access to paywalled literature. There are limited preservation options for non-traditional outputs. Repository and metadata staff face issues of duplication and lack of standardisation; bulk refinement, exporting and importing of metadata between universities is time-consuming. Staff lack efficient metadata tools and workflows thought through at a national level to reduce workload while improving content coverage.

Additional challenges now loom large. The rise of agentic AI offers both threats and opportunities to scholarly publications; the geopolitical environment threatens many of the international connections that underpinned infrastructures. Digital sovereignty, and greater trust in the reliability of partners, is paramount.

## Aim of this paper

This position paper is a call for university libraries to commit to working together so as to help develop an infrastructure for Dutch scientific output that is shared, mature and resilient.

It is based on the concept of a federation. It acknowledges that university libraries are of different sizes, serve varied communities and have access to different levels of technical skills. It acknowledges that universities use different systems to manage publications, which are all at different levels of sophistication. This makes the creation of a shared technical infrastructure difficult.

Therefore, the immediate focus of DURF, and this position paper, lies on the information chain that is supported by the various repositories and CRIS's, and can do so independent of technical choices that are made about these systems. DURF will create a shared approach for the policies concerning these systems - for metadata entry, for full text harvesting, for dissemination, and for long-term preservation.

There are six themes in the DURF project:

1. Integrate systems under shared governance
2. Enable enriched metadata feedback via the OpenAIRE Graph
3. Increase full-text collection
4. Preserve output via the KB's e-Depot
5. Maximise discoverability through multiple channels, such as OpenAlex, Google, Wikidata and EOSC nodes
6. Provide a Dutch Portal as the outlet for curated research output

These themes will be explained in more detail below.

# The DURF Information Chain

![The DURF information ecosystem: repositories and CRIS systems feed a metadata harvester and validator (OpenAIRE PROVIDE), which populates the OpenAIRE Graph; from there, metadata is enriched (OpenAIRE Broker), made discoverable via the Netherlands Research Portal (OpenAIRE Connect), and preserved long-term via the KB e-Depot and URN resolver.](assets/durf-information-chain.svg)

## Roles and parties

Every box in the diagram above plays a **role** in the chain: the repositories and CRIS's, the harvester, the graph, the broker, the portal, the e-Depot, the resolver. Each role comes with a **responsibility** towards the rest of the chain, as the table below shows. But a role cannot sign a position paper, hold a meeting, or make a pledge - only a **party** can. Every role is taken on by a party, and it is that party which carries the responsibility described throughout this paper, and which can count on the other parties in return.

| Role | Responsibility | Party |
| --- | --- | --- |
| Publishing platforms | Supply full texts and CC0 metadata (publishers, preprint servers) to the repositories | Parties outside DURF's own governance |
| Institutional repository / CRIS | Capture and hold an institution's own research output and its metadata | Each university library |
| Metadata harvester & validator (OpenAIRE PROVIDE) | Collect and check records from repositories and CRIS's | OpenAIRE |
| OpenAIRE Graph | Aggregate, deduplicate and cross-reference records nationally and internationally | OpenAIRE |
| Enrichment (OpenAIRE Broker) | Return quality and enrichment suggestions to the source system | OpenAIRE |
| Netherlands Research Portal (OpenAIRE Connect) | Offer a curated, national outlet for Dutch research output | OpenAIRE, with editorial and functional management by the DURF partners |
| e-Depot | Preserve deposited files for the long term | KB (National Library of the Netherlands) |
| URN:NBN resolver | Keep preserved files reliably citable and linkable | KB |
| Other research indexes (OpenAlex, Google, Wikidata, EOSC nodes) | Offer external discovery channels | Parties outside DURF's own governance |

The OpenAIRE Graph plays a central role in this chain. For the metadata of Dutch research output, the OpenAIRE Graph:

- harvests the metadata from every Dutch repository and CRIS;
- unites and deduplicates it with what it knows from other sources;
- serves it out for specific uses: the Netherlands Research Portal, the KB e-Depot and, through the e-Depot, the URN:NBN resolver.

The full texts and the authoritative records stay with the institutions. This shows where DURF's influence lies: not in the part that OpenAIRE runs, but in what the institutions deliver into the Graph, and in what OpenAIRE delivers out of it.

Bringing these parties together under one set of shared rules is called **federated governance**: rather than one central authority controlling every system, each party - a university library, OpenAIRE, the KB - agrees to a small set of common rules (a shared metadata standard, clear interfaces between systems, how disagreements get resolved), and is then responsible for meeting them within the system it operates. That is the shared governance that the DURF project, under theme 1 below, asks signees to commit to.

### Roles and responsibilities

Being part of the federation is not only a duty to the whole. It rests on reciprocity between the parties operating each system: each takes on specific responsibilities, and can expect something in return. The KB's e-Depot, for example, takes on the *responsibility* to archive and safely back up the Dutch scientific corpus deposited by university repositories - but it can only do so if it can *expect* to receive that metadata and full text from those repositories, in a usable, agreed form. Take either one away, and the other cannot be honoured.

[Appendix A](#a-roles-and-responsibilities-matrix) sets these roles and responsibilities out for every pair of parties in the chain. This position paper is not itself a legal agreement. How they relate to existing agreements, such as those between the KB and the institutions, will be worked out in the formal agreements under theme 1.

# The six themes

Below, for each theme, we describe what DURF aims to achieve and what it asks of the signees.

## 1. Integrate systems under shared governance

Bringing Dutch repositories, CRIS's, the harvester, the graph, the portal and the e-Depot together is bigger than agreeing a metadata standard - that belongs mostly under theme 2, below. This theme is about organising DURF as a research commons: metadata, full text and the infrastructure that carries them become resources that the signing parties manage, maintain and are accountable for together, as a community, rather than separately.

That takes more than good intentions. It takes the right legal structures - to share all fields of metadata openly, to capture and share full text, to jointly maintain and financially uphold the Netherlands Research Portal and OpenAIRE's services, and to commit to backing up content in the KB's e-Depot. These commitments apply both during the DURF project and after it ends. It is these commitments, brought together across all six themes, that this position paper asks its signees to make.

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

A metadata harvester and validator (OpenAIRE PROVIDE) collects records from institutional repositories and CRIS systems into the OpenAIRE Graph, where they are deduplicated, cross-referenced and enriched (OpenAIRE Broker) - with the results fed back to the originating repositories rather than disappearing into a one-way pipeline. Those results are suggestions, not changes: each institution decides which enrichments it accepts into its own system. Aggregation and dissemination of metadata and the related content also becomes much easier if each institute registering research output does so in a unified manner.

Therefore, the signees of the DURF Position Paper agree to:

* form a NL Research Information Content Board, through EduStandaard, to steward the shared metadata standard;
* develop an updated metadata application profile, translating the current NL-DIDL-MODS requirements to OpenAIRE's CERIF and DC guidelines;
* support repositories, CRIS systems and the KB's e-Depot in adopting that profile, and monitor compliance;
* monitor the use of core persistent identifiers (ROR, ORCID, DOI) and promote their local implementation;
* connect their repositories to the OpenAIRE Graph's enrichment feedback loop, and review the suggestions it returns.

### Outputs

* A NL Research Information Content Board, formalised through EduStandaard.
* An updated metadata application profile, aligned with OpenAIRE's CERIF and DC guidelines.
* Each university library, as the party operating its repository/CRIS system, has adopted the updated metadata- and exchange-standards for high-quality research metadata that comply with international guidelines and meet national requirements.
* Monitoring of core PID (ROR, ORCID, DOI) usage, with shared compliance and best-practice reports.
* University libraries regularly harvesting their repository/CRIS content into, and receiving enriched metadata back from, the OpenAIRE Graph.

## 3. Increase full-text collection

Repositories are not just collections of metadata. The collection of the actual research output (whether article, conference paper, book chapter or other output) is also part of the repository's function. Collecting the full text serves various purposes:

* it ensures that the digital object itself, not just its description, is held in public hands, underpinning the university's mission to preserve its intellectual output in the long term
* it allows for the upload and sharing of Green OA articles (particularly under NL's Taverne Agreement)
* it helps create corpora for use in text and data mining
* it provides a corpus for multiple AI uses
* it facilitates better aggregation and dissemination

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

Good metadata is only useful if it reaches researchers where they actually search. Dutch research output should be discoverable not only through institutional repositories, but through the channels researchers actually use: aggregators such as OpenAlex, general search engines such as Google (Scholar), open knowledge bases such as Wikidata, and the network of EOSC nodes that connects European research infrastructure. Wikidata is a particularly strong candidate: it is open, widely reused by other services, and one of the sources used to train AI. Poor-quality metadata endangers findability across every one of these channels, which is why the standardisation and enrichment work above matters here too.

At the moment, universities do their best efforts, but without a standardised approach across these channels that leads to consistently high-quality discoverability.

Discoverability is no longer only about people. DURF wants all publicly funded Dutch research to be open to people and machines alike, including as material on which AI is trained. This is of strategic importance. AI models, wherever in the world they are built, increasingly shape how people find and understand knowledge. Dutch research should be well represented in them, so that the value of Dutch science, and its careful search for what is true, stays present in those models and in the answers they give. That openness needs the right conditions. We want to offer it lawfully and on fair terms, and in a way that keeps it accessible to people: the growing traffic from AI - crawlers, bulk downloads to train language models, and AI assistants searching on someone's behalf - should never make our repositories slow or unreachable for the researchers, students and citizens they are there for.

Therefore, the signees of the DURF Position Paper agree to work towards a shared approach for maximising the discoverability of Dutch research output, for people and machines alike, across OpenAlex, Google, Wikidata, EOSC nodes and other relevant channels, building on the metadata and full-text work above.

### Outputs

* Mappings and best practices for the major indexes, improving the visibility of Dutch research output.
* DOI-minting for grey literature held in DURF repositories.
* A monitoring system tracking DURF content's visibility across the major indexes.

## 6. Provide a Dutch Portal as the outlet for curated research output

Alongside the many channels through which Dutch research output can be discovered, DURF partners also commit to the Netherlands Research Portal (built on OpenAIRE Connect) as the national, curated showcase of that output - a single outlet where the results of shared governance, enriched metadata and full-text collection come together for a Dutch and international audience.

A portal is only as good as the care it gets. The DURF partners therefore do more than deliver their output to it: they share the responsibility for running it, through its editorial care and functional management, and for developing it further. The signees provide the input for new functionality, and so decide together where the portal goes next. If they want to take it in the direction of a public portal, that is possible. The KB's WijsNL project shows what that could look like: a search environment that makes finding and understanding research possible for everyone, starting with the open access publications of researchers at Dutch universities - the very output that DURF brings together. The aim is a portal that serves not only libraries, but everyone who wants clear, understandable access to Dutch research and to the researchers behind it: researchers, policy makers, professionals and citizens looking for knowledge or expertise.

Therefore, the signees of the DURF Position Paper agree to:

* share their curated research output with the Netherlands Research Portal, and keep it up to date;
* take shared responsibility for the portal's editorial care and functional management;
* provide input for new functionality and help develop the portal further, so that researchers, policy makers, professionals and citizens can find and understand Dutch research and the experts behind it;
* support its role as DURF's public-facing outlet.

### Outputs

* A Netherlands Research Portal Steering Committee, with rotating NaMeCo membership.
* Regular stakeholder needs assessments, feeding development roadmaps aligned with OpenAIRE Connect.
* Quarterly portal updates, with a major version released annually.
* Single sign-on to OpenAIRE's PROVIDE, CONNECT and MONITOR services via SURFconext.
* All DURF signatories have their institutional research output represented, and kept up to date, on the Netherlands Research Portal.
* Shared editorial care and functional management of the Netherlands Research Portal by the DURF partners.

# Appendix

## A. Roles and responsibilities matrix

The matrix below can be read two ways. Along a **row**, it lists a system's responsibilities to each system it interacts with. Down a **column**, it lists what that system can expect from the others. The same cell is both at once - a responsibility from one side, an expectation from the other. Blank cells mean no direct relationship in this chain. If any one party cannot commit to its cell, the balance in that relationship - and often others downstream of it - needs to be revisited.

Two examples:

- Find the row **Repository / CRIS** and follow it to the column **e-Depot**. The cell reads "Supply full text & metadata for archiving". So the repository is *responsible* for supplying its full texts and metadata, and the e-Depot can *expect* to receive them.
- Now find the row **e-Depot** and follow it to the column **Repository**. The cell reads "Archive & safely back up the deposited content". So the e-Depot is *responsible* for archiving and backing up, and the repository can *expect* its content to be kept safe.

Together, these two cells, mirrored across the diagonal, show the reciprocity: each side takes something on, and each side gets something back.

The matrix is an illustration of the relationships in the chain, not a legal agreement. How it relates to existing agreements, such as those between the KB and the institutions, will be worked out under theme 1.

<div class="durf-matrix-wrap">
<table class="durf-matrix">
<thead>
<tr><th>Responsibility of &darr; / Expected by &rarr;</th><th>Publishing</th><th>Repository</th><th>Provide</th><th>Graph</th><th>Broker</th><th>Portal</th><th>e-Depot</th><th>Resolver</th><th>Indexes</th></tr>
</thead>
<tbody>
<tr><th>Publishing platforms</th>
<td class="d">&mdash;</td>
<td class="u">Supply full texts and CC0 metadata</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
</tr>
<tr><th>Repository / CRIS</th>
<td class="l">No formal commitment - outside DURF's own governance</td>
<td class="d">&mdash;</td>
<td class="u">Expose complete, standards-compliant metadata for harvesting</td>
<td class="n">&ndash;</td>
<td class="u">Review enrichment suggestions; apply the ones it accepts</td>
<td class="u">Keep its output up to date; share in editorial care &amp; functional management</td>
<td class="u">Supply full text &amp; metadata for archiving</td>
<td class="n">&ndash;</td>
<td class="u">Expose crawlable, standards-compliant metadata</td>
</tr>
<tr><th>Provide (harvester)</th>
<td class="n">&ndash;</td>
<td class="l">Validate records; report errors back</td>
<td class="d">&mdash;</td>
<td class="u">Deliver validated, harvested records</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
</tr>
<tr><th>Graph</th>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="d">&mdash;</td>
<td class="u">Feed aggregated records for enrichment</td>
<td class="u">Supply the aggregated, curated dataset</td>
<td class="u">Route metadata &amp; full text toward preservation</td>
<td class="n">&ndash;</td>
<td class="u">Redistribute enriched metadata externally</td>
</tr>
<tr><th>Broker (enrichment)</th>
<td class="n">&ndash;</td>
<td class="l">Return quality &amp; enrichment signals to source</td>
<td class="n">&ndash;</td>
<td class="l">Return enriched, deduplicated records</td>
<td class="d">&mdash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
</tr>
<tr><th>Portal (Connect)</th>
<td class="n">&ndash;</td>
<td class="l">Present each institution's output clearly to researchers, policy makers, professionals &amp; citizens</td>
<td class="n">&ndash;</td>
<td class="l">Report errors &amp; curation needs spotted in the portal</td>
<td class="n">&ndash;</td>
<td class="d">&mdash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
</tr>
<tr><th>e-Depot</th>
<td class="n">&ndash;</td>
<td class="l">Archive &amp; safely back up the deposited content</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="d">&mdash;</td>
<td class="u">Register preserved items for persistent IDs</td>
<td class="n">&ndash;</td>
</tr>
<tr><th>URN:NBN resolver</th>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="l">Resolve URN:NBN to the current, preserved location</td>
<td class="d">&mdash;</td>
<td class="n">&ndash;</td>
</tr>
<tr><th>Other indexes</th>
<td class="n">&ndash;</td>
<td class="l">No formal commitment - outside DURF's own governance</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="d">&mdash;</td>
</tr>
</tbody>
</table>
</div>

<p class="durf-matrix-legend"><span><i class="u"></i> above the diagonal &mdash; read as an expectation</span><span><i class="l"></i> below the diagonal &mdash; read as a responsibility</span></p>

## B. Technical background: data products, data lake and data contracts

The approach in this paper borrows a few concepts from [data mesh architecture](https://www.datamesh-architecture.com/), which SURF's Open Research Information programme is also exploring for the ORI DuckLake.

- **Data product.** A bundle of a pipeline, the data it produces and a description of what it offers, with an owner who is responsible for it. Applied here: each system in the chain is a shared building block, but the commitments belong to the party operating it.
- **Data lake.** A place where data is refined in layers, often called bronze, silver and gold. DURF builds no lake of its own, but the OpenAIRE Graph plays that role for the metadata: it harvests the metadata as delivered (bronze), unites and deduplicates it (silver), and serves it out for specific uses such as the Netherlands Research Portal, the e-Depot and the resolver (gold). Because the full texts and authoritative records stay with the institutions, the Graph can always be rebuilt from the sources.
- **Data contracts.** The handoffs between parties can be written down as data contracts: machine-readable agreements on what is delivered, in which form and of which quality. Examples exist for every arrow in the diagram, including a Dutch application profile of the OpenAIRE Guidelines for CRIS Managers (see [Read more](#c-read-more)).

The Dutch slice of the OpenAIRE Graph is available as the `netherlands` community, for example through the Graph API: `https://api.openaire.eu/graph/v2/researchProducts?relCommunityId=netherlands&type=publication`.

## C. Read more

1. <a id="ref-1"></a>[Nederland als wetenschapsland 2024](https://assets.ctfassets.net/zlnfaxb2lcqx/01Hzv33cwHLycsbtTCv2QK/cff31c51400a0b3c58a34b439fd15758/Nederland-als-wetenschapsland-2024.pdf) - the source for the Netherlands' impact being 72% above the global average.
2. <a id="ref-2"></a>[OpenAIRE Monitor: research output of the Netherlands](https://monitor.openaire.eu/dashboard/netherlands/research-output/publications/all) - over 127,000 articles per year.
3. NWO, [Future-proofing the Netherlands as a knowledge hub](https://www.nwo.nl/en/future-proofing-the-netherlands-as-a-knowledge-hub): "The Netherlands is a global leader in knowledge and innovation."
4. [Organizing Research as a Commons](https://doi.org/10.5281/zenodo.21468732) - background to theme 1.
5. [The invisible infrastructure: why metadata is now a C-level strategic asset](https://www.helibtech.com/helibtech-viewpoints/the-strategic-pivot-from-collection-management-to-research-enablement-the-invisible-infrastructure-why-metadata-is-now-a-c-level-strategic-asset) - on the OCLC report on metadata; background to theme 2.
6. OCLC Research, _Improving Open Access Discovery for Academic Library Users_. Dublin, Ohio: OCLC Research. <https://doi.org/10.25333/4xem-xr80> - background to theme 5.
7. [Data governance for a federated repository ecosystem](https://durf-project.github.io/durf-data-mesh-architecture/) - how the parties in the chain can deliver their data as data products, with example data contracts.
8. [Netherlands Research Portal - for developers](https://netherlands.openaire.eu/develop) - API access to the Dutch slice of the OpenAIRE Graph.
9. KB, [WijsNL](https://www.kb.nl/over-ons/projecten/wijsnl) - a project for a search environment that makes scientific research findable and understandable for everyone, starting with open access publications by researchers at Dutch universities; background to theme 6.
