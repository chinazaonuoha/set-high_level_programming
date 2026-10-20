#!/usr/bin/env bash

# Exit immediately if a command fails, treat unset variables as errors,
# and prevent errors in pipelines from being masked.
set -euo pipefail

# --- CONFIGURATION & STYLING HELPERS ---
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

# --- CORE OPERATIONS ---

git_status() {
    info "Checking repository status..."
    git status
}

git_add() {
    info "Staging changes..."
    git add .
    success "Changes staged successfully."
}

git_commit() {
    local commit_msg="$1"
    
    # If no message was passed via command line, prompt the user interactively
    if [ -z "$commit_msg" ]; then
        read -rp "Enter commit message: " commit_msg
    fi

    if [ -z "$commit_msg" ]; then
        error "Commit message cannot be empty."
    fi

    info "Committing changes with message: '$commit_msg'"
    git commit -m "$commit_msg"
    success "Changes committed."
}

git_push() {
    local current_branch
    current_branch=$(git branch --show-current)
    
    info "Pushing to remote repository on branch '$current_branch'..."
    git push origin "$current_branch"
    success "Push completed successfully."
}

# --- EXTENSIBILITY HOOK ---
# Placeholder for future workflows (e.g., running tests, linting, or deploying)
custom_operation() {
    info "Running custom operation..."
    success "Custom operation completed."
}

# --- MAIN EXECUTION FLOW ---
main() {
    # 1. Guard check: Ensure we are inside a git repository
    if ! git rev-parse --is-inside-work-tree &>/dev/null; then
        error "Not inside a valid git repository."
    fi

    git_status

    # 2. Optimization check: Stop if there's nothing to commit
    if [[ -z $(git status --porcelain) ]]; then
        info "Working tree is clean. No changes to commit or push."
        exit 0
    fi

    # 3. Execute the core pipeline
    git_add
    git_commit "${1:-}"
    git_push

    # Uncomment below if you want to activate the extension hook automatically
    # custom_operation

    success "All git operations completed seamlessly!"
}

# Execute main, passing all command-line arguments forward
main "$@"