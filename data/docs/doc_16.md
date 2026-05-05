# Source: https://docs.github.com/en/rest/using-the-rest-api/issue-event-types

Issue event types - GitHub DocsSkip to main contentGitHub DocsVersion: Free, Pro, & TeamSearch or ask CopilotSearch or askCopilotSelect language: current language is EnglishSearch or ask CopilotSearch or askCopilotOpen menuOpen SidebarIssue event typesFor the REST APIs for issue events and timeline events, learn about each event type, the triggering action on GitHub, and each event's unique properties.Copy as MarkdownIn this articleIssue events are triggered by activity in issues and pull requests and are available in the REST API for Issue events and Timeline events. Each event type specifies whether the event is available in the REST API for issue events or timeline events.
GitHub's REST API considers every pull request to be an issue, but not every issue is a pull request. For this reason, the Issue Events and Timeline Events endpoints may return both issues and pull requests in the response. Pull requests have a pull_request property in the issue object. Because pull requests are issues, issue and pull request numbers do not overlap in a repository. For example, if you open your first issue in a repository, the number will be 1. If you then open a pull request, the number will be 2. Each event type specifies if the event occurs in pull request, issues, or both.
Issue event object common properties
Issue events all have the same object structure, except events that are only available in the REST API for timeline events. Some events also include additional properties that provide more context about the event resources. Refer to the specific event for details about any properties that differ from this object format.
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
assigned
The issue or pull request was assigned to a user.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for assigned
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.assigneeobjectThe person assigned to this issue.assignerobjectThe person who performed the assignment for this issue. This field is available in the REST API for issue events but not the REST API for timeline events.
automatic_base_change_failed
GitHub unsuccessfully attempted to automatically change the base branch of the pull request.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for automatic_base_change_failed
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
automatic_base_change_succeeded
GitHub successfully attempted to automatically change the base branch of the pull request.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for automatic_base_change_succeeded
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
base_ref_changed
The base reference branch of the pull request changed.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for base_ref_changed
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
closed
The issue or pull request was closed. When the commit_id is present, it identifies the commit that closed the issue using "closes / fixes" syntax. For more information about the syntax, see Linking a pull request to an issue.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for closed
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
commented
A comment was added to the issue or pull request.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for commented
This events properties do not use the same structure as the issue event object common properties. The following properties are returned for this event.
NameTypeDescriptionurlstringThe REST API URL to retrieve the issue comment.html_urlstringThe HTML URL of the issue comment.issue_urlstringThe HTML URL of the issue.idintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.userobjectThe person who commented on the issue.created_atstringThe timestamp indicating when the comment was added.updated_atstringThe timestamp indicating when the comment was updated or created, if the comment is never updated.author_associationstringThe permissions the user has in the issue's repository. For example, the value would be "OWNER" if the owner of repository created a comment.bodystringThe comment body text.eventstringThe event value is "commented".actorobjectThe person who generated the event.
committed
A commit was added to the pull request's HEAD branch.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for committed
This events properties do not use the same structure as the issue event object common properties. The following properties are returned for this event.
NameTypeDescriptionshastringThe SHA of the commit in the pull request.node_idstringThe Global Node ID of the event.urlstringThe REST API URL to retrieve the commit.html_urlstringThe HTML URL of the commit.authorobjectThe person who authored the commit.committerobjectThe person who committed the commit on behalf of the author.treeobjectThe Git tree of the commit.messagestringThe commit message.parentsarray of objectsA list of parent commits.verificationobjectThe result of verifying the commit's signature. For more information, see REST API endpoints for Git commits.eventstringThe event value is "committed".
connected
The issue or pull request was linked to another issue or pull request. For more information, see Linking a pull request to an issue.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for connected
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
convert_to_draft
The pull request was converted to draft mode.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for convert_to_draft
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
converted_to_discussion
The issue was closed and converted to a discussion.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssues
Properties for converted_to_discussion
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
cross-referenced
The issue or pull request was referenced from another issue or pull request.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for cross-referenced
This events properties do not use the same structure as the issue event object common properties. The following properties are returned for this event.
NameTypeDescriptionactorobjectThe person who generated the event.created_atstringThe timestamp indicating when the cross-reference was added.updated_atstringThe timestamp indicating when the cross-reference was updated or created, if the cross-reference is never updated.sourceobjectThe issue or pull request that added a cross-reference.source[type]stringThis value will always be "issue" because pull requests are of type issue. Only cross-reference events triggered by issues or pull requests are returned in the REST API for timeline events. To determine if the issue that triggered the event is a pull request, you can check if the source[issue][pull_request] object exists.source[issue]objectThe issue object that added the cross-reference.eventstringThe event value is "cross-referenced".
demilestoned
The issue or pull request was removed from a milestone.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for demilestoned
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.milestoneobjectThe milestone object.milestone[title]stringThe title of the milestone.
deployed
The pull request was deployed.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for deployed
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
deployment_environment_changed
The pull request deployment environment was changed.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for deployment_environment_changed
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
disconnected
The issue or pull request was unlinked from another issue or pull request. For more information, see Linking a pull request to an issue.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for disconnected
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
head_ref_deleted
The pull request's HEAD branch was deleted.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for head_ref_deleted
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
head_ref_restored
The pull request's HEAD branch was restored to the last known commit.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
head_ref_force_pushed
The pull request's HEAD branch was force pushed.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for head_ref_force_pushed
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
labeled
A label was added to the issue or pull request.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for labeled
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.labelobjectThe label added or removed from the issuelabel[name]stringThe name of the label.label[color]stringThe hex color code.
locked
The issue or pull request was locked.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for locked
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.lock_reasonstringThe reason an issue or pull request conversation was locked, if one was provided.
mentioned
The actor was @mentioned in an issue or pull request body.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for mentioned
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
marked_as_duplicate
A user with write permissions marked an issue as a duplicate of another issue, or a pull request as a duplicate of another pull request.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for marked_as_duplicate
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
merged
The pull request was merged. The commit_id attribute is the SHA1 of the HEAD commit that was merged. The commit_repository is always the same as the main repository.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for merged
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
milestoned
The issue or pull request was added to a milestone.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for milestoned
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.milestoneobjectThe milestone object.milestone[title]stringThe title of the milestone.
pinned
The issue was pinned.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssues
Properties for pinned
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
ready_for_review
A draft pull request was marked as ready for review.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for ready_for_review
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
referenced
The issue was referenced from a commit message. The commit_id attribute is the commit SHA1 of where that happened and the commit_repository is where that commit was pushed.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for referenced
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
renamed
The issue or pull request title was changed.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for renamed
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.renameobjectThe name details.rename[from]stringThe previous name.rename[to]stringThe new name.
reopened
The issue or pull request was reopened.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for reopened
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
review_dismissed
The pull request review was dismissed.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for review_dismissed
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.dismissed_reviewobjectThe information for the dismissed review.dismissed_review[state]stringThe state the pull request was in when it was dismissed. Can be one of: commented, approved, or changes_requested.dismissed_review[review_id]stringThe unique identifier of the pull request's review.dismissed_review[dismissal_message]stringThe message the user included when dismissing the review.dismissed_review[dismissal_commit_id]stringThe unique identifier of the commit that dismissed the review if one exists.
review_requested
A pull request review was requested.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for review_requested
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.requested_reviewerobjectThe person requested to review the pull request.review_requesterobjectThe person who requested a review.
review_request_removed
A pull request review request was removed.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for review_request_removed
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.requested_reviewerobjectThe person requested to review the pull request.review_requesterobjectThe person who requested a review.
reviewed
The pull request was reviewed.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsPull requests
Properties for reviewed
This events properties do not use the same structure as the issue event object common properties. The following properties are returned for this event.
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.userobjectThe person who commented on the issue.bodystringThe review summary text.commit_idstringThe SHA of the latest commit in the pull request at the time of the review.submitted_atstringThe timestamp indicating when the review was submitted.statestringThe state of the submitted review. Can be one of: commented, changes_requested, approved or dismissed.html_urlstringThe HTML URL of the review.pull_request_urlstringThe REST API URL to retrieve the pull request.author_associationstringThe permissions the user has in the issue's repository. For example, the value would be "OWNER" if the owner of repository created a comment._linksobjectThe html_url and pull_request_url.eventstringThe event value is "reviewed".
subscribed
Someone subscribed to receive notifications for an issue or pull request.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for subscribed
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
transferred
The issue was transferred to another repository.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssues
Properties for transferred
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
unassigned
A user was unassigned from the issue.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for unassigned
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.assigneeobjectThe person unassigned from this issue.assignerobjectThe person who performed the unassignment for this issue. This field is available in the REST API for issue events but not the REST API for timeline events.
unlabeled
A label was removed from the issue.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for unlabeled
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.labelobjectThe label added or removed from the issuelabel[name]stringThe name of the label.label[color]stringThe hex color code.
unlocked
The issue was unlocked.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for unlocked
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.lock_reasonstringThe reason an issue or pull request conversation was locked, if one was provided.
unmarked_as_duplicate
An issue that a user had previously marked as a duplicate of another issue is no longer considered a duplicate, or a pull request that a user had previously marked as a duplicate of another pull request is no longer considered a duplicate.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for unmarked_as_duplicate
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
unpinned
The issue was unpinned.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssues
Properties for unpinned
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
unsubscribed
Someone unsubscribed from receiving notifications for an issue or pull request.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for unsubscribed
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.
user_blocked
An organization owner blocked a user from the organization. This was done through one of the blocked user's comments on the issue.
This event is available for the following issue types.
REST API for issue eventsREST API for timeline eventsIssuesPull requests
Properties for user_blocked
NameTypeDescriptionidintegerThe unique identifier of the event.node_idstringThe Global Node ID of the event.urlstringThe REST API URL for fetching the event.actorobjectThe person who generated the event.eventstringIdentifies the actual type of event that occurred.commit_idstringThe SHA of the commit that referenced this issue.commit_urlstringThe GitHub REST API link to the commit that referenced this issue.created_atstringThe timestamp indicating when the event occurred.Help and supportDid you find what you needed? Yes NoPrivacy policyHelp us make these docs great!All GitHub docs are open source. See something that's wrong or unclear? Submit a pull request.Make a contributionLearn how to contributeStill need help?Ask the GitHub communityContact supportLegal© 2026 GitHub, Inc.TermsPrivacyStatusPricingExpert servicesBlog