# Embedded PDF viewer

Mozilla PDF.js 6.5.438 is bundled under tools/pdfjs with its Apache 2.0 license. The viewer has a local library colour theme and runs inside an iframe in the article panel. The original PDF files are read without modification.

Upstream release: https://github.com/mozilla/pdf.js/releases/tag/v6.5.438

Use Start Library.command at the repository root. It starts or reuses a loopback-only Python server for the two sibling libraries. Personal-note folders, archives and hidden paths are not served. No upload or external CDN is involved.

After adding a PDF to a published subject folder, run python3 build_reader.py and refresh the reader. PDF title/path indexing is separate from PDF.js text search inside a document. Keep the PDF.js build, worker, renderer, fonts, character maps, locales and viewer at the same version when updating.
