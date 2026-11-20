# Maintaining the study library

## Sources and output

Edit Markdown and source code; regenerate `index.html`. Reader assets live in `tools/reader`. Use lowercase filenames with underscores for new articles. Number files when they have an intended reading order; keep code module names stable where imports depend on them.

## Rebuild

From the repository root:

```bash
python3 -m pip install -r requirements-reader.txt
python3 build_reader.py
```

Refresh `index.html`. Referenced PDFs and images must remain at their relative paths. PDF text is not included in search. Mermaid blocks currently display their source.

## Publishing rules

`MyNotes`, `mynotes`, `my-notes` and `NOTES` folders are excluded case-insensitively. `90_personal_notes`, `98_archive`, `99_build_artifacts`, hidden folders and `tools` are also excluded.

Use headings, fenced code, compact tables and labelled examples. **LEARN**, **LAB**, **EVIDENCE**, **INTERNAL / LATENCY** and **INTERVIEW** labels produce coloured panels. Keep illustrative output labelled as illustrative.

## Links and recovery

Use relative Markdown links. Old article bookmarks resolve through `reader_redirects.json`. Moves are recorded in `tools/reader/reorganization_manifest.json`; changed originals are retained in `.reorganization_backup/20261120`. These support recovery, not automatic rollback.

Course chapters and exercises remain study sources; publishing them does not certify that every statement was fact-checked or every program was executed.
