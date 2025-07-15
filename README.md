# 🤔 Agentic RAG with Gemini Flash Thinking

An intelligent Retrieval-Augmented Generation (RAG) application that combines Google's Gemini Flash Thinking model with advanced document retrieval and web search capabilities. This application provides a sophisticated chat interface for querying documents and web sources with intelligent query rewriting and multi-modal search strategies.

## ✨ Features

### 🧠 Advanced AI Capabilities
- **Gemini Flash Thinking**: Utilizes Google's latest `gemini-2.0-flash-thinking-exp-01-21` model for enhanced reasoning
- **Intelligent Query Rewriting**: Automatically reformulates user queries for better retrieval accuracy
- **Multi-Agent Architecture**: Specialized agents for query rewriting, web search, and response generation

### 📚 Document Processing
- **PDF Support**: Upload and process PDF documents with automatic text extraction
- **Web Content**: Extract and process content from web URLs
- **Smart Chunking**: Recursive text splitting with configurable chunk sizes and overlaps
- **Metadata Enrichment**: Automatic source tracking and timestamp addition

### 🔍 Advanced Search & Retrieval
- **Vector Database**: Qdrant integration for semantic similarity search
- **Configurable Similarity Threshold**: Adjustable relevance filtering (0.0-1.0)
- **Hybrid Search Strategy**: Documents + Web search fallback
- **Force Web Search**: Manual override to search web directly

### 🌐 Web Search Integration
- **Exa AI Integration**: Advanced web search capabilities with domain filtering
- **Domain Filtering**: Configurable search domains (arxiv.org, wikipedia.org, github.com, etc.)
- **Intelligent Fallback**: Automatic web search when document relevance is low

### 💬 Interactive Chat Interface
- **Persistent Chat History**: Maintains conversation context
- **Source Attribution**: Clear indication of information sources
- **Real-time Processing**: Live document uploading and processing
- **Rich UI**: Streamlit-based interface with expandable sections

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Models**: 
  - **Main RAG Agent**: `gemini-2.0-flash-thinking-exp-01-21` (Google's latest thinking model)
  - **Query Rewriter**: `gemini-exp-1206` (Experimental model for query optimization)
  - **Web Search Agent**: `gemini-exp-1206` (For web search result processing)
  - **Embeddings**: `text-embedding-004` (768-dimensional embeddings)
- **Vector Database**: Qdrant Cloud
- **Document Processing**: LangChain, PyPDF
- **Web Search**: Exa AI
- **Agent Framework**: Agno
- **Text Processing**: BeautifulSoup4, Recursive Character Text Splitter

## 📋 Prerequisites

### Required API Keys
1. **Google AI API Key**: For Gemini models and embeddings
   - Get from: [Google AI Studio](https://aistudio.google.com/)
   
2. **Qdrant Cloud**: Vector database service
   - Get from: [Qdrant Cloud](https://cloud.qdrant.io/)
   - You'll need both API key and cluster URL
   
3. **Exa AI API Key** (Optional): For web search functionality
   - Get from: [Exa AI](https://exa.ai/)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "Agentic RAG with Gemini Flash Thinking"
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run main.py
   ```

## 🎯 How to Start

### Quick Start Guide

1. **Run the Setup Script** (Recommended):
   ```bash
   python setup.py
   ```
   This will check your environment, install dependencies, and create a .env template.

2. **Get Your API Keys** (See [API_KEYS_SETUP.md](API_KEYS_SETUP.md) for detailed instructions):
   - **Google AI API Key** (Required): Get from [Google AI Studio](https://aistudio.google.com/)
   - **Qdrant Cloud** (Required): Get from [Qdrant Cloud](https://cloud.qdrant.io/)
   - **Exa AI API Key** (Optional): Get from [Exa AI](https://exa.ai/)

3. **Configure API Keys**:
   - Option A: Enter them in the Streamlit sidebar when you run the app
   - Option B: Create a `.env` file and add your keys:
     ```bash
     GOOGLE_API_KEY=your_google_api_key_here
     QDRANT_API_KEY=your_qdrant_api_key_here
     QDRANT_URL=https://your-cluster.cloud.qdrant.io:6333
     EXA_API_KEY=your_exa_api_key_here
     ```

4. **Launch the Application**:
   ```bash
   streamlit run main.py
   ```

5. **First Steps in the App**:
   - Enter your API keys in the sidebar (if not using .env)
   - Upload a PDF document or enter a web URL
   - Wait for processing to complete
   - Start asking questions about your documents!

### Example First Session

1. **Upload a Document**: Try uploading a research paper (PDF) or enter a Wikipedia URL
2. **Ask a Question**: "What are the main points discussed in this document?"
3. **Explore Features**: 
   - Try the 🌐 toggle to force web search
   - Adjust the similarity threshold slider
   - View the "See rewritten query" and "See document sources" sections

### Troubleshooting First Run

- **"Please enter your Google API Key"**: Make sure you've entered a valid Google AI API key
- **"Qdrant connection failed"**: Check your Qdrant API key and URL format
- **Document processing errors**: Ensure your PDF is text-based (not scanned images)
- **Web search not working**: Verify your Exa AI API key and enable web search in settings

## ⚙️ Configuration

### API Configuration
1. **Google API Key**: Required for all AI operations
2. **Qdrant Settings**:
   - API Key: Your Qdrant Cloud API key
   - URL: Your cluster URL (format: `https://your-cluster.cloud.qdrant.io:6333`)

### Web Search Configuration (Optional)
- **Enable Web Search Fallback**: Checkbox to enable/disable web search
- **Exa AI API Key**: Required if web search is enabled
- **Custom Domains**: Comma-separated list of domains to search

### Search Configuration
- **Similarity Threshold**: Slider (0.0-1.0) to control document relevance filtering
  - Lower values: More documents, potentially less relevant
  - Higher values: Fewer documents, higher relevance

## 📖 Usage

### Basic Workflow
1. **Configure APIs**: Enter your API keys in the sidebar
2. **Upload Documents**: 
   - Upload PDF files using the file uploader
   - Add web URLs for content extraction
3. **Configure Search**: Adjust similarity threshold and web search options
4. **Start Chatting**: Ask questions about your uploaded documents

### Advanced Features
- **Force Web Search**: Use the 🌐 toggle to bypass document search and search the web directly
- **Query Rewriting**: View how your questions are automatically reformulated for better results
- **Source Attribution**: Expand sections to see which documents or web sources provided information

### Example Use Cases
- **Research**: Upload academic papers and ask specific questions
- **Documentation**: Process technical documentation and get quick answers
- **Content Analysis**: Analyze web articles and extract key insights
- **Knowledge Base**: Build a searchable knowledge base from multiple sources

## 🔧 Architecture

### Components
1. **GeminiEmbedder**: Custom embedding class using Google's `text-embedding-004` model
2. **Query Rewriter Agent**: Reformulates user queries using `gemini-exp-1206` for better retrieval
3. **Web Search Agent**: Handles web search using `gemini-exp-1206` with Exa AI tools
4. **RAG Agent**: Main response generation using `gemini-2.0-flash-thinking-exp-01-21` (Google's latest thinking model)
5. **Vector Store**: Qdrant-based semantic search and storage

### AI Model Roles
- **`gemini-2.0-flash-thinking-exp-01-21`**: Primary reasoning and response generation with enhanced thinking capabilities
- **`gemini-exp-1206`**: Query optimization and web search result processing
- **`text-embedding-004`**: Document and query embeddings for semantic similarity search

### Search Strategy
1. **Query Rewriting**: Improve query specificity and detail using experimental Gemini model
2. **Document Search**: Semantic similarity search in vector database using embeddings
3. **Relevance Check**: Filter results based on similarity threshold
4. **Web Fallback**: Search web if no relevant documents found using Exa AI
5. **Response Generation**: Synthesize final answer using Gemini Flash Thinking with source attribution

## 🔒 Security Notes

- API keys are stored in Streamlit session state (not persistent)
- Use password-type inputs for sensitive information
- Consider using environment variables for production deployments

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this application.

## 📄 License

This project is open source. Please check the license file for details.

## 🆘 Troubleshooting

### Common Issues
1. **Qdrant Connection Failed**: Verify your API key and URL format
2. **Google API Errors**: Ensure your API key has proper permissions
3. **Document Processing Errors**: Check file format and size limitations
4. **Web Search Not Working**: Verify Exa AI API key and domain settings

### Support
For technical issues, please check the error messages in the Streamlit interface or create an issue in the repository.
