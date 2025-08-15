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
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%) !important;
        background-size: 400% 400% !important;
        animation: gradientShift 15s ease infinite !important;
        font-family: 'Poppins', 'Inter', 'Segoe UI', sans-serif !important;
        margin: 0 !important;
        padding: 0 !important;
        min-height: 100vh !important;
        overflow-x: hidden !important;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
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
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(30px);
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3),
                    inset 0 1px 0 rgba(255, 255, 255, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.3);
        position: relative;
        overflow: hidden;
        animation: logoGlow 3s ease-in-out infinite alternate;
    }

    @keyframes logoGlow {
        0% { box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3), 0 0 30px rgba(102, 126, 234, 0.5); }
        100% { box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3), 0 0 50px rgba(245, 87, 108, 0.7); }
    }

    .logo-title {
        background: linear-gradient(135deg, #ff6b6b, #4facfe, #f093fb, #ff9ff3);
        background-size: 400% 400%;
        animation: titleGradient 3s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 900;
        font-size: 52px;
        margin: 20px 0 10px 0;
        text-shadow: 0 0 30px rgba(255, 107, 107, 0.5);
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    @keyframes titleGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .logo-subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-size: 18px;
        font-weight: 600;
        margin: 0;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        letter-spacing: 1px;
    }
    /* Buttons */
    .gr-button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 50%, #ff9ff3 100%) !important;
        color: white !important;
        border-radius: 50px;
        padding: 18px 40px;
        font-weight: 700;
        font-size: 18px;
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.4),
                    0 0 20px rgba(255, 107, 107, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin: 12px 0;
        width: 100%;
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .gr-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s;
    }

    .gr-button:hover::before {
        left: 100%;
    }

    .gr-button:hover {
        background: linear-gradient(135deg, #ff5252 0%, #d63031 50%, #fd79a8 100%) !important;
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 20px 40px rgba(255, 107, 107, 0.6),
                    0 0 40px rgba(255, 107, 107, 0.5);
    }

    /* Gallery */
    .gr-gallery {
        border-radius: 25px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        padding: 25px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(25px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2),
                    0 0 25px rgba(116, 75, 162, 0.3);
        max-width: 600px;
        margin: 0 auto;
        animation: galleryGlow 3s ease-in-out infinite alternate;
    }

    @keyframes galleryGlow {
        0% { box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2), 0 0 25px rgba(116, 75, 162, 0.3); }
        100% { box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2), 0 0 35px rgba(240, 147, 251, 0.5); }
    }

    .gr-gallery img {
        max-width: 120px;
        max-height: 120px;
        border-radius: 20px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.3);
    }

    .gr-gallery img:hover {
        transform: scale(1.1) rotate(2deg);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3),
                    0 0 20px rgba(255, 107, 107, 0.6);
    }

    /* Text Boxes */
    .gr-textbox {
        border-radius: 25px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        padding: 25px;
        font-size: 18px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(25px);
        color: #fff;
        font-weight: 500;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2),
                    0 0 20px rgba(79, 172, 254, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: fadeInUp 0.8s ease-out;
    }

    .gr-textbox:focus-within {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.3),
                    0 0 40px rgba(255, 107, 107, 0.6);
        border-color: rgba(255, 255, 255, 0.6);
        background: rgba(255, 255, 255, 0.15);
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
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(30px);
        border-radius: 30px;
        padding: 35px;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.2),
                    inset 0 1px 0 rgba(255, 255, 255, 0.2),
                    0 0 30px rgba(102, 126, 234, 0.3);
        min-height: 500px;
        border: 2px solid rgba(255, 255, 255, 0.2);
        position: relative;
        overflow: hidden;
        animation: containerPulse 4s ease-in-out infinite alternate;
    }

    @keyframes containerPulse {
        0% { box-shadow: 0 25px 60px rgba(0, 0, 0, 0.2), 0 0 30px rgba(102, 126, 234, 0.3); }
        100% { box-shadow: 0 25px 60px rgba(0, 0, 0, 0.2), 0 0 50px rgba(245, 87, 108, 0.4); }
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
        max-width: 300px;
        max-height: 240px;
        margin: 0 auto 25px auto;
        border-radius: 25px;
        border: 3px solid rgba(255, 255, 255, 0.4);
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2),
                    0 0 25px rgba(102, 126, 234, 0.4);
        padding: 15px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }

    .gr-image::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: imageShine 3s ease-in-out infinite;
    }

    @keyframes imageShine {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        50% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        100% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
    }

    .gr-image:hover {
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.3),
                    0 0 40px rgba(245, 87, 108, 0.6);
        transform: translateY(-8px) scale(1.05);
        background: rgba(255, 255, 255, 0.2);
        border-color: rgba(255, 255, 255, 0.6);
    }

    .gr-image > div {
        border-radius: 15px;
        overflow: hidden;
    }

    /* Typography */
    h3 {
        background: linear-gradient(135deg, #ff6b6b, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        margin-bottom: 20px;
        margin-top: 15px;
        text-align: center;
        font-size: 24px;
        text-shadow: 0 2px 10px rgba(255, 107, 107, 0.3);
        letter-spacing: 1px;
        text-transform: uppercase;
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
