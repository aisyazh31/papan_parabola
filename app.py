import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Konfigurasi Halaman & Tema Warna Pastel
st.set_page_config(
    page_title="Scanner Papan Parabola Transparan",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS untuk Tema Pastel Modern (Teal #2A7B88 & Soft Mint #E6F2F2)
st.markdown("""
    <style>
    .main {
        background-color: #F8FBFB;
    }
    .stButton>button {
        background-color: #2A7B88;
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        padding: 0.6rem 1.2rem;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #21616C;
        color: white;
    }
    .card {
        background-color: #E6F2F2;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    h1, h2, h3 {
        color: #2A7B88;
    }
    </style>
""", unsafe_allow_html=True)

# Header Aplikasi
st.markdown("<h2 style='text-align: center; color: #2A7B88;'>📐 Web Scanner Papan Parabola Transparan</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Eksplorasi Fungsi Kuadrat Phygital untuk Pembelajaran Matematika Murid</p>", unsafe_allow_html=True)
st.markdown("---")

# Alur Utama: Upload / Ambil Foto
uploaded_file = st.file_uploader(
    "📷 Ambil Foto / Upload Hasil Kerja Papan Parabola", 
    type=["jpg", "jpeg", "png"],
    help="Unggah foto papan parabola fisik yang telah dipasangi paku dan karet gelang."
)

# Layout 2 Kolom (Responsif untuk HP & Desktop)
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.markdown("### 📍 1. Foto & Input Koordinat Paku")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Dokumentasi Papan Parabola Murid", use_container_width=True)
    else:
        st.info("💡 Belum ada foto diunggah. Silakan ambil atau unggah foto hasil kerja papan parabola Anda di atas.")
        
    st.markdown("Masukkan koordinat (x, y) dari 3 titik paku utama pada papan:")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Paku 1**")
        x1 = st.number_input("x₁", value=-2.0, step=1.0, format="%.1f", key="x1")
        y1 = st.number_input("y₁", value=4.0, step=1.0, format="%.1f", key="y1")
    with c2:
        st.markdown("**Paku 2 (Puncak)**")
        x2 = st.number_input("x₂", value=0.0, step=1.0, format="%.1f", key="x2")
        y2 = st.number_input("y₂", value=0.0, step=1.0, format="%.1f", key="y2")
    with c3:
        st.markdown("**Paku 3**")
        x3 = st.number_input("x₃", value=2.0, step=1.0, format="%.1f", key="x3")
        y3 = st.number_input("y₃", value=4.0, step=1.0, format="%.1f", key="y3")

with col2:
    st.markdown("### 📊 2. Render Digital & Analisis")
    
    # Validasi & Komputasi Matematika menggunakan NumPy
    x_points = np.array([x1, x2, x3])
    y_points = np.array([y1, y2, y3])
    
    try:
        if len(np.unique(x_points)) < 3:
            st.error("⚠️ Peringatan: Nilai koordinat x pada titik-titik harus berbeda agar membentuk kurva parabola yang valid.")
            valid_parabola = False
        else:
            coeffs = np.polyfit(x_points, y_points, 2)
            a, b, c = coeffs[0], coeffs[1], coeffs[2]
            
            if abs(a) < 1e-5:
                st.warning("⚠️ Titik-titik yang dimasukkan membentuk garis lurus (koefisien kuadrat a ≈ 0). Bukan parabola.")
                valid_parabola = False
            else:
                valid_parabola = True
    except Exception as e:
        st.error(f"Terjadi kesalahan komputasi: {e}")
        valid_parabola = False

    if valid_parabola:
        xp = -b / (2 * a)
        yp = a * (xp ** 2) + b * xp + c
        D = (b ** 2) - (4 * a * c)
        
        if a > 0:
            arah = "Terbuka ke Atas (Titik Balik Minimum)"
        else:
            arah = "Terbuka ke Bawah (Titik Balik Maksimum)"
            
        sign_b = f"+ {b:.2f}x" if b >= 0 else f"- {abs(b):.2f}x"
        sign_c = f"+ {c:.2f}" if c >= 0 else f"- {abs(c):.2f}"
        eq_str = f"f(x) = {a:.2f}x² {sign_b} {sign_c}"
        
        st.markdown(f"""
        <div class="card">
            <h4 style="margin-top:0; color:#2A7B88;">📝 Kartu Ringkasan Analisis</h4>
            <p><b>Persamaan Kuadrat:</b><br><code style="font-size: 1.1em; color: #21616C;">{eq_str}</code></p>
            <p><b>Koordinat Titik Puncak (xₚ, yₚ):</b> ({xp:.2f}, {yp:.2f})</p>
            <p><b>Arah Kurva:</b> {arah}</p>
            <p><b>Nilai Diskriminan (D = b² - 4ac):</b> {D:.2f}</p>
        </div>
        """, unsafe_allow_html=True)
        
        fig, ax = plt.subplots(figsize=(6, 4.5))
        
        x_min_plot = min(x_points) - 2
        x_max_plot = max(x_points) + 2
        x_curve = np.linspace(x_min_plot, x_max_plot, 400)
        y_curve = a * (x_curve ** 2) + b * x_curve + c
        
        ax.plot(x_curve, y_curve, color="#2A7B88", linewidth=3, label=f"Parabola: {eq_str}")
        ax.scatter(x_points, y_points, color="#E07A5F", s=80, zorder=5, label="Titik Paku Fisik")
        ax.scatter([xp], [yp], color="#F4A261", s=120, marker="*", zorder=6, label=f"Puncak ({xp:.1f}, {yp:.1f})")
        
        ax.axhline(0, color='grey', linewidth=1, linestyle='--')
        ax.axvline(0, color='grey', linewidth=1, linestyle='--')
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.set_title("Grafik Digital Presisi", fontsize=12, fontweight='bold', color="#2A7B88")
        ax.set_xlabel("Sumbu X", fontsize=10)
        ax.set_ylabel("Sumbu Y", fontsize=10)
        ax.legend(loc='upper right', fontsize=8)
        
        fig.patch.set_facecolor('#F8FBFB')
        ax.set_facecolor('#FFFFFF')
        
        st.pyplot(fig)
    else:
        st.info("ℹ️ Silakan masukkan koordinat 3 paku yang valid untuk merender grafik dan analisis fungsi kuadrat.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888; font-size: 0.85em;'>Media Pembelajaran Phygital Matematika SMA • Berbasis Streamlit & NumPy</p>", unsafe_allow_html=True)
