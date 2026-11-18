GLOSSARY = [
("A/B testing","Comparing two versions of a page, email or ad with randomly split audiences to see which performs better on a defined metric."),
("Account-based marketing (ABM)","A strategy where marketing and sales focus coordinated, personalised efforts on a defined list of high-value target accounts."),
("Account engagement","A measure of how much activity a target company shows across all its people — visits, content, meetings — rather than per individual lead."),
("Activation rate","The share of new users or sign-ups who reach a defined first-value milestone in a product."),
("Annual contract value (ACV)","The average yearly revenue from a customer contract, excluding one-time fees."),
("Attribution","Assigning credit for conversions or revenue to the marketing touches that preceded them."),
("Average deal size","Total closed-won revenue divided by the number of deals in a period."),
("Buyer enablement","Content and tools that help buyers complete their own internal buying tasks, such as building a business case."),
("Buyer persona","A semi-fictional profile of a typical buyer role, describing goals, pains, objections and information sources."),
("Buying committee","The group of people — often five or more — who influence or approve a B2B purchase."),
("Churn rate","The share of customers or revenue lost over a period."),
("Closed-lost / closed-won","CRM stages marking deals that were lost or won."),
("Cold outreach","Unsolicited one-to-one prospecting by email, phone or social to people with no prior relationship."),
("Content syndication","Distributing your content through third-party publishers, often in exchange for leads."),
("Conversion rate","The percentage of people who take a desired action out of those who had the opportunity."),
("Cost per lead (CPL)","Program spend divided by leads generated."),
("Cost per opportunity","Program spend divided by sales opportunities created — a better efficiency metric than CPL in B2B."),
("CRM","Customer relationship management software that stores contacts, accounts, deals and activity."),
("Customer acquisition cost (CAC)","Total sales and marketing cost to win new customers, divided by the number of new customers."),
("Customer lifetime value (LTV)","Expected gross profit from a customer over the whole relationship."),
("Dark social","Sharing that happens in private channels (messages, private communities) that analytics cannot track."),
("Data enrichment","Adding firmographic, technographic or contact details to existing records from external sources."),
("Demand capture","Marketing aimed at buyers already in-market, such as search ads and review sites."),
("Demand creation","Marketing that builds awareness and preference among buyers who are not yet actively buying."),
("Demand generation","The full set of activities that create and capture interest in your offering and turn it into pipeline."),
("Firmographics","Company attributes used for targeting: industry, size, revenue, location, ownership."),
("Funnel","A model of the stages a buyer passes through from awareness to purchase."),
("Gated content","Content that requires a form submission to access."),
("Go-to-market (GTM)","The plan for how a company reaches target customers and achieves competitive advantage."),
("Ideal customer profile (ICP)","A description of the type of company that gets the most value from your product and is most valuable to you."),
("Inbound marketing","Attracting buyers with useful content and experiences so they come to you."),
("Intent data","Signals that a company or person is researching a topic, product category or competitor."),
("Lead","A person who has shared contact details or been identified as a potential buyer."),
("Lead magnet","A valuable resource offered in exchange for contact details."),
("Lead nurturing","Ongoing, relevant communication that helps leads progress toward buying."),
("Lead scoring","Assigning points to leads based on fit and behaviour to prioritise follow-up."),
("Lifecycle stage","A lead's position in the buying journey, e.g. subscriber, lead, MQL, SQL, opportunity, customer."),
("Lookalike audience","An ad audience built from people similar to an existing customer or lead list."),
("LTV:CAC ratio","Lifetime value divided by acquisition cost; a common gauge of acquisition efficiency."),
("Marketing automation","Software that automates email, scoring, segmentation and workflows."),
("Marketing mix modelling (MMM)","Statistical analysis estimating each channel's contribution to outcomes from aggregate data."),
("Marketing-qualified lead (MQL)","A lead that meets agreed fit and engagement criteria and is ready for sales review."),
("Martech","Marketing technology — the software stack marketers use."),
("Net revenue retention (NRR)","Revenue from an existing customer group after expansion, contraction and churn, as a share of starting revenue."),
("Opportunity","A qualified potential deal tracked in the CRM with an expected value and close date."),
("Payback period","Months needed for gross profit from a customer to repay the cost of acquiring them."),
("Pipeline","The total value of open sales opportunities."),
("Pipeline velocity","How fast revenue moves through pipeline: opportunities × win rate × deal size ÷ cycle length."),
("Positioning","How you define your product's category, audience and differentiation in buyers' minds."),
("Product-led growth (PLG)","A strategy where the product itself drives acquisition, conversion and expansion."),
("Product-qualified lead (PQL)","A user or account whose in-product behaviour signals buying readiness."),
("Programmatic advertising","Automated buying of digital ad inventory, often with account or audience targeting."),
("Retargeting","Showing ads to people who previously visited your site or engaged with your content."),
("Revenue operations (RevOps)","The function aligning systems, data and processes across marketing, sales and customer success."),
("Sales cycle","Time from first qualified contact to closed deal."),
("Sales enablement","Content, training and tools that help sales teams sell more effectively."),
("Sales-qualified lead (SQL)","A lead accepted by sales as worth pursuing as a potential opportunity."),
("Service-level agreement (SLA)","A written agreement between marketing and sales on lead volume and follow-up commitments."),
("Share of voice","Your brand's portion of conversation or visibility in a market versus competitors."),
("Technographics","Data on which technologies a company uses."),
("Thought leadership","Expert, original perspectives that build authority and trust."),
("Total addressable market (TAM)","The total revenue opportunity if you won every possible customer."),
("UTM parameters","Tags added to URLs (source, medium, campaign) so analytics can attribute visits."),
("Value proposition","A concise statement of the benefit you deliver and why it matters to a specific buyer."),
("Win rate","Closed-won opportunities divided by all closed opportunities."),
]

# Martech stack directory: (name, category, url, description) — descriptions are our own summaries.
STACK = [
("HubSpot","CRM & Automation","https://www.hubspot.com","All-in-one CRM with marketing, sales and service hubs; popular with SMB and mid-market teams."),
("Salesforce","CRM & Automation","https://www.salesforce.com","Enterprise CRM platform with a large ecosystem of apps and integrations."),
("Adobe Marketo Engage","CRM & Automation","https://business.adobe.com/products/marketo.html","Enterprise marketing automation for lead management, nurturing and scoring."),
("Pipedrive","CRM & Automation","https://www.pipedrive.com","Pipeline-focused CRM built for small sales teams."),
("Zoho CRM","CRM & Automation","https://www.zoho.com/crm/","Affordable CRM within a wide suite of business apps."),
("ActiveCampaign","CRM & Automation","https://www.activecampaign.com","Email and marketing automation with CRM features for growing businesses."),
("Brevo","Email","https://www.brevo.com","Email, SMS and automation platform with a generous free tier."),
("Mailchimp","Email","https://mailchimp.com","Widely used email marketing platform with templates and automation."),
("beehiiv","Email","https://www.beehiiv.com","Newsletter platform with growth and monetisation tools."),
("6sense","ABM & Intent","https://6sense.com","Revenue AI platform combining account identification, intent data and orchestration."),
("Demandbase","ABM & Intent","https://www.demandbase.com","ABM platform for account targeting, advertising and sales intelligence."),
("Bombora","ABM & Intent","https://bombora.com","Company-level intent data based on content consumption across a publisher co-op."),
("RollWorks","ABM & Intent","https://www.rollworks.com","ABM platform focused on mid-market account targeting and ads."),
("Factors.ai","ABM & Intent","https://www.factors.ai","Account identification and journey analytics for B2B marketing teams."),
("ZoomInfo","Data & Prospecting","https://www.zoominfo.com","Large B2B contact and company database with intent signals."),
("Apollo.io","Data & Prospecting","https://www.apollo.io","Sales intelligence and engagement platform with a freemium plan."),
("Lusha","Data & Prospecting","https://www.lusha.com","Contact data and prospecting tool with browser extension."),
("Cognism","Data & Prospecting","https://www.cognism.com","B2B data provider known for phone-verified mobile numbers."),
("Clay","Data & Prospecting","https://www.clay.com","Data enrichment and workflow tool that combines many data sources."),
("Hunter","Data & Prospecting","https://hunter.io","Email finder and verifier for outreach."),
("Lemlist","Sales Engagement","https://www.lemlist.com","Multichannel cold outreach with personalisation features."),
("Outreach","Sales Engagement","https://www.outreach.io","Sales execution platform for sequences, deals and forecasting."),
("Salesloft","Sales Engagement","https://www.salesloft.com","Revenue workflow platform for cadences and conversation insights."),
("Gong","Sales Engagement","https://www.gong.io","Revenue intelligence from recorded sales conversations."),
("Semrush","SEO & Content","https://www.semrush.com","SEO, content and competitive research suite."),
("Ahrefs","SEO & Content","https://ahrefs.com","SEO toolset known for backlink and keyword data."),
("Moz","SEO & Content","https://moz.com","SEO software and learning resources."),
("Google Search Console","SEO & Content","https://search.google.com/search-console","Free tool to monitor how your site performs in Google Search."),
("Clearscope","SEO & Content","https://www.clearscope.io","Content optimisation for search relevance."),
("Grammarly","SEO & Content","https://www.grammarly.com","AI writing assistant for clarity and correctness."),
("Canva","Creative","https://www.canva.com","Design platform for social graphics, decks and documents."),
("Figma","Creative","https://www.figma.com","Collaborative interface and graphic design tool."),
("Descript","Creative","https://www.descript.com","Video and podcast editing by editing text."),
("Loom","Creative","https://www.loom.com","Async screen and camera video messages."),
("Google Analytics","Analytics","https://marketingplatform.google.com/about/analytics/","Free web analytics for traffic and conversion tracking."),
("Mixpanel","Analytics","https://mixpanel.com","Product analytics for user behaviour and funnels."),
("Amplitude","Analytics","https://amplitude.com","Digital analytics platform for product and marketing teams."),
("Databox","Analytics","https://databox.com","KPI dashboards pulling data from many marketing tools."),
("Looker Studio","Analytics","https://lookerstudio.google.com","Free dashboarding and reporting tool from Google."),
("Hotjar","Analytics","https://www.hotjar.com","Heatmaps, recordings and on-site surveys."),
("LinkedIn Ads","Advertising","https://business.linkedin.com/marketing-solutions/ads","Professional-network ads with job title and company targeting."),
("Google Ads","Advertising","https://ads.google.com","Search, display and video advertising."),
("Microsoft Advertising","Advertising","https://ads.microsoft.com","Search ads on Bing with LinkedIn profile targeting options."),
("StackAdapt","Advertising","https://www.stackadapt.com","Programmatic advertising platform used for B2B campaigns."),
("Unbounce","Conversion","https://unbounce.com","Landing page builder with A/B testing."),
("Typeform","Conversion","https://www.typeform.com","Conversational forms and surveys."),
("Chili Piper","Conversion","https://www.chilipiper.com","Instant meeting booking and lead routing from forms."),
("Calendly","Conversion","https://calendly.com","Scheduling links for meetings and demos."),
("Intercom","Conversion","https://www.intercom.com","Customer messaging and AI support agent."),
("Qualified","Conversion","https://www.qualified.com","Conversational marketing and AI SDR for website visitors."),
("Webflow","Website","https://webflow.com","Visual website builder with CMS for marketing sites."),
("WordPress","Website","https://wordpress.org","Open-source CMS powering a large share of the web."),
("Zoom Webinars","Events","https://www.zoom.com/en/products/webinars/","Webinar hosting with registration and reporting."),
("Livestorm","Events","https://livestorm.co","Browser-based webinar and virtual event platform."),
("Goldcast","Events","https://www.goldcast.io","B2B event platform with content repurposing."),
("Zapier","Automation & AI","https://zapier.com","No-code automation connecting thousands of apps."),
("Make","Automation & AI","https://www.make.com","Visual automation builder for complex workflows."),
("Claude","Automation & AI","https://claude.ai","AI assistant for research, writing, analysis and coding."),
("G2","Reviews","https://www.g2.com","Business software review marketplace."),
("TrustRadius","Reviews","https://www.trustradius.com","B2B technology reviews and buyer research."),
("Capterra","Reviews","https://www.capterra.com","Software reviews and comparisons for small businesses."),
]

TEMPLATES = [
("icp-worksheet","Ideal Customer Profile (ICP) Worksheet","""Company attributes
- Industry / sub-industry:
- Employee range:
- Annual revenue range:
- Regions:
- Technologies used (must-have / nice-to-have):

Buying triggers
- Events that create urgency (funding, new leader, expansion, compliance deadline):

Pains we solve (ranked)
1.
2.
3.

Buying committee
- Economic buyer:
- Champion:
- Technical evaluator:
- Procurement / legal:

Disqualifiers
-

Evidence
- Top 10 customers matching this profile:
- Average deal size / sales cycle / win rate for this segment:"""),
("campaign-brief","Campaign Brief","""Campaign name:
Owner:                Launch date:          End date:
Objective (one metric): e.g. 40 qualified opportunities from Tier 2 manufacturing accounts
Audience: ICP segment + roles
Insight: What do they believe today and why should they change?
Core message (one sentence):
Offer / call to action:
Channels & budget:
 - Paid:
 - Owned:
 - Earned / partners:
Assets needed:
Sales enablement: talk track, email templates, follow-up SLA
Measurement: KPIs, UTM campaign name, reporting date"""),
("cold-email","Cold Email (Problem-First)","""Subject: {{Company}} + {{specific trigger}}

Hi {{First name}},

Noticed {{specific, verifiable observation — new hire, launch, job post}}.
Teams in that spot often run into {{problem}}, which usually shows up as {{symptom}}.

We helped {{similar company}} {{outcome with number}} by {{one-line how}}.

Worth a 15-minute conversation to see if it applies to {{Company}}?

{{Signature}}
P.S. If this isn't relevant, reply "no" and I won't follow up."""),
("nurture-sequence","5-Email Nurture Sequence","""Email 1 (Day 0) — Deliver the resource + one quick win
Email 2 (Day 3) — The common mistake + how to avoid it
Email 3 (Day 7) — Customer story with numbers
Email 4 (Day 12) — Tool or calculator to self-assess
Email 5 (Day 18) — Soft CTA: assessment, consultation or demo
Exit rules: book a meeting, reply, or 3 non-opens → move to monthly newsletter"""),
("marketing-sales-sla","Marketing ↔ Sales SLA","""Definitions
- MQL: fit score ≥ __ AND engagement score ≥ __
- SAL: accepted by sales within __ business hours
- SQL: discovery completed, BANT/MEDDICC criteria met

Marketing commits to: __ MQLs / month; __ $ pipeline / quarter
Sales commits to: first contact within __ hours; __ attempts over __ days; disposition logged
Review: weekly 30-min pipeline meeting; monthly rejection-reason review"""),
("utm-conventions","UTM Naming Conventions","""utm_source: platform, lowercase (linkedin, google, newsletter, partnername)
utm_medium: channel type (cpc, paid-social, email, organic-social, referral)
utm_campaign: yyyy-mm_objective_audience (2026-11_demo_mfg-tier2)
utm_content: creative or placement (video-a, carousel-b, header-link)
utm_term: keyword or audience segment (optional)
Rules: lowercase, hyphens not spaces, never tag internal links."""),
("webinar-run-of-show","Webinar Run of Show (45 min)","""-0:15  Speakers join, tech check, polls loaded
0:00   Welcome, housekeeping, why this matters (2 min)
0:02   Speaker intros (2 min)
0:04   Core content part 1 + poll (12 min)
0:16   Core content part 2 + example (12 min)
0:28   Live Q&A (12 min)
0:40   One clear next step + resource link (3 min)
0:43   Thanks, recording note
+24h   Recording + slides + CTA email; sales follow-up list"""),
("case-study-outline","Case Study Outline","""Headline: {{Customer}} achieved {{result}} in {{timeframe}}
Snapshot box: industry, size, region, products used, top 3 results
The challenge: situation, stakes, what they tried before
Why they chose us: criteria and decision process
The solution: implementation, timeline, teams involved
Results: numbers, before/after, quote from champion
What's next: expansion plans
CTA: talk to us about a similar result"""),
]

NEWS_SOURCES = [
("HubSpot Marketing Blog","https://blog.hubspot.com/marketing/rss.xml"),
("Content Marketing Institute","https://contentmarketinginstitute.com/feed/"),
("chiefmartec","https://chiefmartec.com/feed/"),
("MarTech","https://martech.org/feed/"),
("Search Engine Land","https://searchengineland.com/feed"),
("Moz Blog","https://moz.com/posts/rss/blog"),
("Ahrefs Blog","https://ahrefs.com/blog/feed/"),
("Martech Zone","https://martech.zone/feed/"),
("MarketingProfs","https://www.marketingprofs.com/rss/articles"),
("Search Engine Journal","https://www.searchenginejournal.com/feed/"),
]

YOUTUBE_HANDLES = ["HubSpotMarketing","Semrush","AhrefsCom","Moz","GoogleSearchCentral","LinkedInMarketing","ContentMarketingInstitute","neilpatel","Salesforce","GongIO"]
