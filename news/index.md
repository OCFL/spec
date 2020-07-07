# News

## Version 1.0 of the Oxford Common File Layout (OCFL) Released

The OCFL Editors are pleased to announce version 1.0 of the Oxford Common File Layout, reflecting over 24 months of 
work by the OCFL Editors and the digital preservation and technology communities.

The initiative originated in September 2017 from informal discussions at a Fedora/Samvera camp in Oxford, UK. These 
discussions identified the need for a simple, non-proprietary, specified, open-standards approach to the layout of 
files for the purpose of preservation persistence. Subsequently, a kickoff community meeting attracted 47 attendees 
from 32 institutions, confirming the need and resulting in the establishment of the OCFL Editors team.

### What is OCFL?
  
The OCFL describes an application-independent approach to the storage of digital information in a structured, 
transparent, and predictable manner. It is designed to promote long-term object management best practices within 
digital repositories. In addition, the OCFL's standardized approach facilitates the migration or transfer of content 
between applications that utilize the specification.

The key design goals and benefits of using the OCFL are:

 - Completeness - A repository can be rebuilt purely from the files it stores.
 - Parsability - By humans and machines, to ensure content can be understood in the absence of the original software.
 - Robustness - Against errors, corruption (accidental or deliberate), and migration between storage technologies.
 - Versioning - Repositories can make changes to objects but their history persists - to allow referential integrity 
and recoverability.
 - Storage diversity - Content can be stored on diverse storage infrastructures including cloud object stores.
 - Efficiency - Many design decisions are made with a view to computational, bandwidth and storage efficiency in the 
light of real world experience.

### What information is available?

The OCFL website at https://ocfl.io, includes the most up to date version of the specification and the implementation 
notes as well as the latest editors draft. 

The [OCFL Specification](https://ocfl.io/1.0/spec/) defines both OCFL Objects, a simple structure for content and a JSON document (inventory.json) 
which provides a straightforward but comprehensive register for the object and versions of its content, and an OCFL 
Storage Root, an arrangement for how OCFL Objects are laid out on physical storage. It also contains examples 
illustrating the use of the OCFL, and explanations that ground decisions in prior experience. 

The companion [OCFL Implementation Notes](https://ocfl.io/1.0/implementation-notes/) contains advice for implementing 
the specification including recommendations for digital preservation, storage handling, client behaviors, and best 
practices for dealing with OCFL Objects in motion.

The OCFL Editors are also releasing [validation rules](https://ocfl.io/validation/validation-codes.html) and [fixture 
objects](https://github.com/OCFL/fixtures) for testing OCFL implementations against the specification. We welcome your 
feedback, questions, use cases, and especially details of any implementations or experimentation with OCFL. 

### How can we get involved?

The OCFL is managed through Github at https://github.com/OCFL and it is open for anyone to raise issues or add use 
cases. The OCFL Editors meet twice monthly with Community Meetings once a month detailing progress and giving the 
opportunity to discuss issues verbally. Details can be found on the OCFL wiki, https://github.com/OCFL/spec/wiki, 
which also contains links to the Slack channel and mailing lists.

### The OCFL Editors

Andrew Hankinson (Bodleian Libraries, University of Oxford)
Neil Jefferies (Bodleian Libraries, University of Oxford)
Rosalyn Metz (Emory University)
Julian Morley (Stanford University)
Simeon Warner (Cornell University)
Andrew Woods (LYRASIS)
