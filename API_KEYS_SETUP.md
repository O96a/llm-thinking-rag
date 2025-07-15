# 🔑 API Keys Setup Guide

This document provides step-by-step instructions for obtaining all the required API keys to run the Agentic RAG application.

## 🤖 Google AI API Key (Required)

The Google AI API key is required for accessing Gemini models and embeddings.

### Steps to Get Google AI API Key:

1. **Visit Google AI Studio**:
   - Go to [https://aistudio.google.com/](https://aistudio.google.com/)

2. **Sign In**:
   - Use your Google account to sign in

3. **Get API Key**:
   - Click on "Get API Key" in the left sidebar
   - Click "Create API Key"
   - Select an existing Google Cloud project or create a new one
   - Copy the generated API key

4. **Enable Required APIs** (if needed):
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Navigate to "APIs & Services" > "Library"
   - Search for and enable:
     - "Generative Language API"
     - "AI Platform API"

### Pricing:
- Google AI Studio offers generous free tier
- Check current pricing at [Google AI Pricing](https://ai.google.dev/pricing)

---

## 🗄️ Qdrant Cloud (Required)

Qdrant is used as the vector database for storing and searching document embeddings.

### Steps to Get Qdrant API Key:

1. **Visit Qdrant Cloud**:
   - Go to [https://cloud.qdrant.io/](https://cloud.qdrant.io/)

2. **Create Account**:
   - Sign up with your email or GitHub account
   - Verify your email address

3. **Create a Cluster**:
   - Click "Create Cluster"
   - Choose a cluster name
   - Select region (choose closest to your location)
   - Choose cluster size (Free tier: 1GB storage, 100K vectors)
   - Click "Create"

4. **Get API Credentials**:
   - Once cluster is created, go to "Clusters" page
   - Click on your cluster name
   - In the "Overview" tab, you'll find:
     - **Cluster URL**: `https://your-cluster-id.cloud.qdrant.io:6333`
     - **API Key**: Click "Show API Key" to reveal

### Free Tier:
- 1GB storage
- 100,000 vectors
- Perfect for testing and small projects

### Pricing:
- Check current pricing at [Qdrant Pricing](https://qdrant.tech/pricing/)

---

## 🔍 Exa AI API Key (Optional - For Web Search)

Exa AI provides advanced web search capabilities with semantic search.

### Steps to Get Exa AI API Key:

1. **Visit Exa AI**:
   - Go to [https://exa.ai/](https://exa.ai/)

2. **Sign Up**:
   - Click "Get Started" or "Sign Up"
   - Create an account with your email

3. **Get API Key**:
   - Once logged in, go to your dashboard
   - Navigate to "API Keys" section
   - Click "Create API Key"
   - Copy the generated API key

### Free Tier:
- 1,000 searches per month
- Basic search features

### Pricing:
- Check current pricing at [Exa AI Pricing](https://exa.ai/pricing)

---

## 🛡️ Security Best Practices

### 1. Environment Variables (Recommended for Production)

Create a `.env` file in your project root:

```bash
GOOGLE_API_KEY=your_google_api_key_here
QDRANT_API_KEY=your_qdrant_api_key_here
QDRANT_URL=https://your-cluster.cloud.qdrant.io:6333
EXA_API_KEY=your_exa_api_key_here
```

### 2. Using Environment Variables in Code

If you want to use environment variables instead of the sidebar inputs, modify the code:

```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# In session state initialization
if 'google_api_key' not in st.session_state:
    st.session_state.google_api_key = os.getenv('GOOGLE_API_KEY', '')
if 'qdrant_api_key' not in st.session_state:
    st.session_state.qdrant_api_key = os.getenv('QDRANT_API_KEY', '')
if 'qdrant_url' not in st.session_state:
    st.session_state.qdrant_url = os.getenv('QDRANT_URL', '')
if 'exa_api_key' not in st.session_state:
    st.session_state.exa_api_key = os.getenv('EXA_API_KEY', '')
```

### 3. Never Commit API Keys

Add to your `.gitignore`:

```bash
.env
*.key
config.json
secrets/
```

---

## 🧪 Testing Your Setup

### 1. Test Google AI API:

```python
import google.generativeai as genai

genai.configure(api_key="your_api_key")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Hello, world!")
print(response.text)
```

### 2. Test Qdrant Connection:

```python
from qdrant_client import QdrantClient

client = QdrantClient(
    url="your_qdrant_url",
    api_key="your_qdrant_api_key"
)
print(client.get_collections())
```

### 3. Test Exa AI:

```python
from exa_py import Exa

exa = Exa(api_key="your_exa_api_key")
results = exa.search("latest AI developments", num_results=3)
print(results)
```

---

## ❗ Troubleshooting

### Common Issues:

1. **Google AI API 403 Error**:
   - Check if Generative Language API is enabled in Google Cloud Console
   - Verify API key is correct and has proper permissions

2. **Qdrant Connection Failed**:
   - Verify cluster URL format: `https://cluster-id.cloud.qdrant.io:6333`
   - Check if API key is correct
   - Ensure cluster is running (not paused)

3. **Exa AI Rate Limit**:
   - Check your usage in Exa dashboard
   - Consider upgrading if you've exceeded free tier limits

4. **Network Issues**:
   - Check firewall settings
   - Verify internet connection
   - Some corporate networks may block certain APIs

---

## 💡 Tips for Cost Management

1. **Monitor Usage**:
   - Regularly check your API usage in each service's dashboard
   - Set up billing alerts where available

2. **Optimize Requests**:
   - Use appropriate chunk sizes for documents
   - Implement caching for repeated queries
   - Use similarity thresholds to reduce unnecessary API calls

3. **Development vs Production**:
   - Use smaller models for development and testing
   - Consider rate limiting in production applications

---

## 📞 Support

If you encounter issues getting API keys:

- **Google AI**: [Google AI Support](https://ai.google.dev/support)
- **Qdrant**: [Qdrant Documentation](https://qdrant.tech/documentation/) or [Discord Community](https://discord.gg/qdrant)
- **Exa AI**: [Exa AI Support](https://exa.ai/support)

For application-specific issues, please create an issue in this repository.
