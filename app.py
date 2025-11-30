import streamlit as st
import time
import pandas as pd 

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Mishthi Jain | Digital Designer & CSE",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Python-based Title Animation Functions ---
def typewriter(text, speed=70, session_key='header_typed', element_class="header-title"):
    """Creates a reliable typewriter effect for the main header."""
    container = st.empty()
    display_text = ""
    
    # Check if main name animation has run
    if st.session_state.get(session_key):
        container.markdown(f'<p class="{element_class}">{text}</p>', unsafe_allow_html=True)
        return
        
    for char in text:
        display_text += char
        container.markdown(f'<p class="{element_class}">{display_text}</p>', unsafe_allow_html=True)
        time.sleep(speed / 1000)
    
    st.session_state[session_key] = True

# --- 2. Custom CSS for Dynamic Aesthetic & Enhanced Animations (Max Pop) ---
st.markdown("""
    <style>
    /* 🎨 Base Styling and Dark Green/Dynamic Palette */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@100;400;600;800&display=swap');
    
    :root {
        --primary-color: #A3E4D7; /* Light Aqua/Mint Green for accents */
        --secondary-color: #EAECEE; /* Off-White/Light Gray for Text */
        --highlight-bg: #113C3C; /* Deep, Cool Dark Green background */
        --card-bg: #1A4D4D; /* Slightly lighter Dark Green for cards */
        --text-color: #EAECEE; 
        --skill-accent: #66BB6A; /* Brighter Green for skill boxes */
        --separator-color: #A3E4D7;
    }

    /* *** ENHANCED ANIMATION KEYFRAMES (Faster/Stronger) *** */
    /* Continuous subtle bounce for the main name */
    @keyframes subtle-bounce {
        0%, 100% { transform: translateY(0); text-shadow: 0 0 5px rgba(163, 228, 215, 0.4); }
        50% { transform: translateY(-3px); text-shadow: 0 0 10px rgba(163, 228, 215, 0.8); }
    }

    /* Faster pulsing effect for the background shadow (Card "Fade") */
    @keyframes pulsing-shadow {
        0% { box-shadow: 0 0 10px rgba(163, 228, 215, 0.1); }
        50% { box-shadow: 0 0 30px rgba(163, 228, 215, 0.3); } /* Stronger peak */
        100% { box-shadow: 0 0 10px rgba(163, 228, 215, 0.1); }
    }

    /* Shimmer effect for links */
    @keyframes shimmer {
        0% { opacity: 1; }
        50% { opacity: 0.8; }
        100% { opacity: 1; }
    }

    /* **STRONGER POP-UP/FADE-IN EFFECT** (Increased displacement and speed) */
    @keyframes slideInUp {
      0% {
        opacity: 0;
        transform: translateY(100px); /* VERY aggressive initial slide */
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .stApp {
        background-color: var(--highlight-bg) !important; 
        color: var(--text-color);
        font-family: 'Poppins', sans-serif;
    }

    /* Hide Streamlit footer and menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Global Text Styling */
    p, li {
        font-size: 17px;
        line-height: 1.7;
        color: var(--secondary-color);
    }
    
    /* 🌟 Header Title - Centered, Massive, and Bold (Now with Bounce) */
    .header-title {
        font-size: 90px;
        font-weight: 800;
        color: var(--primary-color);
        text-transform: uppercase;
        letter-spacing: 10px;
        margin-bottom: 5px;
        margin-top: 20px;
        text-align: center;
        /* **NEW: Continuous subtle bounce** */
        animation: subtle-bounce 3s infinite ease-in-out;
    }

    /* Header Subtitle/Context */
    .header-subtitle {
        font-size: 26px;
        color: #66BB6A;
        margin-top: 5px;
        font-weight: 600;
        letter-spacing: 2px;
        text-align: center;
    }
    .header-context {
        font-size: 18px;
        color: var(--secondary-color);
        margin-top: 5px;
        margin-bottom: 5px;
        text-align: center;
    }

    /* Contact Info */
    .contact-info-block {
        text-align: center;
        font-size: 16px;
        color: var(--secondary-color);
        line-height: 1.5;
        margin-top: 20px;
    }
    .contact-info-block a {
        text-decoration: none;
        color: var(--primary-color);
        font-weight: 600;
        margin: 0 15px;
        transition: color 0.3s, transform 0.3s;
        animation: shimmer 2s infinite ease-in-out;
    }
    .contact-info-block a:hover {
        color: var(--secondary-color);
        transform: translateY(-2px); 
    }
    
    hr {
        background-color: var(--separator-color);
        height: 1px;
        border: none;
        opacity: 0.3;
        margin: 20px 0;
    }

    /* --- CONTENT CARD & SLIDE ANIMATION (Scroll Reveal Effect Simulation) --- */
    .content-card {
        background-color: var(--card-bg);
        padding: 0; 
        border-radius: 8px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.4);
        
        /* **FASTER POP-UP AND CONTINUOUS GLOW** */
        animation: slideInUp 0.5s ease-out forwards, pulsing-shadow 2.5s infinite alternate ease-in-out;
        
        margin-top: 50px;
        margin-bottom: 35px;
        border-left: 6px solid var(--primary-color);
        opacity: 0; /* Start hidden for the slideInUp effect */
    }
    
    /* **FASTER STAGGER DELAY** - This creates the sequential reveal on initial load */
    .content-card[data-index="1"] { animation-delay: 0.08s; }
    .content-card[data-index="2"] { animation-delay: 0.16s; }
    .content-card[data-index="3"] { animation-delay: 0.24s; }
    .content-card[data-index="4"] { animation-delay: 0.32s; }
    .content-card[data-index="5"] { animation-delay: 0.4s; }

    /* Animated Section Title (Typewriter simulation) */
    .card-section-title-animated {
        color: var(--secondary-color);
        font-size: 30px;
        font-weight: 800;
        text-transform: uppercase;
        padding: 18px 30px;
        margin: 0;
        letter-spacing: 2px;
        background-color: rgba(163, 228, 215, 0.05);
        border-bottom: 1px solid rgba(163, 228, 215, 0.2);
    }

    .card-inner-content {
        padding: 30px;
    }

    .project-card-title {
        color: var(--primary-color);
        font-size: 24px;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    .project-tech {
        font-style: italic;
        color: #A3B5B5;
        margin-bottom: 20px;
    }
    .project-tech strong {
        color: var(--secondary-color);
    }

    /* Simplified List Styles for narrative flow - REMOVED BOLT EMOJI */
    .flow-list {
        list-style-type: disc; 
        padding-left: 20px;
        margin-top: 10px;
    }
    .flow-list li {
        margin-bottom: 15px;
    }
    
    /* Skill Emphasis Boxes - Updated Green Theme */
    .skill-box {
        background-color: rgba(102, 187, 106, 0.08);
        padding: 18px;
        border-radius: 6px;
        margin-bottom: 25px;
        border-left: 4px solid var(--skill-accent);
        
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease-out, box-shadow 0.3s ease-out;
    }
    .skill-box:hover {
        transform: translateY(-8px); /* More aggressive lift on hover */
        box-shadow: 0 15px 30px rgba(102, 187, 106, 0.3); /* Stronger shadow */
    }
    
    .cgpa-display {
        font-size: 50px;
        font-weight: 900;
        color: var(--primary-color);
        text-align: center;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)


# --- 3. Header Section (Centered & Animated) ---

# Main Header Animation (Typewriter)
typewriter("MISHTHI JAIN", speed=70, session_key='header_typed', element_class="header-title")

# Centered Subtitles 
st.markdown('<p class="header-subtitle">BACHELOR OF TECHNOLOGY</p>', unsafe_allow_html=True)
st.markdown('<p class="header-context">Computer Science (Cyber Security)</p>', unsafe_allow_html=True)
st.markdown('<p class="header-context">Shri Ramdeobaba College of Engineering and Management, Nagpur, India</p>', unsafe_allow_html=True)

# Centered Contact Info
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col1: pass
with col5: pass

# Center block
with col2:
    st.markdown('<div class="contact-info-block" style="text-align: right;">', unsafe_allow_html=True)
    st.markdown('<p style="margin: 0;">+91-9244314388</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="contact-info-block" style="text-align: center;">', unsafe_allow_html=True)
    st.markdown(f'<p style="margin: 0;"><a href="mailto:jainmishthir@gmail.com">jainmishthir@gmail.com</a></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
with col4:
    st.markdown('<div class="contact-info-block" style="text-align: left;">', unsafe_allow_html=True)
    st.markdown(f'<p style="margin: 0;"><a href="https://linkedin.com/in/MishthiJain" target="_blank">LinkedIn</a> | <a href="https://github.com/MishthiJain8" target="_blank">GitHub</a></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- 4. Approach & Summary (Card 1) ---
st.markdown('<div class="content-card" data-index="1">', unsafe_allow_html=True)
# **Simplified:** Typewriter for card headings (this runs quickly on load)
typewriter("My Approach & Value", speed=30, session_key='approach_typed_h', element_class="card-section-title-animated")
st.markdown('<div class="card-inner-content">', unsafe_allow_html=True)

st.markdown("""
<p>
    I am a <strong>Digital Designer</strong> and <strong>Computer Science Engineer</strong> who believes exceptional products are built at the intersection of robust security and flawless user experience. My core value lies in leveraging <strong>full-stack engineering</strong> principles to construct secure, scalable systems while applying a designer's eye to deliver interfaces that are intuitive and impactful.
</p>
<p>
    My primary focus is on <strong>Solution-Oriented Thinking</strong>, translating complex technical challenges (like cloud waste optimization or secure authentication) into elegantly simple, high-performance applications. I support teams by not just coding features, but by <strong>designing reliable, secure systems</strong> that drive tangible business value and user satisfaction.
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. Education (Card 2) ---
st.markdown('<div class="content-card" data-index="2">', unsafe_allow_html=True)
# **Simplified:** Typewriter for card headings
typewriter("Education & Core Metrics", speed=30, session_key='edu_typed_h', element_class="card-section-title-animated")
st.markdown('<div class="card-inner-content">', unsafe_allow_html=True)

edu_col1, edu_col2 = st.columns([1, 2])

with edu_col1:
    st.markdown('<p class="cgpa-display">8.7</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: var(--primary-color); margin-top: -15px; font-weight: 600;">CGPA</p>', unsafe_allow_html=True)

with edu_col2:
    st.markdown('<p class="project-card-title">B.Tech., Computer Science (Cyber Security)</p>', unsafe_allow_html=True)
    st.markdown("""
    <p>
        <strong>Shri Ramdeobaba College of Engineering and Management, Nagpur</strong> <br>
        Expected Completion: October 2025
    </p>
    <p style="font-size: 14px; color: #A3B5B5;">
        *Prior Academic Foundations: Completed Secondary and Senior Secondary education (CBSE) with strong performance in technical subjects.*
    </p>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 6. Projects (Card 3) ---
st.markdown('<div class="content-card" data-index="3">', unsafe_allow_html=True)
# **Simplified:** Typewriter for card headings
typewriter("Featured Impact", speed=30, session_key='projects_typed_h', element_class="card-section-title-animated")
st.markdown('<div class="card-inner-content">', unsafe_allow_html=True)

# Project 1: Agro
st.markdown('<p class="project-card-title">Agro: Smart Agriculture Platform (MERN Stack)</p>', unsafe_allow_html=True)
st.markdown('<p class="project-tech"><strong>Technologies:</strong> React, Node.js, Express, MongoDB, JWT, UPI API</p>', unsafe_allow_html=True)
st.markdown("""
<p>
    A full-stack solution built to empower farmers. This project focused on integrating a machine learning model for <strong>plant disease detection (90% accuracy)</strong> directly into a user-friendly platform. My key contribution was designing and deploying a <strong>JWT-based secure authentication</strong> system and optimizing the Node.js backend to <strong>reduce response time by 25%</strong>, ensuring reliable and fast access to critical information.
</p>
<hr style="border-top: 1px dashed var(--separator-color);">
""", unsafe_allow_html=True)

# Project 2: Cloud Resource Optimizer
st.markdown('<p class="project-card-title">Cloud Resource Optimizer (AWS Automation)</p>', unsafe_allow_html=True)
st.markdown('<p class="project-tech"><strong>Technologies:</strong> Python, AWS SDK (Boto3), Streamlit</p>', unsafe_allow_html=True)
st.markdown("""
<p>
    This addresses the real-world problem of cloud cost wastage. I developed an automated system using <strong>Python and AWS Boto3 SDK</strong> to securely monitor idle EC2 and S3 resources. The output is a <strong>Streamlit dashboard</strong> that visualizes utilization and, critically, uses <strong>anomaly detection</strong> to automatically flag underutilized instances, resulting in an estimated <strong>30% reduction</strong> in unnecessary cloud costs.
</p>
<hr style="border-top: 1px dashed var(--separator-color);">
""", unsafe_allow_html=True)

# Project 3: Algo-Playgroundr
st.markdown('<p class="project-card-title">Algo-Playgroundr: DSA Visualization Tool</p>', unsafe_allow_html=True)
st.markdown('<p class="project-tech"><strong>Technologies:</strong> Java, Data Structures and Algorithms</p>', unsafe_allow_html=True)
st.markdown("""
<p>
    A pedagogical tool designed to transform abstract algorithmic logic into intuitive visual flows. I engineered a <strong>Java-based interactive visualization app</strong> that allows step-by-step execution and <strong>graphical animation</strong> of complex sorting and graph algorithms, directly solving the conceptual difficulty challenge in DSA learning.
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# **--- Increased Space (Separating Projects and Certifications) ---**
st.markdown("<br>" * 2, unsafe_allow_html=True) 

# --- 7. Certifications (NEW SEPARATE CARD - Card 4) ---
st.markdown('<div class="content-card" data-index="4">', unsafe_allow_html=True)
# **Simplified:** Typewriter for card headings
typewriter("Certifications & Foundations", speed=30, session_key='cert_typed_h', element_class="card-section-title-animated")
st.markdown('<div class="card-inner-content">', unsafe_allow_html=True)

# Removed the '⚡ ' from the list
st.markdown("""
<ul class="flow-list">
    <li><strong>Google:</strong> Crash Course on Python</li>
    <li><strong>Duke University/IBM:</strong> Generative AI Applications & Course on Generative AI</li>
    <li><strong>University of London:</strong> Introduction to Network Security</li>
</ul>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# **--- Increased Space (Separating Certifications and Skills) ---**
st.markdown("<br>" * 2, unsafe_allow_html=True) 

# --- 8. Skills & Impact (Final Card 5) ---
st.markdown('<div class="content-card" data-index="5">', unsafe_allow_html=True)
# **Simplified:** Typewriter for card headings
typewriter("Technical Toolbox & Proven Impact", speed=30, session_key='comp_typed_h', element_class="card-section-title-animated")
st.markdown('<div class="card-inner-content">', unsafe_allow_html=True)

col_s1, col_s2 = st.columns(2)

with col_s1:
    st.subheader("Technical Toolbox")
    st.markdown("""
    <div class="skill-box">
        <p style="margin-top: 0;"><strong>Languages:</strong> Python, Java, C</p>
        <p style="margin-bottom: 0;"><strong>Web:</strong> React, Node.js, Express.js, MongoDB, RESTful APIs</p>
    </div>
    <div class="skill-box">
        <p style="margin-top: 0; margin-bottom: 0;"><strong>Platforms/Tools:</strong> AWS SDK (Boto3), Git/GitHub, Linux, VS Code</p>
    </div>
    """, unsafe_allow_html=True)
    
with col_s2:
    st.subheader("Proven Impact")
    st.markdown("""
    <div class="skill-box" style="border-left: 4px solid var(--primary-color);">
        <p style="margin-top: 0;"><strong>Efficiency & Optimization:</strong> Enhanced core algorithm performance, decreasing runtime by <strong>30 percent</strong> during pilot testing.</p>
        <p style="margin-bottom: 0;"><strong>Cost Savings:</strong> Delivered a sustained <strong>30% reduction</strong> in cloud resource wastage through automated detection and remediation systems.</p>
    </div>
    <div class="skill-box" style="border-left: 4px solid var(--primary-color);">
        <p style="margin-top: 0; margin-bottom: 0;"><strong>Collaboration:</strong> Actively contributed to <strong>3+ open-source GitHub repositories</strong>, merging <strong>5+ pull requests</strong> that enhanced project stability and functionality.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)