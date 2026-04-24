"""
styles.py — PlantPulse Zenith Design System
===========================================
Professional Agritech CSS & HTML Templates
"""

ZENITH_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    .stApp { 
        background-color: #01160d;
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(16, 185, 129, 0.1) 0%, transparent 40%),
            radial-gradient(circle at 90% 80%, rgba(5, 150, 105, 0.1) 0%, transparent 40%);
        color: #ecfdf5; 
        font-family: 'Outfit', sans-serif;
    }

    /* Falling Leaf Animation */
    @keyframes blossom {
        0% { transform: translateY(-10vh) rotate(0deg) scale(0.5); opacity: 0; }
        20% { opacity: 0.8; }
        80% { opacity: 0.8; }
        100% { transform: translateY(110vh) rotate(720deg) scale(1); opacity: 0; }
    }
    .blossom-leaf {
        position: fixed; top: -5vh; z-index: 1000; pointer-events: none;
        animation: blossom 15s linear infinite; font-size: 28px; color: #10b981; filter: drop-shadow(0 0 10px rgba(16, 185, 129, 0.4));
    }

    /* Zenith Glassmorphism Cards */
    .zenith-card {
        background: rgba(6, 78, 59, 0.25);
        backdrop-filter: blur(24px);
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 28px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }
    .zenith-card:hover {
        transform: translateY(-5px);
        border-color: #10b981;
        background: rgba(6, 78, 59, 0.35);
        box-shadow: 0 15px 50px rgba(16, 185, 129, 0.1);
    }

    .glow-text {
        color: #34d399;
        text-shadow: 0 0 25px rgba(16, 185, 129, 0.7);
        font-weight: 800;
    }

    .metric-title { font-size: 0.85rem; opacity: 0.7; text-transform: uppercase; letter-spacing: 2px; color: #6ee7b7; }
    .metric-value { font-size: 2.6rem; font-weight: 800; color: #ffffff; }

    /* Custom Status Badges */
    .badge {
        padding: 8px 18px; border-radius: 100px; font-weight: 800; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1.5px;
    }
    .badge-critical { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid #f87171; }
    .badge-warning { background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid #fbbf24; }
    .badge-optimal { background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid #34d399; }

    /* Better tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 12px; background-color: transparent; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; border-radius: 16px; background-color: rgba(6, 95, 70, 0.1); color: #d1fae5; border: 1px solid rgba(16, 185, 129, 0.1); padding: 0 24px;
    }
    .stTabs [aria-selected="true"] { 
        background-color: rgba(16, 185, 129, 0.2) !important; 
        border-color: #10b981 !important; 
        color: #10b981 !important; 
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.2);
    }

    /* Developer Cards */
    .dev-card {
        background: rgba(255, 255, 255, 0.03);
        border-left: 3px solid #10b981;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 0 12px 12px 0;
        font-size: 0.85rem;
    }
    .dev-name { font-weight: 700; color: #34d399; display: block; }
    .dev-meta { font-size: 0.75rem; opacity: 0.6; display: block; }

    /* Scan Line Animation */
    .scan-line {
        position: absolute; width: 100%; height: 2px;
        background: #10b981; box-shadow: 0 0 15px #10b981;
        top: 0; left: 0; z-index: 5;
        animation: scan 3s linear infinite;
    }
    @keyframes scan {
        0% { top: 0; }
        100% { top: 100%; }
    }
    .zenith-btn {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        border: none;
        border-radius: 8px;
        color: white;
        padding: 12px 24px;
        font-weight: bold;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
        transition: all 0.3s ease;
        text-align: center;
        width: 100%;
        display: block;
        text-decoration: none;
    }
    .zenith-btn:hover {
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.8);
        transform: scale(1.05);
    }
    @keyframes pulse-glow {
        0% { box-shadow: 0 0 10px rgba(16, 185, 129, 0.1); }
        50% { box-shadow: 0 0 20px rgba(16, 185, 129, 0.6), inset 0 0 15px rgba(16, 185, 129, 0.2); }
        100% { box-shadow: 0 0 10px rgba(16, 185, 129, 0.1); }
    }
    .sensor-card {
        background: rgba(6, 78, 59, 0.25);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 16px;
        padding: 15px 10px;
        text-align: center;
        animation: pulse-glow 4s infinite;
        margin-bottom: 20px;
    }
    .sensor-val { font-size: 2.2rem; font-weight: 800; color: #34d399; text-shadow: 0 0 10px rgba(52, 211, 153, 0.4); }
    .sensor-label { font-size: 0.75rem; color: #a7f3d0; text-transform: uppercase; letter-spacing: 2px; margin-top: 5px; opacity: 0.8;}
    
    .timeline-step {
        border-left: 3px solid #10b981;
        padding: 0 0 20px 20px;
        position: relative;
    }
    .timeline-step::before {
        content: '';
        position: absolute;
        width: 14px; height: 14px;
        background: #34d399;
        border-radius: 50%;
        left: -8px; top: 0;
        box-shadow: 0 0 10px #34d399;
    }

    /* Voice Assistance UI */
    .voice-pulse {
        width: 40px;
        height: 40px;
        background: #10b981;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        animation: pulse-ring 1.25s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
    }
    @keyframes pulse-ring {
        0% { transform: scale(.33); }
        80%, 100% { opacity: 0; }
    }
</style>
"""

BLOSSOM_LEAVES = """
<div class="blossom-leaf" style="left:5%; animation-delay: 0s;">🌿</div>
<div class="blossom-leaf" style="left:25%; animation-delay: 3s;">🍃</div>
<div class="blossom-leaf" style="left:45%; animation-delay: 7s;">🌱</div>
<div class="blossom-leaf" style="left:65%; animation-delay: 1s;">🌿</div>
<div class="blossom-leaf" style="left:85%; animation-delay: 5s;">🍃</div>
"""

VOICE_ASSIST_JS = """
<script>
    function speakText(text) {
        if ('speechSynthesis' in window) {
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.pitch = 1.1;
            utterance.rate = 1.0;
            window.speechSynthesis.speak(utterance);
        }
    }
    
    // Function to listen for voice commands
    function startVoiceRecognition() {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'en-US';
        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            window.parent.postMessage({
                type: 'voice_command',
                text: transcript
            }, '*');
        };
        recognition.start();
    }
</script>
"""
