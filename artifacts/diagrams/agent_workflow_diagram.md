# Phase 3 Agent Workflow Diagram

Status: final agent workflow view.

```mermaid
flowchart TD
    Start["Start investigation"]
    LoadIndex["Load Obsidian index.md"]
    LoadHot["Load Obsidian hot.md"]
    LoadGraphReport["Load GRAPH_REPORT.md"]
    LoadGraphJson["Load graph.json / graph summary"]
    RankSuspects["Rank suspect nodes"]
    SelectSources["Select focused source files"]
    ReadEvidence["Read focused source evidence"]
    Hypothesize["Hypothesize root cause"]
    PlanFix["Plan minimal modular fix"]
    PlanVerification["Plan verification checks"]
    LogResult["Write investigation log"]

    Start --> LoadIndex
    LoadIndex --> LoadHot
    LoadHot --> LoadGraphReport
    LoadGraphReport --> LoadGraphJson
    LoadGraphJson --> RankSuspects
    RankSuspects --> SelectSources
    SelectSources --> ReadEvidence
    ReadEvidence --> Hypothesize
    Hypothesize --> PlanFix
    PlanFix --> PlanVerification
    PlanVerification --> LogResult
```

## Context Rule

The workflow must read Obsidian and graph artifacts before raw source code.

## Selected Bug Target

The workflow is locked to `print_final_scores` global-state coupling unless a human changes the target.
