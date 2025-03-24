import requests
import zipfile
import io

url = "http://127.0.0.1:5000"
questions = [
    {
        "files": None,
        "question": """Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL.\n    Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 23f2005217@ds.study.iitm.ac.in\n    What is the JSON output of the command? (Paste only the JSON body, not the headers)""",
    },
    {
        "files": "",
        "question": 'Peak Usage Analysis for Regional Content\n    s-anand.net is a personal website that had region-specific music content. One of the site\'s key sections is telugu, which hosts music files and is especially popular among the local audience. The website is powered by robust Apache web servers that record detailed access logs. These logs are essential for understanding user behavior, server load, and content engagement.\n\n    The author noticed unusual traffic patterns during weekend evenings. To better tailor their content and optimize server resources, they need to know precisely how many successful requests are made to the telugu section during peak hours on Sunday. Specifically, they are interested in:\n\n    Time Window: From 12 until before 21.\n    Request Type: Only GET requests.\n    Success Criteria: Requests that return HTTP status codes between 200 and 299.\n    Data Source: The logs for May 2024 stored in a GZipped Apache log file containing 258,074 rows.\n    The challenge is further complicated by the nature of the log file:\n\n    The logs are recorded in the GMT-0500 timezone.\n    The file format is non-standard in that fields are separated by spaces, with most fields quoted by double quotes, except the Time field.\n    Some lines have minor formatting issues (41 rows have unique quoting due to how quotes are escaped).\n    Your Task\n    As a data analyst, you are tasked with determining how many successful GET requests for pages under telugu were made on Sunday between 12 and 21 during May 2024. This metric will help:\n\n    Scale Resources: Ensure that servers can handle the peak load during these critical hours.\n    Content Planning: Determine the popularity of regional content to decide on future content investments.\n    Marketing Insights: Tailor promotional strategies for peak usage times.\n    This GZipped Apache log file (61MB) has 258,074 rows. Each row is an Apache web log entry for the site s-anand.net in May 2024.\n\n    Each row has these fields:\n\n    IP: The IP address of the visitor\n    Remote logname: The remote logname of the visitor. Typically "-"\n    Remote user: The remote user of the visitor. Typically "-"\n    Time: The time of the visit. E.g. [01/May/2024:00:00:00 +0000]. Not that this is not quoted and you need to handle this.\n    Request: The request made by the visitor. E.g. GET /blog/ HTTP/1.1. It has 3 space-separated parts, namely (a) Method: The HTTP method. E.g. GET (b) URL: The URL visited. E.g. /blog/ (c) Protocol: The HTTP protocol. E.g. HTTP/1.1\n    Status: The HTTP status code. If 200 <= Status < 300 it is a successful request\n    Size: The size of the response in bytes. E.g. 1234\n    Referer: The referer URL. E.g. https://s-anand.net/\n    User agent: The browser used. This will contain spaces and might have escaped quotes.\n    Vhost: The virtual host. E.g. s-anand.net\n    Server: The IP address of the server.\n    The fields are separated by spaces and quoted by double quotes ("). Unlike CSV files, quoted fields are escaped via " and not "". (This impacts 41 rows.)\n\n    All data is in the GMT-0500 timezone and the questions are based in this same timezone.\n\n    By determining the number of successful GET requests under the defined conditions, we\'ll be able to:\n\n    Optimize Infrastructure: Scale server resources effectively during peak traffic times, reducing downtime and improving user experience.\n    Strategize Content Delivery: Identify popular content segments and adjust digital content strategies to better serve the audience.\n    Improve Marketing Efforts: Focus marketing initiatives on peak usage windows to maximize engagement and conversion.\n    What is the number of successful GET requests for pages under /telugu/ from 12:00 until before 21:00 on Sundays?',
    },
]

for question in questions:
    file_path = question["files"]
    data = {"question": question}
    if file_path is not None:
        response = requests.post(url, data=data)
    else:
        if file_path is not None:
            zipped_file = io.BytesIO()
            with zipfile.ZipFile(zipped_file, "w") as z:
                for file in file_path:
                    z.write(file)
            zipped_file.seek(0)
            files = {"file": zipped_file}
            response = requests.post(url, files=files, data=data)
        else:
            files = {"file": open(file_path, "rb")}
            response = requests.post(url, files=files, data=data)

    print(response.json())
