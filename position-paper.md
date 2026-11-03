# DURF Position Paper - Draft

_Alastair Dunning (TU Delft), Maurice Vanderfeesten (VU Amsterdam), Simone Kortekaas (KB) and Hilde van Wijngaarde (VU Amsterdam), October 2026_

## Dutch Science and the Role of University Libraries

**Dutch Repository Federation:** together we (libraries) are the custodians of the Dutch Scientific Knowledge Corpus, containing [3.4 million publications](https://netherlands.openaire.eu/search/advanced/research-outcomes?type=publication) from the early 1800s until today. For most publications we do not have a copy  in our repositories, which is weakening our academic and digital autonomy.

This Corpus is created throughout time by thousands of researchers and millions of euros of public money were spent on it. 
This makes this Corpus a **highly valuable asset**, serving as a common resource for the public to benefit.

**Mission:** joining this federation makes each of us (libraries) all/together responsible to maintain the services/pieces of a federative Open Science infrastructure for Dutch publicly funded scientific output, so that the Corpus and its services remain open, findable, accessible, available, and resilient in times of commercial and geopolitical turbulence.

## Why / problem statement

Dutch science is among the most productive and influential in the world: its impact is 72% above the global average<sup><a href="#ref-1">1</a></sup>, and Dutch research institutes publish over 127,000 articles a year<sup><a href="#ref-2">2</a></sup>. Libraries have an essential role in managing, curating, disseminating and preserving that output, through the repositories and CRIS systems that Dutch universities and research institutes have been building since the early 2000s.

These distributed but loosely connected systems are still maturing. While progress has been rapid, it has been lacking in coherent coordination.   The Corpus contains 1.9 million publications from 1995 until 2025.

* Metadata in our repositories and CRIS systems are incomplete, on average 50% of the records are missing essential elements like DOI’s and ORCiDs, making it hard to find and connect literature and use the Dutch knowledge corpus for strategic analysis using overpriced commercial databases that come with their biases underrepresenting numerous fields of sciences. 
* But at the core is that **we do not have autonomy of accessing the fulltext** of our own Dutch scientific  knowledge corpus freely at any moment. 67% of the records do not have a file in the repository, which makes us as an academic community  very vulnerable to commercial and geopolitical turbulence. Having the complete full texts also opens new opportunities that grounds a metadata record in truth, allowing us to e.g. custom classification of research and training our own AI models.

> _Figure to come: DURF Full Text Monitor._

Additional challenges now loom large. The rise of agentic AI offers both threats and opportunities to scholarly publications; one threat could be that access to publications can be blocked and held to ransom in negotiations, an opportunity could be that our Dutch science can be well represented in AI models by offering our high quality open knowledge corpus.

## Central Aim of this paper

**This position paper is initially a call for university libraries, KB and OpenAIRE to commit to working together to help develop and sustain a robust backbone infrastructure for Dutch scientific output that is shared, mature and resilient.**  

**Mandate and Context:** This commitment will give aim to the vision of [NPOS2030](https://doi.org/10.5281/zenodo.7433767) signed by the [Dutch covenant parties in 2023](https://www.rijksoverheid.nl/documenten/2023/03/29/open-science-nl-versnelt-transitie-naar-open-science), and the [UNL Open Science Agenda in 2023](https://doi.org/10.5281/zenodo.10362464), and gives aim to the [“academic freedom statement”](https://www.universiteitenvannederland.nl/en/current/news/statement-on-academic-freedom-the-rectors-of-the-dutch-universities-2025) in 2025 by the Dutch university rectors.

**Institutional autonomy challenges**: This backbone is based on the concept of a [federation](https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/europe-expands-access-sharing-and-use-research-data-and-digital-services-through-first-13-open-2026-10-16_en). It acknowledges the value of “institutional autonomy”; translating in that university libraries are of different sizes, serve varied communities and have access to different levels of technical skills. It acknowledges that universities use different systems to manage publications, which are all at different levels of sophistication. But at the same time this makes the creation of a shared information infrastructure a challenge.

**Building a Strong Federation:** Therefore, the immediate focus of DURF, and this position paper, lies on the information chain that is supported by the various repositories and CRIS's, and can do so independent of technical choices that are made about these systems. DURF will create shared approaches, standards and tools for: the policies (theme 1) concerning these systems: for metadata exchange (theme 2), for full text harvesting (theme 3), for dissemination (theme 5), for long-term preservation (theme 4), and for co-management of the Netherlands Research Portal (theme 6).

There are six themes in the DURF project:

- **Theme 1 - Governance:** Integrate systems under shared governance
- **Theme 2 - Metadata:** Enable enriched metadata feedback-loop via the OpenAIRE Graph
- **Theme 3 - Fulltext:** Increase full-text collection
- **Theme 4 - Archive:** Preserve output via the KB's e-Depot
- **Theme 5 - Discovery:** Maximize discoverability through multiple channels, such as OpenAlex, Google, Wikidata and EOSC nodes
- **Theme 6 - Portal:** Provide a Dutch Portal as the outlet for curated research output

These themes will be explained in more detail below.

# The DURF Information Chain


![The DURF information ecosystem: repositories and CRIS systems feed a metadata harvester and validator (OpenAIRE PROVIDE), which populates the OpenAIRE Graph; from there, metadata is enriched (OpenAIRE Broker), made discoverable via the Netherlands Research Portal (OpenAIRE Connect), and preserved long-term via the KB e-Depot and URN resolver. The Dutch part of the OpenAIRE Graph is part of the Dutch EOSC Node.](assets/durf-information-chain.svg)

## Roles, Responsibilities and Parties

Every box in the diagram above plays a **role** in the information chain: the repositories and CRIS's, the harvester, the graph, the broker, the portal, the e-Depot, the resolver, the publishers and the scientific indexes. Each role comes with a **responsibility** towards the rest of the chain, as the table below shows. But a role cannot sign a position paper, hold a meeting, or make a pledge - only a **party** can. Every role is taken on by a party, and it is that party which carries the responsibility described throughout this paper, and which can count on the other parties in return.

This is why we need to form a Dutch Repository Federation, where we can hold each other accountable. The **core parties** in this federation are: the 13 University Libraries **{Hereafter called: UB}** and KB National Library (as [members of UKB](https://ukb.nl/en/about-ukb/participating-members/)) **{Hereafter called: KB}**, and OpenAIRE AMKE (non-profit) **{Hereafter called: OpenAIRE}**. 
The core parties administer the biggest portion of the content in the OpenAIRE Graph that are associated to Dutch research performing organisations as a whole, and therefore form the backbone of this federation.
The federation welcomes all other Dutch (RPO’s) to join on their own pace; these include: UKB associate members (KNAW, OU), University Medical Centers, Universities of Applied Sciences. That are also the co-operation parties of the DURF Project., and also welcomes all the other Research performing organisations that are currently not a co-operation partner of the DURF project. ([listed here](https://www.surf.nl/en/about/members-of-surf))

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

Bringing these parties together under one set of shared rules is called **federated governance**: rather than one central authority controlling every system, each party - a university library, OpenAIRE, the KB - agrees to a small set of common rules (a shared metadata standard, diversity of licence information that allows fair use and ‘open, but closed if necessary’, clear interfaces between systems, how disagreements get resolved, etc. ), and is then responsible for meeting them within the system it operates. That is the shared governance that the DURF project, under theme 1 below, asks signees to commit to.

### Roles and responsibilities

Being part of the federation is not only a duty to the whole. It rests on reciprocity between the parties operating each system: each takes on specific responsibilities, and can expect something in return. The KB's e-Depot, for example, takes on the *responsibility* to archive and safely back up the Dutch scientific corpus deposited by university repositories - but it can only do so if it can *expect* to receive that metadata and full text from those repositories, in a usable, agreed form. Take either one away, and the other cannot be honoured.

[Appendix B](#b-roles-and-responsibilities-matrix) sets these roles and responsibilities out for every pair of parties in the chain. This position paper is not itself a legal agreement. How they relate to existing agreements, such as those between the KB and the institutions, will be worked out in the formal agreements under theme 1.

# The six themes

Below, for each theme, we describe what DURF aims to achieve and what it asks of the signees.

## 1. Integrate systems under shared governance

Bringing Dutch repositories, CRIS's, the harvester, the graph, the portal and the e-Depot together is bigger than agreeing a metadata standard - that belongs mostly under theme 2, below. This theme is about organising DURF as a research commons: metadata, full text and the infrastructure that carries them become resources that the signing parties manage, maintain and are accountable for together, as a community, rather than separately.

That takes more than good intentions. It takes the right legal structures - to share all fields of metadata openly, to capture and share full text, to jointly maintain and financially uphold the Netherlands Research Portal and OpenAIRE's services, and to commit to backing up content in the KB's e-Depot. These commitments apply both during the DURF project and after it ends. It is these commitments, brought together across all six themes, that this position paper asks its signees to make.

### Commitments for Governance

Therefore, the signees of the DURF Position Paper agree the following:

*STRATEGIC:*

* UB’s and KB believe they are the custodians of the Scientific Knowledge Corpus (metadata and full texts), and committed to the same **central aim** stated above.

*TACTICAL:*

* Dutch University Libraries (UB’s) and KB become member of OpenAIRE AMKE (non-profit), and organize themselves in a National Membership Consortium (NaMeCo), giving Dutch institutions formal representation within OpenAIRE;

*OPERATIONAL:*

* We draft and finalise formal agreements (“afspraken stelsel”) on roles and responsibilities  between the parties that operate the systems they maintain to keep the federated infrastructure operational;
* UB’s draft a legal structure (model contract for publisher negotiations)  under which all fields of metadata are shared as CC0, so they can move freely between systems;
* UB’s and KB create a governance framework covering all six themes, reviewed toward the end of the project to keep it sustainable beyond it;
* UB’s and KB jointly fund the shared infrastructure - contributing to the subscription licenses that cover OpenAIRE's operating costs, and costs for functional management of the portal.
* We meet annually, at “DURF Federation Day” a National Symposium and General Assembly, to hold each other to these commitments.


## 2. Enable enriched metadata feedback via the OpenAIRE Graph

High-quality metadata is a condition for a successful repository. Poor metadata can mean broken links or context-free content. It erodes trust, one of the most important values that university repositories should embody.

A metadata harvester and validator (OpenAIRE PROVIDE) collects records from institutional repositories and CRIS systems into the OpenAIRE Graph, where they are deduplicated, cross-referenced and enriched (OpenAIRE Broker) - with the results fed back to the originating repositories rather than disappearing into a one-way pipeline. Those results are suggestions, not changes: each institution decides which enrichments it accepts into its own system. Aggregation and dissemination of metadata and the related content also becomes much easier if each institute registering research output does so in a unified manner.

### Commitments for Metadata

Therefore, the signees of the DURF Position Paper agree the following:

*STRATEGIC:*

* UB’s believe the Scientific Knowledge Corpus is potentially a highly valuable asset when it has high quality metadata. 

*TACTICAL:*

* UB’s make the Scientific Knowledge Corpus available for harvest and quality enrichment to the OpenAIRE Graph, so Dutch research is connected to the European Open Science Cloud Nodes.

*OPERATIONAL:*

* UB’s and KB form a NL Research Information Content Board (formerly known as ‘WISH’), through EduStandaard.nl, to steward the new shared metadata standard;
* UB’s will contribute to develop an updated metadata application profile, translating the current NL-DIDL-MODS requirements to OpenAIRE's CERIF and DC guidelines;
* UB’s support each other in adopting that new profile, and monitor compliance;
* UB’s will monitor the completeness of core persistent identifiers (ROR, ORCID, DOI) within their records and improve the completeness;
* UB’s will test the OpenAIRE’s metadata enrichment feedback-loop to improve completeness, and OpenAIRE will use the evaluation of the test to improve the graph enrichment algorithms.


## 3. Increase full-text collection

Repositories are not just collections of metadata. The collection of the actual research output (whether article, conference paper, book chapter or other output) is also part of the repository's function. Collecting the full text serves various purposes:

* it ensures that the digital object itself, not just its description, is held in public hands, underpinning the university's mission to preserve its intellectual output in the long term
* it allows for the upload and sharing of Green OA articles (particularly under NL's Taverne Agreement)
* it helps create corpora for use in text and data mining
* it provides a corpus for multiple AI uses
* it facilitates better aggregation and dissemination

Despite this, there are various challenges to importing full-text of research output - different tools and methodologies (with varying levels of effectiveness). Too many article PDFs are still missing from repositories, and this can be much better.

### Commitments for Full-texts

Therefore, the signees of the DURF Position Paper agree the following:

*STRATEGIC:*

* UB’s and KB believe they are the custodians of the Dutch Knowledge Corpus, and feel responsible for the availability (findable and accessible) of metadata and full texts of the Dutch Research Literature.

*TACTICAL:*

* UB’s will add full text to ‘empty’ metadata records, within a defined scope, from the past and present. 

*OPERATIONAL:*

* for past records the UB’s come to an agreement on the scope and financial business case of the full-texts completeness of the back-log/back-files to aim for. (e.g only journal articles, closed and open, from that last 5 years, from all or specific publishers.) 
* for new present records the UB’s come to an agreement with the publishers and other venues to exchange the rich metadata and a copy of full text in the read and publish deals, preferably using a standard protocol (e.g. SWORD)
* UB’s will share and teach each other the tools, methods and services to meet these targets within the agreed scope.


## 4. Preserve output via the KB's e-Depot

While university libraries have capacity to manage their research outputs, tasks related to the long term  preservation of digital publications are undertaken by the National Library of the Netherlands (KB). The KB's e-Depot service ensures that files remain accessible in the long term, that they are associated with the right metadata, and - in the event of any digital disaster - that there is also a safe copy of the deposited material. A persistent URN:NBN resolver, also maintained by the KB, keeps preserved files reliably citable and linkable over time. This gives the KB a unique role in relation to university repositories.

### Commitments for Preservation

Therefore, the signees of the DURF Position Paper agree the following:

*STRATEGIC:*

* UB’s and KB believe that the Dutch Scientific Knowledge corpus is a highly valuable asset for generations to come, and must be preserved and be made accessible for the long term.

*OPERATIONAL:*

* The UB’s will share their repository outputs with the e-Depot for the purposes of long-term preservation.
* The KB will preserve and resolve the metadata and full text that is delivered by the UB’s.


## 5. Maximize discoverability through multiple channels

Good metadata is only useful if it reaches researchers where they actually search. Dutch research output should be discoverable not only through institutional repositories, but through the channels researchers actually use: aggregators such as OpenAlex, general search engines such as Google (Scholar), open knowledge bases such as Wikidata, and the network of EOSC nodes that connects European research infrastructure. Wikidata is a particularly strong candidate: it is open, widely reused by other services, and one of the sources used to train AI. 

Discoverability is no longer only for human consumption. We want all publicly funded Dutch research to be open for humans and machines alike. This is of strategic importance. AI models, wherever in the world they are built, increasingly shape how people find and understand knowledge. 
We believe that Dutch research should be well represented in them, so that the value of Dutch science, and its careful search for what is true, stays present in those models and in the answers they give. That openness needs to happen with the right conditions: lawfully and on fair terms.

### Commitments for Discoverability

Therefore, the signees of the DURF Position Paper agree the following:

*STRATEGIC:*

* UB’s believe Dutch research output must be findable and accessible for researchers and the public on a multitude of relevant outlets and venues to maximize discovery.


*OPERATIONAL:*

* UB’s will share and teach each other the tools and methods to maximize the discoverability of Dutch research output, for human consumption and machines alike. 


## 6. Provide a Dutch Portal as the outlet for curated research output

Alongside the many channels through which Dutch research output can be discovered, DURF partners also commit to the Netherlands Research Portal (built on OpenAIRE Connect) as the national, curated showcase of that output - a single outlet where the results of shared governance, enriched metadata and full-text collection come together for a Dutch and international audience.

A portal is only as good as the care it gets. The DURF partners therefore do more than deliver their output to it: they share the responsibility for running it, through its editorial care and functional management, and for developing it further. The signees provide the input for new functionality, and so decide together where the portal goes next. If they want to take it in the direction of a public portal, that is possible. The KB's WijsNL project shows what that could look like: a search environment that makes finding and understanding research possible for everyone, starting with the open access publications of researchers at Dutch universities - the very output that DURF brings together. The aim is a portal that serves not only libraries, but everyone who wants clear, understandable access to Dutch research and to the researchers behind it: researchers, policy makers, professionals and citizens looking for knowledge or expertise.

### Commitments for Portal

Therefore, the signees of the DURF Position Paper agree the following:

*STRATEGIC:*

* UB’s and KB believe the Netherlands Research Portal as the prime public facing outlet of Dutch research, researchers and research projects; so that researchers, policy makers, professionals and citizens can find and understand Dutch research and the experts behind it;

*OPERATIONAL:*

* UB’s share their curated research output with the Netherlands Research Portal, and keep it up to date;
* UB’s and KB take shared and financial responsibility for the portal's editorial care, functional management;
* UB’s and KB take shared and financial responsibility for the technical hosting and maintenance of the portal by OpenAIRE;
* UB’s and KB provide input for new functionality and help develop the portal further;
* OpenAIRE will provide a development roadmap for the Connect Portal implementation.

# Appendix

## A. Data supporting the problem statement

> _To be completed: the sources and figures behind the problem statement - the size of the Corpus (3.4 million publications; 1.9 million from 1995 until 2025), the share of records missing a DOI or ORCID (about 50%), and the share of records without a full-text file (67%), from the DURF Full Text Monitor._


## B. Roles and responsibilities matrix

Each filled cell reads as a sentence. The small label at the top says who it is **from** (the row) and **to** (the column): the role in the row takes on that responsibility, and the role in the column can expect it in return. Blank cells mean no direct relationship in this chain. If any one party cannot commit to its cell, the balance in that relationship - and often others downstream of it - needs to be revisited.

Two examples:

- **Repository &rarr; e-Depot**: the repository supplies its full text and metadata for archiving, and the e-Depot can expect to receive them.
- **e-Depot &rarr; Repository**: the e-Depot shows the repository that this content is safely backed up and archived, so the repository can count on it being kept safe.

Together, these two cells, mirrored across the diagonal, show the reciprocity: each side takes something on, and each side gets something back. Blue cells deliver something onward along the chain; purple cells return something to an earlier link.

The matrix is an illustration of the relationships in the chain, not a legal agreement. How it relates to existing agreements, such as those between the KB and the institutions, will be worked out under theme 1.

<div class="durf-matrix-wrap">
<table class="durf-matrix">
<thead>
<tr><th>From &darr; / To &rarr;</th><th>Publishing</th><th>Repository</th><th>Provide</th><th>Graph</th><th>Broker</th><th>Portal</th><th>e-Depot</th><th>Resolver</th><th>Indexes</th></tr>
</thead>
<tbody>
<tr><th>Publishing platforms</th>
<td class="d">&mdash;</td>
<td class="u" title="Publishing → Repository: Supplies full texts and CC0 metadata"><span class="durf-matrix-from">Publishing &rarr; Repository</span>Supplies full texts and CC0 metadata</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
</tr>
<tr><th>Repository / CRIS</th>
<td class="l" title="Repository → Publishing: No formal commitment - outside DURF's own governance"><span class="durf-matrix-from">Repository &rarr; Publishing</span>No formal commitment - outside DURF's own governance</td>
<td class="d">&mdash;</td>
<td class="u" title="Repository → Provide: Exposes complete, standards-compliant metadata for harvesting"><span class="durf-matrix-from">Repository &rarr; Provide</span>Exposes complete, standards-compliant metadata for harvesting</td>
<td class="n">&ndash;</td>
<td class="u" title="Repository → Broker: Reviews enrichment suggestions; applies the ones it accepts"><span class="durf-matrix-from">Repository &rarr; Broker</span>Reviews enrichment suggestions; applies the ones it accepts</td>
<td class="u" title="Repository → Portal: Keeps its output up to date; shares in editorial care & functional management"><span class="durf-matrix-from">Repository &rarr; Portal</span>Keeps its output up to date; shares in editorial care &amp; functional management</td>
<td class="u" title="Repository → e-Depot: Supplies full text & metadata for archiving"><span class="durf-matrix-from">Repository &rarr; e&#8209;Depot</span>Supplies full text &amp; metadata for archiving</td>
<td class="n">&ndash;</td>
<td class="u" title="Repository → Indexes: Exposes crawlable, standards-compliant metadata"><span class="durf-matrix-from">Repository &rarr; Indexes</span>Exposes crawlable, standards-compliant metadata</td>
</tr>
<tr><th>Provide (harvester)</th>
<td class="n">&ndash;</td>
<td class="l" title="Provide → Repository: Validates harvested records; reports errors back"><span class="durf-matrix-from">Provide &rarr; Repository</span>Validates harvested records; reports errors back</td>
<td class="d">&mdash;</td>
<td class="u" title="Provide → Graph: Delivers validated, harvested records"><span class="durf-matrix-from">Provide &rarr; Graph</span>Delivers validated, harvested records</td>
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
<td class="u" title="Graph → Broker: Feeds aggregated records for enrichment"><span class="durf-matrix-from">Graph &rarr; Broker</span>Feeds aggregated records for enrichment</td>
<td class="u" title="Graph → Portal: Supplies the aggregated, curated dataset"><span class="durf-matrix-from">Graph &rarr; Portal</span>Supplies the aggregated, curated dataset</td>
<td class="u" title="Graph → e-Depot: Routes metadata & full text toward preservation"><span class="durf-matrix-from">Graph &rarr; e&#8209;Depot</span>Routes metadata &amp; full text toward preservation</td>
<td class="n">&ndash;</td>
<td class="u" title="Graph → Indexes: Makes its data openly available via the Graph API and data dumps on Zenodo"><span class="durf-matrix-from">Graph &rarr; Indexes</span>Makes its data openly available via the Graph API and data dumps on Zenodo</td>
</tr>
<tr><th>Broker (enrichment)</th>
<td class="n">&ndash;</td>
<td class="l" title="Broker → Repository: Returns quality & enrichment suggestions to the source"><span class="durf-matrix-from">Broker &rarr; Repository</span>Returns quality &amp; enrichment suggestions to the source</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="d">&mdash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
</tr>
<tr><th>Portal (Connect)</th>
<td class="n">&ndash;</td>
<td class="l" title="Portal → Repository: Presents each institution's output clearly to researchers, policy makers, professionals & citizens; showcases repositories to deposit output in"><span class="durf-matrix-from">Portal &rarr; Repository</span>Presents each institution's output clearly to researchers, policy makers, professionals &amp; citizens; showcases repositories to deposit output in</td>
<td class="n">&ndash;</td>
<td class="l" title="Portal → Graph: Links entities claimed by users & reports graph errors"><span class="durf-matrix-from">Portal &rarr; Graph</span>Links entities claimed by users &amp; reports graph errors</td>
<td class="n">&ndash;</td>
<td class="d">&mdash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
</tr>
<tr><th>e-Depot</th>
<td class="n">&ndash;</td>
<td class="l" title="e-Depot → Repository: Shows the repository its content is safely backed up and archived"><span class="durf-matrix-from">e&#8209;Depot &rarr; Repository</span>Shows the repository its content is safely backed up and archived</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="d">&mdash;</td>
<td class="u" title="e-Depot → Resolver: Registers preserved items for persistent IDs"><span class="durf-matrix-from">e&#8209;Depot &rarr; Resolver</span>Registers preserved items for persistent IDs</td>
<td class="n">&ndash;</td>
</tr>
<tr><th>URN:NBN resolver</th>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="n">&ndash;</td>
<td class="l" title="Resolver → e-Depot: Resolves URN:NBN to the current, preserved location"><span class="durf-matrix-from">Resolver &rarr; e&#8209;Depot</span>Resolves URN:NBN to the current, preserved location</td>
<td class="d">&mdash;</td>
<td class="n">&ndash;</td>
</tr>
<tr><th>Other indexes</th>
<td class="n">&ndash;</td>
<td class="l" title="Indexes → Repository: No formal commitment - outside DURF's own governance"><span class="durf-matrix-from">Indexes &rarr; Repository</span>No formal commitment - outside DURF's own governance</td>
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

<p class="durf-matrix-legend"><span><i class="u"></i> onward along the chain</span><span><i class="l"></i> back to an earlier link</span></p>

## C. Technical background: data products, data lake and data contracts

The approach in this paper borrows a few concepts from [data mesh architecture](https://www.datamesh-architecture.com/), which SURF's Open Research Information programme is also exploring for the ORI DuckLake.

- **Data product.** A bundle of a pipeline, the data it produces and a description of what it offers, with an owner who is responsible for it. Applied here: each system in the chain is a shared building block, but the commitments belong to the party operating it.
- **Data lake.** A place where data is refined in layers, often called bronze, silver and gold. DURF builds no lake of its own, but the OpenAIRE Graph plays that role for the metadata: it harvests the metadata as delivered (bronze), unites and deduplicates it (silver), and serves it out for specific uses such as the Netherlands Research Portal, the e-Depot and the resolver (gold). Because the full texts and authoritative records stay with the institutions, the Graph can always be rebuilt from the sources.
- **Data contracts.** The handoffs between parties can be written down as data contracts: machine-readable agreements on what is delivered, in which form and of which quality. Examples exist for every arrow in the diagram, including a Dutch application profile of the OpenAIRE Guidelines for CRIS Managers (see [Read more](#d-read-more)).

The Dutch slice of the OpenAIRE Graph is available as the `netherlands` community, for example through the Graph API: `https://api.openaire.eu/graph/v2/researchProducts?relCommunityId=netherlands&type=publication`.

## D. Read more

1. <a id="ref-1"></a>[Nederland als wetenschapsland 2024](https://assets.ctfassets.net/zlnfaxb2lcqx/01Hzv33cwHLycsbtTCv2QK/cff31c51400a0b3c58a34b439fd15758/Nederland-als-wetenschapsland-2024.pdf) - the source for the Netherlands' impact being 72% above the global average.
2. <a id="ref-2"></a>[OpenAIRE Monitor: research output of the Netherlands](https://monitor.openaire.eu/dashboard/netherlands/research-output/publications/all) - over 127,000 articles per year.
3. NWO, [Future-proofing the Netherlands as a knowledge hub](https://www.nwo.nl/en/future-proofing-the-netherlands-as-a-knowledge-hub): "The Netherlands is a global leader in knowledge and innovation."
4. [Organizing Research as a Commons](https://doi.org/10.5281/zenodo.21468732) - background to theme 1.
5. [The invisible infrastructure: why metadata is now a C-level strategic asset](https://www.helibtech.com/helibtech-viewpoints/the-strategic-pivot-from-collection-management-to-research-enablement-the-invisible-infrastructure-why-metadata-is-now-a-c-level-strategic-asset) - on the OCLC report on metadata; background to theme 2.
6. OCLC Research, _Improving Open Access Discovery for Academic Library Users_. Dublin, Ohio: OCLC Research. <https://doi.org/10.25333/4xem-xr80> - background to theme 5.
7. [Data governance for a federated repository ecosystem](https://durf-project.github.io/durf-data-mesh-architecture/) - how the parties in the chain can deliver their data as data products, with example data contracts.
8. [Netherlands Research Portal - for developers](https://netherlands.openaire.eu/develop) - API access to the Dutch slice of the OpenAIRE Graph.
9. KB, [WijsNL](https://www.kb.nl/over-ons/projecten/wijsnl) - a project for a search environment that makes scientific research findable and understandable for everyone, starting with open access publications by researchers at Dutch universities; background to theme 6.
