```markdown
# Design System Documentation: Scientific Chic

## 1. Overview & Creative North Star
### The Creative North Star: "The Observational Plane"
This design system is built to bridge the gap between rigorous academic precision and the ethereal, almost poetic nature of quantum mechanics. We move beyond the "standard dashboard" by treating the UI as an **Observational Plane**—a dark, high-fidelity environment where data and insights emerge from the void.

To achieve this "Scientific Chic" aesthetic, we reject generic, boxed layouts. Instead, we embrace **intentional asymmetry**, **editorial-scale typography**, and **tonal depth**. The goal is to make the researcher's work feel like a premium publication rather than a utility tool. We use breathing room (negative space) not just for clarity, but as a design element that signifies intellectual authority.

---

## 2. Colors & Surface Architecture
The palette is rooted in the deep spectrum of a midnight laboratory, punctuated by the high-energy glow of quantum emitters.

### The "No-Line" Rule
**Explicit Instruction:** Designers are prohibited from using 1px solid borders to define sections or containers. Structural boundaries must be created exclusively through:
1.  **Background Color Shifts:** Placing a `surface-container-low` element against a `surface` background.
2.  **Tonal Nesting:** Using the `surface-container` tiers (Lowest to Highest) to create a sense of physical layering.
3.  **Negative Space:** Using the Spacing Scale (specifically `spacing-8` and `spacing-12`) to imply separation.

### Surface Hierarchy
*   **The Void (Background):** `#0b1326`. This is our canvas.
*   **Layering Levels:** 
    *   Use `surface-container-lowest` for the deepest recessed areas (e.g., sidebars).
    *   Use `surface-container-high` for interactive elements that need to "rise" toward the user.
*   **The Glass & Gradient Rule:** For hero sections or primary calls-to-action, do not use flat fills. Use a subtle linear gradient transitioning from `primary` (#2fd9f4) to `primary-container` (#001b20) at a 135-degree angle. For floating overlays, use a `surface` color at 60% opacity with a `backdrop-filter: blur(20px)` to simulate frosted optical glass.

---

## 3. Typography
Our typography is an editorial dialogue between the classic academic serif and the technical precision of a sans-serif.

*   **Display & Headlines (Newsreader):** This serif choice conveys "Trustworthy Academic." Use `display-lg` for hero statements. To break the template look, use **optical sizing** and generous letter spacing for headlines to give them an authoritative, "Scientific American" editorial feel.
*   **Body & Titles (Inter):** The workhorse. Use `body-lg` for research abstracts. It provides a clean, neutral counterpoint to the expressive headlines.
*   **Data Labels (Space Grotesk):** For technical readouts, coordinates, or "quantum" metrics, use Space Grotesk (`label-md`). Its slightly geometric, monospace-adjacent feel evokes scientific instrumentation.

---

## 4. Elevation & Depth
Depth in this system is achieved through light and material properties, never through heavy shadows.

*   **The Layering Principle:** Stacking is our primary tool. Place a `surface-container-highest` card atop a `surface-container-low` section to create a soft, natural lift.
*   **Ambient Shadows:** If a floating element (like a dropdown) requires a shadow, use a large blur (32px+) with a very low opacity (6%) using the `on-surface` color. It should feel like a soft ambient occlusion, not a "drop shadow."
*   **The Ghost Border Fallback:** If a border is required for extreme accessibility needs, use a "Ghost Border": the `outline-variant` token at **15% opacity**. Anything more is too heavy for the "Scientific Chic" vibe.

---

## 5. Components

### Buttons
*   **Primary:** A subtle gradient of `primary` to `primary-fixed-dim`. No border. Text in `on-primary-fixed`.
*   **Secondary:** Glassmorphic. A semi-transparent `surface-variant` with a `backdrop-blur`.
*   **Tertiary:** Ghost style. `on-surface` text with no container, gaining a subtle `surface-container-highest` background on hover.

### Cards & Lists
*   **The "No Divider" Rule:** Forbid the use of 1px lines between list items. Instead, use vertical white space (Spacing `2.5` or `3`) and a subtle shift to `surface-container-low` on hover to indicate interactivity.
*   **Nesting:** Cards should be `surface-container-low`. Content inside cards should sit on the card's surface without additional boxes, using typography and spacing to define hierarchy.

### Input Fields
*   **Minimalist Entry:** Use a `surface-container-highest` background with a `primary` "glow" (2px height) at the bottom only when focused. Forgo the four-sided box to keep the "Scientific Chic" layout feeling open.

### Specialized Components: The Quantum Visualizer
*   **Interference Patterns:** Use subtle SVG masks of interference fringes (alternating opacity gradients) as background textures for `surface-bright` containers.
*   **Bloch Sphere Icons:** Use thin-stroke (`0.5px`) geometric icons to represent state changes or data points, utilizing the `secondary` (#d0bcff) accent color.

---

## 6. Do’s and Don'ts

### Do:
*   **Embrace Asymmetry:** Place a large `display-md` headline on the left with a small `body-sm` caption offset to the right. It feels intentional and high-end.
*   **Use Tonal Transitions:** Transition between `surface-dim` and `surface-bright` to guide the eye through the information hierarchy.
*   **Prioritize Legibility:** Ensure `on-background` text always meets WCAG AAA standards against the deep `background`.

### Don't:
*   **No "Box-in-a-Box" Design:** Avoid nesting cards inside cards with distinct borders. Use the Surface Scale to differentiate depth.
*   **No Standard Grids:** While the underlying math should be solid, don't make the grid obvious. Let elements breathe and overlap slightly (e.g., an image overlapping a `surface-container` edge) to create a custom, designed feel.
*   **No High-Contrast Borders:** Never use a 100% opaque `outline` color for structural separation. It shatters the "Scientific Chic" sophistication.

---

**Director’s Final Note:** 
Remember, we are designing for a researcher who deals with the invisible and the infinitesimal. The UI should feel like a precision instrument—silent, powerful, and impeccably organized. If a layout feels "crowded," double the spacing. If it feels "standard," remove a line and add a background tone.```