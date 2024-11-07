---
no_site_title: true
---
<img src="https://avatars0.githubusercontent.com/u/35607965" alt="OCFL Hand-drive logo" style="float:right;width:307px;height:307px;"/>
# Oxford Common File Layout Specification v1.1 Change Log
{:.no_toc}

7 October 2022 for v1.1.0, updated 8 November 2024 for v1.1.1

**Editors:**

* [Neil Jefferies](https://orcid.org/0000-0003-3311-3741), [Bodleian Libraries, University of Oxford](http://www.bodleian.ox.ac.uk/)
* [Rosalyn Metz](https://orcid.org/0000-0003-3526-2230), [Emory University](https://web.library.emory.edu/)
* [Julian Morley](https://orcid.org/0000-0003-4176-1933), [Stanford University](https://library.stanford.edu/)
* [Simeon Warner](https://orcid.org/0000-0002-7970-7855), [Cornell University](https://www.library.cornell.edu/)
* [Andrew Woods](https://orcid.org/0000-0002-8318-4225), [Harvard University](https://library.harvard.edu/)

This document is licensed under a [Creative Commons Attribution 4.0
License](https://creativecommons.org/licenses/by/4.0/). [OCFL logo:
"hand-drive"](https://avatars0.githubusercontent.com/u/35607965) by
[Patrick Hochstenbach](http://orcid.org/0000-0001-8390-6171) is
licensed under [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/).

## Contents

This change log combines logs of changes from [Version 1.0 of the OCFL Specification](https://ocfl.io/1.0/spec/) through
[Version 1.1.1 of the OCFL Specification](https://ocfl.io/1.1/spec/):

  * [Changes from OCFL v1.0 to v1.1.0](#changes-from-ocfl-v10-to-v110)
  * [Changes from OCFL v1.1.0 to v1.1.1](#changes-from-ocfl-v110-to-v111)

## Changes from OCFL v1.0 to v1.1.0

[Version 1.1.0 of the OCFL Specification](https://ocfl.io/1.1.0/spec/) is a [minor version](https://semver.org/) update to the [OCFL Specification v1.0](https://ocfl.io/1.0/spec/). The focus is correction and clarification, plus the addition of backwards compatible rules for the specification conformance of prior object versions.

### Additions in v1.1.0

#### Add requirements to specification version number sequence

Added [Conformance of prior versions](https://ocfl.io/1.1/spec/#conformance-of-prior-versions) section to clarify that existing version directories in an object are immutable and that the specification version number sequence must be monotonic. Adds error code [E103](https://ocfl.io/1.1/spec/#E103). (Issue [#544](https://github.com/OCFL/spec/issues/544))

### Clarifications in v1.1.0

#### One conformance declaration per object and storage root

Update the [Object Conformance Declaration](https://ocfl.io/1.1/spec/#object-conformance-declaration) and [Root Conformance Declaration](https://ocfl.io/1.1/spec/#root-conformance-declaration) sections to clarify that there must be exactly one version declaration file. Error codes [E003](https://ocfl.io/1.1/spec/#003) and [E076](https://ocfl.io/1.1/spec/#E076) correspondingly updated. (Issue [#581](https://github.com/OCFL/spec/issues/581))

#### Inventory uses UTF-8 encoding

In [Inventory](https://ocfl.io/1.1/spec/#inventory) section, clarify that UTF-8 encoded JSON must be used for the `inventory.json` files. (Issue [#514](https://github.com/OCFL/spec/issues/514))

#### Version naming convention

Update wording in [Version Directories](https://ocfl.io/1.1/spec/#version-directories) section to talk about version consistency for all versions of an object-at-rest, rather than in terms of the process for adding a version. (Issue [#541](https://github.com/OCFL/spec/issues/541))

#### Clarify manifest block requirements

Add language in [Manifest](https://ocfl.io/1.1/spec/#manifest) section to clarify that the `manifest` block must be a JSON object (adding error code [E106](https://ocfl.io/1.1/spec/#E106)) and that the each key must correspond to a digest value key found in one or more `state` blocks (adding error code [E107](https://ocfl.io/1.1/spec/#E107)). (Issue [#537](https://github.com/OCFL/spec/issues/537))

#### Clarify manifest requirements in historic inventories

Wording of the [Content Directory](https://ocfl.io/1.1/spec/#content-directory) section improved to make it clear that for each historical inventory, the manifest must reference every file in that version directory. (Issue [#538](https://github.com/OCFL/spec/issues/538))

#### Clarify language and error codes for version numbers

Change [Version Directories](https://ocfl.io/1.1/spec/#version-directories) section to be more specific about version numbers. Adds error code [E104](https://ocfl.io/1.1/spec/#E104) for the specific case of missing prefix `v`, and [E105](https://ocfl.io/1.1/spec/#E105) for the specific case of using positive base-ten integers. (Issue [#532](https://github.com/OCFL/spec/issues/532))

#### Clarify that the content directory must be a direct child of the version directory

Change [Content Directory](https://ocfl.io/1.1/spec/#content-directory) section to make it clear that the `contentDirectory` must indicate a direct child of the version directory. Adds error code [E108](https://ocfl.io/1.1/spec/#E108). (Issue [#530](https://github.com/OCFL/spec/issues/530))

#### Clarify that `id` must be the same across all versions

Update [Basic Structure](https://ocfl.io/1.1/spec/#inventory-structure) section to make it clear that the `id` must not change between versions of the same object. Adds error code [E110](https://ocfl.io/1.1/spec/#E110). (Issue [#542](https://github.com/OCFL/spec/issues/542))

#### Use logical state consistently

Use the notion of "logical state" consistently in the [Version](https://ocfl.io/1.1/spec/#version), [Version Inventory and Inventory Digest](https://ocfl.io/1.1/spec/#version-inventory) and [BagIt in an OCFL Object](https://ocfl.io/1.1/spec/#example-bagit-in-ocfl) sections. (Issue [#571](https://github.com/OCFL/spec/issues/571))

#### Clarify digest value case sensitivity requirements

Change [Manifest](https://ocfl.io/1.1/spec/#manifest) and [Fixity](https://ocfl.io/1.1/spec/#fixity) sections to make it clear that the additional requirement for each digest value to appear only once in the manifest or fixity block applies only to case-insensitive digest algorithms. (Issue [#573](https://github.com/OCFL/spec/issues/573))

#### Clarify that fixity value must be a JSON object

Change [Fixity](https://ocfl.io/1.1/spec/#fixity) section to specify that the value of the `fixity` key must be a JSON object. An empty object (`{}`) is allowed, but a JSON `null` value is not. Added error code [E111](https://ocfl.io/1.1/spec/#E111) and made [E055](https://ocfl.io/1.1/spec/#E055) more specific. (Issue [E558](https://github.com/OCFL/spec/issues/558))

#### Clarify use of registered and local extensions

Change [Object Extensions](https://ocfl.io/1.1/spec/#object-extensions) and [Storage Root Extensions](https://ocfl.io/1.1/spec/#storage-root-extensions) to define registered extensions in terms of the [OCFL Extensions Repository](https://ocfl.github.io/extensions/). Added [Documenting Local Extensions](https://ocfl.io/1.1/spec/#documenting-local-extensions) section to describe local extensions. Adds error codes [E112](https://ocfl.io/1.1/spec/#E112) and [E113](https://ocfl.io/1.1/spec/#E113), updates error code [E067](https://ocfl.io/1.1/spec/#E067), and removes error codes `E068` and `E086` which were not being used within the community. Adds warning code [W016](https://ocfl.io/1.1/spec/#W016). (Issues [#557](https://github.com/OCFL/spec/issues/557), [#565](https://github.com/OCFL/spec/issues/565))

#### Improve guidance on inclusion of specification in storage root

With the change from ReSpec to Markdown as the source format for the OCFL Specification it is now easy to store a complete copy of the specification in a storage root. This version suggests using the filename `ocfl_1.1.md` for a copy of the human-readable Markdown specification in the [Root Structure](https://ocfl.io/1.1/spec/#root-structure) section. (Issues [#505](https://github.com/OCFL/spec/issues/505), [#554](https://github.com/OCFL/spec/issues/554))

#### Fix examples to match the specification

Correct several examples that in the 1.0 specification did not fully comply with the specification. (Issue [#539](https://github.com/OCFL/spec/issues/539))

#### Reference RFC version of Bagit specification

Update the reference to the Bagit specification from the draft <https://tools.ietf.org/html/draft-kunze-bagit-17> to [RFC8493](https://datatracker.ietf.org/doc/html/rfc8493). (Issue [#571](https://github.com/OCFL/spec/issues/571))

### Corrections to validation codes

#### Per-version validation codes

Even for minor releases the validations codes may be updated. We have thus moved the `validation-codes.md` file into each version directory so that will be versioned along with the specification. The version of this file for the v1.1 specification is rendered as <https://ocfl.io/1.1/spec/validation-codes.html>. (Issue [#553](https://github.com/OCFL/spec/issues/553))

#### Fix E048 description

The E048 error description in `validation-codes.md` is corrected to remove mention of `message` and `user` because they are optional. (Issue [#531](https://github.com/OCFL/spec/issues/531))

#### Fix E070 description

The E070 error description in `validation-codes.md` is corrected to refer to `extension` rather than `key` (which was left from an earlier draft). (Issue [#573](https://github.com/OCFL/spec/issues/573))

## Changes from OCFL v1.1.0 to v1.1.1

[Version 1.1.1 of the OCFL Specification](https://ocfl.io/1.1/spec/) is a [patch version](https://semver.org/) update to the [OCFL Specification v1.1.0](https://ocfl.io/1.1.0/spec/). There are only clarifications.

### Clarifications in v1.1.1

#### Reword filesystem case sensitivity comments

Version 1.1.0 had an unenforceable MUST regarding filesystem case preservation. The [Filesystem Features](https://ocfl.io/1.1/spec/#filesystem-features) section was change to instead point out that implementation over filesystems that either do not preserve case or are not case sensitive require great care, including making appropriate choices for file paths and filenames. (Issue [#528](https://github.com/OCFL/spec/issues/528))

#### A range of specification sections covering Object Structure

The range of specification sections (3.2 through 3.9) specifying the (Object Structure)[#object-structure] was added to make that explicit. (Issue [#637](https://github.com/OCFL/spec/issues/637))

#### Clarify description of fixity in Implementation Notes

The [fixity](https://ocfl.io/1.1/implementation-notes/#fixity) section of the Implementation Notes has been updated to point out differences in requirements for digests used for content addressing (the manifest and state blocks) and fixity (the fixity block). The section also notes that fixity algorithms may generate the same value for different file content. (Issue [#629](https://github.com/OCFL/spec/issues/629))

#### Update links to Pairtree and NAMASTE specifications

Links to both the Pairtree and NAMASTE specifications have been updates in the [Specification references](https://ocfl.io/1.1/spec/#references) and the [Implementation Notes references](https://ocfl.io/1.1/implementation-notes/#references). (Issues [#627](https://github.com/OCFL/spec/issues/627) and [#629](https://github.com/OCFL/spec/issues/629#issuecomment-1623865455))

### Corrections to validation codes

#### Unenforceable code E091 removed

The E091 code "Filesystems MUST preserve the case of OCFL filepaths and filenames" was unenforceable and was removed as part of rewording the case sensitivity advice. (Issue [#528](https://github.com/OCFL/spec/issues/528))
