# Source: https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization

Setting a personal access token policy for your organization - GitHub DocsSkip to main contentGitHub DocsVersion: Free, Pro, & TeamSearch or ask CopilotSearch or askCopilotSelect language: current language is EnglishSearch or ask CopilotSearch or askCopilotOpen menuOpen SidebarOrganizations/Manage programmatic access/Set a token policyHomeOrganizationsCollaborate with groupsAbout organizationsOrganization dashboardBest practicesCreate new organizationAccess organization settingsCustomize organization profileOrganization news feedGitHub Actions metricsManage membershipInvite users to joinCancel or edit invitationRemove a memberReinstate a memberExport member informationCreate accounts for peopleManage organization rolesRoles in an organizationUse organization rolesPredefined roles permissionsMaintain ownership continuityAdd a billing managerRemove billing managerSecurity manager roleManaging moderatorsManage repository accessManage repository rolesRepository rolesSet base permissionsView people with accessManage individual accessManage team accessManage outside collaboratorsAdd outside collaboratorCancel collaborator invitationRemove collaboratorConvert member to collaboratorConvert collaborator to memberReinstate collaboratorOrganize members into teamsAbout organization teamsCreating an organization teamAdd members to a teamTeam maintainersTeam profile pictureCode review settingsRenaming a teamChanging team visibilityConfiguring team notificationsMove a teamAdd a child teamAdd or change parent teamRemove membersScheduled remindersDeleting a teamManage programmatic accessAbout programmatic accessGitHub App managersReview installed GitHub AppsSet a token policyManage token requestsReview token accessLimit app requests and installationsCredential types referenceManage OAuth accessOAuth app restrictionsRestrict OAuth appsUnrestrict OAuth appsApprove OAuth app accessDeny OAuth app accessManage organization settingsVerify or approve a domainRenaming an organizationTransfer ownershipRestrict repository creationSet repo management policySet visibility changes policyManage forking policyManage pull request reviewsDisable or limit actionsAbout private networkingAbout Azure private networkingConfiguring private networkingTroubleshooting Azure private networkingConfigure retention periodAllow issue deletionOrganization discussionsManage repository discussionsManage the commit signoff policyRestrict team creationManage scheduled remindersManage default branch nameManage default labelsManage display of member namesManage sponsorship updatesManage Pages site publicationManage commit commentsArchive an organizationDelete organizationConvert organization to userUpgrade to Corporate ToSDisable projectsManage projects base permissionsProject visibility permissionsCreate rulesetsManage rulesetsRepository custom propertiesManage or restrict modelsOrganization securityManage 2FAView 2FA usagePrepare to require 2FARequire 2FAManage bots & service accountsManage security settingsManage security & analysisReview audit logIP addresses in audit logAudit log eventsAccess compliance reportsMigrate to improved permissionsConvert Owners teamConvert admin teamMigrate admin teamOrganizations/Manage programmatic access/Set a token policySetting a personal access token policy for your organizationOrganization owners can control access to resources by applying policies to personal access tokensCopy as MarkdownIn this articleRestricting access by personal access tokensEnforcing a maximum lifetime policy for personal access tokensEnforcing an approval policy for fine-grained personal access tokensRestricting access by personal access tokens
Organization owners can prevent personal access tokens from accessing resources owned by the organization with the following options:
Restrict access via personal access tokens: Personal access tokens (classic) or fine-grained personal access tokens cannot access resources owned by the organization. SSH keys created by personal access tokens will continue to work.
Allow access via personal access tokens: Personal access tokens (classic) or fine-grained personal access tokens can access resources owned by the organization.
Regardless of the chosen policy, Personal access tokens will have access to public resources within the organization. By default, both Personal access tokens (classic) and fine-grained personal access tokens are enabled.
In the upper-right corner of GitHub, click your profile picture, then click
Organizations.
Select an organization by clicking on it.
Under your organization name, click
Settings. If you cannot see the "Settings" tab, select the
dropdown menu, then click Settings.
In the left sidebar, under
Personal access tokens, click Settings.
Select either the Fine-grained tokens or Tokens (classic) tab to enforce this policy based on the token type.
Under Fine-grained personal access tokens or Restrict personal access tokens (classic) from accessing your organizations, select your access policy.
Click Save.
Enforcing a maximum lifetime policy for personal access tokens
Organization owners can set maximum lifetime allowances for both fine-grained personal access tokens and personal access tokens (classic) to control access to organization resources.
For fine-grained personal access tokens, the default the maximum lifetime policy for organizations is set to expire within 366 days. Personal access tokens (classic) do not have an expiration requirement.
When you set a policy, tokens with non-compliant lifetimes will be blocked from accessing your organization if the token belongs to a member of your organization. Setting this policy does not revoke or disable these tokens. Users will learn that their existing token is non-compliant when API calls for your organization are rejected.
In the upper-right corner of GitHub, click your profile picture, then click
Organizations.
Select an organization by clicking on it.
Under your organization name, click
Settings. If you cannot see the "Settings" tab, select the
dropdown menu, then click Settings.
In the left sidebar, click
Personal access tokens.
Select either the Fine-grained tokens or Tokens (classic) tab to enforce this policy based on the token type.
Under Set maximum lifetimes for personal access tokens, set the maximum lifetime.
Click Save.
Enforcing an approval policy for fine-grained personal access tokens
Organization owners can manage approval requirements for each fine-grained personal access token that can access the organization with the following options:
Require administrator approval: An organization owner must approve each fine-grained personal access token that can access the organization. Fine-grained personal access tokens created by organization owners will not need approval. This is the default value.
Do not require administrator approval: Fine-grained personal access tokens created by organization members can access resources in the organization without prior approval.
Fine-grained personal access tokens will still be able to read public resources within the organization without approval.
Note
Only fine-grained personal access tokens, not personal access tokens (classic), are subject to approval. Unless the organization has restricted access by personal access tokens (classic), any personal access token (classic) can access organization resources without prior approval. For more information, see Restricting access by personal access tokens on this page.
In the upper-right corner of GitHub, click your profile picture, then click
Organizations.
Select an organization by clicking on it.
Under your organization name, click
Settings. If you cannot see the "Settings" tab, select the
dropdown menu, then click Settings.
In the left sidebar, under
Personal access tokens, click Settings.
Select the Fine-grained tokens tab.
Under Require approval of fine-grained personal access tokens, select the option that meets your needs:
Click Save.
Help and supportDid you find what you needed? Yes NoPrivacy policyHelp us make these docs great!All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.Make a contributionLearn how to contributeStill need help?Ask the GitHub communityContact supportLegal© 2026 GitHub, Inc.TermsPrivacyStatusPricingExpert servicesBlog