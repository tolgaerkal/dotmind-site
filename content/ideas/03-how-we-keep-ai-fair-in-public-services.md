# How we keep AI fair in public services

*Tolga Erkal · November 10, 2026*

## Fairness is designed in, not assumed

An AI agent in a public service is only fair if fairness is built into how it’s designed, tested and run. It doesn’t happen by default.

Government services have a duty that most businesses don’t: they must treat everyone fairly, including people who are hardest to serve. A shop can choose its customers. A state can’t.

That’s why fairness isn’t a feature we add at the end. Here is how we approach it at dotmind, and the questions we think every agency should ask of any AI it uses.

## Where unfairness can creep in

Unfairness rarely comes from one bad decision. It usually slips in through everyday design choices.

- **Past data.** If an agent learns from past decisions, it can repeat past patterns, including unfair ones.
- **Documents and formats.** A check that expects one kind of ID or pay stub can quietly fail people with less common paperwork, such as gig workers or new arrivals.
- **Language and reading level.** Guidance written for confident English readers leaves others behind.
- **Access.** A service that only works well online disadvantages people without reliable internet, devices or digital skills.
- **Hidden reasoning.** If no one can see why an agent flagged a case, no one can spot when it’s wrong for a particular group.

## Five practices we build into every agent

1. **People decide.** Agents check, prepare and recommend. A caseworker makes every decision about rights, benefits or penalties, and can always overrule the agent.
2. **Evidence for every flag.** When an agent flags an issue, it shows the document, the page and the rule behind it. If it can’t point to evidence, it shouldn’t raise the flag.
3. **Rules from rules, not guesses.** Eligibility rules and calculations run in fixed, auditable software. The AI handles language and reading documents, not the arithmetic of entitlement.
4. **Tested across groups before launch.** We test each agent on real, anonymized cases that reflect the people the service actually serves, and compare how it performs across groups. Gaps are fixed before go-live, not after complaints.
5. **Designed for everyone.** Plain language, multiple languages where needed, accessible design, and phone, mail and in-person routes that stay open. Agents can support staff on those channels too.

## What we measure

Fairness is checked before launch and monitored while the service runs. These are the measures we track, broken down by the groups that matter for each service.

| Measure | What it shows |
| --- | --- |
| Flag rate by group | Whether some groups are flagged for issues more often than others |
| Staff overrides | How often caseworkers disagree with the agent, and for whom |
| Wrong flags | Flags that turn out to be mistaken, and who they affect |
| Time to decision | Whether some groups wait longer for an outcome |
| Completion by channel | Whether people using phone, mail or in person do as well as people online |
| Appeals and complaints | Where residents feel the service got it wrong |

When a gap appears, the agent’s named owner in the agency reviews it with us, and we fix the cause, whether that’s the agent, the rules or the process around it.

## What we won’t do

- Let an agent deny anyone a benefit, license or service on its own.
- Use protected characteristics, such as race, religion or disability, to decide how a case is treated.
- Hide how an agent reached a flag or a recommendation from the staff who rely on it.
- Launch an agent that hasn’t been tested on cases that reflect the people the service serves.
- Make the online route the only route.

## Fair by design

AI can make public services fairer, not just faster. Consistent checks, clear evidence and plain language can reduce the variation that comes from overloaded staff and confusing forms. But only if fairness is designed in from the start and checked every day.

If you’re thinking about AI for a public service and want to get this right, [bring us a service](https://dotmind.org/#contact). We’re happy to share how we test.
