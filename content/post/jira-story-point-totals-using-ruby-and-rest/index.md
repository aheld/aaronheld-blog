---
title: "JIRA story point totals using Ruby and Rest"
date: "2012-06-12"
categories: 
  - "code"
  - "ruby"
tags: 
  - "agile"
  - "jira"
  - "ruby"
---

I'm using a hosted version of JIRA and needed to obtain quick totals based on filters that I have setup.

I could not find any easy documentation online so I thought I'd share my quick hack.

The [REST API is very well documented](https://developer.atlassian.com/display/JIRADEV/JIRA+REST+API+Example+-+Query+issues) and uses the same JQL as the filters do.

In order to view the commit list for an iteration I have some JQL that looks like:

fixversion = 20120611 and fixversion was 20120611 ON "2012/06/11" AND status NOT IN (canceled, "on hold")

In order to feed that into the API I needed to construct a url along the lines of

    https://**********.atlassian.net/rest/api/2/search?jql=#{urlencoded JQL string}&fields=customfield\_10003&maxresults=400

The &fields=customfield\_10003 instruct the API to return a minimal fieldlist and only include that custom field, which for me is Story Points.  By default the API will return 50, so bump that to 400 to be safe.

The Ruby code looks like

    def getData(api,qs="")
    url = "https://energyplus.atlassian.net/rest/api/2/#{api}?#{qs}"
    res = open(url,
                    "Authorization" => "Basic " + 
                      Base64.strict\_encode64(USERNAME:PASSWORD)) {|f|
                JSON.parse(f.read)
              })

Calling that function I use something along the lines of

    result =  getData("search", "jql=" + URI::encode(jql + '&fields=customfield\_10003&maxResults=400'))

The final step is to loop through all the results and sum the 'Story Point' values

    puts "Total: " + res\["issues"\].inject(0){|sum, item| sum + item\["fields"\]\["customfield\_10003"\]}.to\_s

If you are having issues with the SSL cert, try adding

    OpenSSL::SSL::VERIFY\_PEER = OpenSSL::SSL::VERIFY\_NONE

Here is my actual script in its undocumented glory: [https://gist.github.com/2919437](https://gist.github.com/2919437)

If you think you can improve it, drop me a note - I'm hiring ;)
