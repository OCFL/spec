---
no_site_title: true
---
<img src="https://avatars0.githubusercontent.com/u/35607965" alt="OCFL Hand-drive logo" style="float:right;width:307px;height:307px;"/>
# Oxford Common File Layout Specification v1.1 Change Log
{:.no_toc}

Draft 6 September 2022

Latest editor's draft: <https://ocfl.io/draft/spec/>

**Editors:**

* [Neil Jefferies](https://orcid.org/0000-0003-3311-3741), [Bodleian Libraries, University of Oxford](http://www.bodleian.ox.ac.uk/)
* [Rosalyn Metz](https://orcid.org/0000-0003-3526-2230), [Emory University](https://web.library.emory.edu/)
* [Julian Morley](https://orcid.org/0000-0003-4176-1933), [Stanford University](https://library.stanford.edu/)
* [Simeon Warner](https://orcid.org/0000-0002-7970-7855), [Cornell University](https://www.library.cornell.edu/)
* [Andrew Woods](https://orcid.org/0000-0002-8318-4225), [Harvard University](https://library.harvard.edu/)

**Former Editors:**

* [Andrew Hankinson](https://orcid.org/0000-0003-2663-0003)

This document is licensed under a [Creative Commons Attribution 4.0
License](https://creativecommons.org/licenses/by/4.0/). [OCFL logo:
"hand-drive"](https://avatars0.githubusercontent.com/u/35607965) by
[Patrick Hochstenbach](http://orcid.org/0000-0001-8390-6171) is
licensed under [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/).

## Changes from OCFL v1.0 to v1.1

[Version 1.1 of the OCFL Specification](https://ocfl.io/draft/spec/) is a [minor version](https://semver.org/) update to the [OCFL Specification v1.0](https://ocfl.io/1.0/spec/). It is intended to add functionality in a backwards compatible manner, and to clarify certain aspects based on a community feedback.

### Additions in v1.1

#### Add requirements version number sequence

Added [Conformance of prior versions](https://ocfl.io/draft/spec/#conformance-of-prior-versions) section to clarify that existing version directories are immutable and that the version number sequence must be monaotonic. Adds error code [E103](https://ocfl.io/draft/spec/#E103) (issue [#544](https://github.com/OCFL/spec/issues/544)).

### Clarifications in v1.1

#### One conformance declaration per object and storage root

Update the [Object Conformance Declaration](https://ocfl.io/draft/spec/#object-conformance-declaration) and [Root Conformance Declaration](https://ocfl.io/draft/spec/#root-conformance-declaration) sections to clarify that there must be exactly one version declaration file. Error codes [E003](https://ocfl.io/draft/spec/#003) and [E076](https://ocfl.io/draft/spec/#E076) correspondingly updated (issue [#581](https://github.com/OCFL/spec/issues/581)).

#### Inventory uses UTF-8 encoding

Clarify that UTF-8 encoded JSON must be used for the `inventory.json` files (issue [#514](https://github.com/OCFL/spec/issues/514)).

#### Version naming convention

Update wording to talk about version consistency for all versions of an object-at-rest, rather than in terms of the process for adding a version (issue [#541](https://github.com/OCFL/spec/issues/541)).

#### Clarify manifest requirements with additional MUSTs

Add language in [Manifest](https://ocfl.io/draft/spec/#manifest) section to clarify that the `manifest` block MUST be a JSON object (adding error code [E106](https://ocfl.io/draft/spec/#E106)) and that the each key MUST correspond to a digest value key found in one or more `state` blocks (adding error code [E107](https://ocfl.io/draft/spec/#E107)) (issue [#537](https://github.com/OCFL/spec/issues/537)).

#### Clarify manifest requirements in historic inventories

[Content Directory](https://ocfl.io/draft/spec/#content-directory) wording improved to make it clear that for each historical inventory, the manifest section must reference every file in that version directory (issue [#538](https://github.com/OCFL/spec/issues/538)].

#### Fix examples to match the specification

Several examples in the 1.0 specification did not fully comply with the specification (issue [#539](https://github.com/OCFL/spec/issues/539)).

#### Clarify language and error codes for version numbers

Change [Version Directories](https://ocfl.io/draft/spec/#version-directories) section changed to be clearer. Adds error code [E104](https://ocfl.io/draft/spec/#E104) for the specific case of missing prefix `v`, and [E105](https://ocfl.io/draft/spec/#E105) for the specific case of using positive base-ten integers (issue [#532](https://github.com/OCFL/spec/issues/532)).

#### Clarify that the content directory must be a direct child of the version directory

Change [Content Directory](https://ocfl.io/draft/spec/#content-directory) section to make it clear that the `contentDirectory` must indicate a direct child of the version directory. Adds error code [E108](https://ocfl.io/draft/spec/#E108) (issue [#530](https://github.com/OCFL/spec/issues/530)).

#### Clarify that `id` must be the same across all versions

Change [Basic Structure](https://ocfl.io/draft/spec/#inventory-structure) section to make it clear that the `id` MUST NOT change between versions of the same object. Adds error code [E110](https://ocfl.io/draft/spec/#E110) (issue [#542](https://github.com/OCFL/spec/issues/542))

#### Use logical state consistently

Use the notion of "logical state" consistently in the [Version](https://ocfl.io/draft/spec/#version), [Version Inventory and Inventory Digest](https://ocfl.io/draft/spec/#version-inventory) and [BagIt in an OCFL Object](https://ocfl.io/draft/spec/#example-bagit-in-ocfl) sections (issue [#571](https://github.com/OCFL/spec/issues/571)).

#### Clarify digest value case sensitivity requirements

Change [Manifest](https://ocfl.io/draft/spec/#manifest) and [Fixity](https://ocfl.io/draft/spec/#fixity) sections to make it clear that the additional requirement for each digest value to appear only once in the manifest or fixity block applies only in the case of case-insensitive digest algorithms (issue [#573](https://github.com/OCFL/spec/issues/573)).

#### Clarify that fixity value MUST be a JSON object

Change [Fixity](https://ocfl.io/draft/spec/#fixity) section to specify that the value of the `fixity` key MUST be a JSON object. An empty object (`{}`) is allowed, but a JSON `null` value is not. Added error code [E111](https://ocfl.io/draft/spec/#E111) and made [E055](https://ocfl.io/draft/spec/#E055) more specific (issue [E558](https://github.com/OCFL/spec/issues/558)).

#### Clarify use of registered and local extensions

Change [Object Extensions](https://ocfl.io/draft/spec/#object-extensions) and [Storage Root Extensions](https://ocfl.io/draft/spec/#storage-root-extensions) to define registered extensions in terms of the [OCFL Extensions Repository](https://ocfl.github.io/extensions/). Added [Documenting Local Extensions](https://ocfl.io/draft/spec/#documenting-local-extensions) to describe local extensions. Adds error codes [E112](https://ocfl.io/draft/spec/#E112) and [E113](https://ocfl.io/draft/spec/#E113), updates error code [E067](https://ocfl.io/draft/spec/#E067), and removes error codes `E068` and `E086` which were not being used within the community. Adds warning code [W016](https://ocfl.io/draft/spec/#W016) (issues [#557](https://github.com/OCFL/spec/issues/557) and [#565](https://github.com/OCFL/spec/issues/565))

#### Improve guidance on inclusion of specification in storage root

With the change from ReSpec to Markdown as the source format for the OCFL Specification it is now easy to store a complete copy of the specification in a storage root. This version suggests using the filename `ocfl_1.1.md` for a copy of the human-readable Markdown specification in the [Root Structure](https://ocfl.io/draft/spec/#root-structure) section (issues [#505](https://github.com/OCFL/spec/issues/505), [#554]()https://github.com/OCFL/spec/issues/554)

#### Reference RFC version of Bagit specification

Update the reference to the Bagit specification from the draft <https://tools.ietf.org/html/draft-kunze-bagit-17> to [RFC8493](https://datatracker.ietf.org/doc/html/rfc8493).

### Corrections to validation codes

#### Per-version validation codes

Even for minor releases the validations codes may be updated. We have thus moved the `validation-codes.md` file into each version directory so that will be versioned along with the specification. The version of this file for the v1.1 specification is rendered as <https://ocfl.io/draft/spec/validation-codes.html> (issue [#553](https://github.com/OCFL/spec/issues/553)).

#### Fix E048 message

The E048 error description in `validation-codes.md` incorrectly suggested `message` and `user` were required, when they are optional (issue [#531](https://github.com/OCFL/spec/issues/531)).

#### Fix E070 message

Correct the E070 error description in `validation-codes.md` to refer to `extension` rather and `key` (from an earlier draft) ([#573](https://github.com/OCFL/spec/issues/573)).
