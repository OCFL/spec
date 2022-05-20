---
---
<img src="https://avatars0.githubusercontent.com/u/35607965" alt="OCFL Hand-drive logo" style="float:right;width:307px;height:307px;"/>
# Implementation Notes, Oxford Common File Layout Specification
{:.no_toc}

Unofficial Draft 05 May 2022

Latest editor's draft: <https://ocfl.io/draft/implementation-notes/>

**Editors:**

* [Neil Jefferies](https://orcid.org/0000-0003-3311-3741), [Bodleian Libraries, University of Oxford](http://www.bodleian.ox.ac.uk/)
* [Rosalyn Metz](https://orcid.org/0000-0003-3526-2230), [Emory University](https://web.library.emory.edu/)
* [Julian Morley](https://orcid.org/0000-0003-4176-1933), [Stanford University](https://library.stanford.edu/)
* [Simeon Warner](https://orcid.org/0000-0002-7970-7855), [Cornell University](https://www.library.cornell.edu/)
* [Andrew Woods](https://orcid.org/0000-0002-8318-4225), [Harvard University](https://library.harvard.edu/)

**Additional Documents:**

* [Specification](https://ocfl.io/draft/spec/)
* [Validation Codes](https://ocfl.io/draft/spec/validation-codes.html)
* [Extensions](https://github.com/OCFL/extensions/)

**Previous version:**
* <https://ocfl.io/1.0/implementation-notes/>

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

This document provides guidance on implementation of the \[[OCFL-Specification](#ref-ocfl-specification)\] for how
clients should behave when operating on OCFL Objects.

## Table of Contents
{:.no_toc #table-of-contents}

* TOC placeholder (required by kramdown)
{:toc}

## 1. Digital Preservation
{: #digital-preservation}

### 1.1 Rebuildability
{: #rebuildability}

A key goal of the OCFL is the rebuildability of a repository from an OCFL storage root without additional information
resources. Consequently, a key implementation consideration should be to ensure that OCFL objects contain all the data
and metadata required to achieve this. With reference to the \[[OAIS](#ref-oais)\] model, this would include all the
descriptive, administrative, structural, representation, and preservation metadata relevant to the object.

Additionally, as an aid to those who may need to recover OCFL objects in the future, it is recommended that a copy of
the \[[OCFL-Specification](#ref-ocfl-specification)\] is stored in the top level of the OCFL storage root. The OCFL
ignores files other than the conformance declaration at the top level so it is a good location to store documentation
that may be useful for recovery.

A more complete approach would be to create a specific OCFL object that contains this documentation and to have a
pointer to its location in the storage root. This documentation object would then be subject to OCFL validation and any
other digital preservation processes that might be implemented without requiring special handling.

### 1.2 Fixity
{: #fixity}

The digests in the manifest are used by the OCFL for content addressability rather than fixity but they are suitable for
use as part of a fixity regime, and the manifest block usefully identifies all the files in an object. OCFL validation
also requires that digests and files match. However, while the characteristics of digest algorithms that make them
suitable for fixity checking and content addressing are closely related, they are not identical. In particular, fixity
against malicious tampering requires that a digest computation is hard to reverse, which is not a requirement for
content addressing. It is this aspect which is the most frequent target for cryptoanalytic attack.

Consequently, it is sensible to allow additional or alternative fixity algorithms to be used. These may be made in a
[fixity block](../spec/#fixity) which has the same layout as a manifest block but permits a broader range of algorithms.
The OCFL will consider a fixity block valid if all the files referenced in the block exist but the OCFL does not
validate digests for all possible algorithms. The fixity block does not have to include all the files in an object to
permit legacy fixity to be imported without requiring continued use of obsolete digest algorithms.

## 2. Storage
{: #storage}

### 2.1 Object Contents
{: #object-contents}

The OCFL separates the content path of stored files from the logical path of these files' content in OCFL object
versions. This is a key feature that allows previous versions of objects to remain immutable but permitting
deduplication, forward delta differencing, and easy file renaming. Consequently, the OCFL only requires that files added
to any version of an OCFL object must be stored somewhere within the relevant version directory, with a corresponding
entry in the manifest block. An entry in the state block determines the path and name of the file within that version by
referencing the manifest entry, not the actual path on disk.

The most transparent approach is to have the path used to store the file on disk the same as the path of the file within
the object when accessioned. This is readily understandable in terms of visual inspection of the physical filesystem.

However, this is not always possible. For example, complex objects with deep file hierarchies may encounter issues if
they come from a fileystem that allows longer paths than are supported by the target OCFL system. In this case, the
decoupling between content paths and logical paths in OCFL objects allows the use of truncated paths for storage while
the full paths can be preserved in state block entries which are not length constrained.

Another use case is importing content from other repository systems which renames files on ingest and stores them in a
flat hierarchy. These can be imported, as is, and the original paths and file names recorded through suitable state
block entries rather than reconstructing a physical file layout. Of course, the OCFL supports ongoing use of such a
methodology.

#### 2.1.1 Data and Metadata
{: #data-and-metadata}

OCFL object versions are composed of series of files/bitstreams but the OCFL does not make any distinction between
different types of files other than those reserved for OCFL functionality: the inventory, its digest file, and
conformance declaration files. It is possible, for example, to create separate data and metadata directories within each
version to help organize material but all files are treated equally for the purpose of OCFL validation and management.

#### 2.1.2 Deduplication
{: #deduplication}

The OCFL supports optional deduplication if a client ensures that all digests in the manifest block refer to a single
file path on disk. This entry is created the first time file content is stored in an OCFL Object. Subsequent references
to that file content should then occur in the state block only. This can be determined by computing the digests of
incoming files and determining if they already exist in the manifest block.

If deduplication is carried out within an object then, for consistency, it is expected that Forward Delta differencing
will also be used between object versions so subsequent references to duplicated content should also refer back to the
original manifest entry rather than updating it to include additional references.

#### 2.1.3 Filesystem metadata
{: #filesystem-metadata}

Filesystem metadata (e.g. permissions, access, and creation times) are not considered portable between filesystems or
preservable through file transfer operations. Nor can these attributes be validated in terms of fixity in a consistent
manner. As such, the OCFL neither explicitly supports nor expects that these attributes remain consistent. If retaining
this metadata is important then files should either be encapsulated in a filesystem image format that preserves this
information, or the metadata extracted and stored explicitly in an additional file.

#### 2.1.4 Empty Directories
{: #empty-directories}

The OCFL preserves files and their content, with directories serving as a useful organizational convention. An empty
directory consists only of filesystem metadata and therefore, as noted above, is not amenable to direct preservation in
OCFL objects. If the preservation of empty directories is considered essential then the suggested route is to insert a
zero length file named `.keep` into the directory which will ensure directories are preserved as part of the file's
path.

Note that `.keep` files are not considered special by the OCFL in any way and are treated exactly the same way as other
files. As such, a non-zero length `.keep` file is not considered invalid.

#### 2.1.5 Objects with Many Small Files
{: #objects-with-many-small-files}

Objects that contain a large number of files can pose performance problems if they are stored in a filesystem as-is.
Fixity checks, object validation and version creation can require an OCFL client to process all the files in an object
which can be time consuming. Additionally, most storage systems have a minimum block size for allocation to files, so a
large number of small files can end up occupying a volume of storage significantly larger than the sum of the individual
file sizes. In this case, assuming that the majority of the files are relatively static data that is unlikely to change
between objects versions, it is sensible to package the static files together in a single, larger file (zip is
recommended). This can be parsed to extract individual files if necessary but can significantly improve the efficiency
of basic OCFL client and storage operations.

### 2.2 Storage Root Hierarchy
{: #storage-root-hierarchy}

Strictly speaking, the OCFL only requires that an OCFL Storage Root contains OCFL Objects in directories, distributed in
some manner in the underlying filesystem. In turn, an OCFL object is identified purely by the presence of a
\[[NAMASTE](#ref-namaste)\] conformance file in the object root. The presence and correctness of inventory files and
version directories are a validation rather than an identification concern.

These definitions allow a lot of freedom as to how objects are arranged beneath an OCFL Storage Root and, while there is
no strict requirement for all OCFL Objects to be arranged according the same system it is nevertheless considered good
practice to do so. In addition, in the interests of rebuildability, it would be prudent to include an indication of the
details of this arrangement alongside the OCFL specification as described in the Rebuildability section.

In the interests of transparency it makes sense for an object's URI, its unique identifier and its location under the
OCFL Storage Root to be aligned and simply derivable from each other. Good examples include:

  * ```
[storage_root]
                ├── 0=ocfl_1.1
                ├── ocfl_1.1.html (optional copy of the OCFL specification)
                ├── d45be626e024
                |   ├── 0=ocfl_object_1.1
                |   ├── inventory.json
                |   ├── inventory.json.sha512
                |   └── v1...
                ├── d45be626e036
                |   ├── 0=ocfl_object_1.1
                |   ├── inventory.json
                |   ├── inventory.json.sha512
                |   └── v1...
                ├── 3104edf0363a
                |   ├── 0=ocfl_object_1.1
                |   ├── inventory.json
                |   ├── inventory.json.sha512
                |   └── v1...
                └── ...
```

* Flat: Each object is contained in a directory with a name that is simply derived from the unique identifier of the
object, possibly with the escaping or replacement of characters that are not permitted in file and directory names.
While this is a very simple approach, most filesystems begin to encounter performance issues when directories contain
more than a few thousand files so this arrangement is best suited to repositories with a small number of objects (or
many OCFL Storage Roots).

  * ```
[storage_root]
                ├── 0=ocfl_1.1
                ├── ocfl_1.1.html (optional copy of the OCFL specification)
                ├── d4
                |   └── 5b
                |       └── e6
                |           └── 26
                |               └── e0
                |                   ├── 24
                |                   |   └──d45be626e024
                |                   |       ├── 0=ocfl_object_1.1
                |                   |       └── ...
                |                   └── 36
                |                       └──d45be626e036
                |                           ├── 0=ocfl_object_1.1
                |                           └── ...
                ├── 31
                |   └── 04
                |       └── ed
                |           └── f0
                |               └── 36
                |                   └── 3a
                |                       └── 3104edf0363a
                |                           ├── 0=ocfl_object_1.1
                |                           └── ...
                └── ...
```

* PairTree: \[[PairTree](#ref-pairtree)\] is designed to overcome the limitations on the number of files in a directory
that most file systems have. It creates hierarchy of directories by mapping identifier strings to directory paths two
characters at a time. For numerical identifiers specified in hexadecimal this means that there are a maximum of 256
items in any directory which is well within the capacity of any modern filesystem. However, for long identifiers,
pairtree creates a large number of directories which will be sparsely populated unless the number of objects is very
large. Traversing all these directories during validation or rebuilding operations can be slow.

  * ```
[storage_root]
                ├── 0=ocfl_1.1
                ├── ocfl_1.1.html (optional copy of the OCFL specification)
                ├── d45
                |   └── be6
                |       └── 26e
                |           ├──d45be626e024
                |           |  ├── 0=ocfl_object_1.1
                |           |  └── ...
                |           └──d45be626e036
                |              ├── 0=ocfl_object_1.1
                |              └── ...
                ├── 310
                |   └── 4ed
                |       └── f03
                |           └── 3104edf0363a
                |               ├── 0=ocfl_object_1.1
                |               └── ...
                └── ...
```

* Truncated n-tuple Tree: This approach aims to achieve some of the scalability benefits of PairTree whilst limiting the
depth of the resulting directory hierarchy. To achieve this, the source identifier can be split at a higher level of
granularity, and only a limited number of the identifier digits are used to generate directory paths. For example, using
triples and three levels with example above yields:

Some identifier schemes may require transformation before such approaches can be used effectively. A simple example
would be sequentially assigned identifiers, which would not distribute objects within the filesystem evenly. Hash
functions may be used to provide a unidirectional mapping between URI/PID and filesystem path, as required by the OCFL.
Encryption algorithms may be used to provide a bi-directional mapping which may be a useful aid to human readability.
Relevant details should be referenced in `ocfl_layout.json` in the Storage Root.

### 2.3 Filesystem Features
{: #filesystem-features}

In order to be portable across as many filesystems as possible, the OCFL makes use of a subset of filesystem features
that are very broadly supported. It is therefore strongly advised to not use additional features in OCFL Storage Roots
since OCFL clients and other filesystem tools that need to operate between different filesystems may exhibit
unpredictable behaviour when feature sets do not match. In particular, using features such as hard and soft (symbolic)
links for deduplication can work at odds with the OCFL's own mechanisms and should be avoided.

Consideration should also be given to calculations of storage usage when migrating between filesystems. Many back-end
filesystem features, which are essentially invisible to user-space code, can have a significant impact on the actual
consumption of storage space compared with the a simple sum of file sizes. Compression, extents and block sub-allocation
are examples of such features which, while providing benefits in terms of storage efficiency, do require care when
considering issues of capacity planning or migration.

## 3. Client Behaviors
{: #client-behaviors}

### 3.1 Basic File Operations
{: #basic-file-operations}

The OCFL and its inventory structure are designed to support and capture the following file operations that create OCFL
versions, regardless of whether optional features, such as deduplication, are used. The OCFL is not concerned with the
process of creating versions but only the final outcome in terms of the differences with the previous version that need
to be recorded and preserved.

* Inheritance: By default a new version of an OCFL Object inherits all the filenames and file content from the previous
version. This serves as the basis against which changes are applied to create a new version. A newly created OCFL
Object, obviously, inherits no content and is populated by file additions.

* Addition: Adds a new file path and corresponding content to an OCFL Object. The path cannot exist in the previous
version of the object, and the content cannot have existed in any earlier versions of the object.

* Updating: Changes the content pointed to by an content path. The path must exist in the previous version of the OCFL
Object, and the content cannot have existed in any earlier versions of the object.

* Renaming: Changes the file path of existing content. The path cannot exist in the previous version of the OCFL Object,
and the content cannot have existed in any earlier versions of the object.

* Deletion: Removes a file path and corresponding content from the current version of an OCFL Object. The path and
content remain available in earlier versions of the object.

* Reinstatement: Makes content from a version earlier than the previous version available in the current version of an
OCFL Object. The content must exist in an earlier version, and not the previous version. The file path may exist in the
previous version, effectively updating the file path with older content, or it may not, effectively adding the older
content as a new file.

* Purging: Purging, as distinct from deletion, covers the complete removal of a file path and corresponding content from
all versions of an OCFL Object. This is a special case that is not supported as part of regular OCFL versioning
operations. An approach to implementing this is covered in a later section.

### 3.2 Versioning
{: #versioning}

#### 3.2.1 Version Numbering
{: #version-numbering}

Version numbering should start with 1 and be positive sequential integers. Names start with a lower case `v`. The
numbers may be zero padded to the left to give fixed length, but, if used, zero padded numbers must always retain at
least one leftmost zero. All versions in an object must use the same version numbering layout which can be easily
determined by looking at one existing version — if the digit following `v` is a zero then the number format is zero
padded to fixed length, otherwise it is simply an integer.

Systems with version directories have often used zero padding in order to show version order with common lexical sorting
tools (such as Unix `ls`). Zero padding is not recommended in order to avoid having to make arbitrary choices of padding
length or to place limits on the number of versions supported.

#### 3.2.2 Version Immutability
{: #version-immutability}

Previous versions of an object should be considered immutable since the composition of later versions of an object may
be dependent on them. In addition, the assumption of immutability ensures that copies of different versions of an object
remain consistent with each other, avoiding issues with identifying canonicity and reconciliation.

One key consequence of this immutabilty is that manifest entries should never be deleted. New entries may be created,
and, if not deduplicating file content, additional references to copies of stored content may be added.

### 3.3 File Purging
{: #file-purging}

Sometimes a file needs to be deleted from all versions of an object, perhaps for legal reasons. Doing this to an OCFL
Object breaks the previous version immutability assumption and is not supported directly. The correct way to do this is
to create a new object that excludes the offending file, with a revised version history taking this into account. The
original object can then be deleted in its entirety. Creating the new object first is good practice as it avoids any
risk of data loss that may occur if an object were to be deleted before the new object is created.

The new object need not have the same identifier as the original object. In this case, the deleted object may be
replaced by a placeholder object using the original identifier and location in the OCFL Storage Root. This is a standard
OCFL object with content that redirects users and software to the new version - possibly with an indication of why the
new object was created, if appropriate. The OCFL does not define redirect mechanisms, the interpretation of object
contents is purely a client application concern.

### 3.4 Migrating to a New Digest Algorithm
{: #digest-migration}

Over time new digest algorithms are developed to increase security and address vulnerabilities in existing algorithms.
It may become desirable to migrate an object to use a new algorithm while retaining [Version
Immutability](#version-immutability). OCFL supports this through the creation of a new version with a new
`digestAlgorithm` that either retains the same object content or is combined with a content update.

Consider an example OCFL object where the `digestAlgorithm` in the `inventory.json` is `sha256` and the OCFL object
contains a single file (`file.txt`). We will illustrate migration to use `sha512` without changing the object content.
The starting `v1` file layout is:

```
[object root]
    ├── 0=ocfl_object_1.1
    ├── inventory.json
    ├── inventory.json.sha256
    └── v1
        ├── inventory.json
        ├── inventory.json.sha256
        └── content
            └── file.txt
```

and the corresponding inventory is:

```
{
  "digestAlgorithm": "sha256",
  "head": "v1",
  "id": "http://example.org/digest_update_example",
  "manifest": {
    "579391...bfe": [
      "v1/content/file.txt"
    ]
  },
  "type": "https://ocfl.io/1.1/spec/#inventory",
  "versions": {
    "v1": {
      "created": "2020-01-01T01:01:01",
      "message": "sha256 forever",
      "state": {
        "579391...bfe": [
          "file.txt"
        ]
      },
      "user": {
        "address": "mailto:secret@example.org",
        "name": "Secret Agent"
      }
    }
  }
}
```

We create a new version, `v2`, using the `digestAlgorithm``sha512`. The `v1` directory and inventory are unchanged. The
`v2` directory has no `content` directory because no new content is added. The new inventory uses `sha512` values for
the `manifest` and `state` blocks, the legacy `sha256` digests are retained in the `fixity` block as an implementation
choice. The file layout of the object with `v2` is:

```
[object root]
    ├── 0=ocfl_object_1.1
    ├── inventory.json
    ├── inventory.json.sha512
    ├── v1
    │   ├── content
    │   │   └── file.txt
    │   ├── inventory.json
    │   └── inventory.json.sha256
    └── v2
        ├── inventory.json
        └── inventory.json.sha512
```

and the corresponding `v2` inventory is:

```
{
  "digestAlgorithm": "sha512",
  "fixity": {
    "sha256": {
      "579391...bfe": [
        "v1/content/file.txt"
      ]
    }
  },
  "head": "v2",
  "id": "http://example.org/digest_update_example",
  "manifest": {
    "7545b8720a60123...f67": [
      "v1/content/file.txt"
    ]
  },
  "type": "https://ocfl.io/1.1/spec/#inventory",
  "versions": {
    "v1": {
      "created": "2020-01-01T01:01:01",
      "message": "sha256 forever",
      "state": {
        "7545b8720a60123...f67": [
          "file.txt"
        ]
      },
      "user": {
        "address": "mailto:secret@example.org",
        "name": "Secret Agent"
      }
    },
    "v2": {
      "created": "2020-03-26T21:00:00",
      "message": "Update sha256 to sha512, no content change",
      "state": {
        "7545b8720a60123...f67": [
          "file.txt"
        ]
      },
      "user": {
        "address": "mailto:special@example.org",
        "name": "Special Agent"
      }
    }
  }
}
```

### 3.5 Log Information
{: #log-information}

There may be the need to record some actions on objects that do not result in changes to the object content. For
example, copying the object to new storage or validating fixity and finding nothing amiss. The `log` directory is the
location in an OCFL object where such events can be recorded. The OCFL does not make any assumptions about the contents
of this directory but, if it exists, then its contents will not be subject any validation processes.

### 3.6 Forward Delta
{: #forward-delta}

Forward delta differencing is a key, though optional, feature of the OCFL that means that parts of an OCFL object
version that are unchanged from a previous version are not stored again. This has the potential to significantly improve
storage efficiency when objects have multiple versions, whether through ongoing curatorial action or the accessioning of
updated material.

When a new version of an OCFL Object is created from an earlier version and a client wishes to implement forward delta
differencing, then the possible file operations are handled in the following manner (with reference to the state and
manifest blocks of the OCFL object's inventory file):

* Inheritance: Files inherited from the previous version unchanged are referenced in the `state` block of the new
version. These entries will be identical to the corresponding entries in the previous version's `state` block. No
changes to the `manifest` block are required. When a new OCFL version of an OCFL Object is created, the starting point
against which changes are made should be to copy the entire `state` block of the previous version, thus inheriting all
the files and content from the previous version.

* Addition: Newly added files appear as new entries in the `state` block of the new version. The file should be stored
and an entry for the new content must be made in the `manifest` block of the object's inventory. The new digest from the
`manifest` block can then be used to create the new `state` block entry. If the file content, as determined by its
digest, corresponds to an existing `manifest` entry then, technically, this is a reinstatement operation rather than
addition and should be flagged to prevent the operation being recorded incorrectly in preservation logs.

* Updating: Files updated from the previous version appear as changed entries in the `state` block of the new version -
with new digests associated with content paths. The updated file should be stored and a new entry for the updated
content must be made in the `manifest` block of the object's inventory. The new digest can then be used to replace the
digest for the old content in the relevant `state` block entry. If the file content, as determined by its digest,
corresponds to an existing `manifest` entry then, technically, this is a reinstatement operation rather than updating
and should be flagged to prevent the operation being recorded incorrectly in preservation logs.

* Renaming: Files renamed from the previous version appear as changed entries in the `state` block of the new version -
with existing digests associated with new file paths. No changes to the `manifest` block are required.

* Deletion: Files deleted from the previous version are simply removed from the `state` block of the new version.

* Reinstatement: Since reinstated content already exists in earlier versions of the OCFL Object, no changes to the
`manifest` block are required. Reinstated entries in the `state` block should replace any entries with the same path
inherited from the previous version. If the file paths are unchanged then these entries will be identical to the
corresponding entries in the earlier version's `state` block.

### 3.7 An Example Approach to Updating OCFL Object Versions
{: #an-example-approach-to-updating-ocfl-object-versions}

The OCFL is designed to be a specification that covers objects at rest and consequently does not specify in detail
update and file locking mechanisms since these are implementation dependent features. Nevertheless, this section
includes a simple example of a way to update OCFL Objects in a manner that tries to ensure that updates are as
transactional as possible, and that failures are detectable and recoverable. Objects that are being updated are, of
course, not expected to be valid OCFL objects until the update operation is completed. Creating a new OCFL Object only
differs from updating in that it involves creating a version directory before version update logic takes over.

#### 3.7.1 Segregating Objects-in-flight
{: #segregating-objects-in-flight}

While an OCFL Object is being created or updated, the files and folders being written should be assembled in a location
that is ignored by OCFL parsers and validators. When an OCFL Version is transferred to the OCFL Object Root, the top
level inventory should be updated as the final operation. This ensures that all the files referenced by the inventory
are valid and, consequently, read-only clients that reference the inventory should continue to operate normally except
for the brief moment when the inventory is actually being updated. In practice, it is expected that upstream caching
should be able to cover this momentary unavailability in the majority of cases. This example approach defines the
following:

* Workspace: Any OCFL Client should have a place to assemble versions before they are transferred to the Storage Root to
make the transfer operation easier to implement in a controllable and recoverable manner. Ideally it should be within
the same filesystem/namespace to make file transfers as atomic as possible, comprising filesystem metadata changes
rather than file copy operations. The Workspace is a directory that contains all such objects-in-flight in a similar
layout to an OCFL Storage Root.

* Object Workspace Directory: In this example, for simplicity, each OCFL Object being created or updated has a path in
the Workspace that is the same as its eventual storage path in the OCFL Storage Root. This means that it is easy for
clients to determine if an object is being updated and also provides a mechanism to implement objects with mutable
current versions without violating OCFL assumptions. When updating an OCFL Object, it is useful to make a copy of the
inventory of most recent stable version of the object in this directory when it is created at the start of the update
operation.

* Version Assembly Directory: In this case, one version assembly directory should exist per OCFL Object at any time and
updates to it should be managed by a single controlling process to avoid conflicts. If updates to multiple objects, or
from multiple sources, need to be supported, then it should be implemented upstream of version assembly in order to
allow additional locking and conflict resolution. It is useful to have a unique transaction identifier for each object
being updated to simplify any overlying process control logic (For example, it could be used as an eTag for a REST API
implementation). This transaction identifier can be used to generate a name for the version assembly directory, which
sits within the object workspace directory.

* Temporary Inventory Files: A top level object inventory file should never be updated in situ. Instead, a new inventory
should be created in a version assembly directory and updated as the version contents are modified. This provides some
level of forensic recovery information in the event of failure during version creation. When the construction of the new
version and its inventory is complete, it can then be copied to a temporary file name alongside the top level inventory.
In this case, temporary inventory files always occur in OCFL Object Roots and are named `tmp_inventory.json`, for
argument's sake. The presence of this file is not valid OCFL and indicative of an update failure.

#### 3.7.2 Operational Logic
{: #operational-logic}

Bearing in mind the definitions specified above, it is possible to sketch out how they can be used to ensure some level
of integrity during OCFL updates.

##### 3.7.2.1 Initiating a New Object Version
{: #initiating-a-new-object-version}

1. Generate a new transaction ID

2. Does a version assembly directory (in the requisite object workspace directory) for the object in question exist? If
yes, then abort with error - there is a transaction in process. Do not start a new transaction without rereading the
updated object.

3. Create a version assembly directory and save the transaction ID - in this case, using it as the version assembly
directory name.

4. Copy inventory from object into version assembly directory as a starting point for the new version

##### 3.7.2.2 Updating a New Object Version
{: #updating-a-new-object-version}

1. Get current transaction ID

2. Does a version assembly directory for the object and transaction ID in question exist? If no, then abort with error -
the transaction ID is invalid for some reason, need to debug!

3. Update object as described earlier.

##### 3.7.2.3 Finalizing a New Object Version
{: #finalizing-a-new-object-version}

1. Get current transaction ID

2. Does a version assembly directory for the object and transaction ID in question exist? If no, then abort with error -
the transaction ID is invalid for some reason, need to debug!

3. Generate inventory checksum file in version assembly directory. This effectively locks and finalizes the inventory.

4. Move/rename version assembly directory to valid OCFL version directory name in OCFL Object Root in the OCFL Storage
Root. At this point all of the new version content is in place in the OCFL Object but the top level inventory still
references the previous version. This is assumed to be an atomic operation. Otherwise, copy the version assembly
directory, keeping its name then rename to a valid version directory.

5. Copy inventory from new version to top level temporary inventory file.

6. Update the inventory by deleting the old one and renaming the temporary one. This should not take very long and is
the only time when read-only clients cannot access the object because the inventory is not valid.

7. Update the inventory checksum by deleting the old one and copying the one from the new version.

8. Delete the transaction ID

9. Clean up the Workspace to remove stale Object and version assembly directories

##### 3.7.2.4 Clean up after failure
{: #clean-up-after-failure}

1. Delete version assembly directories and temporary inventory files - this automatically reverts objects to last known
good version. Assembly directories anywhere in an OCFL Storage Root are a result of failed copies.

2. If the inventory checksum fails then the inventory is corrupted by a failed copy. This should be recoverable from the
most recent version directory (which is the newly created one).

3. Any overlying transactional store will need cleanup but basically repeat 5-9 above after validating all object
checksums - considering some sort of failure has just occurred.

## 4. References
{: #references}

### 4.1 Informative References
{: #informative-references}

<span id="ref-namaste"/>**\[NAMASTE]** Directory Description with Namaste Tags. J. Kunze.9 November 2009. URL:
<https://confluence.ucop.edu/download/attachments/14254149/NamasteSpec.pdf>

<span id="ref-oais"/>**\[OAIS]** Reference Model for an Open Archival Information System (OAIS), Issue 2. June 2012.
URL: <https://public.ccsds.org/pubs/650x0m2.pdf>

<span id="ref-ocfl-specification"/>**\[OCFL-Specification]** OCFL Specification. URL: <https://ocfl.io/draft/spec>

<span id="ref-pairtree"/>**\[PairTree]** Pairtrees for Object Storage. J. Kunze; M. Haye; E. Hetzner; M. Reyes; C.
Snavely. 12 August 2008\. URL: <https://confluence.ucop.edu/display/Curation/PairTree>

