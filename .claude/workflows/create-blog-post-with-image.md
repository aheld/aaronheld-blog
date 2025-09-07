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

####  Create Initial Post File
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

### 2. Wait for the content
Prompt the user to enter the content.

Once the content is entered, read it and update the front matter created in the previous step


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

### 7. Publish to GitHub
1. Stage and commit changes:
```bash
git add content/post/post-slug-name/
git commit -m "$(cat <<'EOF'
Add new post: Post Title

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

2. Push to trigger deployment:
```bash
git push
```

### 8. Monitor Deployment
Use the GitHub Actions monitor agent to track deployment:
```
Use the github-actions-monitor agent to check deployment status and wait for completion
```
- Agent will automatically check workflow run status
- Deployment typically takes 1-2 minutes
- Agent provides detailed error reporting if deployment fails
- Agent confirms successful completion before proceeding

### 9. Validate Publication
Once deployment completes:
1. Navigate to https://www.aaronheld.com/
2. Verify post appears on homepage
3. Click into post to validate:
   - Header image displays correctly
   - Attribution links work (both photographer and Unsplash)
   - Content renders properly
   - Tags and categories function

## Common Issues

### Post Not Appearing
- **Draft status**: Remove `draft: true` or use `hugo server -D`
- **Date format**: Use `"YYYY-MM-DD"` not `"YYYY-MM-DDTHH:MM:SSZ"`
- **Future dates**: Ensure date is not in the future

### Image Issues
- **File path**: Ensure image is in same directory as `index.md`
- **Attribution**: Always include proper Unsplash attribution with UTM parameters
- **Alt text**: Provide descriptive alt text for accessibility
- **Image cropping**: Use `magick convert input.jpg -gravity Center -crop 1080x600+0+0 header.jpg` for optimal header dimensions

### Deployment Issues
- **GitHub Actions failure**: The github-actions-monitor agent will provide detailed error logs
- **Attribution links not working**: Ensure HTML anchor tags are properly formatted in front matter caption
- **Site not updating**: Agent will confirm deployment completion before validation step
- **Deployment timeout**: Agent monitors for up to 10 minutes before reporting timeout

## File Structure
```
content/post/post-slug-name/
├── index.md
└── header.jpg
```

## Tools Used
- `mcp__unsplash__search_photos` - Find suitable images
- `curl` - Download images
- `ImageMagick` - Crop and optimize images
- Hugo front matter - Configure post metadata
- PaperMod theme - Cover image support
- `github-actions-monitor` agent - Automated deployment monitoring
- Browser MCP - Validate published site

## Notes
- Always use landscape orientation for header images
- Include both front matter caption and footer attribution
- Test locally before publishing
- Use descriptive, SEO-friendly descriptions
- Use HTML anchor tags in front matter captions for UTM tracking
- Follow CLAUDE.md commit message standards for all commits
- Monitor deployment completion before validating publication