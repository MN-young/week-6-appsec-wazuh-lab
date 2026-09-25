# SecureOps AppSec Lab

Standalone source repository for the Week 6 SecureOps training application and its GitHub Actions security checks.

> [!WARNING]
> This application is intentionally vulnerable. It contains a deliberate SQL injection for controlled Semgrep testing and must not be deployed publicly or used as a production reference.

## Included here

- Flask SecureOps application and templates
- Flask `3.1.3` final dependency state
- Independent Semgrep SAST and pip-audit GitHub Actions jobs
- JSON artifact export before the Semgrep blocking gate
- Expected final CI contrast: Semgrep red by design and pip-audit green

## Portfolio documentation

The complete Week 6 architecture, Wazuh Rules `100202` and `100203`, Shuffle/Slack routing, troubleshooting record, validation, reflection, and curated evidence are maintained with Weeks 1–5 in the [Security Engineering Mentorship Labs Week 6 project](https://github.com/MN-young/security-engineering-mentorship-labs/tree/main/week-6-appsec-wazuh-integration).
