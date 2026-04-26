# Bluesky Comments Integration Specification

## Overview

This specification outlines the implementation of a Bluesky-based commenting system for Aaron Held's Hugo blog using the `bluesky-comments` package. The solution integrates React components with Hugo through a shortcode approach, providing filtered comment display based on Bluesky post discussions.

## Architecture

### Technology Stack
- **Frontend**: React 18+ with `bluesky-comments` package
- **Static Site Generator**: Hugo with custom shortcode
- **Integration Method**: CDN-based React loading (no build process required)
- **Styling**: CSS integration with existing PaperMod theme

### Key Components
1. **Hugo Shortcode** (`layouts/shortcodes/bluesky-comments.html`)
2. **React Component Wrapper** (inline JavaScript)
3. **CSS Styling** (`assets/css/extended/bluesky-comments.css`)
4. **Content Configuration** (front matter integration)

## Implementation Details

### 1. Hugo Shortcode Implementation

**File**: `layouts/shortcodes/bluesky-comments.html`

```html
{{- if .Page.Params.bluesky_comment_url -}}
<div class="bluesky-comments-section">
    <hr class="comments-separator">
    <h3 class="comments-title">Comments via Bluesky</h3>
    <div id="bluesky-comments-{{ .Page.File.UniqueID }}" class="bluesky-comments-container"></div>

    <script type="module">
        import { BlueskyComments, BlueskyFilters } from 'https://unpkg.com/bluesky-comments@latest/dist/bluesky-comments.esm.js';
        import { createElement } from 'https://unpkg.com/react@18/index.js';
        import { createRoot } from 'https://unpkg.com/react-dom@18/client.js';

        const container = document.getElementById('bluesky-comments-{{ .Page.File.UniqueID }}');
        const root = createRoot(container);

        const customFilters = [
            BlueskyFilters.NoPins,
            BlueskyFilters.MinCharacterCountFilter(10),
            (comment) => {
                const text = comment.record?.text || '';
                return !text.includes('x.com') &&
                       !text.includes('linkedin.com') &&
                       !text.includes('twitter.com');
            }
        ];

        root.render(
            createElement(BlueskyComments, {
                uri: '{{ .Page.Params.bluesky_comment_url }}',
                commentFilters: customFilters,
                emptyState: createElement('div', { className: 'no-comments' }, 'No comments yet. Start the discussion on Bluesky!')
            })
        );
    </script>
</div>
{{- end -}}
```

### 2. CSS Styling Integration

**File**: `assets/css/extended/bluesky-comments.css`

```css
/* Bluesky Comments Styling */
.bluesky-comments-section {
    margin-top: 2rem;
    padding-top: 1rem;
}

.comments-separator {
    border: none;
    border-top: 1px solid var(--border);
    margin: 2rem 0 1rem 0;
}

.comments-title {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: var(--content);
}

.bluesky-comments-container {
    max-width: 100%;
    overflow-wrap: break-word;
}

.no-comments {
    padding: 1rem;
    text-align: center;
    color: var(--secondary);
    font-style: italic;
    border: 1px solid var(--border);
    border-radius: 8px;
    background: var(--code-bg);
}

/* Override bluesky-comments default styles to match theme */
.bluesky-comments-container .comment {
    background: var(--entry);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
}

.bluesky-comments-container .comment-author {
    color: var(--primary);
    font-weight: 600;
}

.bluesky-comments-container .comment-text {
    color: var(--content);
    line-height: 1.6;
}

.bluesky-comments-container .comment-date {
    color: var(--secondary);
    font-size: 0.9rem;
}

/* Dark mode adjustments */
[data-theme="dark"] .bluesky-comments-container .comment {
    background: var(--entry);
    border-color: var(--border);
}
```

### 3. Content Integration

#### Front Matter Configuration

Add to blog post front matter:

```yaml
---
title: "Your Post Title"
date: 2025-01-01T00:00:00Z
bluesky_comment_url: "https://bsky.app/profile/aaronheld.com/post/3lbxxx7xxx"
---
```

#### Shortcode Usage in Content

Add at the end of blog post content:

```markdown
{{< bluesky-comments >}}
```

### 4. Filtering Implementation

#### Built-in Filters Applied:
1. **No Pins**: Excludes pinned posts using `BlueskyFilters.NoPins`
2. **Minimum Character Count**: Excludes posts with less than 10 characters
3. **Domain Blacklist**: Filters out comments containing links to:
   - x.com
   - linkedin.com
   - twitter.com

#### Custom Filter Function:
```javascript
const customFilters = [
    BlueskyFilters.NoPins,
    BlueskyFilters.MinCharacterCountFilter(10),
    (comment) => {
        const text = comment.record?.text || '';
        return !text.includes('x.com') &&
               !text.includes('linkedin.com') &&
               !text.includes('twitter.com');
    }
];
```

## Integration with Existing Theme

### PaperMod Theme Compatibility
- Uses CSS custom properties (variables) for consistent theming
- Respects dark/light mode toggle
- Maintains consistent typography and spacing
- Integrates with existing border and color schemes

### Performance Considerations
- **Lazy Loading**: Comments only load when shortcode is present
- **CDN Delivery**: Uses unpkg.com for React and bluesky-comments
- **Minimal Bundle**: No build process required, modern ES modules
- **Conditional Rendering**: Only renders when `bluesky_comment_url` is present

## Deployment Strategy

### Phase 1: Setup Infrastructure
1. Create shortcode template file
2. Add CSS styling file
3. Test with single blog post

### Phase 2: Content Migration
1. Add `bluesky_comment_url` to relevant posts
2. Include shortcode in post templates or manually per post
3. Verify filtering works correctly

### Phase 3: Optimization
1. Monitor performance impact
2. Add loading states if needed
3. Consider caching strategies for production

## Security Considerations

### Content Security Policy (CSP)
Update `static/staticwebapp.config.json` to allow:
```json
{
  "globalHeaders": {
    "Content-Security-Policy": "script-src 'self' 'unsafe-inline' https://unpkg.com; connect-src 'self' https://bsky.social https://public.api.bsky.app;"
  }
}
```

### XSS Protection
- `bluesky-comments` package handles sanitization
- Custom filters prevent malicious link injection
- React's built-in XSS protection applies

## Testing Strategy

### Unit Testing
- Test shortcode rendering with/without `bluesky_comment_url`
- Verify filter functions work correctly
- Test CSS theming in light/dark modes

### Integration Testing
- Verify comments load from real Bluesky posts
- Test responsive design on mobile devices
- Validate performance impact on page load

### Content Testing
- Test with various Bluesky post formats
- Verify filtering removes unwanted content
- Test empty state display

## Maintenance and Updates

### Regular Tasks
1. Monitor `bluesky-comments` package updates
2. Update CDN URLs if package structure changes
3. Verify Bluesky API compatibility

### Content Management
1. Add `bluesky_comment_url` to new posts when discussion exists
2. Include shortcode in post templates for consistent placement
3. Monitor comment quality and adjust filters as needed

## Configuration Options

### Optional Enhancements
```html
<!-- Add to shortcode for additional customization -->
{{- $showAvatars := .Get "avatars" | default true -}}
{{- $maxComments := .Get "max" | default 50 -}}
{{- $sortOrder := .Get "sort" | default "newest" -}}
```

### Theme Integration
- Consider adding to single post template automatically
- Option to enable/disable globally via config.yml
- Potential integration with existing comment system toggle

## Success Metrics

### Technical Metrics
- Page load time impact < 200ms
- Comment loading time < 2 seconds
- Zero JavaScript errors in console
- 100% mobile responsiveness score

### Content Metrics
- Comments successfully filtered (no spam/unwanted links)
- Consistent theming across light/dark modes
- Proper rendering of Bluesky content (links, mentions, etc.)

### User Experience
- Seamless integration with existing blog design
- Clear indication of comment source (Bluesky)
- Easy navigation to original Bluesky discussion

---

*This specification provides a comprehensive approach to integrating Bluesky comments with Hugo while maintaining performance, security, and design consistency with the existing blog infrastructure.*