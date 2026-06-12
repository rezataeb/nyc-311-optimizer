# NYC 311 Complaint Optimizer

Turn plain English frustrations into strong, legally grounded NYC 311 complaints — routed to the right agency with a direct filing link.

**Live demo:** https://nyc-311-optimizer.vercel.app

## What It Does

1. You describe your problem in plain English
2. Pick a tone: **Polite**, **Firm**, or **Urgent**
3. Claude rewrites it into a specific, legally grounded complaint and returns:
   - Optimized complaint text (3–5 sentences)
   - 311 category (e.g. `HEAT/HOT WATER`, `NOISE`, `SANITATION`)
   - Responsible agency acronym and full name (e.g. HPD, DOT, DSNY)
   - Legal note — what the city is obligated to do and by when
   - Response likelihood: **High**, **Medium**, or **Low**
4. Copy the complaint with one click or go straight to the 311 filing page

Three ready-to-file examples are pre-loaded on every page visit.

## Run Locally

```bash
npm install
npm run dev
```

Open `http://localhost:5173`.

Requires a `.env` file at the project root:

```
ANTHROPIC_API_KEY=sk-ant-...
```

## Project Structure

```
.
├── api/
│   └── optimize.js     # Vercel serverless function — proxies Anthropic API
├── index.html          # entire frontend — HTML, CSS, and JS in one file
├── package.json        # scripts and Vite dev dependency
└── .env                # ANTHROPIC_API_KEY (never committed)
```

## Tech Stack

- **Frontend:** Vanilla JS, single `index.html`, no framework
- **Build/Dev:** Vite + Vercel Dev
- **AI:** Anthropic Claude Haiku (`claude-haiku-4-5-20251001`) via serverless proxy
- **Hosting:** Vercel (auto-deploys on push to `main`)
- **No backend, no database, no login**

## Deploy

```bash
npx vercel --prod
```

The API key lives in Vercel's server environment and is never exposed in the browser bundle.
