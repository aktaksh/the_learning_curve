# Maintaining the study library

## Sources and output

Edit Markdown and source code; regenerate `index.html`. Reader assets live in `tools/reader`. Use lowercase filenames with underscores for new articles. Number files when they have an intended reading order; keep code module names stable where imports depend on them.

## Rebuild

For normal use, double-click **Start Library.command**. It creates a private `.venv` if needed, installs missing dependencies, refreshes the index and opens the local reader. The first setup may need internet access; later launches reuse the installed packages.

For a manual rebuild from the repository root after setup:

```bash
.venv/bin/python build_reader.py
```

Double-click **Start Library.command** to open the reader. The launcher serves only the two library roots on the local computer and excludes personal-note and archive paths. Keep its Terminal window open; Control-C stops it. PDF.js is bundled locally, so reading does not require an external CDN.

Add PDFs to a published subject folder and rebuild. They open inside the library with search, page controls, zoom and thumbnails. Search within a PDF uses the viewer's search control; global article search indexes PDF titles and paths, not their complete contents. Scanned pages need an existing text layer for text search.

Referenced PDFs and images must remain at their relative paths. Opening `index.html` directly with `file://` still supports articles; PDF viewing requires the launcher. Mermaid blocks currently display their source.

## Publishing rules

`MyNotes`, `mynotes`, `my-notes` and `NOTES` folders are excluded case-insensitively. `90_personal_notes`, `98_archive`, `99_build_artifacts`, hidden folders and `tools` are also excluded.

Use headings, fenced code, compact tables and labelled examples. **LEARN**, **LAB**, **EVIDENCE**, **INTERNAL / LATENCY** and **INTERVIEW** labels produce coloured panels. Keep illustrative output labelled as illustrative.

## Links and recovery

Use relative Markdown links. Old article bookmarks resolve through `reader_redirects.json`. Moves are recorded in `tools/reader/reorganization_manifest.json`; changed originals are retained in `.reorganization_backup/20261120`. These support recovery, not automatic rollback.

Course chapters and exercises remain study sources; publishing them does not certify that every statement was fact-checked or every program was executed.
