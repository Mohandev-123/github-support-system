# Source: https://docs.github.com/en/rest/using-the-rest-api/github-event-types

GitHub event types - GitHub DocsSkip to main contentGitHub DocsVersion: Free, Pro, & TeamSearch or ask CopilotSearch or askCopilotSelect language: current language is EnglishSearch or ask CopilotSearch or askCopilotOpen menuOpen SidebarGitHub event typesFor the GitHub Events API, learn about each event type, the triggering action on GitHub, and each event's unique properties.Copy as MarkdownIn this articleThe Events API can return different types of events triggered by activity on GitHub. Each event response contains shared properties, but has a unique payload object determined by its event type. The Event object common properties describes the properties shared by all events, and each event type describes the payload properties that are unique to the specific event.
Event object common properties
The event objects returned from the Events API endpoints have the same structure.
Event API attribute nameTypeDescriptionidintegerUnique identifier for the event.typestringThe type of event. Events uses PascalCase for the name.actorobjectThe user that triggered the event.actor.idintegerThe unique identifier for the actor.actor.loginstringThe username of the actor.actor.display_loginstringThe specific display format of the username.actor.gravatar_idstringThe unique identifier of the Gravatar profile for the actor.actor.urlstringThe REST API URL used to retrieve the user object, which includes additional user information.actor.avatar_urlstringThe URL of the actor's profile image.repoobjectThe repository object where the event occurred.repo.idintegerThe unique identifier of the repository.repo.namestringThe name of the repository, which includes the owner and repository name. For example, octocat/hello-world is the name of the hello-world repository owned by the octocat personal account.repo.urlstringThe REST API URL used to retrieve the repository object, which includes additional repository information.payloadobjectThe event payload object is unique to the event type. See the event type below for the event API payload object.publicbooleanWhether the event is visible to all users.created_atstringThe date and time when the event was triggered. It is formatted according to ISO 8601.orgobjectThe organization that was chosen by the actor to perform action that triggers the event.The property appears in the event object only if it is applicable.org.idintegerThe unique identifier for the organization.org.loginstringThe name of the organization.org.gravatar_idstringThe unique identifier of the Gravatar profile for the organization.org.urlstringThe REST API URL used to retrieve the organization object, which includes additional organization information.org.avatar_urlstringThe URL of the organization's profile image.
Example WatchEvent event object
This example shows the format of the WatchEvent response when using the Events API.
HTTP/2 200
Link: <https://api.github.com/resource?page=2>; rel="next",
<https://api.github.com/resource?page=5>; rel="last"
[
{
"id": "12345",
"type": "WatchEvent",
"actor": {
"id": 1,
"login": "octocat",
"display_login": "octocat",
"gravatar_id": "",
"url": "https://api.github.com/users/octocat",
"avatar_url": "https://github.com/images/error/octocat_happy.gif"
},
"repo": {
"id": 3,
"name": "octocat/Hello-World",
"url": "https://api.github.com/repos/octocat/Hello-World"
},
"payload": {
"action": "started"
},
"public": false,
"created_at": "2011-09-06T17:26:27Z",
"org": {
"id": 1,
"login": "github",
"gravatar_id": "",
"url": "https://api.github.com/orgs/github",
"avatar_url": "https://github.com/images/error/octocat_happy.gif"
},
}
]
CommitCommentEvent
A commit comment is created. The type of activity is specified in the action property of the payload object. For more information, see REST API endpoints for commit comments.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for CommitCommentEvent
KeyTypeDescriptionactionstringThe action performed. Can be created.commentobjectThe commit comment resource.
CreateEvent
A Git branch or tag is created. For more information, see REST API endpoints for Git database.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for CreateEvent
KeyTypeDescriptionrefstringThe git ref resource branch, or null if ref_type is repository.ref_typestringThe type of Git ref object created in the repository. Can be either branch, tag, or repository.full_refstringThe fully-formed ref resource, meaning that for branches the format is refs/heads/<branch_name>.master_branchstringThe name of the repository's default branch (usually main).descriptionstringThe repository's current description.pusher_typestringCan be either user or a deploy key.
DeleteEvent
A Git branch or tag is deleted. For more information, see the REST API endpoints for Git database REST API.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for DeleteEvent
KeyTypeDescriptionrefstringThe git ref resource branch.ref_typestringThe type of Git ref object deleted in the repository. Can be either branch or tag.full_refstringThe fully-formed ref resource, meaning that for branches the format is refs/heads/<branch_name>.pusher_typestringCan be either user or a deploy key.
DiscussionEvent
A discussion is created in a repository. For more information, see GitHub Discussions documentation.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for DiscussionEvent
KeyTypeDescriptionactionstringThe action performed. Can be created.discussionobjectThe discussion that was created.
ForkEvent
A user forks a repository. For more information, see REST API endpoints for repositories.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for ForkEvent
KeyTypeDescriptionactionstringThe action performed. Can be forked.forkeeobjectThe created repository resource.
GollumEvent
A wiki page is created or updated. For more information, see About wikis.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for GollumEvent
KeyTypeDescriptionpagesarrayThe pages that were updated.pages[][page_name]stringThe name of the page.pages[][title]stringThe current page title.pages[][summary]stringAn optional note about the page. Can be null.pages[][action]stringThe action that was performed on the page. Can be created or edited.pages[][sha]stringThe latest commit SHA of the page.pages[][html_url]stringPoints to the HTML wiki page.
IssueCommentEvent
Activity related to an issue or pull request comment. The type of activity is specified in the action property of the payload object. For more information, see the REST API endpoints for issues.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for IssueCommentEvent
KeyTypeDescriptionactionstringThe action that was performed on the comment. Can be created.issueobjectThe issue the comment belongs to.commentobjectThe comment itself.
IssuesEvent
Activity related to an issue. The type of activity is specified in the action property of the payload object. For more information, see the REST API endpoints for issues.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for IssuesEvent
KeyTypeDescriptionactionstringThe action that was performed. Can be one of opened, closed, reopened.issueobjectThe issue itself.assigneeobjectThe optional user who was assigned or unassigned from the issue.assigneesarrayThe optional array of assignee objects detailing the assignees on the issue.labelobjectThe optional label that was added or removed from the issue.labelsarrayThe optional array of label objects describing the labels on the issue.
MemberEvent
Activity related to repository collaborators. The type of activity is specified in the action property of the payload object. For more information, see REST API endpoints for collaborators.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for MemberEvent
KeyTypeDescriptionactionstringThe action that was performed. Can be added to indicate a user accepted an invitation to a repository.memberobjectThe user that was added.
PublicEvent
When a private repository is made public.
Event payload object for PublicEvent
This event returns an empty payload object.
PullRequestEvent
Activity related to pull requests. The type of activity is specified in the action property of the payload object. For more information, see REST API endpoints for pull requests.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for PullRequestEvent
KeyTypeDescriptionactionstringThe action that was performed. Can be one of opened, closed, merged, reopened, assigned, unassigned, labeled, or unlabeled.numberintegerThe pull request number.pull_requestobjectThe pull request itself.assigneeobjectThe optional user who was assigned or unassigned from the issue.assigneesarrayThe optional array of assignee objects detailing the assignees on the issue.labelobjectThe optional label that was added or removed from the issue if the action was labeled or unlabeled.labelsarrayThe optional array of label objects describing the labels on the pull request if the action was labeled or unlabeled.
PullRequestReviewEvent
Activity related to pull request reviews. The type of activity is specified in the action property of the payload object. For more information, see REST API endpoints for pull requests.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for PullRequestReviewEvent
KeyTypeDescriptionactionstringThe action that was performed. Can be created, updated, or dismissed.pull_requestobjectThe pull request the review pertains to.reviewobjectThe review that was affected.
PullRequestReviewCommentEvent
Activity related to pull request review comments in the pull request's unified diff. The type of activity is specified in the action property of the payload object. For more information, see REST API endpoints for pull requests.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for PullRequestReviewCommentEvent
KeyTypeDescriptionactionstringThe action that was performed on the comment. Can be created.pull_requestobjectThe pull request the comment belongs to.commentobjectThe comment itself.
PushEvent
One or more commits are pushed to a repository branch or tag.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for PushEvent
KeyTypeDescriptionrepository_idintegerThe unique identifier of the repository where the push occurred.push_idintegerThe unique identifier for the push.refstringThe full git ref that was pushed. Example: refs/heads/main.headstringThe SHA of the most recent commit on ref after the push.beforestringThe SHA of the most recent commit on ref before the push.
ReleaseEvent
Activity related to a release. The type of activity is specified in the action property of the payload object. For more information, see the REST API endpoints for releases and release assets REST API.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for ReleaseEvent
KeyTypeDescriptionactionstringThe action that was performed. Can be published.releaseobjectThe release object.
WatchEvent
When someone stars a repository. The type of activity is specified in the action property of the payload object. For more information, see REST API endpoints for activity.
The event object includes properties that are common for all events. Each event object includes a payload property and the value is unique to each event type. The payload object for this event is described below.
Event payload object for WatchEvent
KeyTypeDescriptionactionstringThe action that was performed. Currently, can only be started.Help and supportDid you find what you needed? Yes NoPrivacy policyHelp us make these docs great!All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.Make a contributionLearn how to contributeStill need help?Ask the GitHub communityContact supportLegal© 2026 GitHub, Inc.TermsPrivacyStatusPricingExpert servicesBlog