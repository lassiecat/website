#!/bin/bash
# LassieCat Website Deployment Script

echo "🚀 Deploying LassieCat Website to GitHub Pages..."
echo ""

# Initialize git if needed
if [ ! -d .git ]; then
    echo "📦 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial LassieCat website commit"
    echo ""
    echo "⚠️  Before deploying, you need to:"
    echo "   1. Create a GitHub repository: lassiecat/website"
    echo "   2. Run: git remote add origin https://github.com/lassiecat/website.git"
    echo "   3. Run: git push -u origin main"
    echo ""
    echo "📖 Then enable GitHub Pages in repository Settings > Pages"
fi

echo "✅ Website ready for deployment!"
echo ""
echo "To deploy:"
echo "   1. Create GitHub repo: lassiecat/website"
echo "   2. Push to GitHub"
echo "   3. Enable GitHub Pages in Settings"
echo ""
echo "🌐 Your site will be live at:"
echo "   https://lassiecat.github.io/website"
echo ""
echo "Or connect a custom domain!"
