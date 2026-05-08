## GOTCHA
1. kets from |...\\rangle to \\lvert...\\rangle, so Markdown no longer splits the math into extra columns.
2. Inside markdown tables, any `|` character inside a cell (including inside `$...$` math like `S|\psi\rangle`) is parsed as a column separator and breaks the row. Either escape every bar as `\|`, switch kets to `\lvert...\rvert`, or drop math delimiters in table cells and use plain unicode (`|ψ⟩`, `|0⟩`). Inline `$...$` math also fails to render in some previewers — prefer `$$...$$` blocks outside tables and plain unicode inside tables.

## FORMAT (FOR MATH)
1. make sure everything math related is in proper latex so it renders in the markdown previews

## Where to find content
1. in output/claude-vision