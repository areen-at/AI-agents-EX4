"""State types for the graph-guided investigation workflow."""

from __future__ import annotations

from typing import Literal, TypedDict


EvidenceType = Literal["graph", "obsidian", "source", "test", "agent_inference"]


class EvidenceItem(TypedDict):
    claim: str
    source: str
    evidence_type: EvidenceType
    confidence: str
    verification_step: str


class SuspectNode(TypedDict):
    node_id: str
    label: str
    source_file: str
    reason: str
    rank: int


class TextUnitMetric(TypedDict):
    path: str
    characters: int
    estimated_tokens: int


class InvestigationState(TypedDict):
    bug_summary: str
    selected_files: list[str]
    graph_artifacts: list[str]
    obsidian_context: list[str]
    suspect_nodes: list[SuspectNode]
    evidence: list[EvidenceItem]
    text_units_read: list[TextUnitMetric]
    proposed_fix: str
    verification_plan: str
    status: str
