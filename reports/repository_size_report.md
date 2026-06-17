# Repository Size Report

Status: Phase 0 updated with measured repository size.

## Requirement

The general assignment note says a different repository may be used if it is meaningful code with approximately 10,000+ source lines and at least 70 source-code files.

However, the lecturer explicitly allowed using `martinpeck/broken-python` for this project. This report documents the repository-size gap transparently.

## Selected Repository

[`martinpeck/broken-python`](https://github.com/martinpeck/broken-python)

## Counting Method

The repository was cloned locally and Python source files were counted recursively.

Meaningful source lines were counted as non-empty lines that do not begin with `#`.

Command used:

```powershell
$files = Get-ChildItem -Recurse -File -Filter '*.py' -LiteralPath 'work\target_repos\broken-python' |
  Where-Object { $_.FullName -notmatch '\\.git\\' }

$rows = foreach ($f in $files) {
  $all = Get-Content -LiteralPath $f.FullName
  $meaningful = ($all | Where-Object {
    $_.Trim().Length -gt 0 -and -not $_.Trim().StartsWith('#')
  }).Count
  [PSCustomObject]@{
    RelativePath = (Resolve-Path -LiteralPath $f.FullName -Relative)
    TotalLines = $all.Count
    MeaningfulLines = $meaningful
  }
}
```

## Included File Types

`.py`

## Excluded Paths

Generated files, dependency folders, virtual environments, caches, and `.git` internals were excluded.

## Results

| Metric | Value |
|---|---:|
| Source-code files | 5 |
| Total Python lines | 446 |
| Meaningful source lines | 260 |

## File Breakdown

| File | Total Lines | Meaningful Lines |
|---|---:|---:|
| `mathsquiz/mathsquiz-step1.py` | 158 | 93 |
| `mathsquiz/mathsquiz-step2.py` | 57 | 38 |
| `mathsquiz/mathsquiz-step3.py` | 62 | 37 |
| `mathsquiz/mathsquiz.py` | 94 | 53 |
| `polygons/polygons.py` | 75 | 39 |

## Conclusion

The selected repository does not satisfy the general numeric threshold of 10,000+ source lines and 70+ source-code files.

It is still selected because the lecturer explicitly allowed this repository for the project. The submission must therefore compensate by making the investigation, Graphify/Obsidian workflow, agent-instruction architecture, token-efficiency comparison, and original extensions especially clear and rigorous.
