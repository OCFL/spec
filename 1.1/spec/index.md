---
no_site_title: true
---
<img src="https://avatars0.githubusercontent.com/u/35607965" alt="OCFL Hand-drive logo" style="float:right;width:307px;height:307px;"/>
# Oxford Common File Layout Specification
{:.no_toc}

7 October 2022

**This Version:**
* <https://ocfl.io/1.1/spec/>

**Latest Published Version:**
* <https://ocfl.io/latest/spec/>

**Editors:**

* [Neil Jefferies](https://orcid.org/0000-0003-3311-3741), [Bodleian Libraries, University of Oxford](http://www.bodleian.ox.ac.uk/)
* [Rosalyn Metz](https://orcid.org/0000-0003-3526-2230), [Emory University](https://web.library.emory.edu/)
* [Julian Morley](https://orcid.org/0000-0003-4176-1933), [Stanford University](https://library.stanford.edu/)
* [Simeon Warner](https://orcid.org/0000-0002-7970-7855), [Cornell University](https://www.library.cornell.edu/)
* [Andrew Woods](https://orcid.org/0000-0002-8318-4225), [Harvard University](https://library.harvard.edu/)

**Former Editors:**

* [Andrew Hankinson](https://orcid.org/0000-0003-2663-0003)

**Additional Documents:**

* [Implementation Notes](https://ocfl.io/1.1/implementation-notes/)
* [Specification Change Log](https://ocfl.io/1.1/spec/change-log.html)
* [Validation Codes](https://ocfl.io/1.1/spec/validation-codes.html)
* [Extensions](https://github.com/OCFL/extensions/)

**Previous Version:**
* <https://ocfl.io/1.0/spec/>

**Repository:**
* [Github](https://github.com/ocfl/spec)
* [Issues](https://github.com/ocfl/spec/issues)
* [Commits](https://github.com/ocfl/spec/commits)
* [Use Cases](https://github.com/ocfl/Use-Cases)

This document is licensed under a [Creative Commons Attribution 4.0
License](https://creativecommons.org/licenses/by/4.0/). [OCFL logo:
"hand-drive"](https://avatars0.githubusercontent.com/u/35607965) by
[Patrick Hochstenbach](http://orcid.org/0000-0001-8390-6171) is
licensed under [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/).

## Introduction
{:.no_toc #abstract}

_This section is non-normative._

This Oxford Common File Layout (OCFL) specification describes an application-independent approach to the storage of
digital objects in a structured, transparent, and predictable manner. It is designed to promote long-term access and
management of digital objects within digital repositories.

### Need
{:.no_toc #need}

The OCFL initiative began as a discussion amongst digital repository practitioners to identify well-defined, common, and
application-independent file management for a digital repository's persisted objects and represents a specification of
the community’s collective recommendations addressing five primary requirements: completeness, parsability, versioning,
robustness, and storage diversity.

#### Completeness
{:.no_toc #completeness}

The OCFL recommends storing metadata and the content it describes together so the OCFL object can be fully understood in
the absence of original software. The OCFL does not make recommendations about what constitutes an object, nor does it
assume what type of metadata is needed to fully understand the object, recognizing those decisions may differ from one
repository to another. However, it is recommended that when making this decision, implementers consider what is
necessary to rebuild the objects from the files stored.

#### Parsability
{:.no_toc #parsability}

One goal of the OCFL is to ensure objects remain fixed over time. This can be difficult as software and infrastructure
change, and content is migrated. To combat this challenge, the OCFL ensures that both humans and machines can understand
the layout and corresponding inventory regardless of the software or infrastructure used. This allows for humans to read
the layout and corresponding inventory, and understand it without the use of machines. Additionally, if existing
software were to become obsolete, the OCFL could easily be understood by a light weight application, even without the
full feature repository that might have been used in the past.

#### Versioning
{:.no_toc #versioning}

Another need expressed by the community was the need to update and change objects, either the content itself or the
metadata associated with the object. The OCFL relies heavily on the prior art in the \[[Moab](#ref-moab)\] Design for
Digital Object Versioning which utilizes forward deltas to track the history of the object. Utilizing this schema allows
implementers of the OCFL to easily recreate past versions of an OCFL object. Like with objects, the OCFL remains silent
on when versioning should occur recognizing this may differ from implementation to implementation.

#### Robustness
{:.no_toc #robustness}

The OCFL also fills the need for robustness against errors, corruption, and migration. The versioning schema ensures an
OCFL object is robust enough to allow for the discovery of human errors. The fixity checking built into the OCFL via
content addressable storage allows implementers to identify file corruption that might happen outside of normal human
interactions. The OCFL eases content migrations by providing a technology agnostic method for verifying OCFL objects
have remained fixed.

#### Storage diversity
{:.no_toc #storage-diversity}

Finally, the community expressed a need to store content on a wide variety of storage technologies. With that in mind,
the OCFL was written with an eye toward various storage infrastructures including cloud object stores.

### Note
{:.no_toc #note}

This normative specification describes the nature of an OCFL Object (the "object-at-rest") and the arrangement of OCFL
Objects under an OCFL Storage Root. A set of recommendations for how OCFL Objects should be acted upon (the
"object-in-motion") can be found in the \[[OCFL-Implementation-Notes](#ref-ocfl-implementation-notes)\]. The OCFL
editorial group recommends reading both the specification and the implementation notes in order to understand the full
scope of the OCFL.

This specification is designed to operate on storage systems that employ a hierarchical metaphor for presenting data to
users. On traditional disk-based storage this may take the form of files and directories, and this is the terminology we
use in this specification since it is widely known. However, it may equally apply to object stores, where namespaces,
containers, and objects present a similar organization hierarchy to users.

## Table of Contents
{:.no_toc #table-of-contents}

* TOC placeholder (required by kramdown)
{:toc}

## 1. Conformance
{: #conformance}

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this
specification are non-normative. Everything else in this specification is normative.

The key words <span class="rfc2119">MAY</span>, <span class="rfc2119">MUST</span>, <span class="rfc2119">MUST
NOT</span>, <span class="rfc2119">SHOULD</span>, and <span class="rfc2119">SHOULD NOT</span> are to be interpreted as
described in \[[RFC2119](#ref-rfc2119)\].

## 2. Terminology
{: #terminology}

* <a name="dfn-content-path"/>**Content Path:** The file path of a file on disk or in an object store, relative to the
[OCFL Object Root](#dfn-ocfl-object-root). Content paths are used in the [Manifest](#dfn-manifest) within an
[Inventory](#dfn-inventory).

* <a name="dfn-digest"/>**Digest:** An algorithmic characterization of the contents of a file conforming to a standard
digest algorithm.

* <a name="dfn-extension"/>**Extension:** Extensions are used to collaborate, review, and publish additional
non-normative functions related to OCFL. Extensions are intended to be informational and cite-able, but outside the
scope of the normal specification process. Registered extensions may be found in the [OCFL Extensions
repository.](https://ocfl.github.io/extensions/)

* <a name="dfn-inventory"/>**Inventory:** A file, expressed in JSON, that tracks the history and current state of an
OCFL Object.

* <a name="dfn-logical-path"/>**Logical Path:** A path that represents a file's location in the [logical
state](#dfn-logical-state) of an object. Logical paths are used in conjunction with a digest to represent the file name
and path for a given bitstream at a given version.

* <a name="dfn-logical-state"/>**Logical State:** A grouping of logical paths tied to their corresponding bitstreams
that reflect the state of the object content for a given version.

* <a name="dfn-logs-directory"/>**Logs Directory:** A directory for storing information about the content (e.g., actions
performed) that is not part of the content itself.

* <a name="dfn-manifest"/>**Manifest:** A section of the [Inventory](#dfn-inventory) listing all files and their digests
within an OCFL Object.

* <a name="dfn-ocfl-object"/>**OCFL Object:** A group of one or more content files and administrative information, that
together have a unique identifier. The object may contain a sequence of versions of the files that represent the
evolution of the object's contents.

* <a name="dfn-ocfl-object-root"/>**OCFL Object Root:** The base directory of an [OCFL Object](#dfn-ocfl-object),
identified by a \[[NAMASTE](#ref-namaste)\] file "0=ocfl_object_1.1".

* <a name="dfn-ocfl-storage-root"/>**OCFL Storage Root:** A base directory used to store OCFL Objects, identified by a
\[[NAMASTE](#ref-namaste)\] file "0=ocfl_1.1".

* <a name="dfn-ocfl-version"/>**OCFL Version:** The state of an [OCFL Object](#dfn-ocfl-object)'s content which is
constructed using the incremental changes recorded in the sequence of corresponding and prior version directories.

* <a name="dfn-registered-extension-name"/>**Registered Extension Name:** The registered name of an extension is the
name provided in the _Extension Name_ property of the extension's definition in the [OCFL Extensions
repository](https://ocfl.github.io/extensions/).

## 3. OCFL Object
{: #object-spec}

An OCFL Object is a group of one or more content files and administrative information, that are together identified by a
URI. The object may contain a sequence of versions of the files that represent the evolution of the object's contents.

A file is defined as a content bitstream that can be stored and transmitted. Directories (also called "folders") allow
for the organization of files into tree-like hierarchies. The content of an OCFL Object is the files and the directories
they are organized in that are stored _within_ the hierarchy layout described in this specification.

An OCFL Object includes administrative information that identifies a directory as an OCFL Object, and also provides a
means of tracking changes to the contents of the object over time.

An OCFL Object is therefore:

1. A conceptual gathering of all files (data and metadata), the directories they are organized in, and their changes
over time which together form the digital representation of an entity that need to be managed, in preservation terms, as
a single coherent whole (i.e., content); and

2. A file and directory layout and administrative information on a storage medium that provides a defined structure for
the storage of this content, and through which these files and their changes may be understood (i.e., structure).

A key goal of the OCFL is the rebuildability of a repository from an OCFL Storage Root without additional information
resources. Consequently, a key implementation consideration should be to ensure that OCFL Objects contain all the data
and metadata required to achieve this. With reference to the \[[OAIS](#ref-oais)\] model, this would include all the
descriptive, administrative, structural, representation and preservation metadata relevant to the object.

A central feature of the OCFL specification is support for versioning. This recognizes that digital objects will change
over time, through new requirements, fixes, updates, or format shifts. The specification takes no position on what
constitutes a version or a versionable action, but it is recommended that implementers have a clear position on this
within their local storage policies.

### 3.1 Object Structure
{: #object-structure}

The OCFL Object structure organizes content files and administrative information in order to support content storage and
object validation. The structure for an object with one version is shown in the following figure:

```
[object_root]
    ├── 0=ocfl_object_1.1
    ├── inventory.json
    ├── inventory.json.sha512
    └── v1
        ├── inventory.json
        ├── inventory.json.sha512
        └── content
               └── ... content files ...
```

The [OCFL Object Root](#dfn-ocfl-object-root) <span id="E001" class="rfc2119">MUST NOT</span> contain files or
directories other than those specified in the following sections.

### 3.2 Object Conformance Declaration
{: #object-conformance-declaration}

The OCFL specification version declaration <span id="E002" class="rfc2119">MUST</span> be formatted according to the
\[[NAMASTE](#ref-namaste)\] specification. There <span id="E003" class="rfc2119">MUST</span> be exactly one version
declaration file in the base directory of the [OCFL Object Root](#dfn-ocfl-object-root) giving the OCFL version in the
filename. The filename <span id="E004" class="rfc2119">MUST</span> conform to the pattern `T=dvalue`, where `T` <span
id="E005" class="rfc2119">MUST</span> be 0, and `dvalue` <span id="E006" class="rfc2119">MUST</span> be `ocfl_object_`,
followed by the OCFL specification version number. The text contents of the file <span id="E007"
class="rfc2119">MUST</span> be the same as `dvalue`, followed by a newline (`\n`).

### 3.3 Version Directories
{: #version-directories}

OCFL Object content <span id="E008" class="rfc2119">MUST</span> be stored as a sequence of one or more versions. Each
object version is stored in a version directory under the object root. Version directory names <span id="E104"
class="rfc2119">MUST</span> be constructed by prepending `v` to the version number. The version number <span id="E105"
class="rfc2119">MUST</span> be taken from the sequence of positive, base-ten integers: 1, 2, 3, etc.. The version number
sequence <span id="E009" class="rfc2119">MUST</span> start at 1 and <span id="E010" class="rfc2119">MUST</span> be
continuous without missing integers.

Implementations <span id="W001" class="rfc2119">SHOULD</span> use version directory names constructed without
zero-padding the version number, ie. `v1`, `v2`, `v3`, etc..

For compatibility with existing filesystem conventions, implementations <span class="rfc2119">MAY</span> use zero-padded
version directory numbers, with the following restriction: If zero-padded version directory numbers are used then they
<span id="E011" class="rfc2119">MUST</span> start with the prefix `v` and then a zero. For example, in an implementation
that uses five digits for version directory names then `v00001` to `v09999` are allowed, `v10000` is not allowed.

The first version of an object defines the naming convention for all version directories for the object. All version
directories of an object <span id="E012" class="rfc2119">MUST</span> use the same naming convention: either a non-padded
version directory number, or a zero-padded version directory number of consistent length. The version naming convention
<span id="E013" class="rfc2119">MUST</span> be consistent across all versions. In all cases, references to files inside
version directories from inventory files <span id="E014" class="rfc2119">MUST</span> use the actual version directory
names.

There <span id="E015" class="rfc2119">MUST</span> be no other files as children of a version directory, other than an
[inventory file](#inventory) and a [inventory digest](#inventory-digest). The version directory <span id="W002"
class="rfc2119">SHOULD NOT</span> contain any directories other than the designated content sub-directory. Once created,
the contents of a version directory are expected to be immutable.

#### 3.3.1 Content Directory
{: #content-directory}

Version directories <span id="E016" class="rfc2119">MUST</span> contain a designated content sub-directory if the
version contains files to be preserved, and <span id="W003" class="rfc2119">SHOULD NOT</span> contain this sub-directory
otherwise. The name of this designated sub-directory <span class="rfc2119">MAY</span> be defined in the [inventory
file](#inventory) using the key `contentDirectory` with the value being the chosen sub-directory name as a string,
relative to the version directory. The `contentDirectory` value <span id="E108" class="rfc2119">MUST</span> represent a
direct child directory of the version directory in which it is found. As such, the `contentDirectory` value <span
id="E017" class="rfc2119">MUST NOT</span> contain the forward slash (`/`) path separator and <span id="E018"
class="rfc2119">MUST NOT</span> be either one or two periods (`.` or `..`). If the key `contentDirectory` is set, it
<span id="E019" class="rfc2119">MUST</span> be set in the first version of the object and <span id="E020"
class="rfc2119">MUST NOT</span> change between versions of the same object.

If the key `contentDirectory` is not present in the [inventory file](#inventory) then the name of the designated content
sub-directory <span id="E021" class="rfc2119">MUST</span> be `content`. OCFL-compliant tools (including any validators)
<span id="E022" class="rfc2119">MUST</span> ignore all directories in the object version directory except for the
designated content directory.

Every file within a version's content directory <span id="E023" class="rfc2119">MUST</span> be referenced in the
[manifest](#manifest) section of that version's inventory. There <span id="E024" class="rfc2119">MUST NOT</span> be
empty directories within a version's content directory. A directory that would otherwise be empty <span
class="rfc2119">MAY</span> be maintained by creating a file within it named according to local conventions, for example
by making an empty `.keep` file.

### 3.4 Digests
{: #digests}

A [digest](#dfn-digest) plays two roles in an OCFL Object. The first is that digests allow for content-addressable
reference to files within the OCFL Object. That is, the connection between a file's [content path](#dfn-content-path) on
physical storage and its [logical path](#dfn-logical-path) in a version of the object's content is made with a digest of
its contents, rather than its filename. This use of the content digest facilitates de-duplication of files with the same
content within an object, such as files that are unchanged from one version to the next. The second role that digests
play is provide for fixity checks to determine whether a file has become corrupt, through hardware degradation or
accident for example.

For content-addressing, OCFL Objects <span id="E025" class="rfc2119">MUST</span> use either `sha512` or `sha256`, and
<span id="W004" class="rfc2119">SHOULD</span> use `sha512`. The choice of the `sha512` digest algorithm as default
recognizes that it has no known collision vulnerabilities and multiple implementations are available.

For storage of additional fixity values, or to support legacy content migration, implementers <span id="E026"
class="rfc2119">MUST</span> choose from the following controlled vocabulary of digest algorithms, or from a list of
additional algorithms given in the \[[Digest-Algorithms-Extension](#ref-digest-algorithms-extension)\]. OCFL clients
<span id="E027" class="rfc2119">MUST</span> support all fixity algorithms given in the table below, and <span
class="rfc2119">MAY</span> support additional algorithms from the extensions. Optional fixity algorithms that are not
supported by a client <span id="E028" class="rfc2119">MUST</span> be ignored by that client.

| Digest Algorithm Name | Note |
| --- | --- |
| `md5` | Insecure. Use only for legacy fixity values. MD5 algorithm and hex encoding defined by \[[RFC1321](#ref-rfc1321)\]. For example, the `md5` digest of a zero-length bitstream is `d41d8cd98f00b204e9800998ecf8427e`. |
| `sha1` | Insecure. Use only for legacy fixity values. SHA-1 algorithm defined by \[[FIPS-180-4](#ref-fips-180-4)\] and <span id="E029" class="rfc2119">MUST</span> be encoded using hex (base16) encoding \[[RFC4648](#ref-rfc4648)\]. For example, the `sha1` digest of a zero-length bitstream is `da39a3ee5e6b4b0d3255bfef95601890afd80709`. |
| `sha256` | Non-truncated form only; note performance implications. SHA-256 algorithm defined by \[[FIPS-180-4](#ref-fips-180-4)\] and <span id="E030" class="rfc2119">MUST</span> be encoded using hex (base16) encoding \[[RFC4648](#ref-rfc4648)\]. For example, the `sha256` digest of a zero-length bitstream starts `e3b0c44298fc1c149afbf4c8996fb92427ae41e4...` (64 hex digits long). |
| `sha512` | Default choice. Non-truncated form only. SHA-512 algorithm defined by \[[FIPS-180-4](#ref-fips-180-4)\] and <span id="E031" class="rfc2119">MUST</span> be encoded using hex (base16) encoding \[[RFC4648](#ref-rfc4648)\]. For example, the `sha512` digest of a zero-length bitstream starts `cf83e1357eefb8bdf1542850d66d8007d620e405...` (128 hex digits long). |
| `blake2b-512` | Full-length form only, using the 2B variant (64 bit) as defined by \[[RFC7693](#ref-rfc7693)\]. <span id="E032" class="rfc2119">MUST</span> be encoded using hex (base16) encoding \[[RFC4648](#ref-rfc4648)\]. For example, the `blake2b-512` digest of a zero-length bitstream starts `786a02f742015903c6c6fd852552d272912f4740...` (128 hex digits long). |

An OCFL Inventory <span class="rfc2119">MAY</span> contain a fixity section that can store one or more blocks containing
fixity values using multiple digest algorithms. See the [section on fixity](#fixity) below for further details.

> Non-normative note: Implementers may also store copies of their file digests in a system external to their OCFL Object
stores at the point of ingest, to further safeguard against the possibility of malicious manipulation of file contents
and digests.
>
> Implementers should be aware that base16 digests are case insensitive. Different tools will generate digests in
uppercase or lowercase, and this may lead to case differences between references to a digest and the digest itself
within the inventory. If string-based methods are used to work with digests and inventories (as is the case in most
common JSON libraries) then extra care must be taken to ensure case-insensitive comparisons are being made.

### 3.5 Inventory
{: #inventory}

An OCFL Object Inventory <span id="E033" class="rfc2119">MUST</span> follow the JSON (defined by
\[[RFC8259](#ref-rfc8259)\]) structure described in this section with contents encoded in UTF-8, and <span id="E034"
class="rfc2119">MUST</span> be named `inventory.json`. The order of entries in both the JSON objects and arrays used in
inventory files has no significance. An OCFL Object Inventory <span id="E102" class="rfc2119">MUST NOT</span> contain
any keys not described in this specification.

The forward slash (/) path separator <span id="E035" class="rfc2119">MUST</span> be used in content paths in the
[manifest](#manifest) and [fixity](#fixity) blocks within the inventory. Implementations that target systems using other
separators will need to translate paths appropriately.

> Non-normative note: A \[[JSON-Schema](#ref-json-schema)\] for validating OCFL Object Inventory files is provided at
[inventory_schema.json](inventory_schema.json).

#### 3.5.1 Basic Structure
{: #inventory-structure}

Every OCFL inventory <span id="E036" class="rfc2119">MUST</span> include the following keys:

* `id`: A unique identifier for the OCFL Object. This <span id="E037" class="rfc2119">MUST</span> be unique in the local
context, <span id="E110" class="rfc2119">MUST NOT</span> change between versions of the same object, and <span id="W005"
class="rfc2119">SHOULD</span> be a URI \[[RFC3986](#ref-rfc3986)\]. There is no expectation that a URI used is
resolvable. For example, URNs \[[RFC8141](#ref-rfc8141)\] <span class="rfc2119">MAY</span> be used.

* `type`: A type for the inventory JSON object that also serves to document the OCFL specification version that the
inventory complies with. In the object root inventory this <span id="E038" class="rfc2119">MUST</span> be the URI of the
inventory section of the specification version matching the object conformance declaration. For the current
specification version the value is `https://ocfl.io/1.1/spec/#inventory`.

* `digestAlgorithm`: The digest algorithm used for calculating digests for content-addressing within the OCFL Object and
for the [Inventory Digest](#inventory-digest). This <span id="E039" class="rfc2119">MUST</span> be the algorithm used in
the `manifest` and `state` blocks, see the [section on Digests](#digests) for more information about algorithms.

* `head`: The version directory name of the most recent version of the object. This <span id="E040"
class="rfc2119">MUST</span> be the version directory name with the highest version number.

There <span class="rfc2119">MAY</span> be the following key:

* `contentDirectory`: The name of the designated content directory within the version directories. If not specified then
the content directory name is `content`.

In addition to these keys, there <span id="E041" class="rfc2119">MUST</span> be two other blocks present, `manifest` and
`versions`, which are discussed in the next two sections.

#### 3.5.2 Manifest
{: #manifest}

The value of the `manifest` key <span id="E106" class="rfc2119">MUST</span> be a JSON object, and each key <span
id="E107" class="rfc2119">MUST</span> correspond to a digest value key found in one or more `state` blocks of the
current and/or previous `version` blocks of the [OCFL Object](#dfn-ocfl-object). The value for each key <span id="E092"
class="rfc2119">MUST</span> be an array containing the [content path](#dfn-content-path)s of files in the OCFL Object
that have content with the given digest. As JSON keys are case sensitive, for digest algorithms with case insensitive
digest values, there is an additional requirement that each digest value <span id="E096" class="rfc2119">MUST</span>
occur only once in the manifest block for any digest algorithm, regardless of case. Content paths within a manifest
block <span id="E042" class="rfc2119">MUST</span> be relative to the [OCFL Object Root](#dfn-ocfl-object-root). The
following restrictions avoid ambiguity and provide path safety for clients processing the `manifest`.

* The content path <span id="E098" class="rfc2119">MUST</span> be interpreted as a set of one or more path elements
joined by a `/` path separator.

* Path elements <span id="E099" class="rfc2119">MUST NOT</span> be `.`, `..`, or empty (`//`).

* A content path <span id="E100" class="rfc2119">MUST NOT</span> begin or end with a forward slash (`/`).

* Within an inventory, content paths <span id="E101" class="rfc2119">MUST</span> be unique and non-conflicting, so the
content path for a file cannot appear as the initial part of another content path.

> Non-normative note: If only one file is stored in the OCFL Object for each digest, fully de-duplicating the content,
then there will be only one [content path](#dfn-content-path) for each digest. There may, however, be multiple logical
paths for a given digest if the content was not entirely de-duplicated when constructing the OCFL Object.
>
> An example manifest object for three content paths, all in version 1, is shown below:
>
> ```json
"manifest": {
  "7dcc35...c31": [ "v1/content/foo/bar.xml" ],
  "cf83e1...a3e": [ "v1/content/empty.txt" ],
  "ffccf6...62e": [ "v1/content/image.tiff" ]
}
> ```

#### 3.5.3 Versions
{: #versions}

An OCFL Object Inventory <span id="E043" class="rfc2119">MUST</span> include a block for storing versions. This block
<span id="E044" class="rfc2119">MUST</span> have the key of `versions` within the inventory, and it <span id="E045"
class="rfc2119">MUST</span> be a JSON object. The keys of this object <span id="E046" class="rfc2119">MUST</span>
correspond to the names of the [version directories](#version-directories) used. Each value <span id="E047"
class="rfc2119">MUST</span> be another JSON object that characterizes the version, as described in the [3.5.3.1
Version](#version) section.

##### 3.5.3.1 Version
{: #version}

A JSON object to describe one [OCFL Version](#dfn-ocfl-version), which <span id="E048" class="rfc2119">MUST</span>
include the following keys:

* `created`: The value of this key is the datetime of creation of this version. It <span id="E049"
class="rfc2119">MUST</span> be expressed in the Internet Date/Time Format defined by \[[RFC3339](#ref-rfc3339)\]. This
format requires the inclusion of a timezone value or `Z` for UTC, and that the time component be granular to the second
level (with optional fractional seconds).

* `state`: The value of this key is a JSON object, containing a list of keys and values corresponding to the [logical
state](#dfn-logical-state) of the object at that version. The keys of this JSON object are digest values, each of which
<span id="E050" class="rfc2119">MUST</span> exactly match a digest value key in the [manifest of the
inventory](#manifest). The value for each key is an array containing [logical path](#dfn-logical-path) names of files in
the OCFL Object's logical state that have content with the given digest.

[Logical paths](#logical-path) present the structure of an OCFL Object at a given version. This is given as an array of
values, with the following restrictions to provide for path safety in the common case of the logical path value
representing a file path.

* The logical path <span id="E051" class="rfc2119">MUST</span> be interpreted as a set of one or more path elements
joined by a `/` path separator.

* Path elements <span id="E052" class="rfc2119">MUST NOT</span> be `.`, `..`, or empty (`//`).

* A logical path <span id="E053" class="rfc2119">MUST NOT</span> begin or end with a forward slash (`/`).

* Within a version, logical paths <span id="E095" class="rfc2119">MUST</span> be unique and non-conflicting, so the
logical path for a file cannot appear as the initial part of another logical path.

> Non-normative note: The [logical state](#dfn-logical-state) of the object uses content-addressing to map logical paths
to their bitstreams, as expressed in the manifest section of the inventory. Notably, the version state provides
de-duplication of content within the OCFL Object by mapping multiple logical paths with the same content to the same
digest in the manifest. See \[[OCFL-Implementation-Notes](#ref-ocfl-implementation-notes)\].
>
> An example `state` block is shown below:
>
> ```json
"state": {
  "4d27c8...b53": [ "foo/bar.xml" ],
  "cf83e1...a3e": [ "empty.txt", "empty2.txt" ]
}
> ```
>
> This `state` block describes an object with 3 files, two of which have the same content (`empty.txt` and
`empty2.txt`), and one of which is in a sub-directory (`bar.xml`). The [logical state](#dfn-logical-state) shown as a
tree is thus:
>
> ```
├── empty.txt
├── empty2.txt
└── foo
    └── bar.xml
> ```

The JSON object describing an [OCFL Version](#dfn-ocfl-version), <span id="W007" class="rfc2119">SHOULD</span> include
the following keys:

* `message`: The value of this key is freeform text, used to record the rationale for creating this version. It <span
id="E094" class="rfc2119">MUST</span> be a JSON string.

* `user`: The value of this key is a JSON object intended to identify the user or agent that created the current [OCFL
Version](#dfn-ocfl-version). The value of the `user` key <span id="E054" class="rfc2119">MUST</span> contain a user name
key, `name` and <span id="W008" class="rfc2119">SHOULD</span> contain an address key, `address`. The `name` value is any
readable name of the user, e.g., a proper name, user ID, agent ID. The `address` value <span id="W009"
class="rfc2119">SHOULD</span> be a URI: either a mailto URI \[[RFC6068](#ref-rfc6068)\] with the e-mail address of the
user or a URL to a personal identifier, e.g., an ORCID iD.

#### 3.5.4 Fixity
{: #fixity}

An OCFL Object inventory <span class="rfc2119">MAY</span> include a block for storing additional fixity information to
supplement the complete set of digests in the [Manifest](#manifest), for example to support legacy digests from a
content migration. If present, this block <span id="E055" class="rfc2119">MUST</span> have the key of `fixity` within
the inventory, and its value <span id="E111" class="rfc2119">MUST</span> be a JSON object, which <span
class="rfc2119">MAY</span> be empty.

The keys within the `fixity` block <span id="E056" class="rfc2119">MUST</span> correspond to the controlled vocabulary
of [digest algorithm names](#digest-algorithms) listed in the [Digests](#digests) section, or in a table given in an
[Extension](#dfn-extension). The value of the fixity block for a particular digest algorithm <span id="E057"
class="rfc2119">MUST</span> follow the structure of the [3.5.2 Manifest](#manifest) block; that is, a key corresponding
to the digest value, and an array of [content path](#dfn-content-path)s. The `fixity` block for any digest algorithm
<span class="rfc2119">MAY</span> include digest values for any subset of content paths in the object. Where included,
the digest values given <span id="E093" class="rfc2119">MUST</span> match the digests of the files at the corresponding
content paths. As JSON keys are case sensitive, for digest algorithms with case insensitive digest values, there is an
additional requirement that each digest value <span id="E097" class="rfc2119">MUST</span> occur only once in the
`fixity` block for any digest algorithm, regardless of case. There is no requirement that all content files have a value
in the `fixity` block, or that fixity values provided in one version are carried forward to later versions.

> An example `fixity` with `md5` and `sha1` digests is shown below. In this case the `md5` digest values are provided
only for version 1 content paths.
>
> ```json
"fixity": {
  "md5": {
    "184f84e28cbe75e050e9c25ea7f2e939": [ "v1/content/foo/bar.xml" ],
    "c289c8ccd4bab6e385f5afdd89b5bda2": [ "v1/content/image.tiff" ],
    "d41d8cd98f00b204e9800998ecf8427e": [ "v1/content/empty.txt" ]
  },
  "sha1": {
    "66709b068a2faead97113559db78ccd44712cbf2": [ "v1/content/foo/bar.xml" ],
    "a6357c99ecc5752931e133227581e914968f3b9c": [ "v2/content/foo/bar.xml" ],
    "b9c7ccc6154974288132b63c15db8d2750716b49": [ "v1/content/image.tiff" ],
    "da39a3ee5e6b4b0d3255bfef95601890afd80709": [ "v1/content/empty.txt" ]
  }
}
> ```

### 3.6 Inventory Digest
{: #inventory-digest}

Every occurrence of an inventory file <span id="E058" class="rfc2119">MUST</span> have an accompanying sidecar file
named `inventory.json.ALGORITHM` stating its digest, where `ALGORITHM` is the chosen digest algorithm for the object.
The ALGORITHM <span id="E059" class="rfc2119">MUST</span> match the value given for the `digestAlgorithm` key in the
inventory. An example might be `inventory.json.sha512`.

The digest sidecar file <span id="E060" class="rfc2119">MUST</span> contain the digest of the inventory file. This <span
id="E061" class="rfc2119">MUST</span> follow the format:

```
DIGEST inventory.json
```

One or more whitespace characters (spaces or tabs) must separate DIGEST from the string `inventory.json`; that is, the
name of the inventory file in the same directory.

The digest of the inventory <span id="E062" class="rfc2119">MUST</span> be computed only after all changes to the
inventory have been made, and thus writing the digest sidecar file is the last step in the versioning process.

### 3.7 Version Inventory and Inventory Digest
{: #version-inventory}

Every OCFL Object <span id="E063" class="rfc2119">MUST</span> have an inventory file within the OCFL Object Root,
corresponding to the state of the OCFL Object at the current version. Additionally, every version directory <span
id="W010" class="rfc2119">SHOULD</span> include an inventory file that is an [Inventory](#inventory) of all content for
versions up to and including that particular version. Where an OCFL Object contains `inventory.json` in version
directories, the inventory file in the OCFL Object Root <span id="E064" class="rfc2119">MUST</span> be the same as the
file in the most recent version. See also requirements for the corresponding [Inventory Digest](#inventory-digest).

In the case that prior version directories include an inventory file there will be multiple inventory files describing
prior versions within the OCFL Object. Each `version` block in each prior inventory file <span id="E066"
class="rfc2119">MUST</span> represent the same [logical state](#dfn-logical-state) as the corresponding `version` block
in the current inventory file. Additionally, the values of the `created`, `message` and `user` keys in each `version`
block in each prior inventory file <span id="W011" class="rfc2119">SHOULD</span> have the same values as the
corresponding keys in the corresponding `version` block in the current inventory file.

> Non-normative note: Storing an inventory for every version provides redundancy for this critical information in a way
that is compatible with storage strategies that have immutable version directories.

#### 3.7.1 Conformance of prior versions
{: #conformance-of-prior-versions}

Version directories in OCFL are intended to be immutable in that existing version directories do not change when a new
version directory is added. Each version directory within an OCFL Object <span id="E103" class="rfc2119">MUST</span>
conform to either the same or a later OCFL specification version as the preceding version directory. If inventories are
stored in the version directories then the OCFL specification version for a given version directory is apparent from the
`type` attribute in that [inventory](#inventory-structure).

### 3.8 Logs Directory
{: #logs-directory}

The base directory of an OCFL Object <span class="rfc2119">MAY</span> contain a directory named `logs`, which <span
class="rfc2119">MAY</span> be empty. Implementers <span id="W012" class="rfc2119">SHOULD</span> use the [logs
directory](#dfn-logs-directory) for storing files that contain a record of actions taken on the object. Since these logs
may be subject to local standards requirements, the format of these logs is considered out-of-scope for the OCFL Object.
Clients operating on the object <span class="rfc2119">MAY</span> log actions here that are not otherwise captured.

> Non-normative note: The purpose of the logs directory is to provide implementers with a location for storing local
information about actions to the OCFL Object's content that is not part of the content itself.
>
> As an example, implementers may have different local requirements to store audit information for their content. Some
may wish to store a log entry indicating that an audit was conducted, and nothing was wrong, while others may wish to
only store a log entry if an intervention was required.

### 3.9 Object Extensions
{: #object-extensions}

The base directory of an OCFL Object <span class="rfc2119">MAY</span> contain a directory named `extensions` for the
purposes of extending the functionality of an OCFL Object. The `extensions` directory <span id="E067"
class="rfc2119">MUST NOT</span> contain any files or sub-directories other than extension sub-directories.
Extension sub-directories <span id="W013" class="rfc2119">SHOULD</span> be named according to a [registered extension
name](#dfn-registered-extension-name) in the [OCFL Extensions repository](https://ocfl.github.io/extensions/).

> Non-normative note: Extension sub-directories should use the same name as a registered extension in order to both
avoid the possiblity of an extension sub-directory colliding with the name of another registered extension as well as to
facilitate the recognition of extensions by OCFL clients. See also [Documenting Local
Extensions](#documenting-local-extensions).

## 4. OCFL Storage Root
{: #storage-root}

An [OCFL Storage Root](#dfn-ocfl-storage-root) is the base directory of an OCFL storage layout.

### 4.1 Root Structure
{: #root-structure}

An OCFL Storage Root <span id="E069" class="rfc2119">MUST</span> contain a [Root Conformance
Declaration](#root-conformance-declaration) identifying it as such.

An OCFL Storage Root <span class="rfc2119">MAY</span> contain other files as direct children. These might include a
human-readable copy of the OCFL specification to make the storage root self-documenting, or files used to [document
local extensions](#documenting-local-extensions). The source file for this specification document is in
Markdown (described in \[[RFC7764](#ref-rfc7764)\], which is designed to be readable as plain text as well as for
rendering as HTML, and thus makes it suitable for self-documentation. An OCFL validator <span id="E087"
class="rfc2119">MUST</span> ignore any files in the storage root it does not understand.

An OCFL Storage Root <span id="E088" class="rfc2119">MUST NOT</span> contain directories or sub-directories other than
as a directory hierarchy used to store OCFL Objects or for [storage root extensions](#storage-root-extensions). The
directory hierarchy used to store OCFL Objects <span id="E072" class="rfc2119">MUST NOT</span> contain files that are
not part of an OCFL Object. Empty directories <span id="E073" class="rfc2119">MUST NOT</span> appear under a storage
root.

An OCFL Storage Root <span class="rfc2119">MAY</span> contain a file named `ocfl_layout.json` to describe the
arrangement of directories and OCFL objects under the storage root. If present, `ocfl_layout.json` <span id="E070"
class="rfc2119">MUST</span> be a JSON (defined by \[[RFC8259](#ref-rfc8259)\]) document encoded in UTF-8 and include the
following two keys in the root JSON object:

* `extension` - An extension name that identifies an arrangement of directories and OCFL objects under the storage root,
i.e. how OCFL object identifiers are mapped to directory hierarchies. The value of the `extension` key <span id="E071"
class="rfc2119">MUST</span> be the [registered extension name](#dfn-registered-extension-name) for the extension
defining the arrangement under the storage root.

* `description` - A human readable description of the arrangement of directories and OCFL objects under the storage
root.

Although implementations may require multiple OCFL Storage Roots—that is, several logical or physical volumes, or
multiple "buckets" in an object store—each OCFL Storage Root <span id="E074" class="rfc2119">MUST</span> be independent.

The following example OCFL Storage Root represents the minimal set of files and folders:

```
[storage_root]
    ├── 0=ocfl_1.1
    ├── ocfl_1.1.md        (human-readable text of the OCFL specification; optional)
    └── ocfl_layout.json   (description of storage hierarchy layout; optional)
```

### 4.2 Root Conformance Declaration
{: #root-conformance-declaration}

The OCFL version declaration <span id="E075" class="rfc2119">MUST</span> be formatted according to the
\[[NAMASTE](#ref-namaste)\] specification. There <span id="E076" class="rfc2119">MUST</span> be exactly one version
declaration file in the base directory of the [OCFL Storage Root](#dfn-ocfl-storage-root) giving the OCFL version in the
filename. The filename <span id="E077" class="rfc2119">MUST</span> conform to the pattern `T=dvalue`, where `T` <span
id="E078" class="rfc2119">MUST</span> be 0, and `dvalue` <span id="E079" class="rfc2119">MUST</span> be `ocfl_`,
followed by the OCFL specification version number. The text contents of the file <span id="E080"
class="rfc2119">MUST</span> be the same as `dvalue`, followed by a newline (`\n`).

Root conformance indicates that the OCFL Storage Root conforms to this section (i.e. the OCFL Storage Root section) of
the specification. OCFL Objects within the OCFL Storage Root also include a conformance declaration which <span
id="E081" class="rfc2119">MUST</span> indicate OCFL Object conformance to the same or earlier version of the
specification.

### 4.3 Storage Hierarchies
{: #root-hierarchies}

[OCFL Object Root](#dfn-ocfl-object-root)s <span id="E082" class="rfc2119">MUST</span> be stored either as the terminal
resource at the end of a directory storage hierarchy or as direct children of a containing [OCFL Storage
Root](#dfn-ocfl-storage-root).

A common practice is to use a unique identifier scheme to compose this storage hierarchy, typically arranged according
to some form of the \[[PairTree](#ref-pairtree)\] specification. Irrespective of the pattern chosen for the storage
hierarchies, the following restrictions apply:

1. There <span id="E083" class="rfc2119">MUST</span> be a deterministic mapping from an object identifier to a unique
storage path

2. Storage hierarchies <span id="E084" class="rfc2119">MUST NOT</span> include files within intermediate directories

3. Storage hierarchies <span id="E085" class="rfc2119">MUST</span> be terminated by OCFL Object Roots

4. Storage hierarchies within the same OCFL Storage Root <span id="W014" class="rfc2119">SHOULD</span> use just one
layout pattern

5. Storage hierarchies within the same OCFL Storage Root <span id="W015" class="rfc2119">SHOULD</span> consistently use
either a directory hierarchy of OCFL Objects or top-level OCFL Objects

### 4.4 Storage Root Extensions
{: #storage-root-extensions}

The behavior of the storage root may be extended to support features from other specifications.

The base directory of an OCFL Storage Root <span class="rfc2119">MAY</span> contain a directory named `extensions` for
the purposes of extending the functionality of an OCFL Storage Root. The guidelines and limitations for the storage
root `extensions` directory are defined in alignment with those of the [object extensions](#object-extensions).

The `extensions` directory <span id="E112" class="rfc2119">MUST NOT</span> contain any files or sub-directories
other than extension sub-directories. Extension sub-directories <span id="W016" class="rfc2119">SHOULD</span> be named
according to a <a>registered extension name</a>.

> Non-normative notes: Extension sub-directories should use the same name as a registered extension in order to both
avoid the possiblity of an extension sub-directory colliding with the name of another registered extension as well as to
facilitate the recognition of extensions by OCFL clients. See also [Documenting Local
Extensions](#documenting-local-extensions).
>
> Storage extensions can be used to support additional features, such as providing the storage
hierarchy disposition when pairtree is in use, or additional human-readable text about the nature of the storage root.

### 4.5 Documenting Local Extensions
{: #documenting-local-extensions}

It is preferable that both [Object Extensions](#object-extensions) and [Storage Root
Extenstions](#storage-root-extensions) are documented and registered in the [OCFL Extensions
repository](https://ocfl.github.io/extensions/). However, local extensions <span class="rfc2119">MAY</span> be
documented by including a plain text document directly in the storage root, thus making the storage root
self-documenting.

### 4.6 Filesystem features
{: #filesystem-features}

In order to maximize the compatibility of the OCFL with different filesystems, and thus improve the portability of OCFL
Objects between different systems, some restrictions on the use of certain filesystem features are necessary. If the
preservation of non-OCFL-compliant features is required then the content <span id="E089" class="rfc2119">MUST</span> be
wrapped in a suitable disk or filesystem image format which OCFL can treat as a regular file.

1. Filesystem metadata (e.g. permissions, access, and creation times) are not considered portable between filesystems or
preservable through file transfer operations. These attributes also cannot be validated in terms of fixity in a
consistent manner. As such, the OCFL does not support the portability of these attributes.

2. Hard and soft (symbolic) links are not portable and <span id="E090" class="rfc2119">MUST NOT</span> be used within
OCFL Storage hierarchies. A common use case for links is storage deduplication. OCFL inventories provide a portable
method of achieving the same effect by using digests to address content.

3. File paths and filenames in the OCFL are case sensitive. Filesystems <span id="E091" class="rfc2119">MUST</span>
preserve the case of OCFL filepaths and filenames.

4. Transparent filesystem features such as compression and encryption should be effectively invisible to OCFL
operations. Consequently, they should not be expected to be portable.

## 5. Examples
{: #examples}

_This section is non-normative._

### 5.1 Minimal OCFL Object
{: #example-minimal-object}

The following example OCFL Object has content that is a single file (`file.txt`), and just one version (`v1`):

```
[object root]
    ├── 0=ocfl_object_1.1
    ├── inventory.json
    ├── inventory.json.sha512
    └── v1
        ├── inventory.json
        ├── inventory.json.sha512
        └── content
            └── file.txt
```

The inventory for this OCFL Object, the same both at the top-level and in the `v1` directory, might be:

```json
{
  "digestAlgorithm": "sha512",
  "head": "v1",
  "id": "http://example.org/minimal",
  "manifest": {
    "7545b8...f67": [ "v1/content/file.txt" ]
  },
  "type": "https://ocfl.io/1.1/spec/#inventory",
  "versions": {
    "v1": {
      "created": "2018-10-02T12:00:00Z",
      "message": "One file",
      "state": {
        "7545b8...f67": [ "file.txt" ]
      },
      "user": {
        "address": "mailto:alice@example.org",
        "name": "Alice"
      }
    }
  }
}
```

### 5.2 Versioned OCFL Object
{: #example-versioned-object}

The following example OCFL Object has three versions:

```
[object root]
    ├── 0=ocfl_object_1.1
    ├── inventory.json
    ├── inventory.json.sha512
    ├── v1
    │   ├── inventory.json
    │   ├── inventory.json.sha512
    │   └── content
    │       ├── empty.txt
    │       ├── foo
    │       │   └── bar.xml
    │       └── image.tiff
    ├── v2
    │   ├── inventory.json
    │   ├── inventory.json.sha512
    │   └── content
    │       └── foo
    │           └── bar.xml
    └── v3
        ├── inventory.json
        └── inventory.json.sha512
```

In `v1` there are three files, `empty.txt`, `foo/bar.xml`, and `image.tiff`. In `v2` the content of `foo/bar.xml` is
changed, `empty2.txt` is added with the same content as `empty.txt`, and `image.tiff` is removed. In `v3` the file
`empty.txt` is removed, and `image.tiff` is reinstated. As a result of forward-delta versioning, the object tree above
shows only new content added in each version. The inventory shown below details the other changes, includes additional
fixity information using `md5` and `sha1` digest algorithms, and minimal metadata for each version.

```json
{
  "digestAlgorithm": "sha512",
  "fixity": {
    "md5": {
      "184f84e28cbe75e050e9c25ea7f2e939": [ "v1/content/foo/bar.xml" ],
      "2673a7b11a70bc7ff960ad8127b4adeb": [ "v2/content/foo/bar.xml" ],
      "c289c8ccd4bab6e385f5afdd89b5bda2": [ "v1/content/image.tiff" ],
      "d41d8cd98f00b204e9800998ecf8427e": [ "v1/content/empty.txt" ]
    },
    "sha1": {
      "66709b068a2faead97113559db78ccd44712cbf2": [ "v1/content/foo/bar.xml" ],
      "a6357c99ecc5752931e133227581e914968f3b9c": [ "v2/content/foo/bar.xml" ],
      "b9c7ccc6154974288132b63c15db8d2750716b49": [ "v1/content/image.tiff" ],
      "da39a3ee5e6b4b0d3255bfef95601890afd80709": [ "v1/content/empty.txt" ]
    }
  },
  "head": "v3",
  "id": "ark:/12345/bcd987",
  "manifest": {
    "4d27c8...b53": [ "v2/content/foo/bar.xml" ],
    "7dcc35...c31": [ "v1/content/foo/bar.xml" ],
    "cf83e1...a3e": [ "v1/content/empty.txt" ],
    "ffccf6...62e": [ "v1/content/image.tiff" ]
  },
  "type": "https://ocfl.io/1.1/spec/#inventory",
  "versions": {
    "v1": {
      "created": "2018-01-01T01:01:01Z",
      "message": "Initial import",
      "state": {
        "7dcc35...c31": [ "foo/bar.xml" ],
        "cf83e1...a3e": [ "empty.txt" ],
        "ffccf6...62e": [ "image.tiff" ]
      },
      "user": {
        "address": "mailto:alice@example.com",
        "name": "Alice"
      }
    },
    "v2": {
      "created": "2018-02-02T02:02:02Z",
      "message": "Fix bar.xml, remove image.tiff, add empty2.txt",
      "state": {
        "4d27c8...b53": [ "foo/bar.xml" ],
        "cf83e1...a3e": [ "empty.txt", "empty2.txt" ]
      },
      "user": {
        "address": "mailto:bob@example.com",
        "name": "Bob"
      }
    },
    "v3": {
      "created": "2018-03-03T03:03:03Z",
      "message": "Reinstate image.tiff, delete empty.txt",
      "state": {
        "4d27c8...b53": [ "foo/bar.xml" ],
        "cf83e1...a3e": [ "empty2.txt" ],
        "ffccf6...62e": [ "image.tiff" ]
      },
      "user": {
        "address": "mailto:cecilia@example.com",
        "name": "Cecilia"
      }
    }
  }
}
```

### 5.3 Different Logical and Content Paths in an OCFL Object
{: #example-object-diff-paths}

The following example OCFL Object inventory shows how content paths may differ from logical paths. The example object
has just one version, `v1`, which has two files with logical paths `a file.wxy` and `another file.xyz` as shown in the
`state` block. The corresponding content paths are `v1/content/3bacb119a98a15c5` and `v1/content/9f2bab8ef869947d`
respectively, as shown in the `manifest`. Except for location within the appropriate version directory, `v1/content` in
this example, the OCFL specification does not constrain the choice of content paths used when creating or updating an
OCFL object. The choice might depend on particular limitations of, or optimizations for, the target storage system, or
on portability considerations. Any compliant implementation will be able to recover version state with the original
logical paths.

```json
{
  "digestAlgorithm": "sha512",
  "head": "v1",
  "id": "http://example.org/diff-paths",
  "manifest": {
    "7545b8...f67": [ "v1/content/3bacb119a98a15c5" ],
    "af318d...3cd": [ "v1/content/9f2bab8ef869947d" ]
  },
  "type": "https://ocfl.io/1.1/spec/#inventory",
  "versions": {
    "v1": {
      "created": "2019-03-14T20:31:00Z",
      "state": {
        "7545b8...f67": [ "a file.wxy" ],
        "af318d...3cd": [ "another file.xyz" ]
      },
      "user": {
        "address": "mailto:admin@example.org",
        "name": "Some Admin"
      }
    }
  }
}
```

### 5.4 BagIt in an OCFL Object
{: #example-bagit-in-ocfl}

\[[BagIt](#ref-bagit)\] is a common file packaging specification, but unlike the OCFL it does not provide a mechanism
for content versioning. Using the OCFL it is possible to store a BagIt structure with content versioning, such that when
the [logical state](#dfn-logical-state) is resolved, it creates a valid BagIt 'bag'. This example will illustrate one
way this can be accomplished, using the [example of a basic
bag](https://datatracker.ietf.org/doc/html/rfc8493#section-4.1) given in the BagIt specification.

```
[object root]
    ├── 0=ocfl_object_1.1
    ├── inventory.json
    ├── inventory.json.sha512
    └── v1
        ├── inventory.json
        ├── inventory.json.sha512
        └── content
            └── myfirstbag
                ├── bagit.txt
                ├── data
                │   └── 27613-h
                │       └── images
                │           ├── q172.png
                │           └── q172.txt
                └── manifest-md5.txt
```

If, for example, a new directory were added in a subsequent version, the OCFL Object would look like this:

```
[object root]
    ├── 0=ocfl_object_1.1
    ├── inventory.json
    ├── inventory.json.sha512
    ├── v1
    │   ├── inventory.json
    │   ├── inventory.json.sha512
    │   └── content
    │       └── myfirstbag
    │           ├── bagit.txt
    │           ├── data
    │           │   └── 27613-h
    │           │       └── images
    │           │           ├── q172.png
    │           │           └── q172.txt
    │           └── manifest-md5.txt
    └── v2
        ├── inventory.json
        ├── inventory.json.sha512
        └── content
            └── myfirstbag
                ├── data
                │   └── 27614-h
                │       └── images
                │           ├── q173.png
                │           └── q173.txt
                └── manifest-md5.txt
```

The state of the object at version 2 would be the following BagIt object:

```
myfirstbag
    ├── bagit.txt
    ├── data
    │   ├── 27613-h
    │   │   └── images
    │   │       ├── q172.png
    │   │       └── q172.txt
    │   └── 27614-h
    │       └── images
    │           ├── q173.png
    │           └── q173.txt
    └── manifest-md5.txt
```

The OCFL Inventory for this object would be as follows:

```json
{
  "digestAlgorithm": "sha512",
  "head": "v2",
  "id": "urn:uri:example.com/myfirstbag",
  "manifest": {
    "cf83e1...a3e": [ "v1/content/myfirstbag/bagit.txt" ],
    "f15428...83f": [ "v1/content/myfirstbag/manifest-md5.txt" ],
    "85f2b0...007": [ "v1/content/myfirstbag/data/27613-h/images/q172.png" ],
    "d66d80...8bd": [ "v1/content/myfirstbag/data/27613-h/images/q172.txt" ],
    "2b0ff8...620": [ "v2/content/myfirstbag/manifest-md5.txt" ],
    "921d36...877": [ "v2/content/myfirstbag/data/27614-h/images/q173.png" ],
    "b8bdf1...927": [ "v2/content/myfirstbag/data/27614-h/images/q173.txt" ]
  },
  "type": "https://ocfl.io/1.1/spec/#inventory",
  "versions": {
    "v1": {
      "created": "2018-10-09T11:20:29.209164Z",
      "message": "Initial Ingest",
      "state": {
        "cf83e1...a3e": [ "myfirstbag/bagit.txt" ],
        "85f2b0...007": [ "myfirstbag/data/27613-h/images/q172.png" ],
        "d66d80...8bd": [ "myfirstbag/data/27613-h/images/q172.txt" ],
        "f15428...83f": [ "myfirstbag/manifest-md5.txt" ]
      },
      "user": {
        "address": "mailto:someone@example.org",
        "name": "Some One"
      }
    },
    "v2": {
      "created": "2018-10-31T11:20:29.209164Z",
      "message": "Added new images",
      "state": {
        "cf83e1...a3e": [ "myfirstbag/bagit.txt" ],
        "85f2b0...007": [ "myfirstbag/data/27613-h/images/q172.png" ],
        "d66d80...8bd": [ "myfirstbag/data/27613-h/images/q172.txt" ],
        "2b0ff8...620": [ "myfirstbag/manifest-md5.txt" ],
        "921d36...877": [ "myfirstbag/data/27614-h/images/q173.png" ],
        "b8bdf1...927": [ "myfirstbag/data/27614-h/images/q173.txt" ]
      },
      "user": {
        "address": "mailto:somebody-else@example.org",
        "name": "Somebody Else"
      }
    }
  }
}
```

### 5.5 Moab in an OCFL Object
{: #example-moab-in-ocfl}

\[[Moab](#ref-moab)\] is an archive information package format developed and used by Stanford University. Many of the
ideas in Moab have been refined by the OCFL, and the OCFL is designed to give institutions currently using Moab an easy
path to adoption.

Converting content preserved in a Moab object in a way that does not compromise existing Moab access patterns whilst
allowing for the eventual use of OCFL-native workflows requires a Moab to OCFL conversion tool. This tool uses the
Moab-versioning gem to extract deltas and digests of the Moab data directory for each Moab version and translate those
into version `state` blocks in an OCFL inventory file, which would be placed in the root directory of the Moab object.
The content of the `data` directory in the Moab version directories (and thus, the bitstreams that Moab is preserving)
is tracked by OCFL, via the `contentDirectory` value. The contents of the Moab `manifests` directories are not tracked,
as the intention is not to encapsulate a Moab object inside an OCFL object, but rather to migrate Moab's preserved
bitstreams into an OCFL object without compromising legacy access patterns.

During the transitionary period the OCFL inventory file exists only in the root of the Moab object. Once OCFL-native
object creation workflows have been completed, future versions of that object will be fully OCFL compliant - new
versions will no longer have a manifests directory and will contain an OCFL inventory file. At this stage OCFL tools
will be able to access all versions of the content originally preserved by Moab.

Consider the following sample Moab object:

```
[object root]
    └── bj102hs9687
        ├── v0001
        │     ├── data
        │     │   ├── content
        │     │   │   ├── eric-smith-dissertation-augmented.pdf
        │     │   │   └── eric-smith-dissertation.pdf
        │     │   └── metadata
        │     │       ├── contentMetadata.xml
        │     │       ├── descMetadata.xml
        │     │       ├── identityMetadata.xml
        │     │       ├── provenanceMetadata.xml
        │     │       ├── relationshipMetadata.xml
        │     │       ├── rightsMetadata.xml
        │     │       ├── technicalMetadata.xml
        │     │       └── versionMetadata.xml
        │     └── manifests
        │         ├── fileInventoryDifference.xml
        │         ├── manifestInventory.xml
        │         ├── signatureCatalog.xml
        │         ├── versionAdditions.xml
        │         └── versionInventory.xml
        ├── v0002
        │     ├── data
        │     │   └── metadata
        │     │       ├── contentMetadata.xml
        │     │       ├── embargoMetadata.xml
        │     │       ├── events.xml
        │     │       ├── identityMetadata.xml
        │     │       ├── provenanceMetadata.xml
        │     │       ├── relationshipMetadata.xml
        │     │       ├── rightsMetadata.xml
        │     │       ├── versionMetadata.xml
        │     │       └── workflows.xml
        │     └── manifests
        │         ├── fileInventoryDifference.xml
        │         ├── manifestInventory.xml
        │         ├── signatureCatalog.xml
        │         ├── versionAdditions.xml
        │         └── versionInventory.xml
        └── v0003
              ├── data
              │   └── metadata
              │       ├── contentMetadata.xml
              │       ├── descMetadata.xml
              │       ├── embargoMetadata.xml
              │       ├── events.xml
              │       ├── identityMetadata.xml
              │       ├── provenanceMetadata.xml
              │       ├── rightsMetadata.xml
              │       ├── technicalMetadata.xml
              │       ├── versionMetadata.xml
              │       └── workflows.xml
              └── manifests
                  ├── fileInventoryDifference.xml
                  ├── manifestInventory.xml
                  ├── signatureCatalog.xml
                  ├── versionAdditions.xml
                  └── versionInventory.xml
```

An OCFL inventory that tracks the `data` directory would include a manifest comprised as follows. Note the absence of
the `manifests` directory, as we are not encapsulating the Moab object in an OCFL object, and the presence of
`contentDirectory` to specify `data` as the preserved content directory:

```json
{
  "digestAlgorithm": "sha512",
  "head": "v3",
  "id": "druid:bj102hs9687",
  "contentDirectory": "data",
  "manifest": {
    "98114a...588": [ "v0001/data/content/eric-smith-dissertation-augmented.pdf" ],
    "7f3d87...15b": [ "v0001/data/content/eric-smith-dissertation.pdf" ],
    "6d19f0...064": [ "v0001/data/metadata/technicalMetadata.xml" ],
    "6e4be4...375": [ "v0001/data/metadata/provenanceMetadata.xml" ],
    "d8a319...d0f": [ "v0001/data/metadata/descMetadata.xml" ],
    "de823a...acc": [ "v0001/data/metadata/rightsMetadata.xml" ],
    "080617...40c": [ "v0001/data/metadata/identityMetadata.xml" ],
    "e15267...58d": [ "v0001/data/metadata/versionMetadata.xml" ],
    "0d9e0b...9a2": [ "v0001/data/metadata/contentMetadata.xml" ],
    "dd9289...31d": [ "v0001/data/metadata/relationshipMetadata.xml" ],
    "7519c5...63f": [ "v0002/data/metadata/provenanceMetadata.xml" ],
    "abda4c...622": [ "v0002/data/metadata/workflows.xml" ],
    "76549e...b2b": [ "v0002/data/metadata/rightsMetadata.xml" ],
    "bdc4d6...3b6": [ "v0002/data/metadata/events.xml" ],
    "7b331c...f9b": [ "v0002/data/metadata/identityMetadata.xml" ],
    "80ceac...b9c": [ "v0002/data/metadata/versionMetadata.xml" ],
    "4853a2...fbe": [ "v0002/data/metadata/contentMetadata.xml" ],
    "1d5090...f5f": [ "v0002/data/metadata/relationshipMetadata.xml" ],
    "f209bf...ceb": [ "v0002/data/metadata/embargoMetadata.xml" ],
    "dd9125...d4b": [ "v0003/data/metadata/technicalMetadata.xml" ],
    "d9e177...477": [ "v0003/data/metadata/provenanceMetadata.xml" ],
    "4f5908...4f5": [ "v0003/data/metadata/workflows.xml" ],
    "e64db0...500": [ "v0003/data/metadata/descMetadata.xml" ],
    "05fa51...818": [ "v0003/data/metadata/rightsMetadata.xml" ],
    "d70dd8...5ad": [ "v0003/data/metadata/events.xml" ],
    "509a2d...dc6": [ "v0003/data/metadata/identityMetadata.xml" ],
    "548066...893": [ "v0003/data/metadata/versionMetadata.xml" ],
    "93884e...aae": [ "v0003/data/metadata/contentMetadata.xml" ],
    "4c5ab4...b02": [ "v0003/data/metadata/embargoMetadata.xml" ]
  },
  "type": "https://ocfl.io/1.1/spec/#inventory",
  "versions": {
    "v1": {
      "created": "2019-03-14T20:31:00Z",
      "state": {
        "98114a...588": [ "content/eric-smith-dissertation-augmented.pdf" ],
        "7f3d87...15b": [ "content/eric-smith-dissertation.pdf" ],
        "6d19f0...064": [ "metadata/technicalMetadata.xml" ],
        "6e4be4...375": [ "metadata/provenanceMetadata.xml" ],
        "d8a319...d0f": [ "metadata/descMetadata.xml" ],
        "de823a...acc": [ "metadata/rightsMetadata.xml" ],
        "080617...40c": [ "metadata/identityMetadata.xml" ],
        "e15267...58d": [ "metadata/versionMetadata.xml" ],
        "0d9e0b...9a2": [ "metadata/contentMetadata.xml" ],
        "dd9289...31d": [ "metadata/relationshipMetadata.xml" ]
      }
    },
    "v2": {
      "created": "2019-03-24T09:22:00Z",
      "state": {
        "98114a...588": [ "content/eric-smith-dissertation-augmented.pdf" ],
        "7f3d87...15b": [ "content/eric-smith-dissertation.pdf" ],
        "6d19f0...064": [ "metadata/technicalMetadata.xml" ],
        "7519c5...63f": [ "metadata/provenanceMetadata.xml" ],
        "d8a319...d0f": [ "metadata/descMetadata.xml" ],
        "76549e...b2b": [ "metadata/rightsMetadata.xml" ],
        "7b331c...f9b": [ "metadata/identityMetadata.xml" ],
        "80ceac...b9c": [ "metadata/versionMetadata.xml" ],
        "4853a2...fbe": [ "metadata/contentMetadata.xml" ],
        "1d5090...f5f": [ "metadata/relationshipMetadata.xml" ],
        "abda4c...622": [ "metadata/workflows.xml" ],
        "bdc4d6...3b6": [ "metadata/events.xml" ],
        "f209bf...ceb": [ "metadata/embargoMetadata.xml" ]
      }
    },
    "v3": {
      "created": "2019-04-02T11:07:00Z",
      "state": {
        "98114a...588": [ "content/eric-smith-dissertation-augmented.pdf" ],
        "7f3d87...15b": [ "content/eric-smith-dissertation.pdf" ],
        "dd9125...d4b": [ "metadata/technicalMetadata.xml" ],
        "d9e177...477": [ "metadata/provenanceMetadata.xml" ],
        "e64db0...500": [ "metadata/descMetadata.xml" ],
        "05fa51...818": [ "metadata/rightsMetadata.xml" ],
        "509a2d...dc6": [ "metadata/identityMetadata.xml" ],
        "548066...893": [ "metadata/versionMetadata.xml" ],
        "93884e...aae": [ "metadata/contentMetadata.xml" ],
        "1d5090...f5f": [ "metadata/relationshipMetadata.xml" ],
        "4f5908...4f5": [ "metadata/workflows.xml" ],
        "d70dd8...5ad": [ "metadata/events.xml" ],
        "4c5ab4...b02": [ "metadata/embargoMetadata.xml" ]
      }
    }
  }
}
```

### 5.6 Example Extended OCFL Storage Root
{: #example-extended-storage-root}

The following example OCFL Storage Root has an extension containing custom content. The OCFL Storage Root itself remains
valid.

```
[storage root]
    ├── 0=ocfl_1.1
    ├── extensions
    │   └── 0000-example-extension
    │       └── file-example.txt
    ├── ocfl_1.1.txt
    └── ocfl_layout.json
```

### 5.7 Example Extended OCFL Object
{: #example-extended-object}

The following example OCFL Object has an extension containing custom content. The OCFL Object itself remains valid.

```
[object root]
    ├── 0=ocfl_object_1.1
    ├── inventory.json
    ├── inventory.json.sha512
    ├── extensions
    │   └── 0000-example-extension
    │       └── file1-draft.txt
    └── v1
        ├── inventory.json
        ├── inventory.json.sha512
        └── content
            └── file.txt
```

## 6. References
{: #references}

### 6.1 Normative References
{: #normative-references}

<span id="ref-fips-180-4"/>**\[FIPS-180-4]** FIPS PUB 180-4 Secure Hash Standard. U.S. Department of Commerce/National
Institute of Standards and Technology. URL: <https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf>

<span id="ref-namaste"/>**\[NAMASTE]** Directory Description with Namaste Tags. J. Kunze.9 November 2009. URL:
<https://confluence.ucop.edu/download/attachments/14254149/NamasteSpec.pdf>

<span id="ref-rfc1321"/>**\[RFC1321]** The MD5 Message-Digest Algorithm. R. Rivest. IETF. April 1992. Informational.
URL: <https://www.rfc-editor.org/rfc/rfc1321>

<span id="ref-rfc2119"/>**\[RFC2119]** Key words for use in RFCs to Indicate Requirement Levels. S. Bradner. IETF.
March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

<span id="ref-rfc3339"/>**\[RFC3339]** Date and Time on the Internet: Timestamps. G. Klyne; C. Newman. IETF. July 2002.
Proposed Standard. URL: <https://www.rfc-editor.org/rfc/rfc3339>

<span id="ref-rfc3986"/>**\[RFC3986]** Uniform Resource Identifier (URI): Generic Syntax. T. Berners-Lee; R. Fielding;
L. Masinter. IETF. January 2005. Internet Standard. URL: <https://www.rfc-editor.org/rfc/rfc3986>

<span id="ref-rfc4648"/>**\[RFC4648]** The Base16, Base32, and Base64 Data Encodings. S. Josefsson. IETF. October 2006.
Proposed Standard. URL: <https://www.rfc-editor.org/rfc/rfc4648>

<span id="ref-rfc7693"/>**\[RFC7693]** The BLAKE2 Cryptographic Hash and Message Authentication Code (MAC). M-J.
Saarinen, Ed.; J-P. Aumasson. IETF. November 2015. Informational. URL: <https://www.rfc-editor.org/rfc/rfc7693>

<span id="ref-rfc8259"/>**\[RFC8259]** The JavaScript Object Notation (JSON) Data Interchange Format. T. Bray, Ed..
IETF. December 2017\. Internet Standard. URL: <https://www.rfc-editor.org/rfc/rfc8259>

### 6.2 Informative References
{: #informative-references}

<span id="ref-bagit"/>**\[BagIt]** The BagIt File Packaging Format (V1.0). J. Kunze; J. Littman; E. Madden; J.
Scancella; C. Adams. 17 September 2018. URL: <https://datatracker.ietf.org/doc/html/rfc8493>

<span id="ref-digest-algorithms-extension"/>**\[Digest-Algorithms-Extension]** OCFL Community Extension 0001: Digest
Algorithms. OCFL Editors.URL: <https://ocfl.github.io/extensions/0001-digest-algorithms.html>

<span id="ref-json-schema"/>**\[JSON-Schema]** JSON Schema Validation: A Vocabulary for Structural Validation of JSON.
A. Wright; H Andrews.20 September 2018. URL: <https://json-schema.org/latest/json-schema-validation.html>

<span id="ref-moab"/>**\[Moab]** The Moab Design for Digital Object Versioning. Richard Anderson.15 July 2013. URL:
<https://journal.code4lib.org/articles/8482>

<span id="ref-oais"/>**\[OAIS]** Reference Model for an Open Archival Information System (OAIS), Issue 2. June 2012.
URL: <https://public.ccsds.org/pubs/650x0m2.pdf>

<span id="ref-ocfl-implementation-notes"/>**\[OCFL-Implementation-Notes]** OCFL Implementation Notes v1.1. URL:
<https://ocfl.io/1.1/implementation-notes>

<span id="ref-pairtree"/>**\[PairTree]** Pairtrees for Object Storage. J. Kunze; M. Haye; E. Hetzner; M. Reyes; C.
Snavely. 12 August 2008\. URL: <https://confluence.ucop.edu/display/Curation/PairTree>

<span id="ref-rfc6068"/>**\[RFC6068]** The 'mailto' URI Scheme. M. Duerst; L. Masinter; J. Zawinski. IETF. October 2010.
Proposed Standard. URL: <https://www.rfc-editor.org/rfc/rfc6068>

<span id="ref-rfc7764"/>**\[RFC7764]** Guidance on Markdown: Design Philosophies, Stability Strategies, and Select
Registrations. S. Leonard. IETF. March 2016. URL:  <https://www.rfc-editor.org/rfc/rfc7764>

<span id="ref-rfc8141"/>**\[RFC8141]** Uniform Resource Names (URNs). P. Saint-Andre; J. Klensin. IETF. April 2017.
Proposed Standard. URL: <https://www.rfc-editor.org/rfc/rfc8141>
