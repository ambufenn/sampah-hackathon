import streamlit as st
import dashscope
import os
import base64
from dotenv import load_dotenv

# Load API key dari .env
load_dotenv()
api_key = os.getenv("API_KEY")

# Cek jika API key tersedia
if not api_key:
    raise ValueError("API_KEY tidak ditemukan di .env!")

# Set API key ke DashScope
dashscope.api_key = api_key

# Folder untuk menyimpan gambar yang di-upload
UPLOAD_FOLDER = "upload"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Fungsi untuk mengonversi gambar ke Base64
def encode_image_to_base64(image_file):
    return base64.b64encode(image_file.read()).decode("utf-8")

# Setup Streamlit UI
st.title("Sampah Bercuan - Klasifikasi Sampah dengan AI")
st.write("Upload gambar sampah, dan AI akan mengklasifikasikannya.")

# Upload file gambar
uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Simpan gambar ke folder upload
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Tampilkan gambar yang di-upload
    st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)

    # Encode gambar ke Base64
    encoded_image = encode_image_to_base64(uploaded_file)

    # Format pesan sesuai dengan API DashScope
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Apa yang ada di gambar ini?"},
                {"type": "image", "image": {"base64": encoded_image}}
            ]
        }
    ]

    # Kirim request ke API
    with st.spinner("Menganalisis gambar..."):
       try:
        response = dashscope.Generation.call(
        model="qwen-vl-max",
        messages=messages,
        temperature=0.7,
        max_tokens=500,
        result_format="message"
    )

    print("Response API:", response)  # Debugging untuk melihat isi response

    if response and isinstance(response, dict):
        result = response.get("output", {}).get("text", "Tidak ada hasil.")
    else:
        result = "Gagal mendapatkan hasil dari AI."

    st.subheader("Hasil Analisis AI:")
    st.write(result)

    except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")





# # import os
# # import requests
# # import streamlit as st
# # import base64
# # from dotenv import load_dotenv

# # # Load API key dari .env
# # load_dotenv()
# # api_key = os.getenv("API_KEY")

# # # Cek jika API key tersedia
# # if not api_key:
# #     raise ValueError("API_KEY tidak ditemukan di .env!")

# # # Folder untuk menyimpan gambar yang di-upload
# # UPLOAD_FOLDER = "upload"
# # if not os.path.exists(UPLOAD_FOLDER):
# #     os.makedirs(UPLOAD_FOLDER)

# # # Streamlit UI
# # st.title("Sampah Bercuan")
# # st.write("Upload gambar sampah untuk klasifikasi dan mendapatkan saldo e-wallet.")

# # # Fungsi encode gambar ke base64
# # def encode_image(file_path):
# #     with open(file_path, "rb") as image_file:
# #         return base64.b64encode(image_file.read()).decode("utf-8")

# # # Fungsi untuk klasifikasi gambar menggunakan API
# # def categorize_image(file_path):
# #     try:
# #         image_base64 = encode_image(file_path)
# #         response = requests.post(
# #             "https://dashscope-intl.aliyuncs.com/api/v1/multimodal/chat",
# #             headers={
# #                 "Authorization": f"Bearer {api_key}",
# #                 "Content-Type": "application/json",
# #             },
# #             json={
# #                 "model": "qwen-vl-plus",
# #                 "messages": [
# #                     {"role": "system", "content": "You are an AI that categorizes images."},
# #                     {"role": "user", "content": "Apa kategori dari gambar ini?", "images": [f"data:image/jpeg;base64,{image_base64}"]}
# #                 ]
# #             }
# #         )
# #         result = response.json()
# #         return result.get("output", {}).get("text", "Kategori tidak ditemukan.")
# #     except Exception as e:
# #         return f"Error: {str(e)}"

# # # Layout utama untuk upload gambar
# # uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "png", "jpeg"])
# # st.markdown("---")

# # # Menampilkan hasil upload gambar dan klasifikasi
# # if uploaded_file is not None:
# #     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
# #     with open(file_path, "wb") as f:
# #         f.write(uploaded_file.getbuffer())

# #     # Tampilkan gambar yang diupload
# #     st.image(file_path, caption="Gambar yang diupload", use_container_width=True)

# #     # Klasifikasi gambar
# #     kategori = categorize_image(file_path)
# #     st.subheader("Hasil Klasifikasi")
# #     st.write(kategori)



# import streamlit as st
# import dashscope
# import os
# import base64
# from dotenv import load_dotenv

# # Load API key dari .env
# load_dotenv()
# api_key = os.getenv("API_KEY")

# # Cek jika API key tersedia
# if not api_key:
#     raise ValueError("API_KEY tidak ditemukan di .env!")

# # Set API key ke DashScope
# dashscope.api_key = api_key

# # Folder untuk menyimpan gambar yang di-upload
# UPLOAD_FOLDER = "upload"
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# # Fungsi untuk mengonversi gambar ke Base64
# def encode_image_to_base64(image_file):
#     return base64.b64encode(image_file.read()).decode("utf-8")

# # Setup Streamlit UI
# st.title("Sampah Bercuan - Klasifikasi Sampah dengan AI")
# st.write("Upload gambar sampah, dan AI akan mengklasifikasikannya.")

# # Upload file gambar
# uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Simpan gambar ke folder upload
#     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
    
#     # Tampilkan gambar yang di-upload
#     st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)

#     # Encode gambar ke Base64
#     encoded_image = encode_image_to_base64(uploaded_file)

#     # Format pesan sesuai dengan Qwen-VL-Plus API
#     messages = [
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": "Apa yang ada di gambar ini?"},
#                 {"type": "image", "image": {"base64": encoded_image}}
#             ]
#         }
#     ]

#     # Kirim request ke API
#     with st.spinner("Menganalisis gambar..."):
#         try:
#             response = dashscope.ChatCompletion.create(
#                 model="qwen-vl-plus",
#                 messages=messages,
#                 temperature=0.7,
#                 max_tokens=500,
#                 response_format={"type": "text"}
#             )
            
#             # Ambil hasil analisis
#             result = response.output.choices[0].message["content"]
#             st.subheader("Hasil Analisis AI:")
#             st.write(result)

#         except Exception as e:
#             st.error(f"Terjadi kesalahan: {e}")
