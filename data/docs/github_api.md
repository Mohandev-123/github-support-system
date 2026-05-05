# GitHub API Documentation

## Authentication

### Personal Access Tokens

GitHub uses personal access tokens (PATs) for authentication. To create a PAT:

1. Go to GitHub Settings > Developer settings > Personal access tokens
2. Click "Generate new token"
3. Select scopes needed for your application
4. Store the token securely

### OAuth Applications

For web applications, use OAuth 2.0 authentication:
- Redirect users to GitHub authorization endpoint
- Exchange authorization code for access token
- Use token to make API requests

## Common API Endpoints

### Users
- `GET /users/{username}` - Get user information
- `GET /user` - Get authenticated user
- `PATCH /user` - Update authenticated user

### Repositories
- `GET /repos/{owner}/{repo}` - Get repository
- `GET /user/repos` - List authenticated user's repositories
- `POST /user/repos` - Create new repository

### Issues
- `GET /repos/{owner}/{repo}/issues` - List repository issues
- `POST /repos/{owner}/{repo}/issues` - Create issue
- `PATCH /repos/{owner}/{repo}/issues/{number}` - Update issue

## Rate Limiting

- Unauthenticated requests: 60 requests per hour
- Authenticated requests: 5000 requests per hour
- GraphQL: 5000 points per hour

Check rate limit status: `GET /rate_limit`

## Webhooks

Webhooks allow you to build integrations that subscribe to events on GitHub.

### Setting Up Webhooks
1. Go to repository Settings > Webhooks
2. Choose events to subscribe to
3. Provide payload URL for receiving notifications

### Webhook Events
- push - Code pushed to repository
- pull_request - Pull request created/updated
- issues - Issue created/updated
- repository - Repository created/deleted
