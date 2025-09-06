# Create Blog Post with Header Image Workflow

This workflow documents the process for creating a new blog post with a header image from Unsplash.

## Prerequisites
- Hugo site with PaperMod theme
- Unsplash integration available in Claude Code
- Image editing tools (curl for download)

## Steps

### 1. Create Post Structure
```bash
mkdir -p "content/post/post-slug-name"
```

### 2. Create Initial Post File
Create `content/post/post-slug-name/index.md` with basic front matter:
```yaml
---
title: "Post Title"
date: "YYYY-MM-DD"
description: "Brief description for SEO and social sharing"
categories: ["Category"]
tags: ["tag1", "tag2", "tag3"]
---
```

**Important**: Use `"YYYY-MM-DD"` date format, not full timestamp format.

### 3. Find and Download Header Image
1. Search Unsplash for relevant images:
   - Use specific search terms related to post topic
   - Set `orientation: "landscape"` for header images
   - Limit results with `per_page: 5` to avoid token limits

2. Download selected image:
```bash
curl -o "content/post/post-slug-name/header.jpg" "[unsplash-regular-url]"
```

### 4. Add Header Image to Front Matter
Update the post front matter to include cover image:
```yaml
---
title: "Post Title"
date: "YYYY-MM-DD"
description: "Brief description"
categories: ["Category"]
tags: ["tag1", "tag2"]
cover:
    image: "header.jpg"
    alt: "Descriptive alt text"
    caption: "Photo by [Photographer](link) on [Unsplash](photo-link)"
---
```

### 5. Add Attribution Footer
Include proper attribution at the end of the post:
```markdown
---

*Header photo by [Photographer Name](photographer-link) on [Unsplash](photo-link)*
```

### 6. Test Locally
```bash
hugo server -D  # Include drafts during development
hugo server     # Production preview
```

### 7. Publish
Remove `draft: true` from front matter or set `draft: false` when ready to publish.

## Common Issues

### Post Not Appearing
- **Draft status**: Remove `draft: true` or use `hugo server -D`
- **Date format**: Use `"YYYY-MM-DD"` not `"YYYY-MM-DDTHH:MM:SSZ"`
- **Future dates**: Ensure date is not in the future

### Image Issues
- **File path**: Ensure image is in same directory as `index.md`
- **Attribution**: Always include proper Unsplash attribution
- **Alt text**: Provide descriptive alt text for accessibility

## File Structure
```
content/post/post-slug-name/
├── index.md
└── header.jpg
```

## Tools Used
- `mcp__unsplash__search_photos` - Find suitable images
- `curl` - Download images
- Hugo front matter - Configure post metadata
- PaperMod theme - Cover image support

## Notes
- Always use landscape orientation for header images
- Include both front matter caption and footer attribution
- Test locally before publishing
- Use descriptive, SEO-friendly descriptions