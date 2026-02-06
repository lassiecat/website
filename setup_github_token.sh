#!/bin/bash
# LassieCat Website - GitHub Setup with Token
# Use this if you have a GitHub Personal Access Token

set -e

echo "🚀 LassieCat Website - GitHub Setup"
echo "===================================="
echo ""

# Configuration
REPO_NAME="website"
REPO_DESC="The official LassieCat cryptocurrency website"
DIR=~/.openclaw/workspace/lassiecat-website

# Check for token
if [ -z "$1" ]; then
    echo "Usage: $0 YOUR_GITHUB_TOKEN"
    echo ""
    echo "To create a token:"
    echo "1. Go to: https://github.com/settings/tokens"
    echo "2. Click: Generate new token (classic)"
    echo "3. Note: 'repo' scope required"
    echo "4. Copy the token"
    echo ""
    echo "Then run: $0 YOUR_TOKEN"
    exit 1
fi

TOKEN="$1"
GH_USER=$(curl -s -H "Authorization: token $TOKEN" https://api.github.com/user | grep -o '"login": "[^"]*"' | cut -d'"' -f4)

echo "📦 Setting up for: @$GH_USER"
echo ""

# Configure git
echo "1️⃣  Configuring Git..."
read -p "Your email: " GH_EMAIL
git config --global user.name "$GH_USER"
git config --global user.email "$GH_EMAIL"
echo "   ✅ Git configured"
echo ""

# Create repository via API
echo "2️⃣  Creating repository..."
RESPONSE=$(curl -s -X POST -H "Authorization: token $TOKEN" \
  -d "{\"name\":\"$REPO_NAME\",\"description\":\"$REPO_DESC\",\"private\":false}" \
  https://api.github.com/user/repos 2>/dev/null)

if echo "$RESPONSE" | grep -q '"id"'; then
    echo "   ✅ Repository created!"
else
    echo "   ℹ️  Repository might already exist"
fi
echo ""

# Add remote and push
echo "3️⃣  Pushing code..."
cd "$DIR"
git remote remove origin 2>/dev/null || true
git remote add origin "https://$TOKEN@github.com/$GH_USER/$REPO_NAME.git"
git branch -M main
git push -u origin main
echo "   ✅ Code pushed!"
echo ""

# Enable Pages via API
echo "4️⃣  Enabling GitHub Pages..."
curl -s -X POST -H "Authorization: token $TOKEN" \
  -d "{\"source\":{\"branch\":\"main\"},\"path\":\"/\"}" \
  "https://api.github.com/repos/$GH_USER/$REPO_NAME/pages"
echo "   ✅ GitHub Pages enabled!"
echo ""

# Summary
echo "===================================="
echo "🎉 Website Deployed Successfully!"
echo ""
echo "🌐 Your site will be live at:"
echo "   https://$GH_USER.github.io/$REPO_NAME"
echo ""
echo "📁 Repository:"
echo "   https://github.com/$GH_USER/$REPO_NAME"
echo ""
echo "💰 Cost: \$0 (GitHub Pages is free!)"

