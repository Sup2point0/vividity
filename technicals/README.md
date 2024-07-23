# Palette Definitions

Here you’ll find the JSON schema for colour palette definitions. For the palettes themselves, see [colours](../colours/).

Vividity colour palettes define a particular set of fields, which are used to build the interface. This means you can easily change between palettes while keeping the same semantic intent!

Some of these fields can be ommitted, in which case other colours will be used. This is perfectly normal, since some palettes won’t need to define all that many colours!


<br>


## Metadata

### Shard
Each palette needs a unique identifier for it. Since this will ultimately be used as a CSS class, it should be in `kebab-case`.

### Name
This is the actual displayed name of the palette, distinct from the internally used shard. Capitalisation, spacing, etc. are all preserved.

### Description
A short and sweet description of what the palette’s like. Often dramatic, cryptic, and a little random!

### Duality
Palettes should specify whether they have a light or dark theme, which is generally determined by the background colours they use.


<br>


## Colours

### Core
The key accent colours.

| key | field | notes |
| :-- | :---- | :---- |
| `prot` | Primary accent | The most prominent accent colour! |
| `deut` | Secondary accent | An accent colour to go alongside the primary. |
| `focus` | Focus interaction | Colour of outlines for keyboard navigation. |

### Text
Text can be formatted in a lot of ways!

| key | field | notes |
| :-- | :---- | :---- |
| `text` | Regular text |
| `text-prot` | Accented text | For highlighting, table headers, ... |
| `text-deut` | Minor text | For captions, footnotes, ... |
| `text-trit` | Really minor text | If you need it! |
| `text-bold` | Bold text | A colour to give bold text instead of increasing the weight (cuz colour is more subtle than weight!) |
| `text-code` | Inline code | Colour of inline `code`. Won’t affect code blocks since those use syntax highlighting. |

### Background
There’s so much that goes into the background. Structure, hierarchy, flow, it’s all here.

| key | field | notes |
| :-- | :---- | :---- |
| `back` | Background | The normal colour of the background. |
| `back-prot` | For emphasised parts of the background, like tables, blockquotes, ... |
| `back-deut` | For blocks of the background, like the navbar, footer, ... |
| `back-trit` | If you need it! |

### Lines
Lines are a key part of a UI! And just reusing the colour from the background often doesn’t work that well – a thin line is hugely different to a solid block of colour.

| key | field | notes |
| :-- | :---- | :---- |
| `line` | Lines | For underlines, blockquotes, ... |
| `line-prot` | Highlight lines | For flavourful lines! |
| `line-deut` | Background lines | For horizontal rules, ... |

### Links
Who doesn’t love nicely coloured links?

| key | field | notes |
| :-- | :---- | :---- |
| `link` | Links | |
| `link-visited` | Visited link | The colour of links you’ve already visited. |
| `link-hover` | Hovered link | The colour when you hover over a link. |
| `link-click` | Clicked link | The colour when you click the link! |

### Cards
This refers to blocks of promotional content, like items in an online store.

| key | field | notes |
| :-- | :---- | :---- |
| `card` | Card | The background colour of cards. |
| `card-hover` | Hovered card | Cards can change colour when you hover over them!
| `card-click` | Clicked card | Oh, you clicked the card!! |
