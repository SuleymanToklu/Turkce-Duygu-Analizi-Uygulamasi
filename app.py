# This script uses a pre-trained model and does not require any training.
# It is designed to work out-of-the-box with minimal setup.

import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# --- Page Configuration ---
# Set up the page title, icon, and layout.
st.set_page_config(
    page_title="Türkçe Duygu Analizi",
    page_icon="🤖",
    layout="centered"
)


# --- Model Loading ---
# This function loads a pre-trained sentiment analysis model.
# @st.cache_resource ensures the model is loaded only once, making the app faster.
@st.cache_resource
def load_model():
    """
    Load the pre-trained model and tokenizer from Hugging Face Hub.
    This model is already fine-tuned for Turkish sentiment analysis.
    """
    model_name = "savasy/bert-base-turkish-sentiment-cased"
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        return tokenizer, model
    except Exception as e:
        # Handle potential network errors or other issues during download.
        st.error(f"Model yüklenirken bir hata oluştu: {e}")
        return None, None


# --- Prediction Function ---
def predict(text, tokenizer, model):
    """
    Analyzes the input text and returns the predicted sentiment and confidence score.
    """
    # Prepare the text for the model.
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    # The model does not require gradient calculations for inference.
    with torch.no_grad():
        outputs = model(**inputs)

    # Convert model output (logits) to probabilities.
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)

    # The model has labels: 0 for 'negative', 1 for 'positive'.
    # Get the predicted class index.
    predicted_class_id = torch.argmax(probabilities, dim=1).item()

    # Get the confidence score for the predicted class.
    confidence = probabilities[0][predicted_class_id].item()

    # Map class ID to a human-readable label.
    sentiment = "Pozitif" if predicted_class_id == 1 else "Negatif"

    return sentiment, confidence


# --- Streamlit App Layout ---
st.title("✅ Türkçe Duygu Analizi Uygulaması")
st.markdown(
    "Aşağıdaki metin kutusuna bir cümle yazın ve 'Analiz Et' butonuna tıklayın. "
    "Bu uygulama, hazır eğitilmiş bir modeli kullanarak metnin duygu durumunu tahmin edecektir."
)

# Load the model and tokenizer.
tokenizer, model = load_model()

# Check if the model was loaded successfully before showing the rest of the UI.
if tokenizer and model:
    # Create a text area for user input.
    user_input = st.text_area("Metin:", "Bu ürünün kalitesi beklentimin çok üzerindeydi, kesinlikle tavsiye ederim.",
                              height=150)

    # Create a button to trigger the analysis.
    if st.button("Analiz Et", type="primary"):
        if user_input:
            # If input is provided, run the prediction.
            with st.spinner('Analiz ediliyor...'):
                sentiment, confidence = predict(user_input, tokenizer, model)

            st.markdown("---")
            st.subheader("Sonuç")

            # Display the result in a colored box.
            if sentiment == "Pozitif":
                st.success(f"Tahmin Edilen Duygu: **{sentiment}** 👍")
            else:
                st.error(f"Tahmin Edilen Duygu: **{sentiment}** �")

            # Display the confidence score.
            st.metric(label="Modelin Güven Skoru", value=f"{confidence:.2%}")

        else:
            # Show a warning if the user clicks without entering text.
            st.warning("Lütfen analiz edilecek bir metin girin.")
else:
    st.header("Başlatma Hatası")
    st.write("Uygulama başlatılamadı. Lütfen internet bağlantınızı kontrol edin ve sayfayı yenileyin.")