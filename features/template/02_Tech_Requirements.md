# Technical Requirements

## 1. Overview

### Feature Name

`<Feature name>`

### Related PRD

`features/<feature-folder>/01_PRD.md`

### Summary

Briefly describe the technical change required to deliver the product behavior.

## 2. Architecture Fit

### Affected Areas

- `data/crm.json`: `<fixture or data-shape changes>`
- `src/crm.js`: `<business logic changes>`
- `src/main.js`: `<rendering or event changes>`
- `src/styles.css`: `<styling changes>`
- `test/crm.test.js`: `<test coverage changes>`

### Constraints

- Preserve the static, client-side dashboard architecture.
- Do not introduce network-dependent runtime behavior.
- Preserve the no-build setup unless explicitly justified.
- Keep reusable sales-operations logic in `src/crm.js`.

## 3. Data Model

### Existing Inputs

- `<Existing field>`: `<Current meaning>`
- `<Existing field>`: `<Current meaning>`

### New or Changed Inputs

| Field | Type | Required | Source | Notes |
| --- | --- | --- | --- | --- |
| `<fieldName>` | `<type>` | `<Yes/No>` | `data/crm.json` | `<Notes>` |

### Derived Values

| Value | Calculation | Owner Filter Aware | Explainability Required |
| --- | --- | --- | --- |
| `<valueName>` | `<Rule or function>` | `<Yes/No>` | `<Yes/No>` |

## 4. Business Logic Requirements

### Deterministic Rules

1. `<Rule name>`: `<Plain-English rule and threshold>`
2. `<Rule name>`: `<Plain-English rule and threshold>`

### Forecast and Risk Behavior

- Forecast categories must remain one of `Commit`, `Best Case`, `Pipeline`, or `At Risk`.
- Risk labels should identify deals needing attention without flagging every imperfect deal.
- Account health and opportunity risk must remain separate concepts.

### Explainability

Each recommendation, score, label, or category must include:

- Triggering condition
- User-facing reason
- Source data used

## 5. UI Requirements

### Rendering Changes

- `<Component or section>` displays `<new value or interaction>`.
- `<Component or section>` updates when owner filters change.

### Interaction Rules

- Owner filters must affect pipeline metrics, opportunities, accounts, and tasks consistently.
- Empty states must be useful and specific.
- Calculated outputs must show enough context for a sales manager to act.

## 6. Error and Edge Case Handling

- Missing optional CRM fields should not break dashboard rendering.
- Missing required CRM fields should fall back to a clear default or be covered by fixture validation.
- Empty filtered books should show zeroed metrics and empty lists consistently.
- Conflicting signals should preserve separate account health and opportunity risk explanations.

## 7. Performance Requirements

- Calculations should run in memory against the local fixture data.
- Rendering should remain responsive for the expected fixture size.
- Avoid repeated expensive calculations inside per-record render loops when a summary can be calculated once.

## 8. Accessibility Requirements

- Interactive controls must be keyboard accessible.
- New status, risk, or category labels must not rely on color alone.
- Text content must remain readable at supported viewport sizes.

## 9. Testing Requirements

### Unit Tests

Add or update tests in `test/crm.test.js` for:

- `<Business logic rule>`
- `<Owner filter behavior>`
- `<Account snapshot behavior>`
- `<Pipeline summary behavior>`

### Manual Tests

1. Run `npm test`.
2. Run `npm run dev`.
3. Verify the dashboard loads.
4. Verify the feature works with all owners selected.
5. Verify the feature works with each individual owner selected.

## 10. Migration and Compatibility

### Fixture Migration

Describe required changes to `data/crm.json` and whether old fixture shapes must still be supported.

### Backward Compatibility

- `<Compatibility requirement>`
- `<Compatibility requirement>`

## 11. Security and Privacy

- Do not add external services, API keys, trackers, or remote data loading.
- Do not expose sensitive customer data beyond the local fixture context.
- Keep sample data synthetic unless explicitly approved.

## 12. Open Technical Questions

- `<Question>`
- `<Question>`

## 13. Technical Decision Log

| Date | Decision | Owner | Notes |
| --- | --- | --- | --- |
| `<YYYY-MM-DD>` | `<Decision>` | `<Owner>` | `<Notes>` |

