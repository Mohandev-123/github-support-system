# Source: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

Managing your personal access tokens - GitHub DocsSkip to main contentGitHub DocsVersion: Free, Pro, & TeamSearch or ask CopilotSearch or askCopilotSelect language: current language is EnglishSearch or ask CopilotSearch or askCopilotOpen menuOpen SidebarAuthentication/Account security/Manage personal access tokensHomeAuthenticationAccount securityAuthentication to GitHubCreate a strong passwordSwitching between accountsVerifying devices on sign inUpdate access credentialsManage personal access tokensReviewing your SSH keysDeploy keysToken expirationReview security logSecurity log eventsRemove sensitive dataAbout anonymized URLsGitHub's IP addressesSSH key fingerprintsSudo modeUnauthorized accessViewing and managing sessionsSecure your account with 2FAAbout 2FAAbout mandatory 2FAConfigure 2FAConfigure 2FA recoveryAccess GitHub with 2FACountries supporting SMSChange 2FA methodTroubleshooting 2FARecover an account with 2FADisable 2FAAuthenticate with a passkeyAbout passkeysManage your passkeysSign in with a passkeyConnect with SSHAbout SSHCheck for existing SSH keyGenerate new SSH keyAdd a new SSH keyTest your SSH connectionSSH key passphrasesSSH agent forwardingManaging deploy keysTroubleshooting SSHUse SSH over HTTPS portRecover SSH key passphraseDeleted or missing SSH keysError: Host key verification failedPermission denied (publickey)Error: Bad file numberError: Key already in usePermission denied other-userPermission denied other-repoAgent failure to signssh-add "illegal option" errorSSL certificate problemError: Unknown key typeSSH key auditVerify commit signaturesCommit signature verificationExisting GPG keysGenerating a new GPG keyAdd a GPG keyTell Git about your signing keyAssociate email with GPG keySigning commitsSigning tagsDisplaying verification for all commitsTroubleshoot verificationCheck verification statusUse verified email in GPG keyAuthentication/Account security/Manage personal access tokensManaging your personal access tokensYou can use a personal access token in place of a password when authenticating to GitHub in the command line or with the API.Copy as MarkdownIn this articleAbout personal access tokensCreating a fine-grained personal access tokenCreating a personal access token (classic)Deleting a personal access tokenUsing a personal access token on the command lineFurther readingWarning
Treat your access tokens like passwords. For more information, see Keeping your personal access tokens secure.
About personal access tokens
Personal access tokens are an alternative to using passwords for authentication to GitHub when using the GitHub API or the command line.
Personal access tokens are intended to access GitHub resources on behalf of yourself. To access resources on behalf of an organization, or for long-lived integrations, you should use a GitHub App. For more information, see About creating GitHub Apps.
A token has the same capabilities to access resources and perform actions on those resources that the owner of the token has, and is further limited by any scopes or permissions granted to the token. A token cannot grant additional access capabilities to a user. For example, a personal access token can be configured with an admin:org scope, but if the owner of the token is not an organization owner, the token will not give administrative access to the organization.
Types of personal access tokens
GitHub currently supports two types of personal access tokens: fine-grained personal access tokens and personal access tokens (classic). GitHub recommends that you use fine-grained personal access tokens instead of personal access tokens (classic) whenever possible.
Note
Fine-grained personal access tokens, while more secure and controllable, cannot accomplish every task that a personal access token (classic) can. See the section on Fine-grained personal access tokens limitations below to learn more.
Both fine-grained personal access tokens and personal access tokens (classic) are tied to the user who generated them and will become inactive if the user loses access to the resource.
Organization owners can set a policy to restrict the access of personal access tokens (classic) to their organization. For more information, see Setting a personal access token policy for your organization.
Fine-grained personal access tokens
Fine-grained personal access tokens have several security advantages over personal access tokens (classic), but also have limitations that may prevent you from using them in every scenario. These limits, and our plans to fix them, can be found in the section below.
If you can use a fine-grained personal access token for your scenario, you'll benefit from these improvements:
Each token is limited to access resources owned by a single user or organization.
Each token can be further limited to only access specific repositories for that user or organization.
Each token is granted specific, fine-grained permissions, which offer more control than the scopes granted to personal access tokens (classic).
Organization owners can require approval for any fine-grained personal access tokens that can access resources in the organization.
Fine-grained personal access tokens limitations
Fine-grained personal access tokens do not support every feature of personal access tokens (classic). These feature gaps are not permanent - GitHub is working to close them. You can review our public roadmap for more details on when these scenarios will be supported.
The major gaps in fine-grained personal access tokens are:
Using fine-grained personal access token to contribute to public repos where the user is not a member.
Using fine-grained personal access token to contribute to repositories where the user is an outside or repository collaborator.
Using fine-grained personal access token to access multiple organizations at once.
Using fine-grained personal access token to access Packages.
Using fine-grained personal access token to call the Checks API.
Using fine-grained personal access token to access Projects owned by a user account.
All of these gaps will be solved over time, as GitHub continues to invest in more secure access patterns.
Personal access tokens (classic)
Personal access tokens (classic) are less secure. However, some features currently will only work with personal access tokens (classic):
Only personal access tokens (classic) have write access for public repositories that are not owned by you or an organization that you are not a member of.
Outside collaborators can only use personal access tokens (classic) to access organization repositories that they are a collaborator on.
A few REST API endpoints are only available with a personal access tokens (classic). To check whether an endpoint also supports fine-grained personal access tokens, see the documentation for that endpoint, or see Endpoints available for fine-grained personal access tokens.
If you choose to use a personal access token (classic), keep in mind that it will grant access to all repositories within the organizations that you have access to, as well as all personal repositories in your personal account.
As a security precaution, GitHub automatically removes personal access tokens that haven't been used in a year. To provide additional security, we highly recommend adding an expiration to your personal access tokens.
Keeping your personal access tokens secure
Personal access tokens are like passwords, and they share the same inherent security risks. Before creating a new personal access token, consider if there is a more secure method of authentication available to you:
To access GitHub from the command line, you can use GitHub CLI or Git Credential Manager instead of creating a personal access token.
When using a personal access token in a GitHub Actions workflow, consider whether you can use the built-in GITHUB_TOKEN instead. For more information, see Use GITHUB_TOKEN for authentication in workflows.
If these options are not possible, and you must create a personal access token, consider using another CLI service to store your token securely.
When using a personal access token in a script, you can store your token as a secret and run your script through GitHub Actions. For more information, see Using secrets in GitHub Actions. You can also store your token as a Codespaces secret and run your script in Codespaces. For more information, see Managing your account-specific secrets for GitHub Codespaces.
For more information about best practices, see Keeping your API credentials secure.
Creating a fine-grained personal access token
Note
There is a limit of 50 fine-grained personal access tokens you can create. If you require more tokens or are building automations, consider using a GitHub App for better scalability and management. For more information, see Deciding when to build a GitHub App.
Verify your email address, if it hasn't been verified yet.
In the upper-right corner of any page on GitHub, click your profile picture, then click
Settings.
In the left sidebar, click
Developer settings.
In the left sidebar, under
Personal access tokens, click Fine-grained tokens.
Click Generate new token.
Under Token name, enter a name for the token.
Under Expiration, select an expiration for the token. Infinite lifetimes are allowed but may be blocked by a maximum lifetime policy set by your organization or enterprise owner. For more information, See Enforcing a maximum lifetime policy for personal access tokens.
Optionally, under Description, add a note to describe the purpose of the token.
Under Resource owner, select a resource owner. The token will only be able to access resources owned by the selected resource owner. Organizations that you are a member of will not appear if the organization has blocked the use of fine-grained personal access tokens. For more information, see Setting a personal access token policy for your organization.
Optionally, if the resource owner is an organization that requires approval for fine-grained personal access tokens, below the resource owner, in the box, enter a justification for the request.
Under Repository access, select which repositories you want the token to access. You should choose the minimal repository access that meets your needs. Tokens always include read-only access to all public repositories on GitHub.
If you selected Only select repositories in the previous step, under the Selected repositories dropdown, select the repositories that you want the token to access.
Under Permissions, select which permissions to grant the token. Depending on which resource owner and which repository access you specified, there are repository, organization, and account permissions. You should choose the minimal permissions necessary for your needs.
The REST API reference document for each endpoint states whether the endpoint works with fine-grained personal access tokens and states what permissions are required in order for the token to use the endpoint. Some endpoints may require multiple permissions, and some endpoints may require one of multiple permissions. For an overview of which REST API endpoints a fine-grained personal access token can access with each permission, see Permissions required for fine-grained personal access tokens.
Click Generate token.
If you selected an organization as the resource owner and the organization requires approval for fine-grained personal access tokens, then your token will be marked as pending until it is reviewed by an organization administrator. Your token will only be able to read public resources until it is approved. If you are an owner of the organization, your request is automatically approved. For more information, see Reviewing and revoking personal access tokens in your organization.
Pre-filling fine-grained personal access token details using URL parameters
You can share templates for a fine-grained personal access token via links. Storing token details this way makes it easier to automate workflows and improve your developer experience by directing users to token creation with relevant fields already completed.
Each supported field can be set using a specific query parameter. All parameters are optional and validated by the token generation form to ensure that the combinations of permissions and resource owner makes sense.
An example URL template is shown here, with line breaks for legibility:
HTTPhttps://github.com/settings/personal-access-tokens/new
?name=Repo-reading+token
&description=Just+contents:read
&target_name=octodemo
&expires_in=45
&contents=read
https://github.com/settings/personal-access-tokens/new
?name=Repo-reading+token
&description=Just+contents:read
&target_name=octodemo
&expires_in=45
&contents=read
Try the URL to create a token with contents:read and metadata:read, with the given name and description and an expiration date 45 days in the future. You'll see an error message indicating Cannot find the specified resource owner: octodemo because you're not a member of the octodemo organization.
Below are some example URLs that generate the tokens we see most often:
Read repo contents
Push access to repos
GitHub Models access
Update code and open a PR
Manage Copilot licenses in an organization
Make Copilot requests
Supported Query Parameters
To create your own token template, follow the query parameter details provided in this table:
ParameterTypeExample ValueValid ValuesDescriptionnamestringDeploy%20Bot≤ 40 characters, URL-encodedPre-fills the token’s display name.descriptionstringUsed+for+deployments≤ 1024 chars, URL-encodedPre-fills the description for the token.target_namestringoctodemoUser or organization slugSets the token's resource target. This is the owner of the repositories that the token will be able to access. If not provided, defaults to the current user's account.expires_ininteger30 or noneInteger between 1 and 366, or noneDays until expiration or none for non-expiring. If not provided, the default is 30 days, or less if the target has a token lifetime policy set.<permission>stringcontents=readA series of permission and access levels.The permissions the token should have. Permissions can be set to read, write, or admin, but not every permission supports each of those levels.
Permissions
Each supported permission is set using its name as a query parameter, with the value specifying the desired access level. Valid access levels are read, write, and admin. Some permissions only support read, some only support write, and only a few have admin. Use as many permissions as needed, in the form &contents=read&pull_requests=write&....
You do not need to include both read and write for a permission in your URL—write always includes read, and admin always includes write.
Account Permissions
Account permissions are only used when the current user is set as the resource owner.
Parameter nameDisplay nameAccess levelsblockingBlock another userread, writecodespaces_user_secretsCodespaces user secretsread, writecopilot_messagesCopilot Chatreadcopilot_editor_contextCopilot Editor Contextreadcopilot_requestsCopilot requestswriteemailsEmail addressesread, writeuser_eventsEventsreadfollowersFollowersread, writegpg_keysGPG keysread, writegistsGistswritekeysGit SSH keysread, writeinteraction_limitsInteraction limitsread, writeknowledge_basesKnowledge basesread, writeuser_modelsModelsreadplanPlanreadprivate_repository_invitationsPrivate repository invitationsreadprofileProfilewritegit_signing_ssh_public_keysSSH signing keysread, writestarringStarringread, writewatchingWatchingread, write
Note
The copilot_requests permission enables making Copilot requests for the given user, which count towards the user's premium request allowance or are charged to overage billing if the allowance is exceeded. For more information about Copilot requests and billing, see Requests in GitHub Copilot.
Repository Permissions
Repository permissions work for both user and organization resource owners.
Parameter nameDisplay nameAccess levelsactionsActionsread, writeadministrationAdministrationread, writeartifact_metadataArtifact Metadataread, writeattestationsAttestationsread, writesecurity_eventsCode scanning alertsread, writecodespacesCodespacesread, writecodespaces_lifecycle_adminCodespaces lifecycle adminread, writecodespaces_metadataCodespaces metadatareadcodespaces_secretsCodespaces secretswritestatusesCommit statusesread, writecontentsContentsread, writerepository_custom_propertiesCustom propertiesread, writevulnerability_alertsDependabot alertsread, writedependabot_secretsDependabot secretsread, writedeploymentsDeploymentsread, writediscussionsDiscussionsread, writeenvironmentsEnvironmentsread, writeissuesIssuesread, writemerge_queuesMerge queuesread, writemetadataMetadatareadpagesPagesread, writepull_requestsPull requestsread, writerepository_advisoriesRepository security advisoriesread, writesecret_scanning_alertsSecret scanning alertsread, writesecretsSecretsread, writeactions_variablesVariablesread, writerepository_hooksWebhooksread, writeworkflowsWorkflowswrite
Organization Permissions
Organization permissions can only be used if the resource owner is an organization.
Parameter nameDisplay nameAccess levelsorganization_api_insightsAPI Insightsreadorganization_administrationAdministrationread, writeorganization_user_blockingBlocking usersread, writeorganization_campaignsCampaignsread, writeorganization_custom_org_rolesCustom organization rolesread, writeorganization_custom_propertiesCustom repository propertiesread, write, adminorganization_custom_rolesCustom repository rolesread, writeorganization_eventsEventsreadorganization_copilot_seat_managementGitHub Copilot Businessread, writeissue_typesIssue Typesread, writeorganization_knowledge_basesKnowledge basesread, writemembersMembersread, writeorganization_modelsModelsreadorganization_network_configurationsNetwork configurationsread, writeorganization_announcement_bannersOrganization announcement bannersread, writeorganization_codespacesOrganization codespacesread, writeorganization_codespaces_secretsOrganization codespaces secretsread, writeorganization_codespaces_settingsOrganization codespaces settingsread, writeorganization_dependabot_secretsOrganization dependabot secretsread, writeorganization_code_scanning_dismissal_requestsCode scanning dismissal requestsread, writeorganization_private_registriesPrivate registriesread, writeorganization_planPlanreadorganization_projectsProjectsread, write, adminorganization_secretsSecretsread, writeorganization_self_hosted_runnersSelf-hosted runnersread, writeteam_discussionsTeam discussionsread, writeorganization_actions_variablesVariablesread, writeorganization_hooksWebhooksread, write
Creating a personal access token (classic)
Note
Organization owners can restrict the access of personal access token (classic) to their organization. If you try to use a personal access token (classic) to access resources in an organization that has disabled personal access token (classic) access, your request will fail with a 403 response. Instead, you must use a GitHub App, OAuth app, or fine-grained personal access token.
Warning
Your personal access token (classic) can access every repository that you can access. GitHub recommends that you use fine-grained personal access tokens instead, which you can restrict to specific repositories. Fine-grained personal access tokens also enable you to specify fine-grained permissions instead of broad scopes.
Verify your email address, if it hasn't been verified yet.
In the upper-right corner of any page on GitHub, click your profile picture, then click
Settings.
In the left sidebar, click
Developer settings.
In the left sidebar, under
Personal access tokens, click Tokens (classic).
Select Generate new token, then click Generate new token (classic).
In the "Note" field, give your token a descriptive name.
To give your token an expiration, select Expiration, then choose a default option or click Custom to enter a date.
Select the scopes you'd like to grant this token. To use your token to access repositories from the command line, select repo. A token with no assigned scopes can only access public information. For more information, see Scopes for OAuth apps.
Click Generate token.
Optionally, to copy the new token to your clipboard, click .
To use your token to access resources owned by an organization that uses SAML single sign-on, authorize the token. For more information, see Authorizing a personal access token for use with single sign-on in the GitHub Enterprise Cloud documentation.
Deleting a personal access token
You should delete a personal access token if it is no longer needed. If you delete a personal access token that was used to create a deploy key, the deploy key will also be deleted.
In the upper-right corner of any page on GitHub, click your profile picture, then click
Settings.
In the left sidebar, click
Developer settings.
In the left sidebar, under
Personal access tokens, click either Fine-grained tokens or Tokens (classic), depending on which type of personal access token you'd like to delete.
To the right of the personal access token you want to delete, click Delete.
Note
If you find a leaked personal access token belonging to someone else, you can submit a revocation request through the REST API. See Best practices for preventing data leaks in your organization.
Using a personal access token on the command line
Once you have a personal access token, you can enter it instead of your password when performing Git operations over HTTPS.
For example, to clone a repository on the command line you would enter the following git clone command. You would then be prompted to enter your username and password. When prompted for your password, enter your personal access token instead of a password.
$ git clone https://github.com/USERNAME/REPO.git
Username: YOUR-USERNAME
Password: YOUR-PERSONAL-ACCESS-TOKEN
Although you are required to enter your username along with your personal access token, the username is not used to authenticate you. Instead, the personal access token is used to authenticate you. If you do not enter a username, you will receive an error message that your credentials are invalid.
Personal access tokens can only be used for HTTPS Git operations. If your repository uses an SSH remote URL, you will need to switch the remote from SSH to HTTPS.
If you are not prompted for your username and password, your credentials may be cached on your computer. You can update your credentials in the Keychain to replace your old password with the token.
Instead of manually entering your personal access token for every HTTPS Git operation, you can cache your personal access token with a Git client. Git will temporarily store your credentials in memory until an expiry interval has passed. You can also store the token in a plain text file that Git can read before every request. For more information, see Caching your GitHub credentials in Git.
Further reading
About authentication to GitHub
Token expiration and revocation
Help and supportDid you find what you needed? Yes NoPrivacy policyHelp us make these docs great!All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.Make a contributionLearn how to contributeStill need help?Ask the GitHub communityContact supportLegal© 2026 GitHub, Inc.TermsPrivacyStatusPricingExpert servicesBlog