# Mendeley makes a mess of BibTeX

Mendeley will automatically generate a BibTeX file from your library but it kind of sucks sometimes:

1. There's no way to include/exclude particular fields from the BibTeX export.  This is a problem because [some packages](http://www.ctan.org/pkg/apacite) look for the presence of particular information (like a `month` field) to determine whether an `@article` is from an academic journal or magazine.  You could fix this manually by going through and deleting the `month` entry for every single item in your library, but why.

2. If you've ever shared something in your library with a group, it gets a duplicate entry in the BibTeX file.  This makes BibTeX exit with an error even though it runs perfectly fine, screwing up any kind of automatic build system you might have set up.


## Quik Start
    python3 clean_library.py -i input_bib -o output_bib 

## Cleaning a DIR 
    python3 batch_clean.py -i dir_path


