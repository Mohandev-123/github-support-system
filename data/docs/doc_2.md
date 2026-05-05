# Source: https://docs.github.com/en/rest/quickstart

Quickstart for GitHub REST API - GitHub DocsSkip to main contentGitHub DocsVersion: Free, Pro, & TeamSearch or ask CopilotSearch or askCopilotSelect language: current language is EnglishSearch or ask CopilotSearch or askCopilotOpen menuOpen SidebarQuickstart for GitHub REST APILearn how to get started with the GitHub REST API.Tool navigationCopy as MarkdownIn this articleIntroduction
This article describes how to quickly get started with the GitHub REST API using GitHub CLI, curl, or JavaScript. For a more detailed guide, see Getting started with the REST API.
Using GitHub CLI in the command line
GitHub CLI is the easiest way to use the GitHub REST API from the command line.
Install GitHub CLI on macOS, Windows, or Linux. For more information, see Installation in the GitHub CLI repository.
To authenticate to GitHub, run the following command from your terminal.
gh auth login
Select where you want to authenticate to:
If you access GitHub at GitHub.com, select GitHub.com.
If you access GitHub at a different domain, select Other, then enter your hostname (for example: octocorp.ghe.com).
Follow the rest of the on-screen prompts.
GitHub CLI automatically stores your Git credentials for you when you choose HTTPS as your preferred protocol for Git operations and answer "yes" to the prompt asking if you would like to authenticate to Git with your GitHub credentials. This can be useful as it allows you to use Git commands like git push and git pull without needing to set up a separate credential manager or use SSH.
Make a request using the GitHub CLI api subcommand, followed by the path. Use the --method or -X flag to specify the method. For more information, see the GitHub CLI api documentation.
This example makes a request to the "Get Octocat" endpoint, which uses the method GET and the path /octocat. For the full reference documentation for this endpoint, see REST API endpoints for meta data.
Shellgh api /octocat --method GET
gh api /octocat --method GET
Using GitHub CLI in GitHub Actions
You can also use GitHub CLI in your GitHub Actions workflows. For more information, see Using GitHub CLI in workflows.
Authenticating with an access token
Instead of using the gh auth login command, pass an access token as an environment variable called GH_TOKEN. GitHub recommends that you use the built-in GITHUB_TOKEN instead of creating a token. If this is not possible, store your token as a secret and replace GITHUB_TOKEN in the example below with the name of your secret. For more information about GITHUB_TOKEN, see Use GITHUB_TOKEN for authentication in workflows. For more information about secrets, see Using secrets in GitHub Actions.
The following example workflow uses the List repository issues endpoint, and requests a list of issues in the octocat/Spoon-Knife repository.
YAMLon:
workflow_dispatch:
jobs:
use_api:
runs-on: ubuntu-latest
permissions:
issues: read
steps:
- env:
GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
run: |
gh api https://api.github.com/repos/octocat/Spoon-Knife/issues
on:
workflow_dispatch:
jobs:
use_api:
runs-on: ubuntu-latest
permissions:
issues: read
steps:
- env:
GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
run: |
gh api https://api.github.com/repos/octocat/Spoon-Knife/issues
Authenticating with a GitHub App
If you are authenticating with a GitHub App, you can create an installation access token within your workflow:
Store your GitHub App's ID as a configuration variable. In the following example, replace APP_ID with the name of the configuration variable. You can find your app ID on the settings page for your app or through the API. For more information, see REST API endpoints for GitHub Apps. For more information about configuration variables, see Store information in variables.
Generate a private key for your app. Store the contents of the resulting file as a secret. (Store the entire contents of the file, including -----BEGIN RSA PRIVATE KEY----- and -----END RSA PRIVATE KEY-----.) In the following example, replace APP_PEM with the name of the secret. For more information, see Managing private keys for GitHub Apps. For more information about secrets, see Using secrets in GitHub Actions.
Add a step to generate a token, and use that token instead of GITHUB_TOKEN. Note that this token will expire after 60 minutes. For example:
YAMLon:
workflow_dispatch:
jobs:
track_pr:
runs-on: ubuntu-latest
steps:
- name: Generate token
id: generate-token
uses: actions/create-github-app-token@v2
with:
app-id: ${{ vars.APP_ID }}
private-key: ${{ secrets.APP_PEM }}
- name: Use API
env:
GH_TOKEN: ${{ steps.generate-token.outputs.token }}
run: |
gh api https://api.github.com/repos/octocat/Spoon-Knife/issues
on:
workflow_dispatch:
jobs:
track_pr:
runs-on: ubuntu-latest
steps:
- name: Generate token
id: generate-token
uses: actions/create-github-app-token@v2
with:
app-id: ${{ vars.APP_ID }}
private-key: ${{ secrets.APP_PEM }}
- name: Use API
env:
GH_TOKEN: ${{ steps.generate-token.outputs.token }}
run: |
gh api https://api.github.com/repos/octocat/Spoon-Knife/issues
Using Octokit.js
You can use Octokit.js to interact with the GitHub REST API in your JavaScript scripts. For more information, see Scripting with the REST API and JavaScript.
Create an access token. For example, create a personal access token or a GitHub App user access token. You will use this token to authenticate your request, so you should give it any scopes or permissions that are required to access that endpoint. For more information, see Authenticating to the REST API or Identifying and authorizing users for GitHub Apps.
Warning
Treat your access token like a password.
To keep your token secure, you can store your token as a secret and run your script through GitHub Actions. For more information, see the Using Octokit.js in GitHub Actions section.
You can also store your token as a Codespaces secret and run your script in Codespaces. For more information, see Managing encrypted secrets for your codespaces.
If these options are not possible, consider using another CLI service to store your token securely.
Install octokit. For example, npm install octokit. For other ways to install or load octokit, see the Octokit.js README.
Import octokit in your script. For example, import { Octokit } from "octokit";. For other ways to import octokit, see the Octokit.js README.
Create an instance of Octokit with your token. Replace YOUR-TOKEN with your token.
JavaScriptconst octokit = new Octokit({
auth: 'YOUR-TOKEN'
});
const octokit = new Octokit({
auth: 'YOUR-TOKEN'
});
Use octokit.request to execute your request. Send the HTTP method and path as the first argument. Specify any path, query, and body parameters in an object as the second argument. For more information about parameters, see Getting started with the REST API.
For example, in the following request the HTTP method is GET, the path is /repos/{owner}/{repo}/issues, and the parameters are owner: "octocat" and repo: "Spoon-Knife".
JavaScriptawait octokit.request("GET /repos/{owner}/{repo}/issues", {
owner: "octocat",
repo: "Spoon-Knife",
});
await octokit.request("GET /repos/{owner}/{repo}/issues", {
owner: "octocat",
repo: "Spoon-Knife",
});
Using Octokit.js in GitHub Actions
You can also execute your JavaScript scripts in your GitHub Actions workflows. For more information, see Workflow syntax for GitHub Actions.
Authenticating with an access token
GitHub recommends that you use the built-in GITHUB_TOKEN instead of creating a token. If this is not possible, store your token as a secret and replace GITHUB_TOKEN in the example below with the name of your secret. For more information about GITHUB_TOKEN, see Use GITHUB_TOKEN for authentication in workflows. For more information about secrets, see Using secrets in GitHub Actions.
The following example workflow:
Checks out the repository content
Sets up Node.js
Installs octokit
Stores the value of GITHUB_TOKEN as an environment variable called TOKEN and runs .github/actions-scripts/use-the-api.mjs, which can access that environment variable as process.env.TOKEN
on:
workflow_dispatch:
jobs:
use_api_via_script:
runs-on: ubuntu-latest
permissions:
issues: read
steps:
- name: Check out repo content
uses: actions/checkout@v6
- name: Setup Node
uses: actions/setup-node@v4
with:
node-version: '16.17.0'
cache: npm
- name: Install dependencies
run: npm install octokit
- name: Run script
run: |
node .github/actions-scripts/use-the-api.mjs
env:
TOKEN: ${{ secrets.GITHUB_TOKEN }}
The following is an example JavaScript script with the file path .github/actions-scripts/use-the-api.mjs.
import { Octokit } from "octokit"
const octokit = new Octokit({
auth: process.env.TOKEN
});
try {
const result = await octokit.request("GET /repos/{owner}/{repo}/issues", {
owner: "octocat",
repo: "Spoon-Knife",
});
const titleAndAuthor = result.data.map(issue => {title: issue.title, authorID: issue.user.id})
console.log(titleAndAuthor)
} catch (error) {
console.log(`Error! Status: ${error.status}. Message: ${error.response.data.message}`)
}
Authenticating with a GitHub App
If you are authenticating with a GitHub App, you can create an installation access token within your workflow:
Store your GitHub App's ID as a configuration variable. In the following example, replace APP_ID with the name of the configuration variable. You can find your app ID on the settings page for your app or through the App API. For more information, see REST API endpoints for GitHub Apps. For more information about configuration variables, see Store information in variables.
Generate a private key for your app. Store the contents of the resulting file as a secret. (Store the entire contents of the file, including -----BEGIN RSA PRIVATE KEY----- and -----END RSA PRIVATE KEY-----.) In the following example, replace APP_PEM with the name of the secret. For more information, see Managing private keys for GitHub Apps. For more information about secrets, see Using secrets in GitHub Actions.
Add a step to generate a token, and use that token instead of GITHUB_TOKEN. Note that this token will expire after 60 minutes. For example:
on:
workflow_dispatch:
jobs:
use_api_via_script:
runs-on: ubuntu-latest
steps:
- name: Check out repo content
uses: actions/checkout@v6
- name: Setup Node
uses: actions/setup-node@v4
with:
node-version: '16.17.0'
cache: npm
- name: Install dependencies
run: npm install octokit
- name: Generate token
id: generate-token
uses: actions/create-github-app-token@v2
with:
app-id: ${{ vars.APP_ID }}
private-key: ${{ secrets.APP_PEM }}
- name: Run script
run: |
node .github/actions-scripts/use-the-api.mjs
env:
TOKEN: ${{ steps.generate-token.outputs.token }}
Using curl in the command line
Note
If you want to make API requests from the command line, GitHub recommends that you use GitHub CLI, which simplifies authentication and requests. For more information about getting started with the REST API using GitHub CLI, see the GitHub CLI version of this article.
Install curl if it isn't already installed on your machine. To check if curl is installed, execute curl --version in the command line. If the output provides information about the version of curl, that means curl is installed. If you get a message similar to command not found: curl, you need to download and install curl. For more information, see the curl project download page.
Create an access token. For example, create a personal access token or a GitHub App user access token. You will use this token to authenticate your request, so you should give it any scopes or permissions that are required to access the endpoint. For more information, see Authenticating to the REST API.
Warning
Treat your access token like a password.
To keep your token secure, you can store your token as a Codespaces secret and use the command line through Codespaces. For more information, see Managing encrypted secrets for your codespaces.
You can also use GitHub CLI instead of curl. GitHub CLI will take care of authentication for you. For more information, see the GitHub CLI version of this page.
If these options are not possible, consider using another CLI service to store your token securely.
Use the curl command to make your request. Pass your token in an Authorization header. Replace YOUR-TOKEN with your token.
Shellcurl --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR-TOKEN"
curl --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR-TOKEN"
Note
In most cases, you can use Authorization: Bearer or Authorization: token to pass a token. However, if you are passing a JSON web token (JWT), you must use Authorization: Bearer.
Using curl commands in GitHub Actions
You can also use curl commands in your GitHub Actions workflows.
Authenticating with an access token
GitHub recommends that you use the built-in GITHUB_TOKEN instead of creating a token. If this is not possible, store your token as a secret and replace GITHUB_TOKEN in the example below with the name of your secret. For more information about GITHUB_TOKEN, see Use GITHUB_TOKEN for authentication in workflows. For more information about secrets, see Using secrets in GitHub Actions.
YAMLon:
workflow_dispatch:
jobs:
use_api:
runs-on: ubuntu-latest
permissions:
issues: read
steps:
- env:
GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
run: |
curl --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer $GH_TOKEN"
on:
workflow_dispatch:
jobs:
use_api:
runs-on: ubuntu-latest
permissions:
issues: read
steps:
- env:
GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
run: |
curl --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer $GH_TOKEN"
Authenticating with a GitHub App
If you are authenticating with a GitHub App, you can create an installation access token within your workflow:
Store your GitHub App's ID as a configuration variable. In the following example, replace APP_ID with the name of the configuration variable. You can find your app ID on the settings page for your app or through the App API. For more information, see REST API endpoints for GitHub Apps. For more information about configuration variables, see Store information in variables.
Generate a private key for your app. Store the contents of the resulting file as a secret. (Store the entire contents of the file, including -----BEGIN RSA PRIVATE KEY----- and -----END RSA PRIVATE KEY-----.) In the following example, replace APP_PEM with the name of the secret. For more information, see Managing private keys for GitHub Apps. For more information about storing secrets, see Using secrets in GitHub Actions.
Add a step to generate a token, and use that token instead of GITHUB_TOKEN. Note that this token will expire after 60 minutes. For example:
YAMLon:
workflow_dispatch:
jobs:
use_api:
runs-on: ubuntu-latest
steps:
- name: Generate token
id: generate-token
uses: actions/create-github-app-token@v2
with:
app-id: ${{ vars.APP_ID }}
private-key: ${{ secrets.APP_PEM }}
- name: Use API
env:
GH_TOKEN: ${{ steps.generate-token.outputs.token }}
run: |
curl --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer $GH_TOKEN"
on:
workflow_dispatch:
jobs:
use_api:
runs-on: ubuntu-latest
steps:
- name: Generate token
id: generate-token
uses: actions/create-github-app-token@v2
with:
app-id: ${{ vars.APP_ID }}
private-key: ${{ secrets.APP_PEM }}
- name: Use API
env:
GH_TOKEN: ${{ steps.generate-token.outputs.token }}
run: |
curl --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer $GH_TOKEN"
Next steps
For a more detailed guide, see Getting started with the REST API.Help and supportDid you find what you needed? Yes NoPrivacy policyHelp us make these docs great!All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.Make a contributionLearn how to contributeStill need help?Ask the GitHub communityContact supportLegal© 2026 GitHub, Inc.TermsPrivacyStatusPricingExpert servicesBlog