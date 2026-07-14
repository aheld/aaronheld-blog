# Summary: Same Architecture, One Hour Each

## SEO Description (1–2 sentences)

Video for explaining system architecture has gotten cheap fast, so I documented my Market Finder harvester two ways, a written C4 doc and a five-minute animated video generated from it with Fable, in about an hour each. The tie is real and it's a trap; here's what each medium actually does and when the moving version earns its hour.

## Impact Statement (3–4 sentences)

Static diagrams are great at structure and bad at behavior, and the harvester's whole value is behavior: a loop with replay, human review gates, sticky fields, and a quality score. I took the existing architecture doc, handed it to Fable, and got an animated explainer for roughly the same hour the doc took, but only because the code was already documented and the video pipeline already existed. The honest lesson is a three-layer cost story (a conditional marginal tie, a real cold-start gap, and a polish tax text never pays) plus a narrow rule for when the moving version is worth making. The written doc stays canonical and lives in git; the video is a mental-model bootstrap I want to eventually run as just another CI/CD step, next to API docs and Storybook.
