import streamlit as st
import os
import requests
from dotenv import load_dotenv

# Load API key dari .env
load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    st.error("API key tidak ditemukan. Pastikan Anda telah mengatur .env dengan benar.")
    st.stop()

# Base URL API DashScope
base_url = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions"

st.title("Klasifikasi Gambar dengan Qwen VL Max")
st.write("Masukkan URL gambar sampah, dan AI akan mengklasifikasikannya.")

# Input URL gambar
image_url = st.text_input("Masukkan URL gambar", "https://images.weserv.nl/?url=i.imgur.com/5xBqZe7.jpeg")

if image_url:
    # Tampilkan gambar yang diinput
    st.image(image_url, caption="Gambar yang diunggah", use_column_width=True)

    # Format request ke API DashScope
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Apa kategori dari sampah ini?"},
                {"type": "image_url", "image_url": {"url": image_url}}
            ]
        }
    ]

    if st.button("Kirim"):
        with st.spinner("Menganalisis gambar..."):
            try:
                response = requests.post(
                    base_url,
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "qwen-vl-max",
                        "messages": messages
                    }
                )

                # Cek respons dari API
                if response.status_code == 200:
                    result = response.json()
                    st.subheader("Hasil Analisis AI:")
                    st.write(result)
                else:
                    st.error(f"Terjadi kesalahan: {response.status_code} - {response.text}")

            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")

# import streamlit as st
# import os
# import requests
# import base64
# from dotenv import load_dotenv

# # Load API key dari .env
# load_dotenv()
# api_key = os.getenv("API_KEY")

# if not api_key:
#     st.error("API key tidak ditemukan. Pastikan Anda telah mengatur .env dengan benar.")
#     st.stop()

# # Base URL API DashScope
# base_url = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions"

# st.title("Klasifikasi Gambar dengan Qwen VL Max")
# st.write("Unggah gambar sampah, dan AI akan mengklasifikasikannya.")

# uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Konversi gambar ke Base64
#     image_bytes = uploaded_file.getvalue()
#     image_base64 = base64.b64encode(image_bytes).decode("utf-8")

#     # Tampilkan gambar
#     st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)

#     # Format request ke API DashScope
#     messages = [
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": "Apa kategori dari sampah ini?"},
#                 {"type": "image_base64", "image_base64": {"data": image_base64}}
#             ]
#         }
#     ]

#     if st.button("Kirim"):
#         with st.spinner("Menganalisis gambar..."):
#             try:
#                 response = requests.post(
#                     base_url,
#                     headers={
#                         "Authorization": f"Bearer {api_key}",
#                         "Content-Type": "application/json"
#                     },
#                     json={
#                         "model": "qwen-vl-max",
#                         "messages": messages
#                     }
#                 )

#                 # Cek respons dari API
#                 if response.status_code == 200:
#                     result = response.json()
#                     st.subheader("Hasil Analisis AI:")
#                     st.write(result)
#                 else:
#                     st.error(f"Terjadi kesalahan: {response.status_code} - {response.text}")

#             except Exception as e:
#                 st.error(f"Terjadi kesalahan: {e}")


# # import streamlit as st
# # import requests
# # import os
# # import base64
# # from dotenv import load_dotenv

# # # Load API Key dari .env
# # load_dotenv()
# # api_key = os.getenv("API_KEY")

# # # Pastikan API Key tersedia
# # if not api_key:
# #     st.error("API Key tidak ditemukan. Periksa file .env!")
# #     st.stop()

# # # Setup Streamlit
# # st.title("Klasifikasi Gambar Sampah dengan Qwen VL Max")
# # st.write("Unggah gambar sampah, dan AI akan mengklasifikasikannya.")

# # # Upload file gambar
# # uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

# # if uploaded_file:
# #     st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)

# #     # Konversi gambar ke Base64
# #     with st.spinner("Mengonversi gambar..."):
# #         img_bytes = uploaded_file.getvalue()
# #         img_base64 = base64.b64encode(img_bytes).decode("utf-8")

# #     # Kirim gambar ke DashScope
# #     messages = [
# #         {
# #             "role": "user",
# #             "content": [
# #                 {"type": "text", "text": "Apa kategori dari sampah ini?"},
# #                 {"type": "image", "image": {"base64": img_base64}}
# #             ]
# #         }
# #     ]

# #     # Kirim request ke DashScope
# #     if st.button("Kirim"):
# #         with st.spinner("Menganalisis gambar..."):
# #             try:
# #                 response = requests.post(
# #                     "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions",
# #                     headers={
# #                         "Authorization": f"Bearer {api_key}",
# #                         "Content-Type": "application/json"
# #                     },
# #                     json={"model": "qwen-vl-max", "messages": messages}
# #                 )

# #                 # Cek hasil respons
# #                 if response.status_code == 200:
# #                     result = response.json()
# #                     st.subheader("Hasil Analisis AI:")
# #                     st.write(result)
# #                 else:
# #                     st.error(f"Terjadi kesalahan: {response.status_code} - {response.text}")

# #             except Exception as e:
# #                 st.error(f"Terjadi kesalahan: {e}")

# # # import streamlit as st
# # # import os
# # # import requests
# # # from dotenv import load_dotenv

# # # # Load API key from .env
# # # load_dotenv()
# # # api_key = os.getenv("API_KEY")

# # # # Cek jika API key tersedia
# # # if not api_key:
# # #     st.error("API key tidak ditemukan. Pastikan Anda telah mengatur .env dengan benar.")
# # #     st.stop()

# # # # Base URL dan endpoint
# # # base_url = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
# # # endpoint = "/chat/completions"

# # # # Setup Streamlit UI
# # # st.title("Klasifikasi Gambar dengan Qwen VL Max")
# # # st.write("Unggah gambar sampah, dan AI akan mengklasifikasikannya.")

# # # # Upload file gambar
# # # uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

# # # if uploaded_file is not None:
# # #     # Simpan gambar ke folder upload
# # #     file_path = f"upload/{uploaded_file.name}"
# # #     with open(file_path, "wb") as f:
# # #         f.write(uploaded_file.getbuffer())
    
# # #     # Tampilkan gambar yang di-upload
# # #     st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)

# # #     # Dapatkan URL gambar (pastikan ini dapat diakses oleh API)
# # #     # Anda mungkin perlu mengupload gambar ke server yang dapat diakses publik
# # #     image_url = f"http://localhost:8501/{file_path}"  # Ganti dengan URL yang sesuai

# # #     # Format request untuk DashScope
# # #     messages = [
# # #         {
# # #             "role": "user",
# # #             "content": [
# # #                 {"type": "text", "text": "Apa kategori dari sampah ini?"},
# # #                 {"type": "image_url", "image_url": {"url": image_url}}
# # #             ]
# # #         }
# # #     ]

# # #     # Kirim request ke API
# # #     if st.button("Kirim"):
# # #         with st.spinner("Menganalisis gambar..."):
# # #             try:
# # #                 response = requests.post(
# # #                     f"{base_url}{endpoint}",
# # #                     headers={
# # #                         "Authorization": f"Bearer {api_key}",
# # #                         "Content-Type": "application/json"
# # #                     },
# # #                     json={
# # #                         "model": "qwen-vl-max",
# # #                         "messages": messages
# # #                     }
# # #                 )

# # #                 # Cek status respons
# # #                 if response.status_code == 200:
# # #                     result = response.json()
# # #                     st.subheader("Hasil Analisis AI:")
# # #                     st.write(result)
# # #                 else:
# # #                     st.error(f"Terjadi kesalahan: {response.status_code} - {response.text}")

# # #             except Exception as e:
# # #                 st.error(f"Terjadi kesalahan: {e}")


# # # # # import streamlit as st
# # # # # import dashscope
# # # # # import os
# # # # # from dotenv import load_dotenv

# # # # # # Load API key from .env
# # # # # load_dotenv()
# # # # # api_key = os.getenv("API_KEY")

# # # # # # Check if API key is available
# # # # # if not api_key:
# # # # #     raise ValueError("API_KEY not found in .env!")

# # # # # # Set API key to DashScope
# # # # # dashscope.api_key = api_key

# # # # # # Folder to save uploaded images
# # # # # UPLOAD_FOLDER = "upload"
# # # # # if not os.path.exists(UPLOAD_FOLDER):
# # # # #     os.makedirs(UPLOAD_FOLDER)

# # # # # # Setup Streamlit UI
# # # # # st.title("Waste Classification with AI")
# # # # # st.write("Upload an image of waste, and AI will classify it.")

# # # # # # Upload image file
# # # # # uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# # # # # if uploaded_file is not None:
# # # # #     # Save the uploaded image
# # # # #     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
# # # # #     with open(file_path, "wb") as f:
# # # # #         f.write(uploaded_file.getbuffer())
    
# # # # #     # Display the uploaded image
# # # # #     st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

# # # # #     # Get the image URL (ensure it's publicly accessible)
# # # # #     image_url = f"http://localhost:8501/{file_path}"  # Change to a public URL if needed

# # # # #     # Prepare request for DashScope
# # # # #     messages = [
# # # # #         {
# # # # #             "role": "user",
# # # # #             "content": [
# # # # #                 {"type": "text", "text": "What category does this waste belong to?"},
# # # # #                 {"type": "image_url", "image_url": {"url": image_url}}
# # # # #             ]
# # # # #         }
# # # # #     ]

# # # # #     # Send request to API
# # # # #     with st.spinner("Analyzing the image..."):
# # # # #         try:
# # # # #             response = dashscope.Generation.call(
# # # # #                 api_key=api_key,
# # # # #                 model="qwen-vl-plus",  # Change to the appropriate model
# # # # #                 messages=messages,
# # # # #                 result_format="message"
# # # # #             )

# # # # #             # Display API response
# # # # #             st.subheader("API Response:")
# # # # #             st.json(response)

# # # # #             # Extract and display the result
# # # # #             output = response.get("output", {})
# # # # #             result = output.get("text", "No result found.")
# # # # #             st.subheader("AI Analysis Result:")
# # # # #             st.write(result)

# # # # #         except Exception as e:
# # # # #             st.error(f"An error occurred: {e}")

# # # # # # import streamlit as st
# # # # # # import dashscope
# # # # # # import os
# # # # # # import base64
# # # # # # from dotenv import load_dotenv

# # # # # # # Load API key dari .env
# # # # # # load_dotenv()
# # # # # # api_key = os.getenv("API_KEY")

# # # # # # # Cek jika API key tersedia
# # # # # # if not api_key:
# # # # # #     raise ValueError("API_KEY tidak ditemukan di .env!")

# # # # # # # Set API key ke DashScope
# # # # # # dashscope.api_key = api_key

# # # # # # # Folder untuk menyimpan gambar yang di-upload
# # # # # # UPLOAD_FOLDER = "upload"
# # # # # # if not os.path.exists(UPLOAD_FOLDER):
# # # # # #     os.makedirs(UPLOAD_FOLDER)

# # # # # # # Fungsi untuk mengonversi gambar ke Base64
# # # # # # def encode_image_to_base64(image_file):
# # # # # #     return base64.b64encode(image_file.read()).decode("utf-8")

# # # # # # # Setup Streamlit UI
# # # # # # st.title("Sampah Bercuan - Klasifikasi Sampah dengan AI")
# # # # # # st.write("Upload gambar sampah, dan AI akan mengklasifikasikannya.")

# # # # # # # Upload file gambar
# # # # # # uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

# # # # # # if uploaded_file is not None:
# # # # # #     # Simpan gambar ke folder upload
# # # # # #     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
# # # # # #     with open(file_path, "wb") as f:
# # # # # #         f.write(uploaded_file.getbuffer())
    
# # # # # #     # Tampilkan gambar yang di-upload
# # # # # #     st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)

# # # # # #     # Encode gambar ke Base64
# # # # # #     encoded_image = encode_image_to_base64(uploaded_file)

# # # # # #     # Format request untuk DashScope
# # # # # #     messages = [
# # # # # #         {
# # # # # #             "role": "user",
# # # # # #             "content": [
# # # # # #                 {"type": "text", "text": "Apa kategori dari sampah ini?"},
# # # # # #                 {"type": "image", "image": {"base64": encoded_image}}
# # # # # #             ]
# # # # # #         }
# # # # # #     ]

# # # # # #     # Kirim request ke API
# # # # # #    # Kirim request ke API
# # # # # #     with st.spinner("Menganalisis gambar..."):
# # # # # #         try:
# # # # # #             response = dashscope.MultiModalConversation.call(
# # # # # #                 model="qwen-vl-max",
# # # # # #                 messages=messages,
# # # # # #                 temperature=0.7,
# # # # # #                 max_tokens=500,
# # # # # #                 result_format="message"
# # # # # #             )
    
# # # # # #             # Debugging: Tampilkan tipe respons
# # # # # #             st.subheader("Debugging API Response:")
# # # # # #             st.write("Tipe respons:", type(response))
# # # # # #             st.json(response)  # Tampilkan respons untuk debugging
    
# # # # # #             # Coba akses nilai hasil analisis
# # # # # #             if isinstance(response, dict):
# # # # # #                 # Debugging: Tampilkan semua kunci dalam respons
# # # # # #                 st.write("Kunci dalam respons:", response.keys())
    
# # # # # #                 output = response.get("output", None)
    
# # # # # #                 # Pastikan output tidak None dan adalah dictionary
# # # # # #                 if output is not None and isinstance(output, dict):
# # # # # #                     result = output.get("text", "Tidak ada hasil yang ditemukan.")
# # # # # #                 else:
# # # # # #                     result = "Format output tidak sesuai harapan."
# # # # # #             else:
# # # # # #                 result = "Respons API tidak dalam format yang benar."
    
# # # # # #             st.subheader("Hasil Analisis AI:")
# # # # # #             st.write(result)
    
# # # # # #         except Exception as e:
# # # # # #             st.error(f"Terjadi kesalahan: {e}")

# # # # # # # import streamlit as st
# # # # # # # import dashscope
# # # # # # # import os
# # # # # # # import base64
# # # # # # # from dotenv import load_dotenv

# # # # # # # # Load API key dari .env
# # # # # # # load_dotenv()
# # # # # # # api_key = os.getenv("API_KEY")

# # # # # # # # Cek jika API key tersedia
# # # # # # # if not api_key:
# # # # # # #     raise ValueError("API_KEY tidak ditemukan di .env!")

# # # # # # # # Set API key ke DashScope
# # # # # # # dashscope.api_key = api_key

# # # # # # # # Folder untuk menyimpan gambar yang di-upload
# # # # # # # UPLOAD_FOLDER = "upload"
# # # # # # # if not os.path.exists(UPLOAD_FOLDER):
# # # # # # #     os.makedirs(UPLOAD_FOLDER)

# # # # # # # # Fungsi untuk mengonversi gambar ke Base64
# # # # # # # def encode_image_to_base64(image_file):
# # # # # # #     return base64.b64encode(image_file.read()).decode("utf-8")

# # # # # # # # Setup Streamlit UI
# # # # # # # st.title("Sampah Bercuan - Klasifikasi Sampah dengan AI")
# # # # # # # st.write("Upload gambar sampah, dan AI akan mengklasifikasikannya.")

# # # # # # # # Upload file gambar
# # # # # # # uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

# # # # # # # if uploaded_file is not None:
# # # # # # #     # Simpan gambar ke folder upload
# # # # # # #     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
# # # # # # #     with open(file_path, "wb") as f:
# # # # # # #         f.write(uploaded_file.getbuffer())
    
# # # # # # #     # Tampilkan gambar yang di-upload
# # # # # # #     st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)

# # # # # # #     # Encode gambar ke Base64
# # # # # # #     encoded_image = encode_image_to_base64(uploaded_file)

# # # # # # #     # Format request untuk DashScope
# # # # # # #     messages = [
# # # # # # #         {
# # # # # # #             "role": "user",
# # # # # # #             "content": [
# # # # # # #                 {"type": "text", "text": "Apa kategori dari sampah ini?"},
# # # # # # #                 {"type": "image", "image": {"base64": encoded_image}}
# # # # # # #             ]
# # # # # # #         }
# # # # # # #     ]

# # # # # # #     # Kirim request ke API
# # # # # # #     with st.spinner("Menganalisis gambar..."):
# # # # # # #         try:
# # # # # # #             response = dashscope.MultiModalConversation.call(
# # # # # # #                 model="qwen-vl-max",
# # # # # # #                 messages=messages,
# # # # # # #                 temperature=0.7,
# # # # # # #                 max_tokens=500,
# # # # # # #                 result_format="message"
# # # # # # #             )

# # # # # # #             # Debugging: Tampilkan seluruh respons API di Streamlit
# # # # # # #             st.subheader("Debugging API Response:")
# # # # # # #             st.json(response)

# # # # # # #             # Periksa apakah response adalah dictionary
# # # # # # #             if isinstance(response, dict):
# # # # # # #                 output = response.get("output", {})

# # # # # # #                 # Pastikan output adalah dictionary
# # # # # # #                 if isinstance(output, dict):
# # # # # # #                     result = output.get("text", "Tidak ada hasil.")
# # # # # # #                 else:
# # # # # # #                     result = "Format output tidak sesuai harapan."
# # # # # # #             else:
# # # # # # #                 result = "Respons API tidak dalam format yang benar."

# # # # # # #             st.subheader("Hasil Analisis AI:")
# # # # # # #             st.write(result)

# # # # # # #         except Exception as e:
# # # # # # #             st.error(f"Terjadi kesalahan: {e}")


# # # # # # # # import streamlit as st
# # # # # # # # import dashscope
# # # # # # # # import os
# # # # # # # # import base64
# # # # # # # # from dotenv import load_dotenv

# # # # # # # # # Load API key dari .env
# # # # # # # # load_dotenv()
# # # # # # # # api_key = os.getenv("API_KEY")

# # # # # # # # # Cek jika API key tersedia
# # # # # # # # if not api_key:
# # # # # # # #     raise ValueError("API_KEY tidak ditemukan di .env!")

# # # # # # # # # Set API key ke DashScope
# # # # # # # # dashscope.api_key = api_key

# # # # # # # # # Folder untuk menyimpan gambar yang di-upload
# # # # # # # # UPLOAD_FOLDER = "upload"
# # # # # # # # if not os.path.exists(UPLOAD_FOLDER):
# # # # # # # #     os.makedirs(UPLOAD_FOLDER)

# # # # # # # # # Fungsi untuk mengonversi gambar ke Base64
# # # # # # # # def encode_image_to_base64(image_file):
# # # # # # # #     return base64.b64encode(image_file.read()).decode("utf-8")

# # # # # # # # # Setup Streamlit UI
# # # # # # # # st.title("Sampah Bercuan - Klasifikasi Sampah dengan AI")
# # # # # # # # st.write("Upload gambar sampah, dan AI akan mengklasifikasikannya.")

# # # # # # # # # Upload file gambar
# # # # # # # # uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

# # # # # # # # if uploaded_file is not None:
# # # # # # # #     # Simpan gambar ke folder upload
# # # # # # # #     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
# # # # # # # #     with open(file_path, "wb") as f:
# # # # # # # #         f.write(uploaded_file.getbuffer())
    
# # # # # # # #     # Tampilkan gambar yang di-upload
# # # # # # # #     st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)

# # # # # # # #     # Encode gambar ke Base64
# # # # # # # #     encoded_image = encode_image_to_base64(uploaded_file)

# # # # # # # #     # Format request untuk DashScope
# # # # # # # #     messages = [
# # # # # # # #         {
# # # # # # # #             "role": "user",
# # # # # # # #             "content": [
# # # # # # # #                 {"type": "text", "text": "Apa kategori dari sampah ini?"},
# # # # # # # #                 {"type": "image", "image": {"base64": encoded_image}}
# # # # # # # #             ]
# # # # # # # #         }
# # # # # # # #     ]

# # # # # # # #     # Kirim request ke API
# # # # # # # #     with st.spinner("Menganalisis gambar..."):
# # # # # # # #         try:
# # # # # # # #             response = dashscope.MultiModalConversation.call(
# # # # # # # #                 model="qwen-vl-max",
# # # # # # # #                 messages=messages,
# # # # # # # #                 temperature=0.7,
# # # # # # # #                 max_tokens=500,
# # # # # # # #                 result_format="message"
# # # # # # # #             )

# # # # # # # #             # Debugging: print response
# # # # # # # #             print("Response API:", response)

# # # # # # # #             if response and response.get("output"):
# # # # # # # #                 result = response["output"].get("text", "Tidak ada hasil.")
# # # # # # # #             else:
# # # # # # # #                 result = "Gagal mendapatkan hasil dari AI."

# # # # # # # #             st.subheader("Hasil Analisis AI:")
# # # # # # # #             st.write(result)

# # # # # # # #         except Exception as e:
# # # # # # # #             st.error(f"Terjadi kesalahan: {e}")





# # # # # # # # # # import os
# # # # # # # # # # import requests
# # # # # # # # # # import streamlit as st
# # # # # # # # # # import base64
# # # # # # # # # # from dotenv import load_dotenv

# # # # # # # # # # # Load API key dari .env
# # # # # # # # # # load_dotenv()
# # # # # # # # # # api_key = os.getenv("API_KEY")

# # # # # # # # # # # Cek jika API key tersedia
# # # # # # # # # # if not api_key:
# # # # # # # # # #     raise ValueError("API_KEY tidak ditemukan di .env!")

# # # # # # # # # # # Folder untuk menyimpan gambar yang di-upload
# # # # # # # # # # UPLOAD_FOLDER = "upload"
# # # # # # # # # # if not os.path.exists(UPLOAD_FOLDER):
# # # # # # # # # #     os.makedirs(UPLOAD_FOLDER)

# # # # # # # # # # # Streamlit UI
# # # # # # # # # # st.title("Sampah Bercuan")
# # # # # # # # # # st.write("Upload gambar sampah untuk klasifikasi dan mendapatkan saldo e-wallet.")

# # # # # # # # # # # Fungsi encode gambar ke base64
# # # # # # # # # # def encode_image(file_path):
# # # # # # # # # #     with open(file_path, "rb") as image_file:
# # # # # # # # # #         return base64.b64encode(image_file.read()).decode("utf-8")

# # # # # # # # # # # Fungsi untuk klasifikasi gambar menggunakan API
# # # # # # # # # # def categorize_image(file_path):
# # # # # # # # # #     try:
# # # # # # # # # #         image_base64 = encode_image(file_path)
# # # # # # # # # #         response = requests.post(
# # # # # # # # # #             "https://dashscope-intl.aliyuncs.com/api/v1/multimodal/chat",
# # # # # # # # # #             headers={
# # # # # # # # # #                 "Authorization": f"Bearer {api_key}",
# # # # # # # # # #                 "Content-Type": "application/json",
# # # # # # # # # #             },
# # # # # # # # # #             json={
# # # # # # # # # #                 "model": "qwen-vl-plus",
# # # # # # # # # #                 "messages": [
# # # # # # # # # #                     {"role": "system", "content": "You are an AI that categorizes images."},
# # # # # # # # # #                     {"role": "user", "content": "Apa kategori dari gambar ini?", "images": [f"data:image/jpeg;base64,{image_base64}"]}
# # # # # # # # # #                 ]
# # # # # # # # # #             }
# # # # # # # # # #         )
# # # # # # # # # #         result = response.json()
# # # # # # # # # #         return result.get("output", {}).get("text", "Kategori tidak ditemukan.")
# # # # # # # # # #     except Exception as e:
# # # # # # # # # #         return f"Error: {str(e)}"

# # # # # # # # # # # Layout utama untuk upload gambar
# # # # # # # # # # uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "png", "jpeg"])
# # # # # # # # # # st.markdown("---")

# # # # # # # # # # # Menampilkan hasil upload gambar dan klasifikasi
# # # # # # # # # # if uploaded_file is not None:
# # # # # # # # # #     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
# # # # # # # # # #     with open(file_path, "wb") as f:
# # # # # # # # # #         f.write(uploaded_file.getbuffer())

# # # # # # # # # #     # Tampilkan gambar yang diupload
# # # # # # # # # #     st.image(file_path, caption="Gambar yang diupload", use_container_width=True)

# # # # # # # # # #     # Klasifikasi gambar
# # # # # # # # # #     kategori = categorize_image(file_path)
# # # # # # # # # #     st.subheader("Hasil Klasifikasi")
# # # # # # # # # #     st.write(kategori)



# # # # # # # # # import streamlit as st
# # # # # # # # # import dashscope
# # # # # # # # # import os
# # # # # # # # # import base64
# # # # # # # # # from dotenv import load_dotenv

# # # # # # # # # # Load API key dari .env
# # # # # # # # # load_dotenv()
# # # # # # # # # api_key = os.getenv("API_KEY")

# # # # # # # # # # Cek jika API key tersedia
# # # # # # # # # if not api_key:
# # # # # # # # #     raise ValueError("API_KEY tidak ditemukan di .env!")

# # # # # # # # # # Set API key ke DashScope
# # # # # # # # # dashscope.api_key = api_key

# # # # # # # # # # Folder untuk menyimpan gambar yang di-upload
# # # # # # # # # UPLOAD_FOLDER = "upload"
# # # # # # # # # if not os.path.exists(UPLOAD_FOLDER):
# # # # # # # # #     os.makedirs(UPLOAD_FOLDER)

# # # # # # # # # # Fungsi untuk mengonversi gambar ke Base64
# # # # # # # # # def encode_image_to_base64(image_file):
# # # # # # # # #     return base64.b64encode(image_file.read()).decode("utf-8")

# # # # # # # # # # Setup Streamlit UI
# # # # # # # # # st.title("Sampah Bercuan - Klasifikasi Sampah dengan AI")
# # # # # # # # # st.write("Upload gambar sampah, dan AI akan mengklasifikasikannya.")

# # # # # # # # # # Upload file gambar
# # # # # # # # # uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

# # # # # # # # # if uploaded_file is not None:
# # # # # # # # #     # Simpan gambar ke folder upload
# # # # # # # # #     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
# # # # # # # # #     with open(file_path, "wb") as f:
# # # # # # # # #         f.write(uploaded_file.getbuffer())
    
# # # # # # # # #     # Tampilkan gambar yang di-upload
# # # # # # # # #     st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)

# # # # # # # # #     # Encode gambar ke Base64
# # # # # # # # #     encoded_image = encode_image_to_base64(uploaded_file)

# # # # # # # # #     # Format pesan sesuai dengan Qwen-VL-Plus API
# # # # # # # # #     messages = [
# # # # # # # # #         {
# # # # # # # # #             "role": "user",
# # # # # # # # #             "content": [
# # # # # # # # #                 {"type": "text", "text": "Apa yang ada di gambar ini?"},
# # # # # # # # #                 {"type": "image", "image": {"base64": encoded_image}}
# # # # # # # # #             ]
# # # # # # # # #         }
# # # # # # # # #     ]

# # # # # # # # #     # Kirim request ke API
# # # # # # # # #     with st.spinner("Menganalisis gambar..."):
# # # # # # # # #         try:
# # # # # # # # #             response = dashscope.ChatCompletion.create(
# # # # # # # # #                 model="qwen-vl-plus",
# # # # # # # # #                 messages=messages,
# # # # # # # # #                 temperature=0.7,
# # # # # # # # #                 max_tokens=500,
# # # # # # # # #                 response_format={"type": "text"}
# # # # # # # # #             )
            
# # # # # # # # #             # Ambil hasil analisis
# # # # # # # # #             result = response.output.choices[0].message["content"]
# # # # # # # # #             st.subheader("Hasil Analisis AI:")
# # # # # # # # #             st.write(result)

# # # # # # # # #         except Exception as e:
# # # # # # # # #             st.error(f"Terjadi kesalahan: {e}")
