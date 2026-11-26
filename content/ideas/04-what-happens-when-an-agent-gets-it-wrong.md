# What happens when an agent gets it wrong?

*Tolga Erkal · November 17, 2026*

## Mistakes will happen. What matters is what comes next.

AI agents will sometimes get things wrong, just as people do. A trustworthy service is one designed so that mistakes are caught early, fixed quickly, and never quietly harm a resident.

Few technology companies talk about this openly. We think government buyers deserve a straight answer, so here is ours: how we expect agents to fail, the safety nets we build around them, and what happens if a mistake gets through.

## The kinds of mistakes agents make

Knowing how agents fail is the first step to catching them. These are the main types we design for.

| Type of mistake | Example | How it’s caught |
| --- | --- | --- |
| Misreading a document | Reads a date or an amount wrong on a scanned form | Every finding links to the page, so staff can check it in seconds |
| A wrong flag | Marks a valid document as expired | Staff review every flag before anything happens to the resident |
| A missed issue | Fails to notice a missing signature | Rules checks run separately, and random cases get full human review |
| A wrong answer | Gives outdated guidance to a resident | Answers come only from official sources, with links residents can follow |
| Acting beyond its role | Tries to take an action it shouldn’t | Access is limited to the task, so the system refuses the action |

## Five safety nets

No single check is enough, so we layer them. For a mistake to harm a resident, it has to get past all five.

![Safety nets: five layers between an agent mistake and a resident](images/nets.svg)

The most important net is the third: a person reviews the agent’s work and makes the decision. The others make that review faster and more reliable, and catch what a busy reviewer might miss.

## When a mistake does reach a resident

No system is perfect. If a mistake gets through, the priority is to put it right for the person, fast.

1. **The resident can always challenge it.** Every outcome comes with the reasons behind it and a clear way to ask for a review or appeal.
2. **A person reviews the challenge.** Appeals go to staff, never back to the same agent.
3. **The case is corrected.** The record is fixed, and the resident is told what changed and why.
4. **Similar cases are checked.** If one case went wrong, we look for others affected by the same cause.
5. **The agency is told.** The agent’s named owner is informed, with a plain account of what happened.

## Learning from every mistake

Every mistake, caught or not, becomes a test case. We add it to the set of real examples each agent must pass before any change goes live, so the same error can’t quietly return.

We also watch for patterns: how often staff overrule the agent, which flags turn out wrong, and where residents appeal. A rising number is a signal to investigate before it becomes a problem.

And if an agent starts behaving unexpectedly, it can be paused immediately, with the service falling back to the normal staff process.

## Trust comes from how you handle failure

Promising that AI will never make mistakes isn’t credible. Showing exactly how mistakes are caught, corrected and learned from is.

That’s the standard we hold ourselves to at dotmind. If you’d like to see how it works for a service you run, [bring us a service](https://dotmind.org/#contact).
