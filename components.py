import streamlit as st
import streamlit.components.v1 as components
import json

def voice_assistant_component():
    """
    A simple voice assistant component that can speak diagnosis results.
    """
    st.markdown("### 🎙️ Voice Assistant Control")
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("🔊 Speak Diagnosis"):
            if st.session_state.get('last_results'):
                res = st.session_state.last_results
                text = f"Diagnosis complete for {res.get('plant')}. The condition is {res.get('disease')}. {res.get('pathology')}"
                st.markdown(f"<script>speakText('{text}')</script>", unsafe_allow_html=True)
                # Fallback using standard streamlit if the above fails
                components.html(f"""
                <script>
                    const utterance = new SpeechSynthesisUtterance("{text}");
                    window.speechSynthesis.speak(utterance);
                </script>
                """, height=0)

    with col2:
        st.info("Click the button to hear the clinical analysis.")

def voice_recognition_component():
    """
    A component that listens for voice commands and returns the transcript.
    """
    st.markdown("### 🎤 Voice Command")
    
    # Custom HTML for voice recognition
    # This uses a hidden iframe to send messages back to Streamlit
    components.html("""
    <div style="display: flex; align-items: center; gap: 10px; font-family: sans-serif;">
        <button id="start-btn" style="background: #10b981; border: none; border-radius: 50%; width: 50px; height: 50px; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 10px rgba(16,185,129,0.5);">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="white"><path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3z"/><path d="M17 11c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/></svg>
        </button>
        <span id="status" style="color: #6ee7b7; font-size: 0.9rem;">Click to speak</span>
    </div>
    
    <script>
        const btn = document.getElementById('start-btn');
        const status = document.getElementById('status');
        
        if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
            status.innerText = "Speech API not supported";
            btn.disabled = true;
        } else {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            const recognition = new SpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            
            btn.onclick = () => {
                recognition.start();
                status.innerText = "Listening...";
                btn.style.animation = "pulse 1.5s infinite";
            };
            
            recognition.onresult = (event) => {
                const text = event.results[0][0].transcript;
                status.innerText = "Heard: " + text;
                btn.style.animation = "none";
                
                // Send back to Streamlit via a hidden text input trick or just display
                // Since components.html is isolated, we can't easily set a Streamlit widget value
                // but we can use window.parent.postMessage
                window.parent.postMessage({
                    type: 'streamlit:set_component_value',
                    value: text
                }, '*');
            };
            
            recognition.onerror = () => {
                status.innerText = "Error occurred";
                btn.style.animation = "none";
            };
            
            recognition.onend = () => {
                btn.style.animation = "none";
            };
        }
    </script>
    <style>
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(16, 185, 129, 0); }
            100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }
    </style>
    """, height=80)

def clinical_report_downloader(results):
    """
    Handles PDF and CSV downloads correctly.
    """
    from fpdf import FPDF
    import pandas as pd
    import datetime
    
    st.markdown("<h4 style='color:#6ee7b7;'>📄 Enterprise Data Export Modules</h4>", unsafe_allow_html=True)
    colD1, colD2 = st.columns(2)
    
    # Pre-generate PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_text_color(16, 185, 129)
    pdf.set_font("helvetica", "B", 24)
    pdf.cell(0, 20, "PLANTPULSE EMERALD DOSSIER", ln=True, align='C')
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(0, 10, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.set_font("helvetica", "", 12)
    pdf.set_text_color(0, 0, 0)
    
    pdf.ln(10)
    pdf.cell(0, 10, f"Specimen: {results.get('plant')}", ln=True)
    pdf.cell(0, 10, f"Condition: {results.get('disease')}", ln=True)
    pdf.cell(0, 10, f"Confidence: {results.get('score')}%", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Pathology: {results.get('pathology')}")
    pdf.ln(5)
    
    if results.get('rx'):
        pdf.set_font("helvetica", "B", 12)
        pdf.cell(0, 10, "Remediation Directives:", ln=True)
        pdf.set_font("helvetica", "", 12)
        for k, v in results.get('rx', {}).items():
            pdf.multi_cell(0, 10, f"- {k.replace('_',' ').title()}: {v}")
            
    pdf_bytes = pdf.output()
    
    with colD1:
        st.info("Export highly detailed PDF Clinical Dossier for agronomist review.")
        st.download_button(
            label="📥 Download Clinical PDF",
            data=pdf_bytes,
            file_name=f"Emerald_{results.get('plant', 'scan')}.pdf",
            mime="application/pdf",
            use_container_width=True,
            key="pdf_download_btn"
        )
        
    with colD2:
        st.success("Export raw JSON/CSV structured biological matrices.")
        csv_data = [
            {"Metric": "Target", "Value": results.get('plant')},
            {"Metric": "Severity", "Value": results.get('disease')},
            {"Metric": "Confidence", "Value": f"{results.get('score')}%"},
            {"Metric": "Timestamp", "Value": results.get('timestamp')}
        ]
        csv = pd.DataFrame(csv_data).to_csv(index=False)
        st.download_button(
            label="💾 Save Matrix as CSV",
            data=csv,
            file_name=f"emerald_telemetry_{results.get('plant')}.csv",
            mime="text/csv",
            use_container_width=True,
            key="csv_download_btn"
        )
