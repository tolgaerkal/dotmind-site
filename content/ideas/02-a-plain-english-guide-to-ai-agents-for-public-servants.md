# A plain-English guide to AI agents for public servants

*Tolga Erkal · November 3, 2026*

## What is an AI agent?

An AI agent is software that can work toward a goal on its own: it plans the steps, uses tools to take them, checks its work, and asks a person when a decision is needed.

That’s it. No robots, no science fiction. If you’ve ever handed a task to a capable new colleague with clear instructions, access to the right systems and a rule to check with you before anything important, you already understand the idea.

This guide explains agents without jargon, so you can judge where they might help your team, and where they shouldn’t be used.

## Chatbot or agent: what’s the difference?

A chatbot answers. An agent acts.

Ask a chatbot “What documents do I need to renew my license?” and it tells you. Ask an agent to help with the renewal, and it can check the documents you upload, look up your existing license, spot that your proof of address has expired, and prepare the file for a staff member to approve.

| | Chatbot | Agent |
| --- | --- | --- |
| What it does | Answers questions | Works toward a goal over several steps |
| What it can reach | What it was told or trained on | Tools and systems it’s given access to |
| What it produces | A reply | A completed task, or a prepared one for a person to finish |
| Where people fit | Reading the answer | Approving decisions at set checkpoints |

That extra power is why agents need more care. Something that can act in your systems needs clear limits on what it’s allowed to do.

## How an agent works

An agent repeats a simple loop: plan a step, take it with a tool, check the result, and keep going until the work is ready for a person.

![The agent loop: plan, act, check, then a person decides](images/loop.svg)

Each part has a plain meaning. The **goal** is the job, like “prepare this renewal for review.” **Tools** are the actions it’s allowed to take, like reading a document or looking up a record. The **checkpoint** is where it stops and hands over to a person, who makes the decision.

## What agents do well in public services

Agents are strongest at work that is repetitive, follows clear rules, and leaves a trail a person can check.

- **Answering questions from official guidance**, with links to the source, at any hour.
- **Checking submissions as they arrive**, catching missing pages, blurry scans or expired documents before a file joins the queue.
- **Preparing cases for review**, so a caseworker starts with a summary and the evidence, not a stack of attachments.
- **Drafting routine letters and updates** for staff to check and send.
- **Keeping residents informed**, answering “where’s my application?” without a phone call.

In each case the agent takes on the legwork, and staff keep the judgment.

## What agents should not do

Some work should stay with people, however capable the technology becomes.

- **Make final decisions about rights, benefits or penalties.** An agent can recommend; a person decides and is accountable.
- **Do exact calculations by “judgment.”** Benefit amounts and fees should come from fixed rules in ordinary software, which the agent calls as a tool.
- **Act without limits.** An agent should reach only the systems and data its task needs, and nothing more.
- **Replace other ways to get help.** Phone, mail and in-person routes stay for people who can’t or won’t go online.
- **Work invisibly.** Staff should be able to see what an agent did and why, and residents should know when they’re dealing with AI.

## Questions to ask before your agency uses one

Whether a vendor is pitching you or your own team is proposing a pilot, these questions separate a careful plan from a risky one.

1. **What exact problem does it solve, and how will we measure it?** “Use AI” isn’t a goal; “halve incomplete submissions” is.
2. **Where does a person decide?** Ask to see the checkpoints, not just hear about them.
3. **What can it access, and what can it change?** It should have the minimum access the task needs.
4. **How was it tested?** Look for testing on real (anonymized) cases from your service, including how often it gets things wrong.
5. **What happens when it’s wrong?** There should be a clear route to correct errors and for residents to appeal.
6. **Where does residents’ data go?** It should stay under the state’s control, with every action logged.
7. **Who owns it?** Every agent needs a named person in the agency who is accountable for it.

## Glossary

| Term | What it means in plain English |
| --- | --- |
| AI model | The engine that understands and writes language, such as Claude. |
| Agent | Software that uses a model to work toward a goal, step by step. |
| Instructions | The written guidance that tells an agent its job, its limits and its tone. |
| Tool | An action an agent can take in a system, like looking up a case or sending a message. |
| Connector | The secure link between an agent and one of your existing systems. |
| Human checkpoint | A point where the agent stops and waits for a person to decide. |
| Evaluation | Testing an agent on real examples to measure how often it gets things right. |
| Audit log | A record of everything an agent did, for review and accountability. |
| Hallucination | When a model states something false with confidence; checkpoints and sources guard against it. |

## The bottom line

Agents aren’t magic, and they aren’t a threat to good public service. Used well, they take on the repetitive checking and paperwork, so public servants can spend more time on the cases and people that need their judgment.

The key is to start with a real problem, keep people in charge of decisions, and test carefully before trusting.

At dotmind, that’s how we build every agent. If you’d like to explore where agents could help your team, [bring us a service](https://dotmind.org/#contact).
