# Product Requirements Document

## 1. Overview

### Feature Name

`<Feature name>`

### Summary

Briefly describe the feature, the user problem it solves, and why it matters now.

### Background

Add relevant context, including existing dashboard behavior, CRM data shape, sales process assumptions, or stakeholder input.

## 2. Goals

### Business Goals

- `<Goal 1>`
- `<Goal 2>`

### User Goals

- `<Goal 1>`
- `<Goal 2>`

### Non-Goals

- `<Explicitly out-of-scope item>`
- `<Explicitly out-of-scope item>`

## 3. Users and Use Cases

### Primary Users

- Sales managers
- Account executives
- Revenue operations

### Key Use Cases

1. `<User type>` needs to `<action>` so they can `<outcome>`.
2. `<User type>` needs to `<action>` so they can `<outcome>`.

## 4. Current Experience

Describe the current workflow, including where users start, what information they inspect, and where the workflow breaks down.

### Pain Points

- `<Pain point>`
- `<Pain point>`

## 5. Proposed Experience

Describe the intended workflow after the feature ships.

### User Flow

1. User lands on `<screen or section>`.
2. User reviews `<data or recommendation>`.
3. User takes `<decision or action>`.
4. Dashboard reflects `<resulting state>`.

### UX Requirements

- The feature must be understandable without training.
- Recommendation or risk outputs must expose the reason they were produced.
- Owner filters must apply consistently to related metrics, records, and tasks.

## 6. Functional Requirements

| ID | Requirement | Priority | Notes |
| --- | --- | --- | --- |
| FR-1 | `<Requirement>` | Must | `<Notes>` |
| FR-2 | `<Requirement>` | Should | `<Notes>` |
| FR-3 | `<Requirement>` | Could | `<Notes>` |

## 7. Data Requirements

### Inputs

- `<CRM field or derived value>`
- `<CRM field or derived value>`

### Outputs

- `<Displayed value, calculated score, label, summary, or recommendation>`

### Data Shape Changes

Document any required changes to `data/crm.json`. Prefer fixture data changes over hardcoded UI special cases.

```json
{
  "exampleField": "example value"
}
```

## 8. Business Logic

Describe deterministic rules, calculations, scoring, or category assignment.

### Rules

1. `<Rule name>`: `<plain-English rule>`
2. `<Rule name>`: `<plain-English rule>`

### Explainability

For every calculated label, score, forecast category, or recommendation, document the user-facing reason that should be shown.

## 9. Edge Cases

- Missing or incomplete CRM fields
- Empty owner book after filtering
- Opportunities with stale activity but strong account health
- Healthy accounts with high-risk opportunities
- Multiple reasons contributing to one recommendation

## 10. Success Metrics

### Product Metrics

- `<Metric>`
- `<Metric>`

### Quality Metrics

- Calculation behavior is covered by tests in `test/crm.test.js`.
- Dashboard loads successfully through `npm run dev`.

## 11. Rollout Plan

### Release Scope

Describe what will ship in the first version.

### Dependencies

- `<Dependency>`
- `<Dependency>`

### Risks

- `<Risk>`: `<Mitigation>`

## 12. Testing Plan

### Automated Tests

- Add or update tests for risk scoring, forecast categories, owner filters, account snapshots, or pipeline summaries as applicable.

### Manual Verification

1. Run `npm test`.
2. Run `npm run dev`.
3. Verify the dashboard loads.
4. Verify owner filtering affects all relevant views consistently.
5. Verify calculated recommendations display clear reasons.

## 13. Open Questions

- `<Question>`
- `<Question>`

## 14. Decision Log

| Date | Decision | Owner | Notes |
| --- | --- | --- | --- |
| `<YYYY-MM-DD>` | `<Decision>` | `<Owner>` | `<Notes>` |
