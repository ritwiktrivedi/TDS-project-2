titles = [
    "VS Code Version",
    "Make HTTP requests with uv",
    "Run command with npx",
    "Use Google Sheets",
    "Use Excel",
    "Use DevTools",
    "Count Wednesdays",
    "Extract CSV from a ZIP",
    "Use JSON",
    "Multi-cursor edits to convert to JSON",
    "CSS selectors",
    "Process files with different encodings",
    "Use GitHub",
    "Replace across files",
    "List files and attributes",
    "Move and rename files",
    "Compare files",
    "SQL: Ticket Sales",
    "Write documentation in Markdown",
    "Compress an image",
    "Host your portfolio on GitHub Pages",
    "Use Google Colab",
    "Use an Image Library in Google Colab",
    "Deploy a Python API to Vercel",
    "Create a GitHub Action",
    "Push an image to Docker Hub",
    "Write a FastAPI server to serve data",
    "Run a local LLM with Llamafile",
    "LLM Sentiment Analysis",
    "LLM Token Cost",
    "Generate addresses with LLMs",
    "LLM Vision",
    "LLM Embeddings",
    "Embedding Similarity",
    "Vector Databases",
    "Function Calling",
    "Get an LLM to say Yes",
    "Import HTML to Google Sheets",
    "Scrape IMDb movies",
    "Wikipedia Outline",
    "Scrape the BBC Weather API",
    "Find the bounding box of a city",
    "Search Hacker News",
    "Find newest GitHub user",
    "Create a Scheduled GitHub Action",
    "Extract tables from PDF",
    "Convert a PDF to Markdown",
    "Clean up Excel sales data",
    "Clean up student marks",
    "Apache log requests",
    "Apache log downloads",
    "Clean up sales data",
    "Parse partial JSON",
    "Extract nested JSON keys",
    "DuckDB: Social Media Interactions",
    "Transcribe a YouTube video",
    "Reconstruct an image",
]

questions = [
    """Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below.
    What is the output of code -s?""",
    """Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL.
    Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 23f2005217@ds.study.iitm.ac.in
    What is the JSON output of the command? (Paste only the JSON body, not the headers)""",
    """Let's make sure you know how to use npx and prettier.
    Download . In the directory where you downloaded it, make sure it is called README.md, and run npx -y prettier@3.4.2 README.md | sha256sum.
    What is the output of the command?""",
    """Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel)
    =SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 15, 12), 1, 10))
    What is the result?""",
    """Let's make sure you can write formulas in Excel. Type this formula into Excel.
    Note: This will ONLY work in Office 365.
    =SUM(TAKE(SORTBY({13,12,0,14,2,12,9,15,1,7,3,10,9,15,2,0}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 9))
    What is the result?
    Note: If you get #NAME? you have the wrong version of Excel. Find a friend for whom this works.""",
    """Just above this paragraph, there's a hidden input with a secret value.
    What is the value in the hidden input?""",
    """How many Wednesdays are there in the date range 1990-04-08 to 2008-09-29?
    The dates are in the year-month-day format. Include both the start and end date in your count. You can do this using any tool (e.g. Excel, Python, JavaScript, manually).""",
    """Download and unzip file  which has a single extract.csv file inside.
    What is the value in the "answer" column of the CSV file?""",
    """Let's make sure you know how to use JSON. Sort this JSON array of objects by the value of the age field. In case of a tie, sort by the name field. Paste the resulting JSON below without any spaces or newlines.
    [{"name":"Alice","age":60},{"name":"Bob","age":77},{"name":"Charlie","age":55},{"name":"David","age":15},{"name":"Emma","age":2},{"name":"Frank","age":19},{"name":"Grace","age":97},{"name":"Henry","age":67},{"name":"Ivy","age":52},{"name":"Jack","age":59},{"name":"Karen","age":91},{"name":"Liam","age":76},{"name":"Mary","age":16},{"name":"Nora","age":34},{"name":"Oscar","age":0},{"name":"Paul","age":30}]
    Sorted JSON:""",
    """Download  and use multi-cursors and convert it into a single JSON object, where key=value pairs are converted into {key: value, key: value, ...}.
    What's the result when you paste the JSON at tools-in-data-science.pages.dev/jsonhash and click the Hash button?""",
    """Let's make sure you know how to select elements using CSS selectors. Find all <div>s having a foo class in the hidden element below. What's the sum of their data-value attributes?
    Sum of data-value attributes:""",
    """Download and process the files in  which contains three files with different encodings:
    data1.csv: CSV file encoded in CP-1252
    data2.csv: CSV file encoded in UTF-8
    data3.txt: Tab-separated file encoded in UTF-16
    Each file has 2 columns: symbol and value. Sum up all the values where the symbol matches ‚ OR ˆ OR ‡ across all three files.
    What is the sum of all values associated with these symbols?""",
    """Let's make sure you know how to use GitHub. Create a GitHub account if you don't have one. Create a new public repository. Commit a single JSON file called email.json with the value {"email": "23f2005217@ds.study.iitm.ac.in"} and push it.
    Enter the raw Github URL of email.json so we can verify it. (It might look like https://raw.githubusercontent.com/[GITHUB ID]/[REPO NAME]/main/email.json.)""",
    """Download  and unzip it into a new folder, then replace all "IITM" (in upper, lower, or mixed case) with "IIT Madras" in all files. Leave everything as-is - don't change the line endings.
    What does running cat * | sha256sum in that folder show in bash?""",
    """Download  and extract it. Use ls with options to list all files in the folder along with their date and file size.
    What's the total size of all files at least 4297 bytes large and modified on or after Thu, 7 Oct, 2004, 11:03 am IST?
    Don't copy from inside the ZIP file or use Windows Explorer to unzip. That destroys the timestamps. Extract using unzip, 7-Zip or similar utilities and check the timestamps.""",
    """Download  and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt.
    What does running grep . * | LC_ALL=C sort | sha256sum in bash on that folder show?""",
    """Download  and extract it. It has 2 nearly identical files, a.txt and b.txt, with the same number of lines.
    How many lines are different between a.txt and b.txt?""",
    """There is a tickets table in a SQLite database that has columns type, units, and price. Each row is a customer bid for a concert ticket.
    type	units	price
    gold	802	1.42
    Silver	531	1.24
    Silver	301	0.85
    GOLD	916	0.78
    bronze	152	0.91
    ...
    What is the total sales of all the items in the "Gold" ticket type? Write SQL to calculate it.
    Get all rows where the Type is "Gold". Ignore spaces and treat mis-spellings like GOLD, gold, etc. as "Gold". Calculate the sales as Units * Price, and sum them up.""",
    """ Write documentation in Markdown for an **imaginary** analysis of the number of steps you walked each day for a week, comparing over time and with friends. The Markdown must include:
Top-Level Heading: At least 1 heading at level 1, e.g., # Introduction
Subheadings: At least 1 heading at level 2, e.g., ## Methodology
Bold Text: At least 1 instance of bold text, e.g., **important**
Italic Text: At least 1 instance of italic text, e.g., *note*
Inline Code: At least 1 instance of inline code, e.g., sample_code
Code Block: At least 1 instance of a fenced code block, e.g.
print("Hello World")
Bulleted List: At least 1 instance of a bulleted list, e.g., - Item
Numbered List: At least 1 instance of a numbered list, e.g., 1. Step One
Table: At least 1 instance of a table, e.g., | Column A | Column B |
Hyperlink: At least 1 instance of a hyperlink, e.g., [Text](https://example.com)
Image: At least 1 instance of an image, e.g., ![Alt Text](https://example.com/image.jpg)
Blockquote: At least 1 instance of a blockquote, e.g., > This is a quote
Enter your Markdown here:""",
    """Download the image below and compress it losslessly to an image that is less than 1,500 bytes.
By losslessly, we mean that every pixel in the new image should be identical to the original image.
Upload your losslessly compressed image (less than 1,500 bytes)
    """,
    """ Publish a page using GitHub Pages that showcases your work. Ensure that your email address 23f2005217@ds.study.iitm.ac.in is in the page's HTML.
GitHub pages are served via CloudFlare which obfuscates emails. So, wrap your email address inside a:
<!--email_off-->23f2005217@ds.study.iitm.ac.in<!--/email_off-->
What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/
If a recent change that's not reflected, add ?v=1, ?v=2 to the URL to bust the cache.
    """,
    """ Let's make sure you can access Google Colab. Run this program on Google Colab, allowing all required access to your email ID: 23f2005217@ds.study.iitm.ac.in.
import hashlib
import requests
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
creds = GoogleCredentials.get_application_default()
token = creds.get_access_token().access_token
response = requests.get(
  "https://www.googleapis.com/oauth2/v1/userinfo",
  params={"alt": "json"},
  headers={"Authorization": f"Bearer {token}"}
)
email = response.json()["email"]
hashlib.sha256(f"{email} {creds.token_expiry.year}".encode()).hexdigest()[-5:]
What is the result? (It should be a 5-character string)
    """,
    """
Download this image. Create a new Google Colab notebook and run this code (after fixing a mistake in it) to calculate the number of pixels with a certain minimum brightness:
import numpy as np
from PIL import Image
from google.colab import files
import colorsys
# There is a mistake in the line below. Fix it
image = Image.open(list(files.upload().keys)[0])
rgb = np.array(image) / 255.0
lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb)
light_pixels = np.sum(lightness > 0.467)
print(f'Number of pixels with lightness > 0.467: {light_pixels}')
What is the result? (It should be a number)
    """,
    """ Download this  which has the marks of 100 imaginary students.
Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api?name=X&name=Y is made, it returns a JSON response with the marks of the names X and Y in the same order, like this:
{ "marks": [10, 20] }
Make sure you enable CORS to allow GET requests from any origin.
What is the Vercel URL? It should look like: https://your-app.vercel.app/api """,
    """ Create a GitHub action on one of your GitHub repositories. Make sure one of the steps in the action has a name that contains your email address 23f2005217@ds.study.iitm.ac.in. For example:
jobs:
  test:
    steps:
      - name: 23f2005217@ds.study.iitm.ac.in
        run: echo "Hello, world!"
Trigger the action and make sure it is the most recent action.
What is your repository URL? It will look like: https://github.com/USER/REPO
    """,
    """
    Create and push an image to Docker Hub. Add a tag named 23f2005217 to the image.
What is the Docker image URL? It should look like: https://hub.docker.com/repository/docker/$USER/$REPO/general """,
    """ Download . This file has 2-columns:
studentId: A unique identifier for each student, e.g. 1, 2, 3, ...
class: The class (including section) of the student, e.g. 1A, 1B, ... 12A, 12B, ... 12Z
Write a FastAPI server that serves this data. For example, /api should return all students data (in the same row and column order as the CSV file) as a JSON like this:
{
  "students": [
    {
      "studentId": 1,
      "class": "1A"
    },
    {
      "studentId": 2,
      "class": "1B"
    }, ...
  ]
}
If the URL has a query parameter class, it should return only students in those classes. For example, /api?class=1A should return only students in class 1A. /api?class=1A&class=1B should return only students in class 1A and 1B. There may be any number of classes specified. Return students in the same order as they appear in the CSV file (not the order of the classes).
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api
We'll check by sending a request to this URL with ?class=... added and check if the response matches the data.
    """,
    """ Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6_K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
   """,
    """
   DataSentinel Inc. is a tech company specializing in building advanced natural language processing (NLP) solutions. Their latest project involves integrating an AI-powered sentiment analysis module into an internal monitoring dashboard. The goal is to automatically classify large volumes of unstructured feedback and text data from various sources as either GOOD, BAD, or NEUTRAL. As part of the quality assurance process, the development team needs to test the integration with a series of sample inputs—even ones that may not represent coherent text—to ensure that the system routes and processes the data correctly.
Before rolling out the live system, the team creates a test harness using Python. The harness employs the httpx library to send POST requests to OpenAI's API. For this proof-of-concept, the team uses the dummy model gpt-4o-mini along with a dummy API key in the Authorization header to simulate real API calls.
One of the test cases involves sending a sample piece of meaningless text:
gH  Iee4XZdygi HyZ7p8  vH6F8i yxKpn he Dou IH41kL
Write a Python program that uses httpx to send a POST request to OpenAI's API to analyze the sentiment of this (meaningless) text into GOOD, BAD or NEUTRAL. Specifically:
Make sure you pass an Authorization header with dummy API key.
Use gpt-4o-mini as the model.
The first message must be a system message asking the LLM to analyze the sentiment of the text. Make sure you mention GOOD, BAD, or NEUTRAL as the categories.
The second message must be exactly the text contained above.
This test is crucial for DataSentinel Inc. as it validates both the API integration and the correctness of message formatting in a controlled environment. Once verified, the same mechanism will be used to process genuine customer feedback, ensuring that the sentiment analysis module reliably categorizes data as GOOD, BAD, or NEUTRAL. This reliability is essential for maintaining high operational standards and swift response times in real-world applications.
Note: This uses a dummy httpx library, not the real one. You can only use:
response = httpx.get(url, **kwargs)
response = httpx.post(url, json=None, **kwargs)
response.raise_for_status()
response.json()
Code
   """,
    """
   LexiSolve Inc. is a startup that delivers a conversational AI platform to enterprise clients. The system leverages OpenAI’s language models to power a variety of customer service, sentiment analysis, and data extraction features. Because pricing for these models is based on the number of tokens processed—and strict token limits apply—accurate token accounting is critical for managing costs and ensuring system stability.
To optimize operational costs and prevent unexpected API overages, the engineering team at LexiSolve has developed an internal diagnostic tool that simulates and measures token usage for typical prompts sent to the language model.
One specific test case an understanding of text tokenization. Your task is to generate data for that test case.
Specifically, when you make a request to OpenAI's GPT-4o-Mini with just this user message:
List only the valid English words from these: zgnx, LtegJz, a0c0r8KWZq, tbRe, Cfwws, W77TdS4HdK, latxT, sOZHlHzki, 1oRa4bY6pE, RmDJAZgG, I48IrlPO, rm1One6gXM, oJ, vQigOVQyX, lXR, z3fMX, nAazquvtnV, lq, OAAYLKCL, ph8IZ7nhwN, 03G6Ac, Ct, 9pQfGKG, 01yOGR5, eWiUNS95y, CtLB26ICG8, 6oY8ZjXO7u, htZZM4T, yVxmO077K, C, Rfvmqe
... how many input tokens does it use up?
Number of tokens:
Remember: indicating that this is a user message takes up a few extra tokens. You actually need to make the request to get the answer.
   """,
    """
   RapidRoute Solutions is a logistics and delivery company that relies on accurate and standardized address data to optimize package routing. Recently, they encountered challenges with manually collecting and verifying new addresses for testing their planning software. To overcome this, the company decided to create an automated address generator using a language model, which would provide realistic, standardized U.S. addresses that could be directly integrated into their system.
The engineering team at RapidRoute is tasked with designing a service that uses OpenAI's GPT-4o-Mini model to generate fake but plausible address data. The addresses must follow a strict format, which is critical for downstream processes such as geocoding, routing, and verification against customer databases. For consistency and validation, the development team requires that the addresses be returned as structured JSON data with no additional properties that could confuse their parsers.
As part of the integration process, you need to write the body of the request to an OpenAI chat completion call that:
Uses model gpt-4o-mini
Has a system message: Respond in JSON
Has a user message: Generate 10 random addresses in the US
Uses structured outputs to respond with an object addresses which is an array of objects with required fields: street (string) apartment (string) zip (number) .
Sets additionalProperties to false to prevent additional properties.
Note that you don't need to run the request or use an API key; your task is simply to write the correct JSON body.
What is the JSON body we should send to https://api.openai.com/v1/chat/completions for this? (No need to run it or to use an API key. Just write the body of the request below.)
There's no answer box above. Figure out how to enable it. That's part of the test.
   """,
    """
   Acme Global Solutions manages hundreds of invoices from vendors every month. To streamline their accounts payable process, the company is developing an automated document processing system. This system uses a computer vision model to extract useful text from scanned invoice images. Critical pieces of data such as vendor email addresses, invoice or transaction numbers, and other details are embedded within these documents.
Your team is tasked with integrating OpenAI's vision model into the invoice processing workflow. The chosen model, gpt-4o-mini, is capable of analyzing both text and image inputs simultaneously. When an invoice is received—for example, an invoice image may contain a vendor email like alice.brown@acmeglobal.com and a transaction number such as 34921. The system needs to extract all embedded text to automatically populate the vendor management system.
The automated process will send a POST request to OpenAI's API with two inputs in a single user message:
Text: A simple instruction "Extract text from this image."
Image URL: A base64 URL representing the invoice image that might include the email and the transaction number among other details.
Here is an example invoice image:
Write just the JSON body (not the URL, nor headers) for the POST request that sends these two pieces of content (text and image URL) to the OpenAI API endpoint.
Use gpt-4o-mini as the model.
Send a single user message to the model that has a text and an image_url content (in that order).
The text content should be Extract text from this image.
Send the image_url as a base64 URL of the image above. CAREFUL: Do not modify the image.
Write your JSON body here:
   """,
    """
    SecurePay, a leading fintech startup, has implemented an innovative feature to detect and prevent fraudulent activities in real time. As part of its security suite, the system analyzes personalized transaction messages by converting them into embeddings. These embeddings are compared against known patterns of legitimate and fraudulent messages to flag unusual activity.
Imagine you are working on the SecurePay team as a junior developer tasked with integrating the text embeddings feature into the fraud detection module. When a user initiates a transaction, the system sends a personalized verification message to the user's registered email address. This message includes the user's email address and a unique transaction code (a randomly generated number). Here are 2 verification messages:
Dear user, please verify your transaction code 65889 sent to 23f2005217@ds.study.iitm.ac.in
Dear user, please verify your transaction code 42512 sent to 23f2005217@ds.study.iitm.ac.in
The goal is to capture this message, convert it into a meaningful embedding using OpenAI's text-embedding-3-small model, and subsequently use the embedding in a machine learning model to detect anomalies.
Your task is to write the JSON body for a POST request that will be sent to the OpenAI API endpoint to obtain the text embedding for the 2 given personalized transaction verification messages above. This will be sent to the endpoint https://api.openai.com/v1/embeddings.
Write your JSON body here:
    """,
    """
    ShopSmart is an online retail platform that places a high value on customer feedback. Each month, the company receives hundreds of comments from shoppers regarding product quality, delivery speed, customer service, and more. To automatically understand and cluster this feedback, ShopSmart's data science team uses text embeddings to capture the semantic meaning behind each comment.
As part of a pilot project, ShopSmart has curated a collection of 25 feedback phrases that represent a variety of customer sentiments. Examples of these phrases include comments like “Fast shipping and great service,” “Product quality could be improved,” “Excellent packaging,” and so on. Due to limited processing capacity during initial testing, you have been tasked with determine which pair(s) of 5 of these phrases are most similar to each other. This similarity analysis will help in grouping similar feedback to enhance the company’s understanding of recurring customer issues.
ShopSmart has written a Python program that has the 5 phrases and their embeddings as an array of floats. It looks like this:
embeddings = {"Customer service resolved my issue quickly.":[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136],"The price is reasonable for the quality.":[0.056810032576322556,0.0005139651475474238,-0.3013401925563812,-0.030993768945336342,0.15447008609771729,-0.14202508330345154,-0.057095032185316086,0.24548014998435974,0.014820008538663387,-0.15903009474277496,0.11884506791830063,0.12844008207321167,-0.29108017683029175,0.10811006277799606,0.2506101429462433,0.07205754518508911,-0.07718754559755325,-0.19703011214733124,-0.1409800797700882,0.12597008049488068,0.053912531584501266,0.17983511090278625,-0.0464550256729126,-0.08806505054235458,0.04391377419233322,-0.0863550528883934,0.10041505843400955,-0.15637008845806122,0.014499383978545666,-0.1735651046037674,0.02842876687645912,-0.13794007897377014,0.06996753811836243,-0.3663202226161957,-0.11001006513834,-0.05728503316640854,-0.032323770225048065,-0.028405016288161278,0.2435801476240158,-0.23522013425827026,-0.008977505378425121,0.006964691448956728,-0.04856877774000168,-0.09557005763053894,-0.08383754640817642,0.007558442186564207,0.08060754835605621,0.20596012473106384,-0.06901754438877106,-0.1173250675201416],"The payment process was secure and efficient.":[-0.04701301082968712,-0.20167900621891022,-0.22099372744560242,-0.05536692962050438,0.03149012476205826,0.049234796315431595,-0.02104772813618183,0.1948062777519226,0.004417652729898691,-0.11180031299591064,0.25831976532936096,-0.1503705382347107,-0.14669717848300934,-0.15866521000862122,0.07601473480463028,-0.03744451329112053,-0.1256050169467926,-0.004232503939419985,-0.19717617332935333,-0.07204513996839523,0.07216363400220871,0.23426520824432373,0.005728506948798895,-0.08347994089126587,-0.09248558431863785,-0.16150909662246704,-0.10895642638206482,-0.3507460951805115,-0.1641159951686859,-0.1695667803287506,0.21696490049362183,-0.1385210007429123,0.196346715092659,-0.025669043883681297,-0.07808840274810791,-0.0023291732650250196,-0.03386003151535988,0.14717115461826324,0.06078808754682541,-0.0358448289334774,-0.1290413737297058,0.17335861921310425,-0.08033981174230576,0.1285673975944519,-0.040229152888059616,0.11511818319559097,0.10747523605823517,-0.3336827754974365,0.09313730895519257,-0.002255113562569022],"The product description matched the item.":[-0.1778346747159958,0.015024187043309212,-0.48206639289855957,-0.025718823075294495,-0.016542760655283928,-0.14746320247650146,0.08109830319881439,0.14048422873020172,-0.06655876338481903,-0.014773784205317497,-0.022116249427199364,-0.09764105826616287,0.0843939259648323,-0.21104943752288818,0.05166381597518921,0.24917533993721008,-0.04652651399374008,-0.03644577041268349,-0.3680764436721802,0.14306902885437012,0.19114643335342407,0.09570245444774628,0.12562158703804016,0.04345705732703209,-0.05486251413822174,-0.1628427952528,-0.04840049892663956,-0.08885271847248077,0.20407046377658844,0.14849711954593658,0.017899783328175545,-0.17020949721336365,0.13428069651126862,-0.2234565168619156,0.00254037999548018,0.044975630939006805,0.14862637221813202,-0.06594487279653549,0.15728546679019928,0.006142953876405954,-0.207172229886055,-0.020533055067062378,-0.05463634431362152,0.09492701292037964,-0.03237469866871834,0.06752806901931763,-0.08736645430326462,0.08297228813171387,-0.036898110061883926,-0.045621830970048904],"There was a delay in delivery.":[0.14162038266658783,0.133348748087883,-0.04399004951119423,-0.10571397840976715,-0.12250789999961853,0.039634909480810165,0.010010556317865849,0.028512069955468178,-0.011859141290187836,-0.11755745112895966,-0.011624150909483433,-0.05646016448736191,-0.07576064020395279,-0.26845210790634155,-0.060000672936439514,-0.07820453494787216,0.04865850880742073,-0.1497666984796524,-0.28549668192863464,0.24902629852294922,0.0857868641614914,0.053608957678079605,0.24727170169353485,0.0352797694504261,-0.16643528640270233,-0.060595981776714325,0.1174321249127388,-0.17596019804477692,0.04847051948308945,0.14939071238040924,0.12282121926546097,-0.10019955784082413,0.23448826372623444,-0.22408606112003326,-0.16217415034770966,0.1520226001739502,-0.0021325305569916964,0.19927117228507996,0.15578243136405945,0.1492653787136078,-0.26845210790634155,-0.1048993468284607,-0.11906138807535172,-0.012994923628866673,-0.07444469630718231,0.22797122597694397,-0.05166637524962425,-0.07469535619020462,-0.009728568606078625,0.23611752688884735]}
Your task is to write a Python function most_similar(embeddings) that will calculate the cosine similarity between each pair of these embeddings and return the pair that has the highest similarity. The result should be a tuple of the two phrases that are most similar.
Write your Python code here:
import numpy
def most_similar(embeddings):
    # Your code here
    return (phrase1, phrase2)
    """,
    """
    InfoCore Solutions is a technology consulting firm that maintains an extensive internal knowledge base of technical documents, project reports, and case studies. Employees frequently search through these documents to answer client questions quickly or gain insights for ongoing projects. However, due to the sheer volume of documentation, traditional keyword-based search often returns too many irrelevant results.
To address this issue, InfoCore's data science team decides to integrate a semantic search feature into their internal portal. This feature uses text embeddings to capture the contextual meaning of both the documents and the user's query. The documents are pre-embedded, and when an employee submits a search query, the system computes the similarity between the query's embedding and those of the documents. The API then returns a ranked list of document identifiers based on similarity.
Imagine you are an engineer on the InfoCore team. Your task is to build a FastAPI POST endpoint that accepts an array of docs and query string via a JSON body. The endpoint is structured as follows:
POST /similarity
{
  "docs": ["Contents of document 1", "Contents of document 2", "Contents of document 3", ...],
  "query": "Your query string"
}
Service Flow:
Request Payload: The client sends a POST request with a JSON body containing:
docs: An array of document texts from the internal knowledge base.
query: A string representing the user's search query.
Embedding Generation: For each document in the docs array and for the query string, the API computes a text embedding using text-embedding-3-small.
Similarity Computation: The API then calculates the cosine similarity between the query embedding and each document embedding. This allows the service to determine which documents best match the intent of the query.
Response Structure: After ranking the documents by their similarity scores, the API returns the identifiers (or positions) of the three most similar documents. The JSON response might look like this:
{
  "matches": ["Contents of document 3", "Contents of document 1", "Contents of document 2"]
}
Here, "Contents of document 3" is considered the closest match, followed by "Contents of document 1", then "Contents of document 2".
Make sure you enable CORS to allow OPTIONS and POST methods, perhaps allowing all origins and headers.
What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity
We'll check by sending a POST request to this URL with a JSON body containing random docs and query.
    """,
    """
    TechNova Corp. is a multinational corporation that has implemented a digital assistant to support employees with various internal tasks. The assistant can answer queries related to human resources, IT support, and administrative services. Employees use a simple web interface to enter their requests, which may include:
Checking the status of an IT support ticket.
Scheduling a meeting.
Retrieving their current expense reimbursement balance.
Requesting details about their performance bonus.
Reporting an office issue by specifying a department or issue number.
Each question is direct and templatized, containing one or more parameters such as an employee or ticket number (which might be randomized). In the backend, a FastAPI app routes each request by matching the query to one of a set of pre-defined functions. The response that the API returns is used by OpenAI to call the right function with the necessary arguments.
Pre-Defined Functions:
For this exercise, assume the following functions have been defined:
get_ticket_status(ticket_id: int)
schedule_meeting(date: str, time: str, meeting_room: str)
get_expense_balance(employee_id: int)
calculate_performance_bonus(employee_id: int, current_year: int)
report_office_issue(issue_code: int, department: str)
Each function has a specific signature, and the student’s FastAPI app should map specific queries to these functions.
Example Questions (Templatized with a Random Number):
Ticket Status:
Query: "What is the status of ticket 83742?"
→ Should map to get_ticket_status(ticket_id=83742)
Meeting Scheduling:
Query: "Schedule a meeting on 2025-02-15 at 14:00 in Room A."
→ Should map to schedule_meeting(date="2025-02-15", time="14:00", meeting_room="Room A")
Expense Reimbursement:
Query: "Show my expense balance for employee 10056."
→ Should map to get_expense_balance(employee_id=10056)
Performance Bonus Calculation:
Query: "Calculate performance bonus for employee 10056 for 2025."
→ Should map to calculate_performance_bonus(employee_id=10056, current_year=2025)
Office Issue Reporting:
Query: "Report office issue 45321 for the Facilities department."
→ Should map to report_office_issue(issue_code=45321, department="Facilities")
Task Overview:
Develop a FastAPI application that:
Exposes a GET endpoint /execute?q=... where the query parameter q contains one of the pre-templatized questions.
Analyzes the q parameter to identify which function should be called.
Extracts the parameters from the question text.
Returns a response in the following JSON format:
{ "name": "function_name", "arguments": "{ ...JSON encoded parameters... }" }
For example, the query "What is the status of ticket 83742?" should return:
{
  "name": "get_ticket_status",
  "arguments": "{\"ticket_id\": 83742}"
}
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute
We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition.
    """,
    """
    SecurePrompt Technologies is a cybersecurity firm that specializes in deploying large language models (LLMs) for sensitive enterprise applications. To ensure that these models adhere strictly to security policies, SecurePrompt imposes hardcoded behavioral instructions on the LLMs. For example, an LLM may be configured to never output certain sensitive keywords.
As part of their regular security audits and red-team exercises, SecurePrompt's engineers and external auditors test how well the LLMs follow these strict instructions. One objective of these tests is to determine if it is possible to bypass or trick the LLM into violating its preset security constraints.
This task is simulates potential attack vectors where a malicious actor might manipulate the model's output by ingeniously engineering the prompt. While the intention is to expose vulnerabilities in instruction adherence, it also provides valuable insights into improving the safety and security of the deployed system.
Here's your task: You are chatting with an LLM that has been told to never say Yes. You need to get it to say Yes.
Use your AI Proxy token when prompted.
Write a prompt that will get the LLM to say Yes.
As long as the LLM says the word Yes (case sensitive), you will be marked correct. Careful! If you get a correct answer, submit and don't change it. You may get a different answer next time.
    """,
]


import json

data = {}


def function_case(title):
    title = title.lower()
    title = title.replace(" ", "_")
    title = title.replace(":", "")
    title = title.replace("-", "_")
    title = title.replace("(", "")
    title = title.replace(")", "")
    title = title.replace("?", "")
    title = title.replace(",", "")
    return title


for i in range(len(titles)):
    if i >= len(questions):
        break
    data[function_case(titles[i])] = questions[i]

with open("questions.json", "w") as f:
    json.dump(data, f)
