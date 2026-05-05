# Source: https://docs.github.com/en/rest/about-the-rest-api/about-the-openapi-description-for-the-rest-api

About the OpenAPI description for the REST API - GitHub DocsSkip to main contentGitHub DocsVersion: Free, Pro, & TeamSearch or ask CopilotSearch or askCopilotSelect language: current language is EnglishSearch or ask CopilotSearch or askCopilotOpen menuOpen SidebarAbout the OpenAPI description for the REST APIThe GitHub REST API is fully described in an OpenAPI compliant document.Copy as MarkdownIn this articleAbout OpenAPI
OpenAPI is a specification for describing REST API interfaces. It describes the API without requiring access to the source code or additional documentation. The specification is both human and machine readable. For more information, see the OpenAPI specification documentation.
About GitHub's OpenAPI description
GitHub's OpenAPI description of the REST API is publicly available. You can find the description in the open source github/rest-api-description repository.
GitHub provides both 3.0 and 3.1 OpenAPI descriptions.
For each description, there is a version for each product: GitHub Free/GitHub Pro/GitHub Team (api.github.com), GitHub Enterprise Cloud (ghec), and each version of GitHub Enterprise Server (ghes-X.X).
For each product, if date-based versioning is supported, there is also a description for each date-based version. For more information, see API Versions.
Each description is available in a bundled or in a dereferenced format. The bundled format uses $ref to refer to OpenAPI components that are shared between endpoints. The dereferenced format includes the fully expanded description.
Using the GitHub OpenAPI description
Because the OpenAPI description is machine readable, you can use it to do things like:
Generate libraries to facilitate using the REST API
Validate and test an integration that uses the REST API
Explore and interact with the REST API using third-party tools, such as Insomnia or Postman
For example, GitHub uses the OpenAPI description to generate the Octokit SDKs. GitHub also uses the OpenAPI description to generate the REST API reference documentation for each endpoint.Help and supportDid you find what you needed? Yes NoPrivacy policyHelp us make these docs great!All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.Make a contributionLearn how to contributeStill need help?Ask the GitHub communityContact supportLegal© 2026 GitHub, Inc.TermsPrivacyStatusPricingExpert servicesBlog