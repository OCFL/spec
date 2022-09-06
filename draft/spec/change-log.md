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

Added [Conformance of prior versions](https://ocfl.io/draft/spec/#conformance-of-prior-versions) section to clarify that existing version directories are immutable and that the version number sequence must be monaotonic (issue [#544](https://github.com/OCFL/spec/issues/544)).

### Clarifications in v1.1

#### Inventory uses UTF-8 encoding

Clarify that UTF-8 encoded JSON must be used for the `inventory.json` files (issue [#514](https://github.com/OCFL/spec/issues/514)).

#### Version naming convention

Update wording to talk about version consistency for all versions of an object-at-rest, rather than in terms of the process for adding a version (issue [#541](https://github.com/OCFL/spec/issues/541)).

#### Clarify manifest requirements with additional MUSTs

Add language in [Manifest](https://ocfl.io/draft/spec/#manifest) section to clarify that the `manifest` block MUST be a JSON object (adding error code [E106](https://ocfl.io/draft/spec/#E106)) and that the each key MUST correspond to a digest value key found in one or more `state` blocks (adding error code [E107](https://ocfl.io/draft/spec/#E106)) (issue [#537](https://github.com/OCFL/spec/issues/537)).

#### Clarify manifest requirements in historic inventories

[Content Directory](https://ocfl.io/draft/spec/#content-directory) wording improved to make it clear that for each historical inventory, the manifest section must reference every file in that version directory (issue [#538](https://github.com/OCFL/spec/issues/538)].

#### Fix examples to match the specification

Several examples in the 1.0 specification did not fully comply with the specification (issue [#539](https://github.com/OCFL/spec/issues/539)).

#### Clarify language and error codes for version numbers

Change [Version Directories](https://ocfl.io/draft/spec/#version-directories) section changed to be clearer and to add an error code [E104](https://ocfl.io/draft/spec/#E104) for the specific case of missing prefix `v` (issue [#532](https://github.com/OCFL/spec/issues/532)).


#### Clarify that the content directory must be a direct child of the version directory

Change [Content Directory](https://ocfl.io/draft/spec/#content-directory) section to make it clear that the `contentDirectory` must indicate a direct child of the version directory. Adds error code [E108](https://ocfl.io/draft/spec/#E108) (issue [#530](https://github.com/OCFL/spec/issues/530)).

### Corrections to validation codes

#### Per-version validation codes

Even for minor releases the validations codes may be updated. We have thus moved the `validation-codes.md` file into each version directory so that will be versioned along with the specification (issue [#553](https://github.com/OCFL/spec/issues/553)).

#### Fix E048 message

The [E048](https://ocfl.io/draft/spec/#E048) error message was wrong in that it incorrectly suggested `message` and `user` were required, when they are optional (issue [#531](https://github.com/OCFL/spec/issues/531)).


Clarify Content directory path separators in 'contentDirectory' by @awoods in #566, Fixes #530
Update id language so its consistent across all versions by @rosy1280 in #568, Fixes #542
E070 should refer to "[extension, description]" by @srerickson in #574, Fixes #573
Update language around digest case sensitivity in 'fixity' and 'manifest' blocks by @awoods in #575
Clarify that fixity value must be a JSON object by @zimeon in #580, Fixes #558
Refine definition of registered extension name and describe local extensions by @zimeon in #584, Fixes #565
Specify exactly one version conformance declaration required/allowed by @zimeon in #585, Fixes #581
Use the term 'logical state' consistently by @zimeon in #586, Fixes #571
Replace ReSpec HTML drafts with Markdown versions by @zimeon in #596, Fixes #554
Add Andrew Hankinson as former editor by @zimeon in #600, Fixes #599
Improve guidance on inclusion of markdown version of spec by @zimeon in #601, Fixes #505
Replicate specification of Object extension section by @awoods in #607, Fixes #557
Update E067 validation-codes to match language in PR 607 by @rosy1280 in #608
