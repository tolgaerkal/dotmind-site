# Your data stays in your state

*Tolga Erkal · November 24, 2026*

## Residents’ data belongs to the state

When a resident shares a pay stub, a medical letter or a photo ID with a public service, they’re trusting the state with it, not a technology vendor. Our agents are built to keep it that way.

The first question most agencies ask us isn’t about AI accuracy. It’s “where does our data go?” That’s the right first question. Here is our answer, in plain terms.

## Where the data lives

Our agents run inside the state’s own cloud environment, next to the systems they work with. Case files and records never move into dotmind’s systems.

![Where the data lives: inside the state’s environment](images/data.svg)

The only thing that leaves the boundary is the text an agent needs for the task in front of it, sent to an AI model running in a cloud region the state has approved. The agency chooses that environment with us before anything goes live.

## Who and what can see residents’ data

Access is limited to what each task needs, and nothing more.

| Who or what | What it can see | What it can’t |
| --- | --- | --- |
| An agent working on a case | The documents and details for that one case | Other residents’ cases, or systems its task doesn’t use |
| Agency staff | Cases assigned to them, as today | Anything their role doesn’t already allow |
| dotmind engineers | System health and anonymized test data | Live residents’ data, unless the agency grants time-limited access for a specific fix |
| The AI model | Only the text the agent sends for the task at hand | Anything stored in state systems; and under the commercial terms we use, the data isn’t used to train models |

System passwords and keys are held in a secure vault, never by the agent itself, so even a misbehaving agent can’t reach beyond its role.

## What we never do

- Sell, share or reuse residents’ data for anything beyond the service it was given for.
- Use one state’s data to build services for another.
- Use residents’ data to train AI models.
- Copy case records into our own systems; agents work with the state’s records where they already live.
- Keep data longer than the state’s own retention rules allow.

## How your agency can verify it

You shouldn’t have to take our word for it. Every deployment gives the agency ways to check.

- **A full audit log.** Every action an agent takes, and every piece of data it touches, is recorded and visible to the agency.
- **Access you control.** The agency decides which systems agents can reach, and can revoke access at any time.
- **Independent standards.** We design to meet the security and privacy frameworks states rely on, such as StateRAMP/GovRAMP, CJIS for justice data, HIPAA for health data and IRS Publication 1075 for tax data, depending on the service.
- **Your security team at the table.** We review the setup with the agency’s IT and security staff before anything goes live, and on a regular schedule after.

## Trust starts with data

Residents will only use AI-supported services if they trust what happens to their information. Agencies will only adopt them if they stay in control. We build for both.

If data questions are holding your agency back, [bring us a service](https://dotmind.org/#contact). We’ll walk your security team through exactly how it works.
