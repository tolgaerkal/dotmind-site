# Your first AI agent: an open playbook for public services

*v1.0 · November 2026 · by [Tolga Erkal](https://www.linkedin.com/in/tolgaerkal/), dotmind*

A short, practical guide for US state agencies deciding where to use AI agents, and how to do it safely. It's useful for any public-service team. Use it with your own team, with us, or with any vendor.

**Free and open.** Use it, adapt it, share it.

This playbook is published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Copy it, adapt it for your agency and share it. Please credit dotmind.

**How to cite:** dotmind (2026). *Your first AI agent: an open playbook for public services*, v1.0. dotmind.org/playbook.html

## How to use this playbook

Work through the five steps in order. Each one ends with a template you can fill in for one service. A small team can do steps 1 to 4 in a single workshop; step 5 runs for as long as the agent does.

1. Pick where to start
2. Map the service to agent roles
3. Set the guardrails
4. Question any vendor or team
5. Measure fairness and quality

The principle behind every step: **agents gather, check and prepare. People decide.**

**Worked examples.** Each template is filled in using two dotmind [studio studies](studies.html). They're illustrations built from what the agencies publish, not real projects: no agency data was used, and the agencies haven't reviewed or endorsed them.

- **Study A: [Getting a REAL ID at the Delaware DMV](studies/delaware-dmv-real-id.html).** Residents arrive missing documents or with name mismatches. Agents pre-check documents from home. A clerk still checks the originals and issues the card.
- **Study B: [Applying for SNAP food benefits through Delaware DHSS](studies/delaware-snap.html).** Applications arrive incomplete and interviews get missed. Agents help gather documents and prepare for the interview. A caseworker makes every eligibility decision.

## Step 1. Pick where to start

Start where the work is high-volume, rule-based and already digital, not where the technology looks most impressive.

1. **List your high-volume interactions.** Applications, renewals, requests and reports that arrive by the thousand.
2. **Find where people get stuck.** Look for resubmissions, backlogs and “where’s my application?” calls. Ask caseworkers, not just managers.
3. **Score each one honestly.** Rate potential and complexity from 1 to 4. Be strict about data quality and about how much judgment the decision needs.
4. **Pick one with a clear measure.** Choose high readiness and a result that’s easy to see, such as fewer incomplete submissions.
5. **Pilot with people in the loop.** Run alongside the current process, with staff approving every decision.

**Potential** is how much an agent could improve the work. **Complexity** is how hard it would be to do safely, given the data, the stakes and the judgment involved. **Readiness** is potential minus complexity. This scoring is adapted from the World Economic Forum and Capgemini’s [readiness framework for agentic AI in government](https://reports.weforum.org/docs/WEF_Making_Agentic_AI_Work_for_Government_A_Readiness_Framework_2026.pdf).

### Template: score your candidates

| Interaction | Volume per month | Where people get stuck | Potential (1–4) | Complexity (1–4) | Readiness | How we’d measure success |
| --- | --- | --- | --- | --- | --- | --- |
| Example: license renewal | 12,000 | 1 in 4 submissions missing a document | 4 | 2 | 2 | Halve incomplete submissions |
| Study A: REAL ID at the DMV | Use your own data | Missing documents and name mismatches found at the counter | 4 | 2 | 2 | Fewer repeat visits for wrong or missing documents |
| Study B: SNAP application | Use your own data | Missing pay stubs and missed interview calls | 4 | 3 | 1 | Fewer requests for missing documents per case |
| | | | | | | |
| | | | | | | |

*Example from a studio study (not a real project).* Why we scored them this way:

- **Study A, REAL ID (readiness 2).** The document rules are published and stable, and the agent only advises, so complexity stays low. It isn't a 1 because the agent reads photos of identity documents.
- **Study B, SNAP (readiness 1).** High value: missing documents and missed interviews delay food help for families. But income rules, sensitive household data and federal deadlines make it more complex, so the agent should stick to gathering, checking and preparing.

Good first candidates usually look like answering questions from official guidance, booking appointments, or checking documents at upload. Policy planning and workforce changes are better left until you have experience.

## Step 2. Map the service to agent roles

Don’t build one agent per service. Almost every resident interaction uses the same few jobs, so build them as roles and set each one up for the service. A second service then launches faster and inherits tested safeguards.

| Role | What it does | Guardrail |
| --- | --- | --- |
| Guide | Understands what someone needs and explains options and next steps | Hands off to a person when unsure |
| Collect | Gathers information and files once, and checks them at the source | Helps fix problems; never turns people away |
| Verify | Checks identity, documents and facts against records and the rules | Shows the evidence for every finding |
| Prepare | Summarizes the case and drafts the next step for staff | A person makes every decision |
| Route | Sends work to the right team, agency or queue, with context attached | Nothing falls between agencies |
| Communicate | Keeps people informed and explains outcomes clearly | Uses approved, plain-language messages |
| Learn (across all six) | Spots where people get stuck, quality issues and unusual patterns | Feeds findings back to the teams who run the service |

### Template: your service on one page

| Role | What it does in this service | Rules and documents it uses | Systems it can reach | Where a person decides |
| --- | --- | --- | --- | --- |
| Guide | | | | |
| Collect | | | | |
| Verify | | | | |
| Prepare | | | | |
| Route | | | | |
| Communicate | | | | |
| Learn | | | | |

Leave a role blank if the service doesn’t need it. If you can’t fill in “where a person decides,” the design isn’t ready.

### Example: Study B, SNAP on one page

*Example from a studio study (not a real project).*

| Role | What it does in this service | Rules and documents it uses | Systems it can reach | Where a person decides |
| --- | --- | --- | --- | --- |
| Guide | Explains SNAP in plain words and runs the screening with the applicant, including what counts as household and income | DHSS’s published SNAP guidance and screening questions | Public guidance only | The applicant decides whether to apply. The agent never says someone doesn’t qualify, and anyone can submit the first page to lock in their filing date |
| Collect | Builds a personal document checklist and takes photos of pay stubs, lease, childcare receipts and Social Security numbers | The documents DHSS lists for SNAP | The agency’s own application system, to upload documents. Nothing is stored by dotmind | The applicant chooses what to submit |
| Verify | Matches each document to the form and flags gaps, such as a pay stub covering only 2 weeks or a lease with a different address | SNAP verification rules for income, residence and household | Reads documents in the application; can’t change the case | A caseworker reviews every flag, with the document behind it linked |
| Prepare | Prepares a case summary for the caseworker (household, last 30 days’ income with each figure linked to its document, expenses) and a one-page interview summary for the applicant | The layout of the eligibility screen; approved notice templates | Reads the case; writes drafts only | The caseworker makes every eligibility decision and benefit amount, and edits and sends every notice |
| Route | Moves households that may qualify for the 7-day expedited track to the top of the queue | Federal expedited-service criteria | The case queue | Staff confirm whether a case is expedited |
| Communicate | Offers interview times that fit the applicant’s schedule, says which caller ID to expect, and sends plain-language status updates and renewal reminders | Approved messages in English, Spanish and Vietnamese | Interview scheduling and messaging | Staff approve every message template; decision notices come from the caseworker |
| Learn | Spots where applications stall, and checks whether flags and expedited routing fall evenly across languages and household types | The measures in step 5 | Anonymized case data and timestamps | The agent’s owner and the program team decide what to change |

## Step 3. Set the guardrails

Agree these before anything is built. They are what make an agent safe to trust.

**What agents should not do**

- Make final decisions about rights, benefits or penalties. An agent can recommend; a person decides and is accountable.
- Make judgment calls on anything that needs an exact calculation. Calculations follow written rules: amounts and fees come from ordinary software, which the agent calls as a tool.
- Reach beyond its task. Give it only the systems and data the task needs.
- Replace other ways to get help. Phone, mail and in-person routes stay open.
- Work invisibly. Staff can see what it did and why, and residents know when they’re dealing with AI.

**Five safety nets.** For a mistake to reach a resident, it should have to get past all five.

1. **Limited access.** The agent can only reach what its task needs; anything else is refused.
2. **Evidence on every flag.** Each finding links to the page and the rule, so errors are easy to spot.
3. **Staff review.** A person checks the agent’s work and makes every decision.
4. **Reasons and appeal.** Residents see why, and can ask a person to review the outcome.
5. **Monitoring and pause.** Overrides and appeals are tracked, and the agent can be paused at once, falling back to the normal staff process.

**When a mistake gets through:** the resident can challenge it; a person, never the same agent, reviews the challenge; the record is corrected and the resident told why; similar cases are checked; and the agent’s owner is informed. Every mistake becomes a test case the agent must pass before any future change goes live.

### Template: guardrails sign-off

| Question | Our answer |
| --- | --- |
| Named owner in the agency who is accountable for this agent | |
| Decisions only a person can make | |
| Systems and data the agent can reach (and nothing else) | |
| How residents are told they’re dealing with AI | |
| Non-digital routes that stay open | |
| How residents challenge an outcome | |
| Who can pause the agent, and the fallback process | |

### Example: Study A, REAL ID guardrails sign-off

*Example from a studio study (not a real project).*

| Question | Our answer |
| --- | --- |
| Named owner in the agency who is accountable for this agent | A named DMV manager at the pilot location, such as the customer service lead. (No one is named here because this is a studio study.) |
| Decisions only a person can make | Accepting any document, deciding whether someone gets a REAL ID, and issuing the card. The pre-check is advice only. |
| Systems and data the agent can reach (and nothing else) | The photos the resident takes, which are checked on the device or deleted right after the check, and the DMV’s published document rules. No access to the licensing system. |
| How residents are told they’re dealing with AI | The pre-check says it’s an automated assistant, that its advice isn’t a DMV decision, and that a clerk will check the originals. |
| Non-digital routes that stay open | Residents can still walk in without a pre-check, and phone help stays available. |
| How residents challenge an outcome | The pre-check makes no decisions, so there’s nothing to appeal from it. Counter decisions follow the DMV’s existing review process. When the agent is unsure, it says “bring it and ask at the counter,” never “you’ll be rejected.” |
| Who can pause the agent, and the fallback process | The named owner can switch the pre-check off at any time. Residents then use the DMV’s published document guide, as they do today. |

## Step 4. Question any vendor or team

Whether a vendor is pitching you or your own team is proposing a pilot, these questions separate a careful plan from a risky one. Ask to see the answers, not just hear them.

1. **What exact problem does it solve, and how will we measure it?** “Use AI” isn’t a goal; “halve incomplete submissions” is.
2. **Where does a person decide?** Ask to see the checkpoints.
3. **What can it access, and what can it change?** It should have the minimum access the task needs.
4. **How was it tested?** Look for testing on real, anonymized cases from your service, including how often it gets things wrong, and how it performs across the groups you serve.
5. **What happens when it’s wrong?** There should be a clear route to correct errors and for residents to appeal.
6. **Where does residents’ data go?** It should stay under the state’s control, with every action logged.
7. **Who owns it?** Every agent needs a named person in the agency who is accountable for it.

## Step 5. Measure fairness and quality

Fairness is designed in, not assumed. Test before launch on cases that reflect the people the service actually serves, then keep measuring while it runs. Break each measure down by the groups that matter for your service.

### Template: what to track

| Measure | What it shows | Target or threshold | Who reviews it, and how often |
| --- | --- | --- | --- |
| Flag rate by group | Whether some groups are flagged more often than others | | |
| Staff overrides | How often caseworkers disagree with the agent, and for whom | | |
| Wrong flags | Flags that turn out to be mistaken, and who they affect | | |
| Time to decision | Whether some groups wait longer for an outcome | | |
| Completion by channel | Whether phone, mail and in-person users do as well as people online | | |
| Appeals and complaints | Where residents feel the service got it wrong | | |
| Your success measure from step 1 | Whether the agent is doing what it was for | | |

### Example: Study B, SNAP targets

*Example from a studio study (not a real project).* These targets are hypotheses a pilot would test, not results. A real pilot would set them with the agency during discovery.

| Measure | Example target (hypothesis to test) | Who reviews it, and how often |
| --- | --- | --- |
| Flag rate by group | Flag rates within 5 percentage points across languages and household types | Agent owner and a program analyst, monthly |
| Staff overrides | Caseworkers overrule fewer than 1 in 10 flags, with no group noticeably higher | Caseworker supervisors, weekly during the pilot |
| Wrong flags | Fewer than 1 in 20 flags turn out to be mistaken | Agent owner, weekly |
| Time to decision | Every case within the federal 30-day limit, expedited cases within 7 days, and no group waiting longer on average | Program manager, weekly |
| Completion by channel | People applying by phone, on paper or in person complete as often as people online | Agent owner, monthly |
| Appeals and complaints | No rise compared with the months before the pilot | Fair hearings team and agent owner, monthly |
| Your success measure from step 1 | Fewer requests for missing documents per case than for applications without the pre-check | Pilot team, every two weeks |

When a gap appears, the agent’s owner reviews it and fixes the cause, whether that’s the agent, the rules or the process around it. A rising number is a signal to investigate before it becomes a problem.

## Words you’ll hear

| Term | What it means in plain English |
| --- | --- |
| Agent | Software that uses an AI model to work toward a goal, step by step |
| Tool | An action an agent can take in a system, like looking up a case or sending a message |
| Connector | The secure link between an agent and one of your existing systems |
| Human checkpoint | A point where the agent stops and waits for a person to decide |
| Evaluation | Testing an agent on real examples to measure how often it gets things right |
| Audit log | A record of everything an agent did, for review and accountability |
| Hallucination | When a model states something false with confidence; checkpoints and sources guard against it |

## Go further

- [Agent roles matrix](roles.html): the six roles across every kind of resident interaction.
- [Example journey](journey.html): who does what at each step of applying for a service.
- [Studio studies](studies.html): studies of real services, and posts on where to start, fairness, and what happens when an agent gets it wrong.

Want help working through it for one of your services? Discovery with us is free. [Bring us a service](index.html#contact).

Want a walkthrough of the playbook for your team? We run a free 45-minute session. [Email us to book one](mailto:hello@dotmind.org?subject=Playbook%20walkthrough).

## Changelog

| Version | Date | Changes |
| --- | --- | --- |
| v1.0 | November 27, 2026 | First public release |
