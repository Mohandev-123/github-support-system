# Source: https://docs.github.com/en/rest/using-the-rest-api/timezones-and-the-rest-api

Timezones and the REST API - GitHub DocsSkip to main contentGitHub DocsVersion: Free, Pro, & TeamSearch or ask CopilotSearch or askCopilotSelect language: current language is EnglishSearch or ask CopilotSearch or askCopilotOpen menuOpen SidebarTimezones and the REST APISome REST API endpoints allow you to specify timezone information with your request.Copy as MarkdownSome requests that create new data, such as creating a new commit, allow you to provide timezone information when specifying or generating timestamps.
Note that these rules apply only to data passed to the API, not to data returned by the API. Timestamps returned by the API are in UTC time, ISO 8601 format.
Determining the timezone for a request
To determine timezone information for applicable API calls, we apply these rules in order of priority:
Explicitly providing an ISO 8601 timestamp with timezone information
Using the Time-Zone header
Using the last known timezone for the user
Defaulting to UTC without other timezone information
Explicitly providing an ISO 8601 timestamp with timezone information
For API calls that allow for a timestamp to be specified, we use that exact timestamp. These timestamps look something like 2014-02-27T15:05:06+01:00.
An example of this is the API to manage commits. For more information, see REST API endpoints for Git commits.
Using the Time-Zone header
It is possible to supply a Time-Zone header, which defines a timezone according to the list of names from the Olson database.
curl -H "Time-Zone: Europe/Amsterdam" -X POST https://api.github.com/repos/github-linguist/linguist/contents/new_file.md
This means that we generate a timestamp for the moment your API call is made, in the timezone this header defines.
For example, the API to manage contents generates a git commit for each addition or change, and it uses the current time as the timestamp. For more information, see REST API endpoints for repository contents. The Time-Zone header will determine the timezone used for generating that current timestamp.
Using the last known timezone for the user
If no Time-Zone header is specified and you make an authenticated call to the API, we use the last known timezone for the authenticated user. The last known timezone is updated whenever you browse the GitHub website.
Defaulting to UTC without other timezone information
If the steps above don't result in any information, we use UTC as the timezone.Help and supportDid you find what you needed? Yes NoPrivacy policyHelp us make these docs great!All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.Make a contributionLearn how to contributeStill need help?Ask the GitHub communityContact supportLegal© 2026 GitHub, Inc.TermsPrivacyStatusPricingExpert servicesBlog