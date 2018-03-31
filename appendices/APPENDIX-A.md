# Appendix A: Examples

## Sample inventory.jsonld

```$json
{
    "@context": "https://ocfl.io/v1.0/",
    "@id": "urn:ark:12148/btv1b84490444",
    "@type": "ocfl:Object",
    "head": "#v0003",
    // This is a list of all files that are in the object. It must be updated
    // with files added in new versions.
    // Writing the same file to a new location (same checksum, different path)
    // is an error, since versions are fixed and cannot be changed. Instead,
    // if a file is restored in later versions, it can be referenced in its earlier 
    // incarnation.
    "manifest": {
        "77B17E8E7DD2289BD7C080694D92DE3FB6F16DA837A615CB54394405B9D515E2": "v0001/data/page1/btv1b84490444_page1.jp2",
        "FED200F1C8BA3D49B7021F8872E3162AED32A9353DE7B80646230CBEEBA005A4": "v0001/data/page1/btv1b84490444_page1.tiff",
        "101AA4A1C0D62EE217F313DEF9FCBBD0CBB9C3E0FC028FD628C08776867E0076": "v0001/data/page1/btv1b84490444_page1.xmp",
        "99C19A71876725C984C9B7CC0DEEAA5C6DD3468332B2EBD4EC422C697A2BFAB3": "v0001/data/page2/btv1b84490444_page2.tiff",
        "9D15C69555D4BD0E5B7221000820EF118607CCD58C029601C73C6F0492C1B793": "v0002/data/page2/btv1b84490444_page2.jp2",
        "3A5421B5B2473EDF44D733DF10374B7384A8D21FF794D6D5A34311E0C1C63BE8": "v0002/data/page2/btv1b84490444_page2.xmp",
        "5CFF4E95A8A8A990969025BDE377C517332FAB5C0FE06A681437331C8A475128": "v0003/data/page1/btv1b84490444_page1_reshoot.jp2",
        "3A0EA99F25E4906775C78ED8306C244EF83F60DC6188C6F75F541FD4D9AC3FAB": "v0003/data/page1/btv1b84490444_page1_reshoot.tiff",
        "DCF242CF2062C9CB25D49B8965480D9D5E15660857EDCF7B8BF80BC57E58A800": "v0003/data/page1/btv1b84490444_page1_reshoot.xmp",
        "656BA99E1597EC7B7B264DC9DF618BF90ACF0583B7A1816038996B2434800089": "v0001/metadata/mets.xml",
        "A7030C70434B18171D5AAF9B263839DE411B668C8BA7A12DF2204611DB16114D": "v0002/metadata/mets.xml",
        "266BE64BE68B4870CCE510326D435B5692B7CF46BE8E0DF15190D92E017DFD57": "v0003/metadata/mets.xml"
    },
    "versions": [
        {
            "@type": "ocfl:Version",
            "@id": "#v0001",
            "created": "2014-01-01T12:00:00Z",
            "message": "Initial version",
            "client": "OCFL Python Library 1.1.0",
            "user": {
                "name": "Andrew Hankinson",
                "email": "andrew.hankinson@***.uk"
            },
            "members": [
                "77B17E8E7DD2289BD7C080694D92DE3FB6F16DA837A615CB54394405B9D515E2",
                "FED200F1C8BA3D49B7021F8872E3162AED32A9353DE7B80646230CBEEBA005A4",
                "101AA4A1C0D62EE217F313DEF9FCBBD0CBB9C3E0FC028FD628C08776867E0076",
                "99C19A71876725C984C9B7CC0DEEAA5C6DD3468332B2EBD4EC422C697A2BFAB3",
                "656BA99E1597EC7B7B264DC9DF618BF90ACF0583B7A1816038996B2434800089"
            ]
        },
        {
            "@type": "Version",
            "@id": "#v0002",
            "created": "2014-01-01T13:00:00Z",
            "message": "Added page 2 JPEG 2000 and XMP",
            "client": "OCFL Python Library 1.1.0",
            "user": {
                "name": "Andrew Hankinson",
                "email": "andrew.hankinson@***.uk"
            },
            "members": [
                "77B17E8E7DD2289BD7C080694D92DE3FB6F16DA837A615CB54394405B9D515E2",
                "FED200F1C8BA3D49B7021F8872E3162AED32A9353DE7B80646230CBEEBA005A4",
                "101AA4A1C0D62EE217F313DEF9FCBBD0CBB9C3E0FC028FD628C08776867E0076",
                "99C19A71876725C984C9B7CC0DEEAA5C6DD3468332B2EBD4EC422C697A2BFAB3",
                // new files added in version 2
                "9D15C69555D4BD0E5B7221000820EF118607CCD58C029601C73C6F0492C1B793",
                "3A5421B5B2473EDF44D733DF10374B7384A8D21FF794D6D5A34311E0C1C63BE8",
                "A7030C70434B18171D5AAF9B263839DE411B668C8BA7A12DF2204611DB16114D"
            ]
        },
        {
            "@type": "Version",
            "@id": "#v0003",
            "created": "2018-01-05:14:00:00Z",
            "message": "Replaced page 1 with a re-shot version",
            "client": "OCFL Ruby Gem 0.9.5",
            "user": {
                "name": "Andrew Woods",
                "email": "awoods@***.org"
            },
            "members": [
                "99C19A71876725C984C9B7CC0DEEAA5C6DD3468332B2EBD4EC422C697A2BFAB3",
                "9D15C69555D4BD0E5B7221000820EF118607CCD58C029601C73C6F0492C1B793",
                "3A5421B5B2473EDF44D733DF10374B7384A8D21FF794D6D5A34311E0C1C63BE8",
                // new files added in version 3
                "5CFF4E95A8A8A990969025BDE377C517332FAB5C0FE06A681437331C8A475128",
                "3A0EA99F25E4906775C78ED8306C244EF83F60DC6188C6F75F541FD4D9AC3FAB",
                "DCF242CF2062C9CB25D49B8965480D9D5E15660857EDCF7B8BF80BC57E58A800",
                "266BE64BE68B4870CCE510326D435B5692B7CF46BE8E0DF15190D92E017DFD57"
            ]
        }
    ]
}
```