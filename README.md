# par2createdby
show which PAR2 client created that par

Based on info in http://parchive.sourceforge.net/docs/specifications/parity-volume-spec/article-spec.html#i__134603784_1056

The creator packet has a type value of "PAR 2.0\0Creator\0" (ASCII). The packet's body contains the following:

ASCII text identifying the client. This should also include a way to contact the client's creator - either through a URL or an email address. NB: This is not a null terminated string!
