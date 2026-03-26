# 🚚 ShipSense AI

**Intelligent Shipment Diagnostics — Powered by GenAI**

ShipSense AI is a modern web application that provides AI-powered insights and diagnostics for shipment tracking and issue resolution. Built with Streamlit and integrated with n8n workflows, it delivers intelligent analysis of shipment data in a beautiful, user-friendly interface.

---

## ✨ Features

- 🎯 **Smart Shipment Selection** - Quick dropdown access to 200 shipment IDs
- 🤖 **AI-Powered Analysis** - GenAI-driven insights and recommendations
- 🎨 **Modern UI** - Dark-themed, responsive interface with custom styling
- ⚡ **Real-time Processing** - Instant analysis via n8n webhook integration
- 📊 **Detailed Diagnostics** - Comprehensive shipment issue summaries
- 🔍 **Raw Data View** - Expandable JSON response for debugging

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **HTTP Client**: Requests
- **Automation Backend**: n8n (hosted on Railway)
- **Styling**: Custom CSS with Space Mono & DM Sans fonts
- **API Integration**: RESTful webhook

---

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.7 or higher
- pip (Python package manager)
- Active n8n webhook endpoint (or use the default)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/siddharthpurswani/Shipment_issue_summary.git
cd Shipment_issue_summary
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install streamlit requests
```

### 3. Configure n8n Webhook (Optional)

If you have your own n8n instance, update the webhook URL in `app.py`:

```python
N8N_WEBHOOK_URL = "https://your-n8n-instance.com/webhook/shipment-lookup"
```

---

## 🎮 Usage

### Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

### Using the Interface

1. **Select Shipment ID**: Choose from the dropdown menu (200+ shipments available)
2. **Click Analyze**: Hit the "🔍 Analyze" button
3. **View Results**: AI-generated insights appear in the GenAI Reasoning box
4. **Check Raw Data**: Expand "Raw n8n Response" for detailed JSON output

---

## 📁 Project Structure

```
Shipment_issue_summary/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── Shipment Tracker (1).json   # n8n workflow
└── README.md                   # This file
```

---

## 🔧 Configuration

### Shipment IDs

The application includes 200 pre-configured shipment IDs. To add or modify:

1. Open `app.py`
2. Locate the `SHIPMENT_IDS` list
3. Add/remove shipment ID numbers

### Webhook Integration

The app sends POST requests to the n8n webhook with this payload:

```json
{
  "shipment_id": 690
}
```

**Expected Response Format:**

```json
{
  "text": "AI-generated analysis text...",
  "ai_response": "Alternative response key...",
  "output": "Another possible key..."
}
```

The app checks for `text`, `ai_response`, `output`, or `message` keys in the response.

---

## 🎨 Customization


## 🔌 n8n Workflow Setup

<img width="1156" height="528" alt="image" src="https://github.com/user-attachments/assets/b4691f96-8d14-434b-bd68-7c6c3048cd60" />

---
## Sample Output

<img width="1059" height="723" alt="image" src="https://github.com/user-attachments/assets/c5344015-c070-4ae1-8d7d-2d5bc07ae81f" />

## 🐛 Troubleshooting

### Connection Errors

**Error**: `Could not connect to n8n`

**Solution**: 
- Verify n8n workflow is active
- Check webhook URL is correct
- Ensure network connectivity

### Timeout Issues

**Error**: `Request timed out`

**Solution**:
- Increase timeout value in `app.py` (default: 30s)
- Optimize n8n workflow performance

### No AI Response

**Error**: `n8n responded but returned no text`

**Solution**:
- Verify n8n output key matches expected format
- Check the "Raw n8n Response" expander
- Ensure AI node is properly configured

---

## 🚢 Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy with one click


## 👨‍💻 Author

**Siddharth Purswani**

- GitHub: [@siddharthpurswani](https://github.com/siddharthpurswani)

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Automation powered by [n8n](https://n8n.io/)
- Hosted on [Railway](https://railway.app/)
- AI capabilities via Large Language Models

---

## 📧 Support

For issues, questions, or suggestions:

- Open an issue on [GitHub Issues](https://github.com/siddharthpurswani/Shipment_issue_summary/issues)
- Contact the maintainer

---

## 📸 Screenshots

### Main Interface
```
🚚 ShipSense AI
Intelligent Shipment Diagnostics — Powered by GenAI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Select Shipment ID ▼]  [🔍 Analyze]

╔═══════════════════════════════════════╗
║  ● GenAI Reasoning                    ║
║                                       ║
║  [AI-generated insights appear here]  ║
╚═══════════════════════════════════════╝
```

---
