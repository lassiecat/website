#!/bin/bash
# LassieCat Website - Automated GitHub Setup Script
# Run this to deploy your website to GitHub Pages

set -e

echo "🚀 LassieCat Website - GitHub Setup"
echo "===================================="
echo ""

# Step 1: Configure Git
echo "1️⃣  Configuring Git..."
read -p "Your GitHub username: " GH_USER
read -p "Your email: " GH_EMAIL

git config --global user.name "$GH_USER"
git config --global user.email "$GH_EMAIL"
echo "   ✅ Git configured"
echo ""

# Step 2: Install GitHub CLI if not present
echo "2️⃣  Checking GitHub CLI..."
if ! command -v gh &> /dev/null; then
    echo "   Installing GitHub CLI via Homebrew..."
    brew install gh
else
    echo "   ✅ GitHub CLI found"
fi
echo ""

# Step 3: Authenticate
echo "3️⃣  GitHub Authentication"
echo "   Run: gh auth login"
echo "   Choose: GitHub.com > HTTPS > Login with browser"
gh auth login
echo "   ✅ Authenticated"
echo ""

# Step 4: Create repository
echo "4️⃣  Creating GitHub repository..."
gh repo create website --description "The official LassieCat cryptocurrency website" --public --source=. --push
echo "   ✅ Repository created and code pushed!"
echo ""

# Step 5: Enable GitHub Pages
echo "5️⃣  Enabling GitHub Pages..."
gh repo pages --source main --branch
echo "   ✅ GitHub Pages enabled!"
echo ""

# Summary
echo "===================================="
echo "🎉 Website Deployed Successfully!"
echo ""
echo "🌐 Your site will be live at:"
echo "   https://$GH_USER.github.io/website"
echo ""
echo "📁 Repository:"
echo "   https://github.com/$GH_USER/website"
echo ""
echo "💰 Cost: \$0 (GitHub Pages is free!)"
echo ""

