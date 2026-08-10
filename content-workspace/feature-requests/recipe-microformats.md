# Feature Request: Recipe Structured Data (schema.org Recipe)

**Surfaced by**: marry-me-beans-peas-mushrooms
**Date**: 2026-07-21

## Problem

The blog has no structured-data support for recipe content. The "High-Protein Marry Me Beans, Peas & Mushrooms" post ships as a plain Markdown ingredient list and numbered method, readable but invisible to recipe-aware search features: no rich snippet in Google search results (star ratings, cook time, calorie count), no compatibility with recipe-card browser extensions or "save recipe" tools readers might use, no machine-readable prep/cook time or nutrition data.

## Proposed Solution

Add schema.org `Recipe` JSON-LD structured data support to the PaperMod theme layer, surfaced through Hugo front matter so a post can opt in without hand-writing JSON-LD per post. Front matter would carry recipe-specific fields (prepTime, cookTime, servings, ingredients list, instructions list, nutrition) that a partial template renders into a `<script type="application/ld+json">` block, plus optionally a lightly-styled recipe card in the rendered HTML (print-friendly, maybe a "jump to recipe" anchor link for the top of the post).

## Why It Matters

This is the first recipe post on the blog, but food/recipe content is a plausible recurring category (see `_config/themes.md` for how recurring topics graduate into supported patterns). Structured data also directly serves the attribution goal already central to this kind of post: a well-formed Recipe schema can carry the original source's name and URL in a machine-readable way, reinforcing credit rather than just relying on an inline Markdown link.

## Acceptance Criteria

- A post can define recipe fields in its Hugo front matter (ingredients, instructions, prepTime, cookTime, totalTime, servings/yield, nutrition) without hand-authoring JSON-LD.
- The theme renders valid schema.org `Recipe` JSON-LD from those fields, validated against Google's Rich Results Test.
- Rendering degrades gracefully for non-recipe posts (no schema emitted if the front matter fields are absent).
- The visible recipe card in the post body stays readable and print-friendly; structured data doesn't require duplicating the ingredient list by hand in two places.
- Alt text and accessibility rules from `_config/constraints.md` still apply to any recipe images.
