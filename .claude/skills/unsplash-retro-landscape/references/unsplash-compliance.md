# Unsplash API compliance rules (the important stuff)

These are the rules the scripts in this skill must always follow. Source: live Unsplash docs as of the skill's creation:

- <https://unsplash.com/documentation>
- <https://help.unsplash.com/en/articles/2511315-guideline-attribution>
- <https://help.unsplash.com/en/articles/2511258-guideline-triggering-a-download>

## 1. Authentication

Every request to `api.unsplash.com` must include:

```
Authorization: Client-ID <UNSPLASH_ACCESS_KEY>
Accept-Version: v1
```

(Or `?client_id=...` as a query param — header form is preferred.) The skill only ever does public actions, so the Access Key alone is enough; no user OAuth/bearer token needed.

## 2. Search

`GET https://api.unsplash.com/search/photos` with:

- `query` (required)
- `orientation` — `landscape` / `portrait` / `squarish`
- `color` — one of `black_and_white`, `black`, `white`, `yellow`, `orange`, `red`, `purple`, `magenta`, `green`, `teal`, `blue`
- `content_filter` — `low` (default) or `high`
- `per_page` — max 30
- `page` — defaults to 1
- `order_by` — `relevant` (default) or `latest`

## 3. Hotlinking (REQUIRED)

> "we require the image URLs returned by the API to be directly used or embedded in your applications (generally referred to as hotlinking). By using our CDN and embedding the photo URLs in your application, we can better track photo views"

For previews and any display, embed `urls.thumb` / `urls.small` / `urls.regular` directly from `images.unsplash.com`. Do **not** rehost copies for display.

Image requests to `images.unsplash.com` do **not** count against the API rate limit.

## 4. The `ixid` query parameter (REQUIRED)

> "All resizing and manipulations of image URLs must keep this parameter as it allows for your application to report photo views and be compliant with the API Guidelines"

Stripping `ixid` from an image URL or a `download_location` URL breaks view tracking and violates the guidelines. When building resized URLs off `urls.raw` with imgix params (`w`, `h`, `fit`, `q`, `fm`, `auto=format`, `dpr`), append them — do not replace the existing query string.

## 5. Download tracking (REQUIRED, and distinct from fetching bytes)

> "When your application performs something similar to a download (like when a user chooses the image to include in a blog post, set as a header, etc.)" — trigger `GET <photo.links.download_location>` with auth, preserving the `ixid` query param.

Crucial details:

- Use `photo.links.download_location` — **not** `photo.links.download`.
- Authorize with `client_id` (header or query param), else you get a `401`.
- Preserve all existing query params (including `ixid`).
- This is a **pure event endpoint** — it doesn't return image bytes. The actual file bytes come from `urls.full` (or `urls.raw` + size params).
- Fire it **asynchronously** so it never blocks the user.
- Fire it for **every image actually used**, not for previewed-but-discarded candidates.

## 6. Attribution (REQUIRED when displaying)

Exact HTML template from Unsplash:

```html
Photo by <a href="https://unsplash.com/@USERNAME?utm_source=APP_NAME&utm_medium=referral">FULL NAME</a> on <a href="https://unsplash.com/?utm_source=APP_NAME&utm_medium=referral">Unsplash</a>
```

Where:

- `USERNAME` = `user.username` from the photo object
- `FULL NAME` = `user.name`
- `APP_NAME` = the registered Unsplash app name (`utm_source`)
- `utm_medium` is always the literal string `referral`

The skill writes both this HTML form and a Markdown equivalent to `CREDITS.md` for each kept image, and a sidecar `<filename>.credit.json` with structured data (id, links.html, description) so the credits survive even if `CREDITS.md` is regenerated.

## 7. Rate limits

- **Demo mode**: 50 requests/hour.
- **Production mode**: 5000 requests/hour (after Unsplash approves the app).
- Only JSON requests to `api.unsplash.com` count. `images.unsplash.com` requests do not.
- Every response includes `X-Ratelimit-Limit` and `X-Ratelimit-Remaining` headers. Scripts read these and warn when remaining drops below 10.

## 8. Errors to handle

- `401` — missing/invalid `client_id`. Point user back to env-var setup.
- `403` — permissions or rate-limit. Surface the remaining header value.
- `404` — bad photo ID. Skip and continue.
