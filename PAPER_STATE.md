# Paper state

Branch: codex/reference-primary-paper-20260923. Original detached paper worktree and its local edits remain untouched.

The accessible source was an older generic article with unresolved generated-table references and local filesystem paths in the appendix. No saved record substantiating the exact previously reported post-build FAIL was found. This branch uses hash-pinned official ICLR2027 style, resolves the new reference table labels, removes identifying filesystem paths, sets empty PDF author metadata, and separates mechanical PDF validation from scientific readiness.

Latest reduced protocol: one trajectory/item; LLaDA failed64 (minimum32); temporal32; mechanism32; Dream32; LLaDA MATH deep then GSM then optional Dream. Numerical cells remain em dashes until a matching SEALED reference bundle is verified. Existing fallback title is preserved. Abstract and Conclusion were not rewritten; author review remains required.

Build: `tectonic -X compile paper/main.tex --outdir paper/build --keep-logs --keep-intermediates`.
Audit: `PYTHONPATH=/var/tmp/kimhj-v2r-reference/pdf-libs python3 scripts/v2r_pdf_audit.py`.
The PDF is a structural working draft, not a submission-ready scientific paper. Full reference import/figures/package remain pending real sealed evidence.
