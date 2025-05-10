import streamlit as st

# Page Configuration
st.set_page_config(page_title="Muhamad Kahfi Portfolio", layout="centered")

# ---- Custom CSS Styling ----
st.markdown("""
    <style>
        h1, h2, h3, h4 {
            font-family: 'Segoe UI', sans-serif;
        }
        p {
            font-size: 16px;
        }
        .centered-img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 10px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }
        .section {
            margin-top: 40px;
        }
        .contact-btn {
            display: inline-block;
            padding: 12px 24px;
            background-color: #4CAF50;
            border-radius: 8px;
            color: white;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
            text-decoration: none;
            transition: background-color 0.3s ease;
        }
        .contact-btn:hover {
            background-color: #45a049;
        }
        .footer {
            margin-top: 50px;
            font-size: 14px;
            text-align: center;
            color: gray;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Sidebar Navigation ----
st.sidebar.markdown("""
    <h2 style='text-align: left; font-size: 36px; margin-bottom: 10px;'>MK</h2>
""", unsafe_allow_html=True)

selected = st.sidebar.radio("Navigate to:", [
    "About Me",
    'Professional Experience',
    "Education",
    "Projects",
    "Articles",
    "Dashboards",
    "Contact"
])

# ---- About Me ----
if selected == "About Me":
    st.markdown("""
        <h1 style='text-align: center; font-size: 42px;'>Muhamad Kahfi Dwi Prasetio</h1>
        <p style='text-align: center; font-size: 18px;'>Data Analyst | Management Graduate | Data Science Enthusiast</p>
    """, unsafe_allow_html=True)
    st.markdown("### 👋 About Me")
    st.write("""
    Graduated **cum laude** from UIN Bandung (GPA 3.72/4.00) in Management, with a strong interest in data analysis, finance, and business strategy. Experienced in data science using **Python, SQL, Tableau**, and statistical modeling. 
    """)

    # ---- Skills ----
    st.markdown("---")
    st.markdown("## 🛠️ Skills")
    st.write("""
    🔹**Python** (Pandas, NumPy, Streamlit, scikit-learn)  
    🔹**SQL** & Relational Databases  
    🔹**Tableau** for Data Visualization  
    🔹Machine Learning Basics  
    🔹ETL Processes  
    🔹Financial Analysis & Management
    """)

    st.markdown("---")
    st.markdown("## 📄 Download My CV")
    st.link_button("View My CV", "https://drive.google.com/file/d/1W-w1jnNZPr8sKr62sL6F4_-FXdwhJkNN/view?usp=sharing")

# ---- Professional Experience ----
elif selected == "Professional Experience":
    st.markdown("## 🧑‍💼 Professional Experience & Internships")

    st.markdown("#### 🔹 Statistical Analyst – Bandung Premier League (2022–2024)")
    st.write("""
    - Analyzed 40% of match statistics (goals, interceptions, shots on/off target).
    - Compiled player performance reports for internal review.
    """)


    st.markdown("#### 🔹 Statistical Analyst – FOSSBI West Java (2022–2023)")
    st.write("""
    - Collected and analyzed match data.
    - Prepared 35% of player performance reports for youth competitions.
    """)


    st.markdown("#### 🔹 HR & Financial Policy Analyst (Intern) – Ministry of Administrative and Bureaucratic Reform (2023)")
    st.write("""
    - Prepared government meeting materials and official documents.
    - Managed superior permission letters and functional role data.
    - Final evaluation score: 95.42/100.
    """)

    st.markdown("#### 🔹 HR Curriculum Analyst (Intern) – Kompas Growth Center (2022)")
    st.write("""
    - Developed employee development curricula (e.g., time management).
    - Designed final projects to aid WFH adaptation.
    """)



# ---- Projects ----
elif selected == "Projects":
    st.markdown("## 💼 Projects")
    st.markdown("#### 🔹 [ROA Financial Analysis App](https://github.com/kahfidwi/Analisis-Sederhana-Return-on-Asset)")
    st.write("An interactive CLI-based app for company performance comparison using Return on Asset (ROA). Built with Python and `tabulate` module to manage and display structured company data. Enables CRUD operations and financial ratio analysis.")


    st.markdown("#### 🔹 [TransJakarta Service Optimization](https://github.com/kahfidwi/EFISIENSI-MEMPERBAIKI-KUALITAS-LAYANAN-DAN-MENDUKUNG-VISI-SERTA-MISI-TRANSJAKARTA)")
    st.write("Data analysis project to support TransJakarta's mission by analyzing routes, travel time, and user patterns for improving efficiency and quality of service.")


    st.markdown("#### 🔹 [Academic Research Publication](https://digilib.uinsgd.ac.id/id/eprint/89796)")
    st.write("""
    "The Influence of Dividend Yield, Dividend Payout Ratio, and Earnings Volatility on Stock Price Volatility in Banking Sector Companies Listed on the Indonesia Stock Exchange (2018–2022)"**  
Published in UIN Bandung’s Digital Library. This research explores key financial ratios and their effects on stock volatility using empirical methods." 
    Published in UIN Bandung’s Digital Library.
    """)


# ---- Articles ----
elif selected == "Articles":
    st.markdown("## ✍️ Articles")
    
    st.markdown("#### 🔹 [Understanding UNION, UNION ALL, INTERSECT, and MINUS in SQL](https://medium.com/@kahfidw/understanding-union-union-all-intersect-and-minus-in-sql-32665b38ac53)")
    st.write("This article walks through how to use UNION, UNION ALL, INTERSECT, and MINUS in SQL.")
    
    st.markdown("#### 🔹 [Konversi Suhu di Python](https://medium.com/@kahfidw/program-konversi-suhu-di-python-97d25e31aa26)")
    st.write("A basic Python program to convert temperature between Celsius, Reamur, Kelvin, and Fahrenheit.")
    
    st.markdown("#### 🔹 [Social Media Promotion for MSMEs (A Descriptive Study on AEROSTREET)](https://www.academia.edu/106332654/Promosi_di_Media_Sosial_Bagi_UMKM_Studi_Deskriptif_pada_AEROSTREET_?source=swp_share)")
    st.write("With the rapid advancement of technology, competition among both small and medium enterprises has become increasingly intense. Promotion is essential for every business, and the key to successful promotion lies in creating persuasive messages that effectively capture consumer attention on social media platforms. This aligns with the need to keep up with the ever-evolving digital landscape. Aerostreet utilizes social media effectively, as demonstrated by its diverse promotional activities and strategic use of platform features.")

# ---- Dashboards ----
elif selected == "Dashboards":
    st.markdown("## 📊 Tableau Dashboards")

    st.markdown("#### 🔹 [TransJakarta Dashboard](https://public.tableau.com/views/TransjakartaDashboard_17431737096620/BerandaDashboard)")
    st.write("Data analysis project to support TransJakarta's mission by analyzing routes, travel time, and user patterns for improving efficiency and quality of service.")

    st.markdown("#### 🔹 [Superstore Product Analysis](https://public.tableau.com/views/SUPERSTOREDASHBOARD_17417017585820/ProductAnalysis)")
    st.write("Comprehensive dashboard analyzing Superstore's sales and product performance.")

    st.markdown("#### 🔹 [Engagement Analysis NETFLIX_ID](https://public.tableau.com/app/profile/muhamad.kahfi/viz/TheInfluenceofTimeandTypeonInstagramEngagement/ENGAGEMENTNETFLIX_ID)")
    st.write("The Influence of Time and Type on Instagram Engagement.")


# ---- Education ----
elif selected == "Education":
    st.markdown("## 🎓 Education")
    st.markdown("""
    🔹 **Data Science & Machine Learning**  
      Purwadhika Digital Technology School | *2025*  
      Skills: Python, SQL, Tableau, ETL, and Machine Learning
                
    🔹 **Bachelor’s Degree in Economics (Management Department)**  
      UIN Sunan Gunung Djati, Bandung | *2020 - 2024*  
      GPA: **3.72 / 4.00**  
      Thesis: The Influence of Dividend Yield, Dividend Payout Ratio, and Earnings Volatility on Stock Price Volatility in Banking Sector Companies Listed on the Indonesia Stock Exchange (2018–2022)
    """)

# ---- Contact ----
elif selected == "Contact":
    st.markdown("## 📬 Contact")
    st.write("📧 Email: kahfidwi2112@gmail.com")  
    st.write("🔗 LinkedIn: [linkedin.com/in/muhamadkahfidwi](https://www.linkedin.com/in/muhamadkahfidwi)")  
    st.write("💻 GitHub: [github.com/kahfidwi](https://github.com/kahfidwi)")
    st.markdown("""
    <a href="mailto:kahfidwi2112@gmail.com?subject=Contact%20from%20Portfolio" target="_blank" class="contact-btn">
        Contact Me via Email
    </a>
    """, unsafe_allow_html=True)

# ---- Footer ----
st.markdown("<div class='footer'>Thank you for visiting my portfolio 🙏</div>", unsafe_allow_html=True)
