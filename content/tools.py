# Interactive tools. inputs: (id, label, type, default, extra) where type in number|text|select|textarea; for select extra = list of (value,label)
TOOLS = [
{
"slug":"cac-payback-calculator","title":"CAC & Payback Period Calculator","icon":"⏱",
"desc":"Calculate customer acquisition cost and how many months it takes to earn it back.",
"inputs":[("spend","Sales + marketing spend in the period ($)","number",60000,None),("customers","New customers won in the period","number",20,None),("arpa","Average revenue per account per month ($)","number",900,None),("margin","Gross margin (%)","number",80,None)],
"about":"""
## How it works
**Customer acquisition cost (CAC)** is your total sales and marketing spend divided by the number of new customers won in the same period. **Payback period** is CAC divided by the monthly gross profit a customer generates (monthly revenue × gross margin).

## How to read the result
Shorter payback means cash comes back faster and growth can be funded more easily. Many subscription businesses aim to recover CAC within roughly a year; enterprise sellers with high retention can tolerate longer paybacks. Compare your number against your own history and cash runway rather than a universal benchmark.

## Improve it
- Raise conversion rates at each funnel stage so the same spend wins more customers.
- Shift budget toward channels with the lowest cost per opportunity.
- Increase average revenue per account with packaging or annual plans.
"""},
{
"slug":"ltv-cac-calculator","title":"LTV:CAC Ratio Calculator","icon":"⚖",
"desc":"Estimate customer lifetime value and compare it with acquisition cost.",
"inputs":[("arpa","Average revenue per account per month ($)","number",900,None),("margin","Gross margin (%)","number",80,None),("churn","Monthly customer churn (%)","number",2,None),("cac","Customer acquisition cost ($)","number",3000,None)],
"about":"""
## The formula
Lifetime value (LTV) = monthly revenue per account × gross margin ÷ monthly churn rate. The LTV:CAC ratio divides that value by what it costs to acquire the customer.

## Interpreting the ratio
A ratio around 3:1 is a widely used rule of thumb for healthy subscription businesses. Well below that suggests acquisition is too expensive or retention too weak; far above it can mean you are under-investing in growth.

## Caveats
Small changes in churn make large changes in LTV, so use realistic, cohort-based churn. For young companies, cap the lifetime (e.g. five years) to avoid inflated values.
"""},
{
"slug":"marketing-roi-calculator","title":"Marketing ROI Calculator","icon":"📈",
"desc":"Measure the return on a campaign or channel using gross profit, not just revenue.",
"inputs":[("revenue","Revenue attributed to the campaign ($)","number",120000,None),("margin","Gross margin (%)","number",75,None),("cost","Total campaign cost incl. people & tools ($)","number",30000,None)],
"about":"""
## The formula
Marketing ROI = (gross profit from attributed revenue − marketing cost) ÷ marketing cost × 100. Using gross profit instead of revenue avoids overstating returns.

## Getting attribution right
ROI is only as good as the revenue you credit to the campaign. Use consistent UTM tags, CRM campaign association and a self-reported "How did you hear about us?" field. For long B2B cycles, measure over a window that matches your sales cycle.
"""},
{
"slug":"pipeline-reverse-planner","title":"Pipeline Reverse-Planner","icon":"🎯",
"desc":"Work backwards from a revenue goal to the deals, opportunities, SQLs, MQLs and leads you need.",
"inputs":[("target","New revenue target ($)","number",1000000,None),("deal","Average deal size ($)","number",25000,None),("win","Opportunity win rate (%)","number",25,None),("sqlopp","SQL → opportunity rate (%)","number",60,None),("mqlsql","MQL → SQL rate (%)","number",35,None),("leadmql","Lead → MQL rate (%)","number",25,None)],
"about":"""
## Why plan in reverse
Most teams set lead targets by habit. Reverse-planning starts from revenue and uses your real conversion rates to show exactly how much top-of-funnel activity is required — and which conversion rate would give the biggest lift if improved.

## Use your own numbers
Pull conversion rates from the last two or three quarters in your CRM. If a stage has little data, use a conservative estimate and revisit monthly.
"""},
{
"slug":"lead-scoring-builder","title":"Lead Scoring Builder","icon":"🧮",
"desc":"Score a lead on fit and engagement and see whether it should go to sales.",
"inputs":[("title","Job level","select","dir",[("cx","C-level / VP (+20)"),("dir","Director (+15)"),("mgr","Manager (+8)"),("ic","Individual contributor (+3)"),("student","Student / unrelated (−15)")]),
 ("size","Company size vs ICP","select","in",[("in","Inside sweet spot (+15)"),("near","Close to ICP (+7)"),("out","Outside ICP (−10)")]),
 ("email","Email domain","select","work",[("work","Business domain (+5)"),("personal","Personal domain (−10)"),("comp","Competitor (−100)")]),
 ("pricing","Visited pricing page","select","no",[("yes","Yes (+10)"),("no","No (0)")]),
 ("demo","Requested demo / contact","select","no",[("yes","Yes (+40)"),("no","No (0)")]),
 ("webinar","Attended webinar / event","select","no",[("yes","Yes (+10)"),("no","No (0)")]),
 ("clicks","Email clicks in last 14 days","number",2,None),
 ("days","Days since last activity","number",5,None),
 ("threshold","MQL threshold (points)","number",50,None)],
"about":"""
## How the score is built
Fit points reflect who the lead is; engagement points reflect what they have done. Email clicks add 3 points each (capped at 15). Engagement is halved if the last activity was more than 30 days ago — a simple decay rule that stops old activity inflating scores.

## Calibrate with sales
Agree the MQL threshold with sales and review acceptance rates monthly. If sales rejects many MQLs, raise fit weights or the threshold.
"""},
{
"slug":"marketing-budget-allocator","title":"B2B Marketing Budget Allocator","icon":"💰",
"desc":"Split an annual budget across people, programs, technology and a test reserve by growth stage.",
"inputs":[("budget","Annual marketing budget ($)","number",500000,None),("stage","Company stage","select","growth",[("early","Early stage (finding fit)"),("growth","Growth (scaling channels)"),("mature","Mature (efficiency & brand)")])],
"about":"""
## The splits
These starting allocations reflect common patterns: early-stage teams lean on people and experiments; growth-stage teams pour more into programs; mature teams invest more in brand and technology. Treat them as a starting point to adjust with your own pipeline data.

## Keep a reserve
A 10–15% test reserve lets you try new channels without cutting proven programs.
"""},
{
"slug":"utm-builder","title":"UTM Campaign URL Builder","icon":"🔗",
"desc":"Build clean, consistent UTM-tagged links for accurate attribution.",
"inputs":[("url","Destination URL","text","https://example.com/landing",None),("source","utm_source (e.g. linkedin)","text","linkedin",None),("medium","utm_medium (e.g. paid-social)","text","paid-social",None),("campaign","utm_campaign (e.g. 2026-11_demo_mfg)","text","2026-11_demo_mfg",None),("content","utm_content (optional)","text","",None),("term","utm_term (optional)","text","",None)],
"about":"""
## Naming rules that save hours later
Use lowercase, hyphens instead of spaces and a fixed campaign pattern such as yyyy-mm_objective_audience. Never tag internal links on your own site — it overwrites the original source. See our UTM conventions template for a full standard.
"""},
{
"slug":"abm-account-tiering","title":"ABM Account Tiering Calculator","icon":"🏢",
"desc":"Score an account on fit, intent and engagement and assign it to a 1:1, 1:few or 1:many tier.",
"inputs":[("fit","ICP fit (1–10)","number",8,None),("intent","Intent signals (1–10)","number",6,None),("engage","Engagement with you (1–10)","number",4,None),("acv","Potential annual contract value ($)","number",60000,None)],
"about":"""
## The model
Weighted score = fit × 50% + intent × 30% + engagement × 20%, scaled to 100. Accounts with high scores and high potential value go to Tier 1 (fully custom), mid scores to Tier 2 (clustered personalisation) and the rest to Tier 3 (programmatic). Read our ABM playbook for plays at each tier.
"""},
{
"slug":"email-subject-line-checker","title":"Email Subject Line Checker","icon":"✉",
"desc":"Check length, spam-trigger words, personalisation and clarity of a B2B email subject line.",
"inputs":[("subject","Subject line","text","Quick idea for {{Company}}'s Q1 pipeline",None)],
"about":"""
## What we check
Length (roughly 30–50 characters displays fully on most phones), all-caps words, excessive punctuation, common spam-trigger words, personalisation tokens, numbers and question format. The score is a guide — always A/B test with your own audience.
"""},
{
"slug":"webinar-roi-calculator","title":"Webinar ROI Calculator","icon":"🎥",
"desc":"Estimate pipeline and revenue from a webinar based on registrations, attendance and conversion.",
"inputs":[("cost","Total webinar cost ($)","number",8000,None),("reg","Registrants","number",400,None),("attend","Live + on-demand attendance rate (%)","number",45,None),("opp","Attendee → opportunity rate (%)","number",4,None),("deal","Average deal size ($)","number",20000,None),("win","Win rate (%)","number",25,None)],
"about":"""
## Reading the numbers
Webinars rarely close deals on their own; they create opportunities that sales converts later. Track attendees from target accounts separately and follow up within 24 hours — follow-up speed has a large effect on the attendee-to-opportunity rate.
"""},
]
