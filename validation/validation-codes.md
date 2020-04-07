# OCFL Validation Codes

## Requirements

 - Levels of validation: ERROR, WARNING, INFO. The ERROR level corresponds with MUST in the specification, the WARNING level corresponds with SHOULD in the specification, and the INFO level is validator implementation specific.
 - OCFL Spec should define error codes to which validators MUST refer; these error codes will refer to sections in the OCFL Spec.
 - Validators MUST validate OCFL Objects
 - Validators MUST validate OCFL Storage Roots

## Errors (corresponding with MUST in specification)

| Code | Requirement |
| --- | --- |
| [E001](https://ocfl.io/draft/spec/#E001) | The OCFL Object Root MUST NOT contain files or directories other than those specified in the following sections |
| [E002](https://ocfl.io/draft/spec/#E002) | The OCFL version declaration MUST be formatted according to the NAMASTE specification |
| [E003](https://ocfl.io/draft/spec/#E003) | The OCFL version declaration MUST be a file in the base directory of the OCFL Object Root giving the OCFL version in the filename |
| [E004](https://ocfl.io/draft/spec/#E004) | The OCFL version declaration filename MUST conform to the pattern T=dvalue |
| [E005](https://ocfl.io/draft/spec/#E005) | In the OCFL version declaration the filename MUST start with 0 (T MUST be 0) |
| [E006](https://ocfl.io/draft/spec/#E006) | In the OCFL version declaration the filename MUST end with ocfl_object_ (dvalue MUST be ocfl_object_) |
| [E007](https://ocfl.io/draft/spec/#E007) | The text contents of the OCFL version declaration file MUST be the same as dvalue, followed by a newline (\n) |
| [E008](https://ocfl.io/draft/spec/#E008) | OCFL Object content MUST be stored as a sequence of one or more versions |
| [E009](https://ocfl.io/draft/spec/#E009) | The version number sequence MUST start at 1 |
| [E010](https://ocfl.io/draft/spec/#E010) | The version number sequence MUST be continuous without missing integers |
| [E011](https://ocfl.io/draft/spec/#E011) | If zero-padded version directory numbers are used then they MUST start with the prefix v and then a zero |
| [E012](https://ocfl.io/draft/spec/#E012) | All version directories of an object MUST use the same naming convention: either a non-padded version directory number, or a zero-padded version directory number of consistent length |
| [E013](https://ocfl.io/draft/spec/#E013) | Operations that add a new version to an object MUST follow the version directory naming convention established by earlier versions |
| [E014](https://ocfl.io/draft/spec/#E014) | In all cases, references to files inside version directories from inventory files must use the actual version directory names |
| [E015](https://ocfl.io/draft/spec/#E015) | There MUST be no other files as children of a version directory, other than an inventory file and a inventory digest |

## Warnings (corresponding with SHOULD in specification)

| Code | Recommendation |
| --- | --- |
| [W001](https://ocfl.io/draft/spec/#W001) | Implementations SHOULD use version directory names constructed without zero-padding the version number, ie. v1, v2, v3, etc. |
| [W002](https://ocfl.io/draft/spec/#W002) | The version directory SHOULD NOT contain any directories other than the designated content sub-directory. Once created, the contents of a version directory are expected to be immutable |
| [W003](https://ocfl.io/draft/spec/#W003) | Version directories must contain a designated content sub-directory if the version contains files to be preserved, and SHOULD NOT contain this sub-directory otherwise |
| [W004](https://ocfl.io/draft/spec/#W004) | For content-addressing, OCFL Objects SHOULD use sha512 |
| [W005](https://ocfl.io/draft/spec/#W005) | The OCFL Object Inventory id SHOULD be a URI |
| [W006](https://ocfl.io/draft/spec/#W006) | The OCFL Object Inventory digestAlgorithm SHOULD be sha512 -- Q: dupe of W004? |
| [W007](https://ocfl.io/draft/spec/#W007) | In the OCFL Object Inventory, the JSON object describing an OCFL Version, SHOULD include the message and user keys |
| [W008](https://ocfl.io/draft/spec/#W008) | In the OCFL Object Inventory, in the version block, the value of the user key SHOULD contain an address key, address |
| [W009](https://ocfl.io/draft/spec/#W009) | In the OCFL Object Inventory, in the version block, the address value SHOULD be a URI: either a mailto URI [RFC6068] with the e-mail address of the user or a URL to a personal identifier, e.g., an ORCID iD |
| [W010](https://ocfl.io/draft/spec/#W010) | In addition to the inventory in the OCFL Object Root, every version directory SHOULD include an inventory file that is an Inventory of all content for versions up to and including that particular version |
| [W011](https://ocfl.io/draft/spec/#W011) | In the case that prior version directories include an inventory file, the values of the created, message and user keys in each version block in each prior inventory file SHOULD have the same values as the corresponding keys in the corresponding version block in the current inventory file |
| [W012](https://ocfl.io/draft/spec/#W012) | Implementers SHOULD use the logs directory, if present, for storing files that contain a record of actions taken on the object |
| [W013](https://ocfl.io/draft/spec/#W013) | In an OCFL Object, extension sub-directories SHOULD be named according to a registered extension name |
| [W014](https://ocfl.io/draft/spec/#W014) | Storage hierarchies within the same OCFL Storage Root SHOULD use just one layout pattern |
| [W015](https://ocfl.io/draft/spec/#W015) | Storage hierarchies within the same OCFL Storage Root SHOULD consistently use either a directory hierarchy of OCFL Objects or top-level OCFL Objects |
