---
name: frontend-requirements
description: Complete frontend design and implementation specification for Concrete Strength Predictor
type: project
---

# Frontend Requirements — Concrete Strength Predictor

**Last Updated:** 2026-10-08  
**Status:** Design Plan Complete; Ready for Implementation  
**Owner:** Frontend Design Lead

---

## 1. Design Philosophy

### Subject Matter Foundation
- **Domain:** Civil Engineering / Materials Science
- **Audience:** Engineers, material scientists, students, practitioners
- **Tone:** Professional, data-driven, honest about uncertainty
- **Aesthetic Direction:** Material authenticity (concrete/engineering world), not generic tech UI

### Core Principles
1. **Material Authenticity:** Visual language drawn from concrete and engineering contexts
2. **Clarity Over Decoration:** Every visual element encodes functional information (grouping, hierarchy, state)
3. **One Memorable Element:** Prediction display is the hero moment; everything else supports it
4. **Numeric Precision:** Data in monospace; predictions feel authoritative and trustworthy
5. **State Clarity:** Input validation, predictions, warnings use color and icons deliberately
6. **Left-Aligned Hierarchy:** Engineering workflows scan left-to-right; no centering except hero headline

---

## 2. Visual Design System

### Color Palette

| Purpose | Name | Hex | RGB | Usage |
|---------|------|-----|-----|-------|
| Base Background | Concrete Grey | `#1a1a1a` | 26, 26, 26 | Page background (not pure black) |
| Primary Accent | Brass Gold | `#e8b84f` | 232, 184, 79 | Buttons, CTAs, highlights (evoking measurement tools) |
| Secondary | Slate Grey | `#7a8a99` | 122, 138, 153 | Secondary text, dividers, disabled states |
| Text Primary | Off-White | `#f5f5f5` | 245, 245, 245 | Body text, labels |
| Success/Valid | Concrete Green | `#4a9d6f` | 74, 157, 111 | Success messages, valid indicators |
| Warning/Caution | Rust Orange | `#c97a3a` | 201, 122, 58 | Warnings, alerts, risky inputs |
| Error | Deep Red | `#d32f2f` | 211, 47, 47 | Errors, invalid inputs |
| Border/Divider | Charcoal | `#2a2a2a` | 42, 42, 42 | Input borders, section dividers |

**Palette Rationale:**
- Rejects warm-cream + terracotta default (too generic)
- Rejects acid-green SaaS kit (not engineered)
- Colors drawn from concrete material world: grey concrete surfaces, brass/steel reinforcement, rust oxidation
- Brass accent signals precision and measurement tools
- Dark base supports numeric display legibility

### Typography

#### Typeface Selection
- **Display / Headings / Body:** `Inter` (geometric sans-serif)
  - Weights used: 300 (Light), 400 (Regular), 600 (Semibold), 700 (Bold)
  - Reason: Single-family approach avoids "AI-generated two-font" template feel
  - Clean, engineered appearance appropriate to subject matter

- **Numeric Data / Predictions / Labels:** `JetBrains Mono` (monospace)
  - Weight: 400 (Regular), 600 (Semibold)
  - Used sparingly: only for predictions, test results, numeric data
  - Creates visual distinction for critical output

#### Type Scale

| Usage | Font | Size | Line-Height | Weight | Letter-Spacing | Notes |
|-------|------|------|-------------|--------|-----------------|-------|
| Page Title | Inter | 48px | 1.2 | 700 | -0.5px | Hero headline |
| Subtitle | Inter | 18px | 1.5 | 400 | 0 | Tagline below title |
| Section Head | Inter | 24px | 1.4 | 600 | -0.25px | Input group headers |
| Input Label | Inter | 14px | 1.5 | 600 | 0 | Form labels |
| Body Text | Inter | 16px | 1.6 | 400 | 0 | Description, instructions |
| Small Text | Inter | 12px | 1.4 | 400 | 0.5px | Help text, hints, metadata |
| Prediction Value | JetBrains Mono | 56px | 1.1 | 600 | 0 | Main prediction output |
| Prediction Unit | JetBrains Mono | 18px | 1.1 | 400 | 0 | "MPa" label next to prediction |
| Data Label | JetBrains Mono | 12px | 1.4 | 400 | 0.5px | Ratio values, metrics |

**Typographic Rules:**
- Line length: max 80 characters for body text
- No single-word highlights in headlines (e.g., don't italicize one word)
- No ALL-CAPS labels or eyebrows
- Monospace used only for numeric/code-like content
- Weights vary to signal hierarchy, not multiple typefaces

---

## 3. Layout & Structure

### Page Layout Grid
```
┌────────────────────────────────────────────────────────┐
│  HEADER SECTION                                        │
│  • Hero headline: "Concrete Strength Predictor"        │
│  • Subheadline: "Design your mix, predict results"    │
│  • Brief description: 1–2 sentences max               │
└────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────┐
│  INPUT SECTION (Left-aligned form)                     │
│  Grouped by material category:                         │
│                                                        │
│  Binders                                               │
│  ├─ Cement (kg/m³)                                    │
│  ├─ Blast Furnace Slag (kg/m³)                        │
│  └─ Fly Ash (kg/m³)                                   │
│                                                        │
│  Liquid                                                │
│  └─ Water (kg/m³)                                     │
│                                                        │
│  Modifiers                                             │
│  └─ Superplasticizer (kg/m³)                          │
│                                                        │
│  Aggregates                                            │
│  ├─ Coarse Aggregate (kg/m³)                          │
│  └─ Fine Aggregate (kg/m³)                            │
│                                                        │
│  Curing                                                │
│  └─ Age (days)                                        │
│                                                        │
└────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────┐
│  ACTION BUTTON                                         │
│  [Predict Strength]                                    │
│  (Primary CTA: brass background, bold)                │
└────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────┐
│  PREDICTION DISPLAY (Only visible after prediction)   │
│                                                        │
│  48.3 MPa                    (monospace, 56px, bold)  │
│                                                        │
│  ✓ Within expected range for this mix                 │
│  (validation message with icon)                       │
│                                                        │
└────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────┐
│  INSIGHTS SECTION (Optional, appears with prediction) │
│                                                        │
│  Mix Analysis                                          │
│  • Water-Cement Ratio: 0.60 ✓                         │
│  • Coarse-Fine Ratio: 1.24                            │
│  • Age Impact: +12% strength per 28-day cycle         │
│                                                        │
│  Feature Importance (if available)                     │
│  • Age: 35%                                            │
│  • Cement: 28%                                         │
│  • Water: 15%                                          │
│  • Aggregates: 12%                                     │
│                                                        │
└────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────┐
│  SIDEBAR / INFO (Right side, sticky)                  │
│  About This Tool                                       │
│  • Powered by Random Forest ML                        │
│  • Trained on 1,030 real mixes                        │
│  • R² accuracy: 0.85+                                 │
│                                                        │
│  Input Guidelines                                      │
│  • Use realistic mix proportions                       │
│  • Typical cement: 150–400 kg/m³                      │
│  • Typical water: 120–250 kg/m³                       │
│                                                        │
│  Disclaimer                                            │
│  Predictions are estimates. Always validate with      │
│  physical testing before production.                   │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### Responsive Behavior

**Desktop (≥1024px)**
- Main form: 60% width, left column
- Sidebar: 35% width, right column, sticky
- Spacing: 24px gutters between sections
- Input grid: 2 columns for input fields

**Tablet (768px – 1023px)**
- Main form: 100% width, stacked
- Sidebar: Below main content, full width
- Spacing: 20px gutters
- Input grid: 2 columns, adjusted sizing

**Mobile (<768px)**
- Full width, single column
- Sidebar content integrated into main flow
- Spacing: 16px gutters
- Input grid: 1 column
- Hero headline: 36px (from 48px)
- Prediction display: 40px (from 56px)

**Print Support:**
- Hide sidebar and "About" section
- Prediction output centered with timestamp
- Input values listed plainly below prediction

---

## 4. Component Specifications

### 4.1 Input Fields

**Structure:**
```html
<div class="input-group">
  <label for="cement">Cement</label>
  <input 
    type="number" 
    id="cement" 
    name="cement"
    min="0" 
    max="1000"
    step="1"
    placeholder="kg/m³"
    aria-label="Cement quantity in kg/m³"
  />
  <span class="input-hint">Typical: 150–400 kg/m³</span>
  <span class="input-error" role="alert" aria-live="polite">
    Cement must be greater than zero
  </span>
</div>
```

**Styling Rules:**
- Border: 1px solid `#2a2a2a` (Charcoal)
- Border-radius: 4px (sharp corners, engineered feel)
- Padding: 12px (comfortable, not cramped)
- Background: `#1a1a1a` (match page background)
- Text color: `#f5f5f5` (Off-white)
- Focus state: 2px solid `#e8b84f` (Brass), no outline
- Disabled state: background `#2a2a2a`, text `#7a8a99` (Slate grey)
- Placeholder: `#7a8a99` (Slate grey, muted)
- Error state: border `#d32f2f` (Deep red), text `#ff6b6b` (light red for contrast)

**Validation:**
- Real-time validation as user types (no delay)
- Show error message inline below input (not floating popup)
- Success icon (✓) appears when input is valid
- Warning icon (⚠️) appears for unusual but valid values (e.g., water-cement ratio > 1.0)

### 4.2 Primary Button (CTA)

**Structure:**
```html
<button 
  id="predict-btn"
  class="btn btn--primary"
  aria-label="Calculate concrete strength prediction"
>
  Predict Strength
</button>
```

**Styling Rules:**
- Background: `#e8b84f` (Brass gold)
- Text color: `#1a1a1a` (Concrete grey)
- Text: Inter, 16px, 600 (semibold)
- Padding: 14px 32px (prominent, not oversized)
- Border: none
- Border-radius: 4px
- Cursor: pointer
- Font-weight: 600

**States:**
- **Default:** Brass background, normal cursor
- **Hover:** Darker brass `#d4a43a`, slight lift (transform: translateY(-2px))
- **Active/Pressed:** Darker brass `#c4963a`, slight press (transform: translateY(0))
- **Disabled:** Background `#7a8a99` (Slate grey), cursor: not-allowed, opacity 0.6
- **Loading:** Background `#7a8a99`, text "Predicting...", spinner icon (2-second fade-in animation)

**Motion:**
- Hover transform (translateY): 200ms ease-out
- No bounce or spring; linear, purposeful

### 4.3 Prediction Display

**Structure:**
```html
<div class="prediction-result">
  <div class="prediction-value" role="status" aria-live="assertive">
    <span class="prediction-number">48.3</span>
    <span class="prediction-unit">MPa</span>
  </div>
  <div class="prediction-status">
    <span class="status-icon">✓</span>
    <span class="status-message">
      Within expected range for this mix
    </span>
  </div>
</div>
```

**Styling Rules:**
- Container: padding 32px, background `#2a2a2a` (Charcoal), border-radius 4px
- Value number: JetBrains Mono, 56px, 600 (semibold), `#e8b84f` (Brass)
- Unit: JetBrains Mono, 18px, 400, `#7a8a99` (Slate grey)
- Status icon: 24px, color depends on state (✓ green, ⚠️ orange, ✗ red)
- Status message: Inter, 14px, 400, `#f5f5f5` (Off-white)
- Line-height: 1.1 (tight, data-like)

**Animation on Appearance:**
- Fade in: 0 opacity → 1 opacity, 500ms ease-in
- No slide or bounce; pure fade

**States:**
- **Valid (within range):** Icon `✓`, color `#4a9d6f` (green), message "Within expected range for this mix"
- **Warning (edge case):** Icon `⚠️`, color `#c97a3a` (orange), message "Mix proportions are unusual; validate with testing"
- **Error (failed prediction):** Icon `✗`, color `#d32f2f` (red), message "Unable to predict; check inputs"

### 4.4 Input Group Header

**Structure:**
```html
<div class="input-section">
  <h3 class="input-section-title">Binders</h3>
  <div class="input-group">
    <!-- inputs -->
  </div>
</div>
```

**Styling Rules:**
- Title: Inter, 16px, 600 (semibold), `#f5f5f5` (Off-white)
- Border-bottom: 1px solid `#2a2a2a` (Charcoal)
- Padding-bottom: 12px
- Margin-bottom: 20px
- Letter-spacing: normal (no tracking)
- No ALL-CAPS

### 4.5 Insights Section

**Structure:**
```html
<div class="insights-section">
  <h3>Mix Analysis</h3>
  <ul class="insights-list">
    <li>
      <span class="insight-label">Water-Cement Ratio:</span>
      <span class="insight-value">0.60</span>
      <span class="insight-status">✓</span>
    </li>
  </ul>
  
  <h3>Feature Importance</h3>
  <div class="feature-importance">
    <div class="importance-bar">
      <div class="importance-fill" style="width: 35%"></div>
      <span class="importance-label">Age</span>
      <span class="importance-percent">35%</span>
    </div>
  </div>
</div>
```

**Styling Rules:**
- Background: `#2a2a2a` (Charcoal)
- Padding: 24px
- Border-radius: 4px
- Title: Inter, 16px, 600, `#f5f5f5`
- List items: Inter, 14px, 400, `#f5f5f5`
- Insight values: JetBrains Mono, 14px, 400, `#e8b84f` (Brass)
- Status icon: 16px, color coded (green/orange/red)
- Feature importance bars: height 24px, background `#1a1a1a`, fill `#e8b84f`
- Percent label: right-aligned, `#7a8a99` (Slate grey)

---

## 5. Interaction & Behavior

### Input Validation Flow

1. **On Focus:** Show placeholder (if empty) or highlight border (brass color)
2. **On Input (as user types):**
   - Check for minimum/maximum bounds
   - If valid: show ✓ icon, green color
   - If warning: show ⚠️ icon, orange color, display hint below
   - If invalid: show ✗ icon, red color, display error below
3. **On Blur:** Retain validation state until user corrects
4. **On Form Submit:** Block submission if any input is invalid; highlight first invalid field

**Validation Rules by Input:**

| Input | Min | Max | Warning Threshold | Error Condition |
|-------|-----|-----|-------------------|-----------------|
| Cement | 1 | 1000 | None | ≤ 0 |
| Slag | 0 | 500 | > 200 (high replacement) | None |
| Fly Ash | 0 | 500 | > 200 (high replacement) | None |
| Water | 1 | 500 | W/C ratio > 1.0 | ≤ 0 |
| Superplasticizer | 0 | 50 | > 20 (very high dosage) | None |
| Coarse Aggregate | 1 | 1500 | None | ≤ 0 |
| Fine Aggregate | 1 | 1000 | None | ≤ 0 |
| Age | 1 | 365 | > 90 (unusual age) | ≤ 0 |

### Prediction Flow

1. **User enters all inputs** → Validation happens in real-time
2. **User clicks "Predict Strength"** → Button shows loading state ("Predicting...")
3. **Model processes** → API call with validated inputs
4. **Prediction appears** → Fade-in animation, result displayed in monospace, large, bold brass text
5. **Status message & insights** → Green/orange/red icon with context message
6. **Insights section** → Populate with mix ratios, feature importance (if available)
7. **User can edit and re-predict** → Clear button appears next to prediction (optional)

### Error Handling

**Model Loading Error:**
```
🔴 Unable to load prediction model

This tool is temporarily unavailable. Please refresh the page or 
try again later. If the problem persists, contact support.
```
- Tone: Clear, not apologetic
- Icon: Red alert circle
- Button: Refresh page

**Prediction Error:**
```
⚠️ Prediction failed

The model encountered an unexpected input. Please review your values 
and try again. Common issues:
• Water-cement ratio too extreme (check Water and Cement values)
• Mix proportions unusually far from training data
```
- Tone: Helpful, diagnostic
- Suggests what to check

**Network Error:**
```
Connection lost. Check your internet and try again.
```
- Simple, direct

---

## 6. Accessibility Requirements

### WCAG 2.1 Level AA Compliance

**Keyboard Navigation:**
- All interactive elements (inputs, buttons) are focusable via Tab
- Focus order: top-to-bottom, left-to-right (natural reading order)
- Focus indicator: 2px solid `#e8b84f` (brass), visible at all times
- Escape key: Closes any open tooltips or modals

**Screen Reader Support:**
- Form labels: Associated with inputs via `<label for="...">` (not placeholders as labels)
- Input hints: `aria-label` or `aria-describedby` for additional context
- Prediction display: `role="status"` with `aria-live="assertive"` (announces immediately when prediction appears)
- Validation messages: `role="alert"` with `aria-live="polite"` (announces after input change)
- Error/success icons: Accompanied by text, not icon-only

**Color Contrast:**
- All text on background: minimum 4.5:1 contrast ratio (normal text)
- UI components: minimum 3:1 contrast ratio
- Test against WCAG AA standards using WebAIM or similar tool

**Motion & Animation:**
- Respect `prefers-reduced-motion` media query
- If user has reduced motion enabled: skip all animations (fade-in, hover transforms)
- No auto-playing videos or moving elements

**Responsive Text:**
- Min font size: 12px
- Max font size: 56px (prediction value)
- Zoom support: page functional at 200% zoom
- No fixed viewport width

---

## 7. Performance Requirements

### Load Time Targets
- **First Contentful Paint (FCP):** < 1.5 seconds
- **Largest Contentful Paint (LCP):** < 2.5 seconds
- **Cumulative Layout Shift (CLS):** < 0.1

### Bundle Size Targets
- HTML/CSS/JS combined: < 150 KB (before compression)
- Gzipped: < 50 KB
- No external CDN dependencies (fonts, libraries) unless critical

### Runtime Performance
- Input validation: < 50ms (no perceived lag)
- Button click to prediction: < 3 seconds (including model loading time)
- Prediction display animation: 500ms fade-in (smooth, no jank)

### Mobile Performance
- Touch targets: minimum 44×44 px
- No horizontal scroll at any viewport width
- Fast tap response (no 300ms delay; use `touch-action: manipulation`)

---

## 8. Browser & Environment Support

### Supported Browsers
- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- Mobile Safari (iOS): Latest version
- Chrome Mobile (Android): Latest version

### Streamlit Specifics
- Streamlit version: >= 1.28
- Python version: >= 3.8
- Session state management: Use `st.session_state` for predictions cache
- No custom Streamlit components; use native widgets

### Caching & State
- Cache model loading: `@st.cache_resource` for `joblib.load()`
- Cache predictions: `@st.cache_data` with input hash
- Session state: Store last prediction + input values for quick re-run

---

## 9. Copy & Microcopy

### Voice & Tone
- Professional but conversational
- Plain language; avoid jargon where possible
- Active voice for CTAs and messages
- Specific and helpful, not clever or cute

### Key Copy Blocks

**Hero Section:**
```
Concrete Strength Predictor
Design your mix, predict results.

Enter your concrete mix proportions and curing age to estimate 
compressive strength. Predictions powered by machine learning trained 
on 1,030 real mixes.
```

**Input Labels & Hints:**
```
Cement (kg/m³)
Typical: 150–400 kg/m³

Blast Furnace Slag (kg/m³)
Fly ash, slag, or other pozzolanic material. Optional.

Age (days)
Curing age. Longer curing = higher strength.
```

**Button Text:**
```
Predict Strength        (default)
Predicting...           (loading)
Try Again               (after error, optional)
```

**Validation Messages:**
```
✓ Cement must be greater than zero.
⚠️ Water-cement ratio is unusually high (>1.0). Check mix design!
✗ Prediction failed. Check inputs and try again.
```

**Prediction Messages:**
```
✓ Within expected range for this mix
⚠️ Mix proportions are unusual; validate with physical testing
✗ Unable to predict; check inputs
```

**Sidebar / Info:**
```
About This Tool
This app predicts compressive strength of concrete mixes using a 
Random Forest model trained on 1,030 real concrete samples from the 
UCI Machine Learning Repository.

Accuracy: R² score of 0.85+. Predictions are estimates; always 
validate with physical testing before production use.

Input Guidelines
• Cement: Typical range 150–400 kg/m³
• Water: Typical range 120–250 kg/m³
• Aggregates: Typical combined range 1,500–2,000 kg/m³
• Age: Predictions most reliable for 1–365 days
```

**Disclaimer:**
```
Disclaimer
This tool is for educational and research purposes. Predictions are 
estimates based on historical data. Always conduct physical testing 
and follow your region's concrete design standards before production 
use. The developer is not liable for any misuse or incorrect predictions.
```

---

## 10. Implementation Checklist

- [ ] **Setup:** Refactor app paths (relative, portable)
- [ ] **CSS:** Implement full custom stylesheet based on color/type/layout specs
- [ ] **Structure:** Group inputs by material category (Binders, Liquid, Modifiers, etc.)
- [ ] **Inputs:** Add validation, hints, error messages
- [ ] **Button:** Style with brass accent, loading state
- [ ] **Prediction Display:** Monospace, large, prominent with status message
- [ ] **Insights:** Implement mix analysis and feature importance display
- [ ] **Sidebar:** Add About, Guidelines, Disclaimer sections
- [ ] **Error Handling:** Try-catch for model loading, user-friendly messages
- [ ] **Accessibility:** WCAG AA compliance (keyboard, screen reader, contrast, motion)
- [ ] **Responsive:** Test desktop, tablet, mobile layouts
- [ ] **Performance:** Optimize load time, bundle size, runtime
- [ ] **Testing:** Manual QA on all browsers, devices
- [ ] **Documentation:** Inline code comments, README for setup

---

## 11. File Structure & Deliverables

**Expected Deliverables:**
- `app.py` (refactored, production-ready)
- `styles.css` (complete custom stylesheet)
- `requirements.txt` (pinned dependencies)
- `README.md` (setup and usage guide)
- Screenshot/demo of final UI

**Not Included (Future Work):**
- Mobile app (PWA or native)
- Advanced analytics dashboard
- Historical prediction tracking
- User accounts / authentication

---

## 12. Success Criteria

✅ **Design:**
- Visual identity is distinct from SaaS templates
- Color palette drawn from subject matter (concrete/engineering)
- Typography hierarchy is clear without multi-font templates
- No scattered animations or generic hover effects

✅ **Function:**
- All 8 inputs accept valid values
- Real-time validation with clear feedback
- Prediction displays in < 3 seconds
- Error messages are helpful and specific

✅ **Accessibility:**
- WCAG AA Level compliance
- Keyboard navigation works
- Screen reader announces predictions
- Reduced motion respected

✅ **Performance:**
- FCP < 1.5s, LCP < 2.5s
- Bundle < 50 KB gzipped
- Input validation < 50ms

✅ **UX:**
- Left-aligned form easy to scan
- Prediction is the hero moment
- Sidebar provides context without clutter
- Responsive from mobile to desktop

---

## 13. Notes & Future Considerations

**Potential Enhancements (Not in Scope):**
- Model explainability dashboard (SHAP values visualization)
- Batch prediction upload (CSV file)
- Mix design optimizer (suggest optimal proportions for target strength)
- Historical tracking and comparison
- Export predictions as PDF report
- Dark/light theme toggle (currently dark-only)

**Known Constraints:**
- Streamlit framework limits custom interactivity
- Model loading time ~2-3 seconds (acceptable, cached)
- No real-time collaborative features
- Single-user per session (Streamlit default)

**Maintenance:**
- Retraining schedule: Annually or when new data available
- Model versioning: Tag model date (e.g., `rf_best_2026_10_08.pkl`)
- Input data validation: Log unusual inputs for QA

---

**End of Frontend Requirements**
