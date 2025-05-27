import streamlit as st
import time

# Set page config
st.set_page_config(
    page_title="Kashish Bhasin - Hyperpure Operations Intern",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with Zomato color palette
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #E23744 0%, #FF6B73 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(226, 55, 68, 0.3);
    }
    
    .section-header {
        background: linear-gradient(135deg, #FF6B73 0%, #FFB3B8 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        font-weight: bold;
        margin: 1rem 0;
        text-align: center;
    }
    
    .skill-tag {
        background: #E23744;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.9rem;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, #FFF5F5 0%, #FFE8EA 100%);
        padding: 1.5rem;
        border-left: 5px solid #E23744;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .metric-card {
        background: black;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-top: 4px solid #E23744;
        text-align: center;
    }
    
    .contact-info {
        background: #2C3E50;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .cta-button {
        background: linear-gradient(135deg, #E23744 0%, #FF6B73 100%);
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 50px;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(226, 55, 68, 0.4);
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(226, 55, 68, 0.6);
    }
    
    .achievement-badge {
        background: #FFD700;
        color: #2C3E50;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: bold;
        margin: 0.3rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="main-header">
    <h1>🚀 KASHISH BHASIN</h1>
    <h2>Applying for Operations Internship at Hyperpure by Zomato</h2>
    <p style="font-size: 1.2rem; margin-top: 1rem;">
        Product-focused AI/ML specialist ready to optimize operations and drive growth
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar with contact info
with st.sidebar:
    st.markdown("""
    <div class="contact-info">
        <h3>📞 Contact Information</h3>
        <p>📧 kashishbhasinn@gmail.com</p>
        <p>📱 (+91) 9811149303</p>
        <p>🔗 <a href="https://linkedin.com/in/kashish-bhasin" style="color: #FFB3B8;">LinkedIn Profile</a></p>
        <p>💻 <a href="https://github.com/kashishbhasinn" style="color: #FFB3B8;">GitHub Portfolio</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Stats
    st.markdown('<div class="section-header">📊 Quick Stats</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("CGPA", "9.29", "🎯")
        st.metric("Projects", "15+", "🚀")
    with col2:
        st.metric("Experience", "4 Roles", "💼")
        st.metric("Team Size Led", "10+", "👥")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    # Why I'm Perfect for Hyperpure
    st.markdown('<div class="section-header">🎯 Why I\'m Perfect for Hyperpure Operations</div>', unsafe_allow_html=True)
    
    # Key qualifications for the role
    st.markdown("### 🚀 Key Qualifications for Operations Role")
    
    qualifications = {
        "Data Analysis & Reporting": {
            "description": "Built Python-based analytics tools with 92% accuracy, handled 7-9 Cr beneficiary records",
            "relevance": "Perfect for tracking inventory and vendor performance"
        },
        "Operations Strategy": {
            "description": "Led cross-functional teams of 10+ specialists, managed product roadmaps and sprint planning",
            "relevance": "Directly applicable to developing and executing operations strategies"
        },
        "Cross-functional Collaboration": {
            "description": "Collaborated with UI/UX designers, developers, LLM engineers across multiple projects",
            "relevance": "Essential for optimizing processes and customer experience"
        },
        "Process Optimization": {
            "description": "Reduced manual search time by 50%, improved document retrieval efficiency by 70%",
            "relevance": "Critical for operations efficiency at Hyperpure"
        }
    }
    
    for qual, details in qualifications.items():
        with st.expander(f"📈 {qual}"):
            st.write(f"**My Experience:** {details['description']}")
            st.write(f"**Relevance to Hyperpure:** {details['relevance']}")

with col2:
    # Skills relevant to operations
    st.markdown('<div class="section-header">🛠️ Relevant Skills</div>', unsafe_allow_html=True)
    
    operations_skills = [
        "Data Analytics", "SQL", "Python", "Tableau", "Excel",
        "Agile Scrum", "Jira", "KPI Tracking", "Process Optimization",
        "Cross-functional Leadership", "Strategic Planning"
    ]
    
    for skill in operations_skills:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Recent achievements
    st.markdown('<div class="section-header">🏆 Recent Wins</div>', unsafe_allow_html=True)
    
    achievements = [
        "Led 10+ person cross-functional team",
        "Automated analysis for 300K+ patients",
        "Improved efficiency by 70%",
        "Reduced manual work by 50%",
        "Drove 65% sales growth at Dr. Oetker"
    ]
    
    for achievement in achievements:
        st.markdown(f"✅ {achievement}")

# Experience Timeline
st.markdown('<div class="section-header">💼 Relevant Experience Timeline</div>', unsafe_allow_html=True)

experiences = [
    {
        "role": "Product Strategist Intern",
        "company": "Arogo AI, IIT Kharagpur",
        "period": "Feb 2025 - Present",
        "highlights": [
            "Leading cross-functional team of 10+ specialists",
            "Managing product roadmap and sprint planning",
            "Authored PRDs for 300K+ patient pipeline"
        ]
    },
    {
        "role": "Data Intern",
        "company": "IIM Bangalore",
        "period": "Jan 2024 - Oct 2024",
        "highlights": [
            "Built analytics tool with 92% accuracy",
            "Reduced manual handling time by 50%",
            "Delivered strategic insights improving alignment by 30%"
        ]
    },
    {
        "role": "AI Research Intern",
        "company": "DRDO",
        "period": "Jun 2024 - Jul 2024",
        "highlights": [
            "Improved document retrieval efficiency by 70%",
            "Optimized search workflows",
            "Conducted comparative analysis of 15+ databases"
        ]
    }
]

for exp in experiences:
    with st.expander(f"🏢 {exp['role']} at {exp['company']} ({exp['period']})"):
        for highlight in exp['highlights']:
            st.write(f"• {highlight}")

# Technical Projects
st.markdown('<div class="section-header">🚀 Technical Projects Showcasing Operations Skills</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h4>🤖 AI Resume Analysis</h4>
        <p>Developed system with 65% accuracy improvement through user feedback and data analytics</p>
        <strong>Operations Relevance:</strong> Data-driven optimization
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h4>🍳 AI Kitchen Assistant</h4>
        <p>35% improved meal planning efficiency, 40% increased engagement</p>
        <strong>Operations Relevance:</strong> Process efficiency & user experience
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h4>📊 RAG System for DRDO</h4>
        <p>70% improvement in document retrieval efficiency</p>
        <strong>Operations Relevance:</strong> Workflow optimization
    </div>
    """, unsafe_allow_html=True)

# Call to Action Section
st.markdown("---")
st.markdown('<div class="section-header">🎯 Ready to Drive Hyperpure Operations Forward!</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div style="background: #2C3E50; color: white; padding: 1.5rem; border-left: 5px solid #E23744; border-radius: 10px; margin: 1rem 0; text-align: center;">
        <h3 style="color: white; margin-top: 0;">🚀 Why Choose Kashish?</h3>
        <p style="color: white;">✅ Proven track record in data analysis & operations</p>
        <p style="color: white;">✅ Experience leading cross-functional teams</p>
        <p style="color: white;">✅ Strong technical skills with business acumen</p>
        <p style="color: white;">✅ Proactive problem-solver with growth mindset</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hire Me Button with Balloons
    if st.button("🎉 HIRE ME FOR HYPERPURE! 🎉", key="hire_me", help="Click to celebrate and contact!"):
        st.balloons()
        st.success("🎊 Thank you for considering my application! Let's revolutionize operations at Hyperpure together!")
        time.sleep(1)
        st.balloons()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: #2C3E50; color: white; border-radius: 10px;">
    <h4>📧 Ready to Connect?</h4>
    <p>Let\'s discuss how I can contribute to Hyperpure\'s operations excellence! 🚀</p>
</div>
""", unsafe_allow_html=True)

# Add some spacing
st.markdown("<br><br>", unsafe_allow_html=True)
