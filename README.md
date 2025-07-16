# A2A MCP Integration Project

A sophisticated Agent-to-Agent (A2A) integration system featuring specialized agents for text-to-speech conversion and Notion workspace management. Built with Google's Agent Development Kit (ADK) and Model Control Protocol (MCP).

## 🚀 Features

### ElevenLabs Agent
- **Text-to-Speech Conversion**: Convert text to high-quality speech using ElevenLabs API
- **Automated Processing**: Handles file generation and path management
- **MCP Integration**: Uses Model Control Protocol for seamless API communication

### Notion Agent
- **Workspace Search**: Search and retrieve information from Notion pages and databases
- **Database Queries**: Query Notion databases with structured responses
- **Smart ID Resolution**: Automatically extracts and uses database/page IDs from URLs
- **A2A Service**: Runs as a standalone service for agent-to-agent communication

## 🏗️ Architecture

```
adk-mcp-a2a/
├── elevenlabs_agent/          # ElevenLabs TTS agent
│   ├── agent.py              # Agent configuration and setup
│   ├── agent_executor.py     # Agent execution logic
│   ├── prompt.py             # Agent instructions and prompts
│   └── __main__.py           # Entry point
├── notion_agent/             # Notion workspace agent
│   ├── agent.py              # Agent configuration and setup
│   ├── agent_executor.py     # A2A integration and execution
│   ├── prompt.py             # Agent instructions and prompts
│   └── __main__.py           # A2A service entry point
├── utils/
│   └── custom_adk_patches.py # Custom MCP timeout patches
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## 🛠️ Setup

### Prerequisites
- Python 3.8+
- Node.js (for Notion MCP server)
- API Keys for ElevenLabs and/or Notion

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/adk-mcp-a2a.git
cd adk-mcp-a2a
```

2. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:
Create a `.env` file in the root directory:
```env
# ElevenLabs Configuration
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

# Notion Configuration
NOTION_API_KEY=your_notion_api_key_here

# AI Model Configuration
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# A2A Server Configuration (optional)
A2A_NOTION_HOST=localhost
A2A_NOTION_PORT=8002
```

### API Key Setup

#### ElevenLabs
1. Visit [ElevenLabs](https://elevenlabs.io/)
2. Create an account and get your API key
3. Add to `.env` file as `ELEVENLABS_API_KEY`

#### Notion
1. Visit [Notion Developers](https://developers.notion.com/)
2. Create an integration and get your API key
3. Add to `.env` file as `NOTION_API_KEY`
4. Share your Notion pages/databases with the integration

## 🎯 Usage

### ElevenLabs Agent

The ElevenLabs agent converts text to speech using the ElevenLabs API:

```python
from elevenlabs_agent.agent import create_elevenlabs_agent

# Create agent instance
agent = create_elevenlabs_agent()

# Use with ADK Runner for text-to-speech conversion
# Input: "Convert this text to speech"
# Output: Audio file path with speech synthesis
```

### Notion Agent

#### As a Standalone A2A Service

Run the Notion agent as a service:

```bash
python -m notion_agent --host localhost --port 8002
```

The agent will be available at `http://localhost:8002` and provides:
- **Search Capability**: "Search for 'project plan'"
- **Database Queries**: "Find pages about Q3 goals"
- **Information Retrieval**: "Retrieve meeting notes from database"

#### Direct Integration

```python
from notion_agent.agent import create_notion_agent

# Create agent instance
agent = create_notion_agent()

# Use with ADK Runner for Notion operations
```

## 🔧 Configuration

### Custom MCP Timeout

The project includes custom patches for MCP timeout configuration to handle longer operations:

```python
# In utils/custom_adk_patches.py
CUSTOM_STDIO_TIMEOUT_SECONDS = 180  # 3 minutes
```

This addresses the hardcoded 5-second timeout in google-adk 1.2.0, allowing for:
- ElevenLabs TTS processing
- Large Notion database queries
- Extended model operations

### Agent Capabilities

#### ElevenLabs Agent
- **Model**: Claude 3.5 Sonnet (via LiteLLM)
- **Tools**: ElevenLabs MCP server
- **Timeout**: 180 seconds for TTS processing

#### Notion Agent
- **Model**: Gemini 2.0 Flash
- **Tools**: Notion MCP server
- **A2A Integration**: Full A2A service support
- **Skills**: Search, database queries, information retrieval

## 📦 Dependencies

### Core Dependencies
- `google-adk==1.2.1` - Google Agent Development Kit
- `a2a-sdk==0.2.5` - Agent-to-Agent communication
- `fastapi==0.115.12` - Web framework for A2A services
- `litellm==1.72.0` - LLM integration library
- `uvicorn==0.34.3` - ASGI server
- `streamlit==1.45.1` - Web app framework

### Development Dependencies
- `black==25.1.0` - Code formatting
- `isort==6.0.1` - Import sorting
- `mypy==1.16.0` - Type checking
- `pytest==8.4.0` - Testing framework

## 🚦 Current Status

### ✅ Completed Features
- [x] ElevenLabs agent with MCP integration
- [x] Notion agent with A2A service capability
- [x] Custom MCP timeout patches
- [x] Environment variable configuration
- [x] A2A server setup for Notion agent
- [x] Comprehensive agent executors
- [x] Error handling and logging

### 🔄 In Progress
- [ ] ElevenLabs A2A service integration
- [ ] Advanced error recovery mechanisms
- [ ] Performance optimizations

### 📋 Planned Features
- [ ] Additional MCP server integrations
- [ ] Agent orchestration capabilities
- [ ] Advanced caching mechanisms
- [ ] Comprehensive test suite
- [ ] Docker containerization
- [ ] API documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛟 Support

For issues and questions:
1. Check the [Issues](https://github.com/yourusername/adk-mcp-a2a/issues) page
2. Review the ADK documentation
3. Check MCP server documentation for specific integrations

## 🔗 Related Projects

- [Google ADK Python](https://github.com/google/adk-python)
- [A2A SDK](https://github.com/a2a-sdk)
- [ElevenLabs MCP Server](https://github.com/elevenlabs/mcp-server)
- [Notion MCP Server](https://github.com/notionhq/notion-mcp-server)

---

**Note**: This project includes custom patches for MCP timeout configuration. See `utils/custom_adk_patches.py` for implementation details and [GitHub Issue #1086](https://github.com/google/adk-python/issues/1086) for context. 