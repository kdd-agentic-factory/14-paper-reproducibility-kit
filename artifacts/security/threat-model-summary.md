# Threat Model Summary

## Scope

Agentic components: agent orchestrator, MCP gateway, RAG/CAG layer, copilot.

## Primary Threats

| ID | Threat | Likelihood | Impact | Mitigation |
|----|--------|-----------|--------|------------|
| T01 | Prompt injection via tool response | Medium | High | SEC-004: response sanitisation |
| T02 | Unauthorised tool invocation | Low | High | SEC-001: capability-based access |
| T03 | Credential leakage in prompts | Low | Critical | SEC-003: vault injection |
| T04 | Unverified recommendation accepted | Medium | High | Digital twin validation |
| T05 | Synthetic data mistaken for real | Low | Medium | Dataset cards, classification |
| T06 | Audit log tampering | Low | High | Immutable audit store |

## Residual Risk

All residual risks are classified as Low after mitigations. No unmitigated
Critical risks exist in the current architecture.
