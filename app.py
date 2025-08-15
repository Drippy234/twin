# app.py
import gradio as gr
from features import build_model, find_top_matches
from utils import play_sound, generate_personality

# Load model
model, preprocess, device = build_model()

# Cartoon search
def cartoon_lookup(user_img):
    play_sound("cat.mp3")
    images, _ = find_top_matches(user_img, "famous cartoon character face", model, preprocess, device)
    if not images:
        return None, "No cartoon matches found.", ""
    return images, "Your cartoon twins are ready! 😆", generate_personality("You")

# Celebrity search
def celeb_lookup(user_img):
    play_sound("amongus.mp3")
    images, _ = find_top_matches(user_img, "celebrity headshot face", model, preprocess, device)
    if not images:
        return None, "No celebrity matches found.", ""
    return images, "You and these celebs could be siblings! 😎", generate_personality("You")

# UI with clean, elegant glass morphism design
with gr.Blocks(css="""
    /* Global Styles */
    * {
        box-sizing: border-box;
    }

    html, body {
        background: #ffffff !important;
        font-family: 'Inter', 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif !important;
        margin: 0 !important;
        padding: 0 !important;
        min-height: 100vh !important;
        overflow-x: hidden !important;
    }

    /* Gradio Container Transparency */
    .gradio-container, .gr-blocks, #root {
        background: transparent !important;
        background-color: transparent !important;
    }

    /* Main Container */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    /* Logo Container */
    .logo-container {
        text-align: center;
        margin-bottom: 30px;
        background: rgba(248, 250, 252, 0.8);
        backdrop-filter: blur(25px);
        padding: 30px;
        border-radius: 30px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(0, 166, 81, 0.2);
    }

    .logo-title {
        color: #0B6623;
        font-weight: bold;
        font-size: 48px;
        margin: 15px 0 5px 0;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.8);
        background: linear-gradient(135deg, #0B6623, #00A651);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .logo-subtitle {
        color: #666;
        font-size: 16px;
        font-weight: 500;
        margin: 0;
        font-style: italic;
    }
    /* Buttons */
    .gr-button {
        background: linear-gradient(135deg, #00A651 0%, #009246 100%) !important;
        color: white !important;
        border-radius: 25px;
        padding: 16px 32px;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0 4px 12px rgba(0,166,81,0.3);
        border: none !important;
        transition: all 0.3s ease;
        margin: 8px 0;
        width: 100%;
    }

    .gr-button:hover {
        background: linear-gradient(135deg, #009246 0%, #007a3d 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,166,81,0.4);
    }

    /* Gallery */
    .gr-gallery {
        border-radius: 20px;
        border: 1px solid rgba(0, 166, 81, 0.2);
        padding: 20px;
        background: rgba(248, 250, 252, 0.6);
        backdrop-filter: blur(20px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
        max-width: 600px;
        margin: 0 auto;
    }

    .gr-gallery img {
        max-width: 120px;
        max-height: 120px;
        border-radius: 12px;
        transition: transform 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    .gr-gallery img:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }

    /* Text Boxes */
    .gr-textbox {
        border-radius: 20px;
        border: 1px solid rgba(0, 166, 81, 0.2);
        padding: 20px;
        font-size: 18px;
        background: rgba(248, 250, 252, 0.6);
        backdrop-filter: blur(20px);
        color: #333;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
        transition: all 0.4s ease;
        animation: fadeInUp 0.6s ease-out;
    }

    .gr-textbox:focus-within {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.08);
        border-color: rgba(0, 146, 70, 0.4);
        background: rgba(248, 250, 252, 0.8);
    }

    .gr-textbox textarea {
        font-weight: 500;
        line-height: 1.5;
        background: transparent;
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    /* Layout Components */
    .gr-row {
        margin-bottom: 25px;
        justify-content: center;
    }

    .input-column, .results-column {
        background: rgba(248, 250, 252, 0.7);
        backdrop-filter: blur(25px);
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.06);
        min-height: 500px;
        border: 1px solid rgba(0, 166, 81, 0.15);
    }

    .input-column {
        margin-right: 15px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }

    .results-column {
        margin-left: 15px;
    }

    /* Image Component */
    .gr-image {
        max-width: 280px;
        max-height: 220px;
        margin: 0 auto 20px auto;
        border-radius: 20px;
        border: 1px solid rgba(0, 166, 81, 0.2);
        background: rgba(248, 250, 252, 0.6);
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
        padding: 12px;
        transition: all 0.3s ease;
    }

    .gr-image:hover {
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.08);
        transform: translateY(-3px);
        background: rgba(248, 250, 252, 0.8);
    }

    .gr-image > div {
        border-radius: 15px;
        overflow: hidden;
    }

    /* Typography */
    h3 {
        color: #0B6623;
        font-weight: bold;
        margin-bottom: 15px;
        margin-top: 10px;
        text-align: center;
        font-size: 20px;
    }

    .gr-markdown {
        margin-bottom: 10px;
    }
""") as demo:

    # Force CSS refresh with cache buster
    gr.HTML("""
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <style>
        /* Force white background and modern fonts - UPDATED */
        html, body {
            background: #ffffff !important;
            font-family: 'Inter', 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif !important;
        }

        /* Enhanced glass containers for white background */
        .gradio-container {
            background: rgba(248, 250, 252, 0.9) !important;
            backdrop-filter: blur(20px) !important;
            border: 1px solid rgba(0, 166, 81, 0.2) !important;
            border-radius: 20px !important;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08) !important;
        }

        /* Force all containers to have visible glass effect */
        .input-column, .results-column {
            background: rgba(248, 250, 252, 0.8) !important;
            backdrop-filter: blur(25px) !important;
            border: 2px solid rgba(0, 166, 81, 0.2) !important;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1) !important;
        }

        .logo-container {
            background: rgba(248, 250, 252, 0.9) !important;
            backdrop-filter: blur(25px) !important;
            border: 2px solid rgba(0, 166, 81, 0.3) !important;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12) !important;
        }
    </style>
    """)



    # Sophisticated Logo Design
    gr.HTML("""
    <div class="logo-container">
        <svg class="logo-svg" width="80" height="80" viewBox="0 0 100 100" style="margin-bottom: 10px;">
            <!-- Twin faces design -->
            <defs>
                <linearGradient id="faceGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#00A651;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#0B6623;stop-opacity:1" />
                </linearGradient>
                <filter id="glow">
                    <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
                    <feMerge>
                        <feMergeNode in="coloredBlur"/>
                        <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                </filter>
            </defs>

            <!-- Left face -->
            <circle cx="30" cy="40" r="18" fill="url(#faceGradient)" filter="url(#glow)" opacity="0.9"/>
            <circle cx="26" cy="36" r="2" fill="white"/>
            <circle cx="34" cy="36" r="2" fill="white"/>
            <path d="M 24 44 Q 30 48 36 44" stroke="white" stroke-width="2" fill="none"/>

            <!-- Right face -->
            <circle cx="70" cy="40" r="18" fill="url(#faceGradient)" filter="url(#glow)" opacity="0.9"/>
            <circle cx="66" cy="36" r="2" fill="white"/>
            <circle cx="74" cy="36" r="2" fill="white"/>
            <path d="M 64 44 Q 70 48 76 44" stroke="white" stroke-width="2" fill="none"/>

            <!-- Connection line -->
            <path d="M 48 40 Q 50 35 52 40" stroke="#00A651" stroke-width="3" fill="none" opacity="0.7"/>

            <!-- Sparkles -->
            <circle cx="20" cy="25" r="1.5" fill="#FFD700" opacity="0.8">
                <animate attributeName="opacity" values="0.8;0.3;0.8" dur="2s" repeatCount="indefinite"/>
            </circle>
            <circle cx="80" cy="25" r="1.5" fill="#FFD700" opacity="0.8">
                <animate attributeName="opacity" values="0.3;0.8;0.3" dur="2s" repeatCount="indefinite"/>
            </circle>
            <circle cx="50" cy="20" r="2" fill="#FFD700" opacity="0.6">
                <animate attributeName="opacity" values="0.6;0.2;0.6" dur="1.5s" repeatCount="indefinite"/>
            </circle>
        </svg>

        <h1 class="logo-title">Twin Finder</h1>
        <p class="logo-subtitle">Discover Your Digital Doppelgänger</p>
    </div>


    """)

    with gr.Row(elem_classes=["main-container"]):
        # Left Column - Input Section
        with gr.Column(scale=1, elem_classes=["input-column"]):
            gr.Markdown("### 📸 Upload Your Photo")
            user_img = gr.Image(type="pil", label="", width=280, height=220)
            gr.Markdown("### 🔍 Find Your Twin")
            cartoon_btn = gr.Button("🎭 Find Cartoon Twin")
            celeb_btn = gr.Button("⭐ Find Celebrity Twin")

        # Right Column - Results Section
        with gr.Column(scale=1, elem_classes=["results-column"]):
            gr.Markdown("### 🎯 Your Matches")
            gallery = gr.Gallery(label="", columns=3, height=280, object_fit="cover")
            caption = gr.Textbox(label="AI's Opinion", interactive=False)
            personality = gr.Textbox(label="Your AI-Generated Personality", interactive=False)

    cartoon_btn.click(fn=cartoon_lookup, inputs=user_img, outputs=[gallery, caption, personality])
    celeb_btn.click(fn=celeb_lookup, inputs=user_img, outputs=[gallery, caption, personality])


demo.launch()
