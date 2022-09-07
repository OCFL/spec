---
no_site_title: true
---
<img src="https://avatars0.githubusercontent.com/u/35607965" alt="OCFL Hand-drive logo" style="float:right;width:307px;height:307px;"/>
# Oxford Common File Layout Specification v1.1 Change Log
{:.no_toc}

Draft 6 September 2022

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

## Changes from OCFL v1.0 to v1.1

[Version 1.1 of the OCFL Specification](https://ocfl.io/draft/spec/) is a [minor version](https://semver.org/) update to the [OCFL Specification v1.0](https://ocfl.io/1.0/spec/). It is intended to add functionality in a backwards compatible manner, and to clarify certain aspects based on a community feedback.

### Additions in v1.1

#### Add requirements to version number sequence

Added [Conformance of prior versions](https://ocfl.io/draft/spec/#conformance-of-prior-versions) section to clarify that existing version directories are immutable and that the version number sequence must be monotonic. Adds error code [E103](https://ocfl.io/draft/spec/#E103). (Issue [#544](https://github.com/OCFL/spec/issues/544))

### Clarifications in v1.1

#### One conformance declaration per object and storage root

Update the [Object Conformance Declaration](https://ocfl.io/draft/spec/#object-conformance-declaration) and [Root Conformance Declaration](https://ocfl.io/draft/spec/#root-conformance-declaration) sections to clarify that there must be exactly one version declaration file. Error codes [E003](https://ocfl.io/draft/spec/#003) and [E076](https://ocfl.io/draft/spec/#E076) correspondingly updated. (Issue [#581](https://github.com/OCFL/spec/issues/581))

#### Inventory uses UTF-8 encoding

In [Inventory](https://ocfl.io/draft/spec/#inventory) section, clarify that UTF-8 encoded JSON must be used for the `inventory.json` files. (Issue [#514](https://github.com/OCFL/spec/issues/514))

#### Version naming convention

Update wording in [Version Directories](https://ocfl.io/draft/spec/#version-directories) section to talk about version consistency for all versions of an object-at-rest, rather than in terms of the process for adding a version. (Issue [#541](https://github.com/OCFL/spec/issues/541))

#### Clarify manifest block requirements

Add language in [Manifest](https://ocfl.io/draft/spec/#manifest) section to clarify that the `manifest` block must be a JSON object (adding error code [E106](https://ocfl.io/draft/spec/#E106)) and that the each key must correspond to a digest value key found in one or more `state` blocks (adding error code [E107](https://ocfl.io/draft/spec/#E107)). (Issue [#537](https://github.com/OCFL/spec/issues/537))

#### Clarify manifest requirements in historic inventories

Wording of the [Content Directory](https://ocfl.io/draft/spec/#content-directory) section improved to make it clear that for each historical inventory, the manifest must reference every file in that version directory. (Issue [#538](https://github.com/OCFL/spec/issues/538))

#### Clarify language and error codes for version numbers

Change [Version Directories](https://ocfl.io/draft/spec/#version-directories) section to be more specific about version numbers. Adds error code [E104](https://ocfl.io/draft/spec/#E104) for the specific case of missing prefix `v`, and [E105](https://ocfl.io/draft/spec/#E105) for the specific case of using positive base-ten integers. (Issue [#532](https://github.com/OCFL/spec/issues/532))

#### Clarify that the content directory must be a direct child of the version directory

Change [Content Directory](https://ocfl.io/draft/spec/#content-directory) section to make it clear that the `contentDirectory` must indicate a direct child of the version directory. Adds error code [E108](https://ocfl.io/draft/spec/#E108). (Issue [#530](https://github.com/OCFL/spec/issues/530))

#### Clarify that `id` must be the same across all versions

Update [Basic Structure](https://ocfl.io/draft/spec/#inventory-structure) section to make it clear that the `id` must not change between versions of the same object. Adds error code [E110](https://ocfl.io/draft/spec/#E110). (Issue [#542](https://github.com/OCFL/spec/issues/542))

#### Use logical state consistently

Use the notion of "logical state" consistently in the [Version](https://ocfl.io/draft/spec/#version), [Version Inventory and Inventory Digest](https://ocfl.io/draft/spec/#version-inventory) and [BagIt in an OCFL Object](https://ocfl.io/draft/spec/#example-bagit-in-ocfl) sections. (Issue [#571](https://github.com/OCFL/spec/issues/571))

#### Clarify digest value case sensitivity requirements

Change [Manifest](https://ocfl.io/draft/spec/#manifest) and [Fixity](https://ocfl.io/draft/spec/#fixity) sections to make it clear that the additional requirement for each digest value to appear only once in the manifest or fixity block applies only to case-insensitive digest algorithms. (Issue [#573](https://github.com/OCFL/spec/issues/573))

#### Clarify that fixity value must be a JSON object

Change [Fixity](https://ocfl.io/draft/spec/#fixity) section to specify that the value of the `fixity` key must be a JSON object. An empty object (`{}`) is allowed, but a JSON `null` value is not. Added error code [E111](https://ocfl.io/draft/spec/#E111) and made [E055](https://ocfl.io/draft/spec/#E055) more specific. (Issue [E558](https://github.com/OCFL/spec/issues/558))

#### Clarify use of registered and local extensions

Change [Object Extensions](https://ocfl.io/draft/spec/#object-extensions) and [Storage Root Extensions](https://ocfl.io/draft/spec/#storage-root-extensions) to define registered extensions in terms of the [OCFL Extensions Repository](https://ocfl.github.io/extensions/). Added [Documenting Local Extensions](https://ocfl.io/draft/spec/#documenting-local-extensions) section to describe local extensions. Adds error codes [E112](https://ocfl.io/draft/spec/#E112) and [E113](https://ocfl.io/draft/spec/#E113), updates error code [E067](https://ocfl.io/draft/spec/#E067), and removes error codes `E068` and `E086` which were not being used within the community. Adds warning code [W016](https://ocfl.io/draft/spec/#W016). (Issues [#557](https://github.com/OCFL/spec/issues/557), [#565](https://github.com/OCFL/spec/issues/565))

#### Improve guidance on inclusion of specification in storage root

With the change from ReSpec to Markdown as the source format for the OCFL Specification it is now easy to store a complete copy of the specification in a storage root. This version suggests using the filename `ocfl_1.1.md` for a copy of the human-readable Markdown specification in the [Root Structure](https://ocfl.io/draft/spec/#root-structure) section. (Issues [#505](https://github.com/OCFL/spec/issues/505), [#554](https://github.com/OCFL/spec/issues/554))

#### Fix examples to match the specification

Correct several examples that in the 1.0 specification did not fully comply with the specification. (Issue [#539](https://github.com/OCFL/spec/issues/539))

#### Reference RFC version of Bagit specification

Update the reference to the Bagit specification from the draft <https://tools.ietf.org/html/draft-kunze-bagit-17> to [RFC8493](https://datatracker.ietf.org/doc/html/rfc8493). (Issue [#571](https://github.com/OCFL/spec/issues/571))

### Corrections to validation codes

#### Per-version validation codes

Even for minor releases the validations codes may be updated. We have thus moved the `validation-codes.md` file into each version directory so that will be versioned along with the specification. The version of this file for the v1.1 specification is rendered as <https://ocfl.io/draft/spec/validation-codes.html>. (Issue [#553](https://github.com/OCFL/spec/issues/553))

#### Fix E048 description

The E048 error description in `validation-codes.md` is corrected to remove mention of `message` and `user` because they are optional. (Issue [#531](https://github.com/OCFL/spec/issues/531))

#### Fix E070 description

The E070 error description in `validation-codes.md` is corrected to refer to `extension` rather than `key` (which was left from an earlier draft). (Issue [#573](https://github.com/OCFL/spec/issues/573))
