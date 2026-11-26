# Your first AI agent: an open playbook for public services

A short, practical guide for state agencies deciding where to use AI agents, and how to do it safely. Use it with your own team, with us, or with any vendor.

**Free to use.** This playbook is published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Copy it, adapt it for your agency and share it. Please credit dotmind.

## How to use this playbook

Work through the five steps in order. Each one ends with a template you can fill in for one service. A small team can do steps 1 to 4 in a single workshop; step 5 runs for as long as the agent does.

1. Pick where to start
2. Map the service to agent roles
3. Set the guardrails
4. Question any vendor or team
5. Measure fairness and quality

The principle behind every step: **agents gather, check and prepare. People decide.**

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
| | | | | | | |
| | | | | | | |

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

## Step 3. Set the guardrails

Agree these before anything is built. They are what make an agent safe to trust.

**What agents should not do**

- Make final decisions about rights, benefits or penalties. An agent can recommend; a person decides and is accountable.
- Do exact calculations by “judgment.” Amounts and fees come from fixed rules in ordinary software, which the agent calls as a tool.
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
- [Studio Studies](studies.html): studies of real services, and posts on where to start, fairness, and what happens when an agent gets it wrong.

Want help working through it for one of your services? Discovery with us is free. [Bring us a service](index.html#contact).
