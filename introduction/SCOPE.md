# Scope

"File storage" is a broad topic, and can encompass everything from hardware requirements to metadata policies.
Although these are important considerations, the decisions around many of these lie at the organizational level,
and are dependent on local needs and policies. For the OCFL efforts, therefore, the scope of our work will be narrowly
constrained to specifying a file-and-folder hierarchy (or equivalent metaphor) for digital content storage.

## In Scope {#in-scope}

### File-and-folder layout for digital objects {#folder-layout}

The OCFL exists 

## Out of Scope {#out-of-scope}

### Filesystems

We will consider all filesystem formats to be equivalent in their impact on long-term storage. 
There will be no consideration given to the benefits or risks of ZFS or EXT4, for example. Proprietary
or hardware-specific formats (e.g., Isilon OneFS), formats for distributed content delivery (e.g., Hadoop HDFS)
or Object storage (e.g., Ceph or Amazon S3) are taken to be equivalent for the purposes of OCFL, so long
as the filesystem follows a hierarchical storage metaphor.

### Formats

To be useful to the broadest audiences, there will be no effort at standardizing
the contents of a Digital Object beyond the administrative metadata
required to enable OCFL functionality. There will be no efforts at specifying a required metadata format
(e.g., METS or Dublin Core), or binary formats (e.g., PDF/A, TIFF) that form the contents
of an OCFL object.

### Software

While software will be a necessary product of the OCFL, the specification process will not
engage in software development. We will, however, welcome and indeed expect feedback to the specification
from software implementations.

## Complementary specifications

The OCFL specification may refer to existing, complementary specifications that can 
enhance or enable extended functionality, but for which their functionality is not core. These
might include other folder hierarchy practices (e.g., PairTree),
digital preservation event logging (e.g., PREMIS), or standards
for digital object transfer (e.g., BagIt). 
