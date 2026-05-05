#!/bin/bash
# Quick setup script for GitHub Support System

echo "🚀 GitHub Support System Setup"
echo "=============================="

# Activate venv
if [ -d "venv" ]; then
    echo "✓ Virtual environment exists"
    source venv/Scripts/activate
else
    echo "✗ Virtual environment not found. Run: python -m venv venv"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt -q

# Setup environment
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "⚠️  Update .env with your Anthropic API key"
fi

# Create data directories
mkdir -p data/docs data/embeddings

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Add GitHub docs to data/docs/"
echo "2. Run: python main.py ingest data/docs"
echo "3. Run: python main.py"
