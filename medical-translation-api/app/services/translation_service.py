from app.config.settings import settings
from groq import Groq

class TranslationService:
    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)
    
    async def medical_translate(self, text: str, source_lang: str, target_lang: str) -> str:
        prompt = f"""Translate medical texts between {source_lang} and {target_lang} with:

Exact preservation of medical terminology

Retention of numerical values/measurements

Clinical context consistency

Examples:

Cardiology Note
Source (EN): "62yo male with STEMI, BP 140/90 mmHg, prescribed aspirin 81mg OD and atorvastatin 80mg HS."
Target (ES): "Varón de 62 años con IAMCEST, TA 140/90 mmHg, prescrito aspirina 81mg OD y atorvastatina 80mg HS."


Radiology Finding
Source (DE): "15mm nichtverkalkter Lungenrundherd im rechten Oberlappen, BI-RADS 4."
Target (ZH): "右肺上叶15mm非钙化性肺结节，BI-RADS 4级。"

Prescription
Source (EN): "Take metformin 500mg PO BID with meals, hold if eGFR <30 mL/min/1.73m²."
Target (AR): "تناول ميتفورمين 500 مجم عن طريق الفم مرتين يوميًا مع الوجبات، أوقف إذا كان معدل الترشيح الكبيبي <30 مل/دقيقة/1.73 م²."

Rules:

Never localize measurement units (keep mg/dL, IU/L, etc.)

Preserve original drug names (no generics substitution)

Maintain alphanumeric values exactly (HbA1c 7.2% → 7.2% نه ٧٫٢٪)

Retain standardized codes (ICD-10, LOINC, etc.) untranslated


Text : {text}"""
        
        response = self.client.chat.completions.create(
            model=settings.llm_model,
            messages=[{
                "role": "user", 
                "content": prompt
            }],
            temperature=0.1,
            max_tokens=4000
        )
        return response.choices[0].message.content