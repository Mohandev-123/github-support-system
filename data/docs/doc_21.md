# Source: https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/troubleshooting-identity-and-access-management-for-your-organization

Troubleshooting identity and access management for your organization - GitHub Enterprise Cloud DocsSkip to main contentGitHub DocsVersion: Enterprise CloudSearch or ask CopilotSearch or askCopilotSelect language: current language is EnglishSearch or ask CopilotSearch or askCopilotOpen menuOpen SidebarOrganizations/Manage SAML single sign-on/Troubleshooting accessHomeOrganizationsCollaborate with groupsAbout organizationsOrganization dashboardBest practicesCreate new organizationAccess organization settingsCustomize organization profileOrganization news feedDependency insightsGitHub Actions metricsManage membershipInvite users to joinCancel or edit invitationRemove a memberReinstate a memberExport member informationCreate accounts for peopleManage organization rolesRoles in an organizationUse organization rolesCustom roles permissionsPredefined roles permissionsManage custom rolesMaintain ownership continuityAdd a billing managerRemove billing managerSecurity manager roleManaging moderatorsManage repository accessManage repository rolesRepository rolesAbout custom rolesManage custom rolesSet base permissionsView people with accessManage individual accessManage team accessManage outside collaboratorsAdd outside collaboratorCancel collaborator invitationRemove collaboratorConvert member to collaboratorConvert collaborator to memberReinstate collaboratorOrganize members into teamsAbout organization teamsCreating an organization teamAdd members to a teamTeam maintainersTeam profile pictureCode review settingsRenaming a teamChanging team visibilityConfiguring team notificationsSynchronize with an IdPMove a teamAdd a child teamAdd or change parent teamRemove membersScheduled remindersDeleting a teamManage programmatic accessAbout programmatic accessGitHub App managersReview installed GitHub AppsSet a token policyManage token requestsReview token accessLimit app requests and installationsViewing API insightsCredential types referenceManage OAuth accessOAuth app restrictionsRestrict OAuth appsUnrestrict OAuth appsApprove OAuth app accessDeny OAuth app accessManage organization settingsVerify or approve a domainRenaming an organizationTransfer ownershipGovern repository usageRestrict repository creationSet repo management policySet visibility changes policyManage forking policyManage pull request reviewsDisable or limit actionsAbout private networkingAbout Azure private networkingConfiguring private networkingTroubleshooting Azure private networkingConfigure retention periodSet collaborator policyAllow issue deletionOrganization discussionsManage repository discussionsManage the commit signoff policyRestrict deploy keysRestrict team creationCreate an announcement bannerManage scheduled remindersManage default branch nameManage default labelsChange insight visibilityManage display of member namesManage sponsorship updatesManage Pages site publicationManage commit commentsArchive an organizationDelete organizationConvert organization to userUpgrade to Corporate ToSDisable projectsManage projects base permissionsProject visibility permissionsCreate rulesetsManage rulesetsRepository custom propertiesManage or restrict modelsOrganization securityManage 2FAView 2FA usagePrepare to require 2FARequire 2FAManage bots & service accountsManage security settingsManage security & analysisManage allowed IP addressesRestrict email notificationsReview audit logIdentify events by tokenIP addresses in audit logAudit log eventsAccess compliance reportsManage SAML single sign-onIAM with SAML SSOAbout SCIM for organizationsConnect an IdPConfigure SAML & SCIM with OktaEnable & test SAML SSOPrepare to enforce SAML SSOEnforce SAML single sign-onDownload SAML recovery codesManage team synchronizationDisable SAMLUnavailable identity providerTroubleshooting accessGrant access with SAMLManage bots & service accountsManage SAML access2FA & SAML single sign-onManage Git accessSSH certificate authoritiesManage SSH authoritiesMigrate to improved permissionsConvert Owners teamConvert admin teamMigrate admin teamOrganizations/Manage SAML single sign-on/Troubleshooting accessTroubleshooting identity and access management for your organizationReview and resolve common troubleshooting errors for managing your organization's SAML SSO, team synchronization, or identity provider (IdP) connection.Copy as MarkdownIn this articleError: "Current time is earlier than NotBefore condition"Users are repeatedly redirected to authenticateSome users are not provisioned or deprovisioned by SCIMConflicting SAML identity errorFurther readingError: "Current time is earlier than NotBefore condition"
This error can occur when there's too large of a time difference between your IdP and GitHub, which commonly occurs with self-hosted IdPs.
If you encounter this error, make sure the time on your IdP is properly synced with your NTP server.
If you use ADFS as your IdP, also set NotBeforeSkew in ADFS to 1 minute for GitHub. If NotBeforeSkew is set to 0, even very small time differences, including milliseconds, can cause authentication problems.
Users are repeatedly redirected to authenticate
If users are repeatedly redirected to the SAML authentication prompt in a loop, you may need to increase the SAML session duration in your IdP settings.
The SessionNotOnOrAfter value sent in a SAML response determines when a user will be redirected back to the IdP to authenticate. If a SAML session duration is configured for 2 hours or less, GitHub will refresh a SAML session 5 minutes before it expires. If your session duration is configured as 5 minutes or less, users can get stuck in a SAML authentication loop.
To fix this problem, we recommend configuring a minimum SAML session duration of 4 hours. For more information, see SAML configuration reference.
Some users are not provisioned or deprovisioned by SCIM
When you encounter provisioning issues with users, we recommend that you check if the users are missing SCIM metadata.
If SCIM provisioning is implemented for your organization, any changes to a user's organization membership should be triggered from the identity provider. If a user is invited to an organization manually instead of by an existing SCIM integration, their user account may not get properly linked to their SCIM identity. This can prevent the user account from being deprovisioned via SCIM in the future. If a user is removed manually instead of by an existing SCIM integration, a stale linked identity will remain, which can lead to issues if the user needs to re-join the organization.
If an organization member has missing SCIM metadata, then you can re-provision SCIM for the user manually through your IdP.
Auditing users for missing SCIM metadata
If you suspect or notice that any users are not provisioned or deprovisioned as expected, we recommend that you audit all users in your organization.
To check whether users have a SCIM identity (SCIM metadata) in their external identity, you can review SCIM metadata for one organization member at a time on GitHub or you can programmatically check all organization members using the GitHub API.
When the IdP sends a provisioning call to the GitHub SCIM API, the SCIM userName in that API call needs to match the stored SAML nameID in the user's linked SAML identity in the organization. If these two values do not match, the SCIM metadata will not get populated, and the SCIM identity will not get successfully linked. To check whether these values match, use the GitHub API.
Auditing organization members on GitHub
As an organization owner, to confirm that SCIM metadata exists for a single organization member, visit this URL, replacing <organization> and <username>:
https://github.com/orgs/<organization>/people/<username>/sso
If the user's external identity includes SCIM metadata, the organization owner should see a SCIM identity section on that page. If their external identity does not include any SCIM metadata, the SCIM Identity section will not exist.
Auditing organization members through the GitHub API
As an organization owner, you can also query the SCIM REST API or GraphQL to list all SCIM provisioned identities in an organization.
Using the REST API
The SCIM REST API will only return data for users that have SCIM metadata populated under their external identities. We recommend you compare a list of SCIM provisioned identities with a list of all your organization members.
For more information, see:
REST API endpoints for SCIM
REST API endpoints for organization members
Using GraphQL
This GraphQL query shows you the SAML NameId, the SCIM UserName and the GitHub username (login) for each user in the organization. To use this query, replace ORG with your organization name.
{
organization(login: "ORG") {
samlIdentityProvider {
ssoUrl
externalIdentities(first: 100) {
edges {
node {
samlIdentity {
nameId
}
scimIdentity {
username
}
user {
login
}
}
}
}
}
}
}
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{ "query": "{ organization(login: \"ORG\") { samlIdentityProvider { externalIdentities(first: 100) { pageInfo { endCursor startCursor hasNextPage } edges { cursor node { samlIdentity { nameId } scimIdentity {username} user { login } } } } } } }" }' https://api.github.com/graphql
For more information on using the GraphQL API, see:
Guides
Re-provisioning SCIM for users through your identity provider
You can re-provision SCIM for users manually through your IdP. For example, to resolve provisioning errors for Okta, in the Okta admin portal, you can unassign and reassign users to the GitHub app. This should trigger Okta to make an API call to populate the SCIM metadata for these users on GitHub. For more information, see Unassign users from applications or Assign users to applications in the Okta documentation.
To confirm that a user's SCIM identity is created, we recommend testing this process with a single organization member whom you have confirmed doesn't have a SCIM external identity. After manually updating the users in your IdP, you can check if the user's SCIM identity was created using the SCIM API or on GitHub. For more information, see Auditing users for missing SCIM metadata or REST API endpoints for SCIM.
If re-provisioning SCIM for users doesn't help, please contact GitHub Support.
Conflicting SAML identity error
When users attempt to authenticate with your SAML identity provider (IdP) to access a GitHub organization or enterprise for the first time, they may encounter the following error message.
Your GitHub user account [GitHub username] is currently unlinked. However, you are attempting to authenticate with your Identity Provider using [IdP user account] SAML identity which is already linked to a different GitHub user account in the [organization/enterprise]. Please reach out to one of your GitHub [organization/enterprise] owners for assistance.
If the IdP is Entra ID, the error message will include the User Object ID of the linked identity in Entra ID, which GitHub refers to as the External ID.
This error message occurs because an external identity can only be linked to a single GitHub user account within an organization or enterprise.
Identifying the user with a conflicting identity
When users contact you with this error, you can run through the following steps to identify the conflicting accounts.
Use the GitHub GraphQL API to determine which user is linked to the conflicting external identity.
If SAML is configured at the GitHub organization level: an organization owner must query the existing external identities at the organization level and filter them by the SAML NameID of the IdP account that the user is authenticating with when this error occurs. See the org-saml-identities-filtered-by-nameid-username.graphql sample in the platform-samples repository.
If SAML is configured at the GitHub enterprise level: an enterprise owner must query the existing external identities at the enterprise level and filter them by the SAML NameID of the IdP account that the user is authenticating with when this error occurs. See the enterprise-saml-identities-filtered-by-nameid.graphql sample in the platform-samples repository.
If you identified a GitHub user associated with the conflicting external identity, to confirm if the user is still active in the enterprise and any organizations within it, an enterprise owner can follow the steps in Viewing people in your enterprise.
Resolving the conflict
When you have followed the steps to identify conflicting accounts, there are various resolution options depending on your findings. If you encounter issues when attempting to follow these steps or have questions, you can open a GitHub support ticket using the GitHub Support portal.
Conflicting GitHub user no longer needs access
Conflicting GitHub user still needs access
No conflicting GitHub user found
Conflicting GitHub user no longer needs access
If there is a GitHub user account associated with the conflicting external identity that no longer needs access to the GitHub organization or enterprise, remove them as a member. If the user is removed properly, this should also remove their linked SAML identity, and linked SCIM identity if this exists at the organization level.
If you use SCIM provisioning to manage organization membership, you must deprovision the user from your IdP via SCIM, rather than following the steps on GitHub. Otherwise, the user's linked SAML and SCIM identity will remain in the organization, which may continue to cause the error.
If don't use SCIM provisioning to manage organization membership, see Removing a member from your organization or Removing a member from your enterprise. Make sure to also remove the user's access from the GitHub app for the organization or enterprise in your IdP.
To confirm that a SAML or SCIM identity has been successfully removed from a GitHub organization for a user, see Troubleshooting identity and access management for your organization.
Conflicting GitHub user still needs access
If there is a GitHub user account associated with the conflicting external identity and this user still needs access to the organization or enterprise, you will need to either change the linked identity for the user account or have the user who is receiving the error authenticate with a different IdP identity.
If you use SCIM provisioning to manage membership of an organization and you need to change the external identity that is linked to the member's GitHub account, deprovision then reprovision the user from your IdP (for example, unassign and reassign the user to the app).
When the IdP user is deprovisioned, their GitHub account and linked SAML/SCIM identity will be removed from the GitHub organization.
When the IdP user is reprovisioned to the GitHub organization, a new pending organization invitation and new unlinked SCIM identity will be created. This will allow the user to sign in with this GitHub user account, authenticate via SAML, and link the new IdP identity to their account. These steps will help ensure that both the new SAML and SCIM identity are properly linked to the GitHub user account in the organization.
If you don't use SCIM provisioning to manage organization membership, or if SAML is configured at the enterprise level, you can revoke the linked external identity for the user by following the steps in one of the following articles:
Viewing and managing a user's SAML access to your enterprise
Viewing and managing a member's SAML access to your organization
No conflicting GitHub user found
If there is no GitHub user account associated with the conflicting external identity, you can revoke the external identity.
If you use SCIM provisioning to manage membership of the organization, remove the stale, unlinked identity from your IdP (for example, unassign the user from the IdP app).
If the IdP does not send the appropriate SCIM API call to GitHub, the identity will remain in the organization, which may continue to cause the error.
To confirm that a SAML or SCIM identity has been successfully removed from a GitHub organization for a user, see Troubleshooting identity and access management for your organization.
If you don't use SCIM provisioning to manage membership of the organization, to revoke the linked external identity, navigate to one of the following URLs below to revoke the external identity. Replace USERNAME with the GitHub username of the user who cannot sign in, and ORGANIZATION or ENTERPRISE with the appropriate value.
https://github.com/orgs/ORGANIZATION/people/USERNAME/sso
https://github.com/enterprises/ENTERPRISE/people/USERNAME/sso
Further reading
Troubleshooting identity and access management for your enterprise
Help and supportDid you find what you needed? Yes NoPrivacy policyHelp us make these docs great!All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.Make a contributionLearn how to contributeStill need help?Ask the GitHub communityContact supportLegal© 2026 GitHub, Inc.TermsPrivacyStatusPricingExpert servicesBlog