# Long-form playbooks. Body uses mini-markdown: "## " h2, "### " h3, "- " bullets, "1. " numbered, **bold**, blank line = paragraph.
GUIDES = [
{
"slug": "account-based-marketing-playbook",
"title": "Account-Based Marketing (ABM): The Complete Playbook",
"cat": "Strategy",
"desc": "How to pick target accounts, tier them, build buying-committee plays and measure ABM by pipeline instead of clicks.",
"mins": 9,
"takeaways": [
 "ABM flips the funnel: choose accounts first, then create demand inside them.",
 "Tier accounts (1:1, 1:few, 1:many) so effort matches deal value.",
 "Measure account engagement, pipeline and win rate — not lead volume.",
],
"body": """
Account-based marketing is a go-to-market approach where marketing and sales agree on a defined list of companies, then coordinate every touch — ads, content, outreach, events — to win those specific accounts. Instead of generating as many leads as possible and filtering later, ABM starts with the filter.

## When ABM makes sense
ABM pays off when deal sizes are large enough to justify concentrated effort and when buying decisions involve several people. As a rough rule, if your average contract value is in the five figures or above and a typical deal touches three or more stakeholders, ABM deserves a place in your plan. If you sell a low-priced self-serve product, broad demand generation usually returns more per dollar.

## Step 1: Build your ideal customer profile
Start with closed-won data. Pull the last 20–50 customers and look for patterns in industry, employee count, revenue band, tech stack, region and the trigger that made them buy. Then look at churned customers and lost deals to see who you should avoid. Write the ICP as a one-page document that sales signs off on — if sales does not agree with it, ABM will fail at the hand-off.

## Step 2: Select and tier accounts
- **Tier 1 (1:1):** 10–50 accounts with the highest potential value. Fully custom research, content and executive outreach.
- **Tier 2 (1:few):** 50–500 accounts grouped by industry or use case. Personalised by cluster rather than by company.
- **Tier 3 (1:many):** 500+ accounts reached through programmatic ads and automated nurture with light personalisation.

Use fit (how closely they match your ICP), intent (signals they are researching your category) and engagement (how they interact with you) to rank the list. Our free ABM tiering calculator turns these three scores into a tier automatically.

## Step 3: Map the buying committee
For each Tier 1 and Tier 2 account, identify the economic buyer, the champion, the technical evaluator, procurement and likely blockers. Each role needs a different message: the CFO cares about payback, the end user cares about workflow, IT cares about security and integration.

## Step 4: Orchestrate plays
A play is a coordinated sequence across channels. A typical Tier 2 play runs for six to eight weeks: targeted LinkedIn and display ads warm the account, a relevant guide or benchmark is offered, sales development reps follow up with role-specific messages, and an invitation to a small roundtable or a tailored demo closes the loop. Write down the trigger, the channels, the owner and the exit criteria for every play.

## Step 5: Measure what matters
Classic lead metrics undercount ABM because many stakeholders never fill in a form. Track instead:
- Account coverage: share of target accounts with known contacts in each role.
- Account engagement: meetings, site visits, content consumption by account.
- Pipeline created and velocity for target accounts versus non-target accounts.
- Win rate and average deal size on target accounts.

## Common mistakes
1. Picking too many Tier 1 accounts, which spreads effort thin.
2. Running ABM as a marketing-only project with no sales commitments.
3. Personalising only the first line of an email and calling it ABM.
4. Judging success after one quarter when enterprise cycles take two or three.
""",
"faq": [
 ("How many accounts should a small team target?", "Teams of one to three marketers usually manage 20–50 Tier 1/2 accounts well, plus a programmatic Tier 3 list."),
 ("Do I need an expensive ABM platform?", "No. A CRM, LinkedIn Matched Audiences, a spreadsheet for tiering and disciplined sales follow-up are enough to start."),
 ("How long before ABM shows results?", "Engagement lifts within weeks; pipeline impact typically shows in one to two sales cycles."),
],
},
{
"slug": "b2b-demand-generation-strategy",
"title": "B2B Demand Generation Strategy: Build Pipeline That Compounds",
"cat": "Strategy",
"desc": "A practical framework to create demand, capture it efficiently and convert it into qualified pipeline.",
"mins": 8,
"takeaways": [
 "Demand creation (education, brand) and demand capture (search, review sites, retargeting) need separate budgets.",
 "Ungated, genuinely useful content builds trust faster than form-gated PDFs.",
 "Report on pipeline and revenue, not marketing-qualified lead counts alone.",
],
"body": """
Demand generation is everything marketing does to make the right buyers aware of a problem, see you as a credible solution and raise their hand when the time is right. Lead generation is one part of it — the moment of capture — but most of the work happens before anyone fills in a form.

## Create vs. capture
Only a small share of your market is actively buying at any moment. Demand capture targets that in-market slice through search ads, review sites, comparison pages and retargeting. Demand creation reaches the much larger out-of-market majority with education, opinion and brand so that when they do enter a buying cycle, you are already on the shortlist. Split your plan and budget explicitly so the long-term work is not cut every time a quarter looks soft.

## The demand generation engine
1. **Positioning:** a clear statement of who you serve, the problem you solve and why you are different. Every campaign inherits from this.
2. **Content:** a mix of pillar guides, data-backed points of view, short social posts, video and customer stories.
3. **Distribution:** owned (email, website), earned (PR, community, partners) and paid (search, social, sponsorships).
4. **Conversion:** clear next steps on every page — demo, trial, assessment, consultation.
5. **Nurture:** relevant follow-up based on role and behaviour.
6. **Hand-off:** a written service-level agreement with sales on speed and follow-up.

## Choosing channels
Start where your buyers already spend time. For most B2B audiences that means search, LinkedIn, industry newsletters and a handful of communities or events. Test one new channel per quarter with a fixed budget and a clear success metric rather than spreading thinly across everything.

## Gated vs. ungated content
Gating forces a trade: fewer readers, more contact details. Many B2B teams now ungate most content to maximise reach and reserve forms for high-intent offers — a demo, an assessment, a tailored audit, a calculator result emailed to the user. Measure the downstream pipeline from both approaches before deciding.

## Metrics that matter
- Qualified pipeline created and its source.
- Cost per opportunity, not just cost per lead.
- Conversion rates between each stage.
- Sales cycle length and win rate by source.
- Share of search and direct traffic growth as signals of brand demand.

Use our pipeline reverse-planner to work backwards from a revenue target to the number of leads, meetings and opportunities you actually need.
""",
"faq": [
 ("Is demand generation the same as lead generation?", "No. Lead generation captures contact details; demand generation is the broader work of creating and nurturing interest that makes leads worth having."),
 ("What budget split is typical?", "Many B2B teams start near 60% demand creation and 40% capture, then adjust based on pipeline data."),
],
},
{
"slug": "lead-scoring-model",
"title": "How to Build a B2B Lead Scoring Model Sales Actually Trusts",
"cat": "Operations",
"desc": "Combine fit and behaviour scores, set thresholds with sales and keep the model honest with closed-loop data.",
"mins": 7,
"takeaways": [
 "Score fit (who they are) and engagement (what they do) separately.",
 "Set the hand-off threshold together with sales and review it quarterly.",
 "Add negative scores and decay so old activity does not inflate scores.",
],
"body": """
Lead scoring assigns points to leads so sales can focus on the people most likely to buy. Done well, it shortens response times and raises conversion. Done badly, it floods sales with "hot" leads that are students, competitors or tyre-kickers.

## Two dimensions: fit and engagement
**Fit** measures how closely a lead matches your ideal customer profile: job title, seniority, company size, industry, region and technology. **Engagement** measures behaviour: pricing-page visits, demo requests, webinar attendance, repeated email clicks. Keep these separate — a perfect-fit lead with no engagement needs nurture, while a highly engaged poor-fit lead may never buy.

## Building the model
1. Export 12 months of leads with their outcome (became opportunity or not).
2. Compare attributes and actions of converters against non-converters.
3. Give the biggest weights to the attributes and actions with the largest difference.
4. Add negative points for disqualifiers: personal email domains, student titles, competitor domains, unsubscribes.
5. Apply decay — for example, halve behavioural points after 30 days of inactivity.

## Example point scheme
- Director or above: +15; manager: +8; individual contributor: +3.
- Company size inside your sweet spot: +15.
- Pricing page visit: +10; demo request: +40; webinar attended: +10; three or more email clicks in 14 days: +8.
- Personal email: −10; competitor: −100.

Try our lead scoring builder to set weights and see how sample leads would rank.

## Thresholds and SLAs
Agree on a marketing-qualified threshold with sales, plus a response-time commitment such as contacting every MQL within one business day. Track acceptance rate (how many MQLs sales accepts) and conversion to opportunity. If acceptance falls below roughly half, the model needs recalibration.

## Keep it alive
Review the model every quarter using closed-won data. Markets shift, products change and new channels bring different behaviour. A scoring model is a living hypothesis, not a one-time setup.
""",
"faq": [
 ("Should we use predictive AI scoring?", "Predictive scoring helps once you have hundreds of conversions to learn from. Before that, a transparent rules-based model is easier to trust and tune."),
 ("What is a good MQL-to-SQL rate?", "It varies widely by market; track your own trend and focus on improving it quarter over quarter."),
],
},
{
"slug": "b2b-seo-and-ai-search",
"title": "B2B SEO in the Age of AI Search: A 2026 Playbook",
"cat": "Channels",
"desc": "How to earn visibility in classic search results and AI answers with expert content, structure and authority.",
"mins": 9,
"takeaways": [
 "Target problems and comparisons buyers actually search, not just product terms.",
 "Clear structure, original data and expert authorship help both search engines and AI answer engines.",
 "Measure assisted pipeline and branded search growth, not traffic alone.",
],
"body": """
B2B buyers still research heavily online before speaking to a vendor, but the path now runs through classic search results, AI-generated answers and conversational assistants. The fundamentals that win in all three are the same: genuinely useful content, clear structure and real authority.

## Map content to the buying journey
- **Problem-aware:** "how to reduce churn in SaaS", "why are leads not converting". Educational guides.
- **Solution-aware:** "best customer success software", "ABM vs inbound". Comparisons and frameworks.
- **Vendor-aware:** "[your brand] pricing", "[your brand] vs [competitor]", "[your brand] reviews". Honest comparison and pricing pages.

Many B2B sites only cover the last stage. The first two stages hold far more search volume and influence the shortlist.

## Write for experts, structure for machines
Answer the question in the first paragraph, then go deep. Use descriptive headings, short paragraphs, lists, tables and FAQ blocks. Add author bios with real experience. Cite original data — surveys, benchmarks from your own customer base, or calculations — because unique information is what both search engines and AI systems prefer to reference.

## Technical essentials
1. Fast, mobile-friendly pages.
2. Clean internal linking from pillar pages to supporting articles.
3. Structured data (Article, FAQPage, Organization, BreadcrumbList).
4. An XML sitemap kept current, and canonical URLs to avoid duplicates.
5. Crawlable HTML for key content rather than content hidden behind scripts.

## Authority
Earn mentions on industry publications, podcasts, partner sites and review platforms. Contribute expert quotes, publish original research others want to cite, and build free tools people link to — calculators and templates attract links naturally.

## Measuring success
Track rankings for priority topics, organic sign-ups and demo requests, assisted conversions in your attribution model, and growth in branded search. Watch for mentions of your brand inside AI answers for your key questions and test regularly.
""",
"faq": [
 ("Is SEO still worth it with AI answers?", "Yes. AI systems draw heavily on well-structured, authoritative web content, and many buyers still click through to verify details."),
 ("How long does B2B SEO take?", "Expect early wins on niche topics within three to six months and compounding results over a year or more."),
],
},
{
"slug": "linkedin-b2b-marketing",
"title": "LinkedIn for B2B Marketing: Organic, Ads and Employee Advocacy",
"cat": "Channels",
"desc": "Use company pages, founder-led content, Thought Leader-style ads and matched audiences to reach buying committees.",
"mins": 7,
"takeaways": [
 "People follow people — executive and employee posts usually outperform company page posts.",
 "Use matched audiences and company targeting to support ABM lists.",
 "Optimise ads for qualified pipeline, not the cheapest click.",
],
"body": """
LinkedIn is the default professional network for most B2B audiences, which makes it one of the few channels where you can target by job function, seniority and company at scale.

## Organic: lead with people
Company pages matter for credibility, but personal profiles drive most reach. Build a simple program where founders, executives and subject-matter experts post consistently — two to three times a week — sharing lessons, opinions and behind-the-scenes stories. Give them a content bank of ideas, but let them write in their own voice.

## Formats that work
- Short text posts with a strong first line and one clear idea.
- Document (carousel) posts that teach a framework step by step.
- Native video under two minutes.
- Newsletters for a recurring point of view.

## Paid: targeting and structure
Start with matched audiences built from your target account list and website visitors, layered with job function and seniority. Keep audiences large enough to deliver — very narrow audiences become expensive. Run awareness content to cold audiences, then retarget engaged viewers with conversion offers like assessments, demos or events.

## Lead gen forms vs. landing pages
Native lead gen forms prefill profile data and usually convert at higher rates, but lead quality can be lower. Add one or two qualifying questions and route these leads into fast follow-up. Compare cost per opportunity, not cost per lead, across both approaches.

## Employee advocacy
Make sharing easy with a weekly digest of company news and posts. Recognise active contributors. Never force scripted posts — audiences notice and engagement falls.

## Measure
Track follower growth among ICP titles, engagement from target accounts, influenced pipeline, and cost per opportunity from paid campaigns.
""",
"faq": [
 ("How much should we spend on LinkedIn ads?", "Start with a test budget large enough to get statistically useful results on one or two campaigns, then scale what produces qualified pipeline."),
 ("Should the CEO post personally?", "If they can commit to consistency and genuine insight, founder-led content is one of the highest-leverage B2B channels."),
],
},
{
"slug": "b2b-email-marketing-nurture",
"title": "B2B Email Marketing & Lead Nurturing That Converts",
"cat": "Channels",
"desc": "Design nurture tracks by role and stage, protect deliverability and write emails busy buyers actually read.",
"mins": 7,
"takeaways": [
 "Segment by role and stage; one generic newsletter is not a nurture program.",
 "Deliverability (authentication, list hygiene) is a prerequisite for results.",
 "Every email should have one goal and one call to action.",
],
"body": """
Email remains one of the highest-return channels in B2B because it reaches people you already have permission to contact. The difference between noise and pipeline is relevance.

## Foundations: deliverability
Authenticate your sending domain with SPF, DKIM and DMARC. Remove hard bounces immediately and suppress contacts who have not engaged in six months. Warm up new sending domains gradually. Keep complaint rates very low by making unsubscribing easy.

## Build nurture tracks
1. **Welcome:** three to four emails over two weeks introducing your best resources.
2. **Education by role:** separate tracks for executives, managers and practitioners.
3. **Consideration:** case studies, comparisons, ROI tools for engaged contacts.
4. **Re-engagement:** a short sequence for contacts gone quiet, then suppression.

## Writing emails busy buyers read
- Subject lines that are specific and honest — test with our subject line checker.
- One idea and one call to action per email.
- Plain, short paragraphs; most B2B email is read on phones.
- Personalisation that uses context (industry, role, recent action), not just a first name.

## Cold outreach vs. marketing email
Cold outreach is one-to-one prospecting governed by different rules and laws in each region. Keep it relevant, low volume, clearly identified and easy to opt out of. Marketing newsletters should only go to people who opted in.

## Measure
Open rates are unreliable due to privacy features, so focus on clicks, replies, conversions to meetings and pipeline influenced.
""",
"faq": [
 ("How often should we email?", "Weekly or bi-weekly is common for newsletters; nurture cadence depends on stage and engagement."),
 ("Do we need double opt-in?", "It improves list quality and is required or recommended in some regions; check the rules for your audience."),
],
},
{
"slug": "b2b-content-marketing-strategy",
"title": "B2B Content Marketing Strategy: From Editorial Plan to Pipeline",
"cat": "Strategy",
"desc": "Choose a content mission, build pillars, produce efficiently with AI and distribute so content actually gets seen.",
"mins": 8,
"takeaways": [
 "A content mission narrows topics to what your buyers need and you can uniquely say.",
 "Spend as much effort on distribution as on creation.",
 "Repurpose each pillar into many formats to multiply reach.",
],
"body": """
Content marketing in B2B is about earning attention and trust by teaching buyers something valuable. The companies that win treat content like a product: researched, planned, distributed and measured.

## Define a content mission
Write one sentence: "We publish [type of content] for [audience] so they can [outcome]." Everything you publish should pass that test. This prevents random posts that rank for nothing and convert no one.

## Build topic pillars
Choose three to five pillars aligned to the problems your product solves. Each pillar gets a comprehensive guide, supporting articles, a tool or template, and customer proof. Interlink them so readers and search engines see depth.

## Produce efficiently
- Interview internal experts and customers; their insight is your differentiator.
- Use AI to outline, summarise transcripts and draft variants, then edit heavily for accuracy and voice.
- Keep a style guide and a fact-check step — trust is easy to lose.

## Distribute deliberately
For each major piece plan: an email to subscribers, five to ten social posts from people (not just the brand page), a short video, a newsletter or community share, outreach to people quoted, and paid amplification for the best performers.

## Repurpose
A single research report can become a webinar, a slide deck, a carousel, an infographic, a podcast episode, a series of short videos and a sales one-pager.

## Measure
Track engaged readers, returning visitors, subscribers gained, assisted conversions and sales usage of content.
""",
"faq": [
 ("How often should a B2B company publish?", "Consistency matters more than volume. One excellent, well-distributed piece per week beats five thin ones."),
 ("Can AI write our content?", "AI is a strong assistant for drafts and repurposing, but expert input and editing are what make B2B content credible."),
],
},
{
"slug": "marketing-attribution-b2b",
"title": "B2B Marketing Attribution Explained: Models, Limits and What to Use",
"cat": "Analytics",
"desc": "Compare first-touch, last-touch, multi-touch and self-reported attribution, and combine them sensibly.",
"mins": 7,
"takeaways": [
 "No single attribution model is 'true' — each answers a different question.",
 "Pair software attribution with a 'How did you hear about us?' field.",
 "Use incrementality tests for big budget decisions.",
],
"body": """
Attribution tries to answer which marketing activities created revenue. In B2B it is especially hard: long cycles, many stakeholders, dark social and offline conversations.

## Common models
- **First touch:** credits the first recorded interaction. Good for understanding discovery.
- **Last touch:** credits the final interaction before conversion. Good for capture channels.
- **Linear:** splits credit equally across touches.
- **U-shaped / W-shaped:** emphasises first touch, lead creation and opportunity creation.
- **Data-driven:** algorithmic weighting based on observed paths; needs volume.

## The blind spots
Software sees clicks and form fills. It does not see a podcast someone heard, a peer recommendation in a private chat, or a conference conversation. That is why many B2B teams add a required open-text field — "How did you hear about us?" — to demo forms. Self-reported answers often surface channels that tracking misses.

## A practical stack
1. Consistent UTM conventions (use our UTM builder).
2. CRM campaign tracking on every opportunity.
3. A multi-touch view for optimisation of digital channels.
4. Self-reported attribution for discovery.
5. Periodic incrementality or holdout tests for major spend.

## Reporting
Show leaders a simple view: pipeline and revenue by primary source, cost per opportunity by channel, and the trend over time. Avoid false precision.
""",
"faq": [
 ("Which model should a small team use?", "Start with first and last touch plus a self-reported field; add multi-touch once tracking is clean."),
 ("What is marketing mix modelling?", "A statistical approach that estimates channel impact from aggregate spend and outcomes over time, useful at larger budgets."),
],
},
{
"slug": "sales-and-marketing-alignment",
"title": "Sales and Marketing Alignment: SLAs, Shared Metrics and RevOps",
"cat": "Operations",
"desc": "Agree on definitions, hand-offs and shared revenue goals so leads stop falling through the cracks.",
"mins": 6,
"takeaways": [
 "Write shared definitions of lead stages and get both leaders to sign them.",
 "A service-level agreement sets volume targets for marketing and follow-up speed for sales.",
 "Shared pipeline and revenue goals beat separate scorecards.",
],
"body": """
Misalignment between sales and marketing shows up as complaints about lead quality on one side and slow follow-up on the other. The fix is mostly process, not personality.

## Shared definitions
Document what a lead, MQL, SQL, opportunity and closed-won deal mean, with clear entry criteria. Put them in the CRM so stages change automatically where possible.

## The service-level agreement
- Marketing commits to a number of qualified leads or pipeline per month.
- Sales commits to contacting each qualified lead within a set time and a minimum number of attempts.
- Both review the numbers every week or two in a short shared meeting.

## Shared goals
Give both teams a common pipeline and revenue target. Marketing still owns its programs, sales owns closing, but success is measured on the same number.

## Feedback loops
Sales should be able to mark leads as rejected with a reason. Marketing reviews reasons monthly to adjust targeting and scoring. Win/loss interviews feed messaging.

## Revenue operations
A RevOps function owns the systems, data and process across marketing, sales and customer success. Even in small companies, assigning one person to own CRM hygiene and reporting pays off quickly.
""",
"faq": [
 ("Who should own the SLA?", "Usually the heads of marketing and sales jointly, with RevOps tracking compliance."),
 ("What is a good speed-to-lead target?", "Faster is better; many teams aim to contact inbound demo requests within an hour during business hours."),
],
},
{
"slug": "b2b-marketing-budget",
"title": "How to Plan a B2B Marketing Budget (With a Free Allocator)",
"cat": "Strategy",
"desc": "Set a budget from revenue goals, split it across people, programs and tools, and keep a test reserve.",
"mins": 6,
"takeaways": [
 "Build the budget backwards from pipeline targets and unit economics.",
 "Separate people, programs and technology lines.",
 "Hold 10–15% as a test-and-learn reserve.",
],
"body": """
Budgets are often set as a percentage of revenue and then spread across last year's line items. A better approach starts with the outcome you need.

## Start from the target
1. Revenue target for the period.
2. Share of revenue expected from marketing-sourced pipeline.
3. Average deal size and win rate to calculate opportunities needed.
4. Conversion rates to calculate leads and traffic needed.
5. Expected cost per opportunity by channel to estimate program spend.

Our pipeline reverse-planner and CAC calculator handle the arithmetic.

## Split the budget
- **People:** salaries, contractors, agencies.
- **Programs:** paid media, events, content production, sponsorships.
- **Technology:** CRM, automation, analytics, data.
- **Reserve:** experiments with new channels or offers.

## Allocate across the funnel
Balance brand and demand creation with capture. Over-investing in capture often looks efficient short-term while the pool of future buyers shrinks.

## Review cadence
Review monthly against pipeline and quarterly against revenue. Move money from underperforming programs to proven ones, and graduate successful experiments out of the reserve.
""",
"faq": [
 ("What percentage of revenue do B2B companies spend on marketing?", "It ranges widely by growth stage and market; early-stage growth companies typically invest a higher share than mature ones."),
],
},
{
"slug": "webinars-and-b2b-events",
"title": "Webinars and B2B Events: Plan, Promote and Prove ROI",
"cat": "Channels",
"desc": "Run webinars and events that generate pipeline, from topic choice to follow-up and measurement.",
"mins": 6,
"takeaways": [
 "Pick topics your buyers urgently want help with, delivered by credible speakers.",
 "Promotion and follow-up decide ROI more than the event itself.",
 "Measure opportunities and pipeline from attendees, not registrations.",
],
"body": """
Events and webinars give buyers time with experts and give you time with buyers. They are also easy to waste money on.

## Choosing the format
- **Webinars:** scalable education, good for mid-funnel nurture.
- **Roundtables:** small, peer-level discussion for target accounts.
- **Field events and dinners:** high-touch for Tier 1 accounts.
- **Trade shows:** brand presence and meeting density; require pre-booked meetings to pay off.

## Promotion plan
Start three to four weeks out. Use email to segmented lists, speaker and employee posts, partner co-promotion and retargeting. Send reminders one day and one hour before. Expect only a portion of registrants to attend live, so always offer on-demand access.

## Run of show
Open with value, not a company pitch. Keep slides visual, include live polls and Q&A, and finish with one clear next step.

## Follow-up
Within 24 hours send the recording and resources. Prioritise attendees from target accounts and those who asked questions for sales follow-up. Use our webinar ROI calculator to see what attendance and conversion rates you need.
""",
"faq": [
 ("What is the best day for a B2B webinar?", "Mid-week sessions tend to work well, but test with your audience and time zones."),
],
},
{
"slug": "product-led-growth-b2b",
"title": "Product-Led Growth for B2B: When Free Trials Beat Demos",
"cat": "Strategy",
"desc": "How PLG works, when to combine it with sales, and the metrics that signal product-qualified leads.",
"mins": 6,
"takeaways": [
 "PLG lets users experience value before talking to sales.",
 "Product-qualified leads (PQLs) are defined by in-product behaviour.",
 "Most B2B companies end up hybrid: product-led acquisition, sales-assisted expansion.",
],
"body": """
Product-led growth uses the product itself — free tiers, trials, templates — as the main way to acquire and convert customers. It works best when value is quick to experience and the product can be adopted by individuals or small teams first.

## Is PLG right for you?
Ask three questions: can a new user get value in minutes or hours without help? Is there a natural reason to invite colleagues? Is pricing low enough to start on a credit card? If the answers are mostly yes, PLG can lower acquisition costs dramatically.

## Product-qualified leads
Define activation events that predict paying — for example, connecting a data source, inviting three teammates, or hitting a usage limit. Combine with firmographic fit to flag accounts for sales outreach.

## The hybrid model
Self-serve handles small teams; sales assists when usage spreads across a larger company or procurement gets involved. Marketing's role shifts toward onboarding content, in-app education and community.

## Metrics
Time to value, activation rate, free-to-paid conversion, expansion revenue and net revenue retention.
""",
"faq": [
 ("Freemium or free trial?", "Freemium suits products with broad appeal and network effects; time-limited trials suit products where value is clear quickly and conversion urgency helps."),
],
},
]
