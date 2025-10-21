#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simple para reescribir textos específicos de Eliou Masajes usando Google Gemini
"""

import google.generativeai as genai
import time

# Configuración de la API de Google Gemini
GOOGLE_API_KEY = "AIzaSyD1dGRLMfot_aXriZKx-N8ciETqvNByI18"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('models/gemini-pro-latest')

def rewrite_text_for_eliou(text, content_type="general"):
    """
    Reescribe texto específico para Eliou Masajes Porto Alegre
    """
    
    base_prompt = f"""
    Eres un experto copywriter especializado en servicios de salud y bienestar.
    
    CONTEXTO DEL NEGOCIO:
    - Nombre: Eliou Masajes Terapéuticos
    - Ubicación: Porto Alegre, Rio Grande do Sul, Brasil
    - Especialidades: Masajes terapéuticos, fisioterapia, acupuntura
    - Público objetivo: Personas con dolor crónico, estrés, atletas, ejecutivos
    - Teléfono: +56941309260
    - Email: eliou.masajes@gmail.com
    
    INSTRUCCIONES GENERALES:
    1. Reescribe el texto en español de forma profesional y persuasiva
    2. Enfoca en beneficios específicos para el cliente
    3. Usa terminología médica profesional pero accesible
    4. Incluye elementos de urgencia suave y llamadas a la acción
    5. Optimiza para SEO local de Porto Alegre
    6. Mantén el tono cálido pero profesional
    7. Enfatiza la experiencia y credibilidad de Eliou
    
    TIPO DE CONTENIDO: {content_type}
    
    TEXTO ORIGINAL A REESCRIBIR:
    {text}
    
    TEXTO REESCRITO OPTIMIZADO:
    """
    
    try:
        response = model.generate_content(base_prompt)
        if response.text:
            return response.text.strip()
        else:
            return text
    except Exception as e:
        print(f"Error: {e}")
        return text

# Función para procesar múltiples textos
def process_texts():
    """Procesa textos específicos identificados que necesitan mejora"""
    
    texts_to_improve = {
        "hero_title": "Masajes Terapéuticos Profesionales en Porto Alegre",
        "hero_subtitle": "Soy Eliou, masajista profesional especializado en terapias de relajación y rehabilitación. Ofrezco tratamientos personalizados para aliviar el dolor, reducir el estrés y mejorar tu bienestar físico y mental en Porto Alegre, Brasil.",
        "service_massage": "Tratamientos especializados para alivio del dolor muscular, contracturas y tensiones. Técnicas de masaje sueco, deportivo y relajante para restaurar tu bienestar físico y mental en Porto Alegre.",
        "service_physio": "Rehabilitación profesional para lesiones deportivas, problemas posturales y dolor crónico. Evaluaciones personalizadas y planes de tratamiento adaptados a tus necesidades específicas en Porto Alegre.",
        "service_acupuncture": "Medicina tradicional china para equilibrar la energía corporal, reducir el dolor crónico y mejorar la salud general. Sesiones personalizadas con técnicas milenarias aplicadas con estándares modernos.",
        "about_eliou": "Como masajista profesional certificado en Porto Alegre, me especializo en técnicas avanzadas de masaje terapéutico que van más allá de la relajación tradicional.",
        "cta_main": "🎯 Primera Consulta Gratuita para Nuevos Pacientes",
        "cta_subtitle": "Reserva tu evaluación inicial sin costo",
        "blog_title_1": "Cómo Aliviar el Dolor de Espalda",
        "blog_desc_1": "El dolor de espalda es una de las causas más comunes de ausentismo laboral. Descubre técnicas profesionales y ejercicios específicos para prevenir y tratar el dolor de espalda en casa.",
        "testimonial_1": "Eliou es increíble. Llegué con dolor de espalda crónico después de años trabajando en oficina. Sus masajes terapéuticos no solo aliviaron mi dolor, sino que me enseñó ejercicios para prevenir futuras molestias. Altamente recomendado en Porto Alegre.",
        "footer_subscribe": "Suscríbete a nuestro newsletter",
        "contact_address": "Rua dos Andradas 1234, Centro, Porto Alegre - RS, Brasil"
    }
    
    print("🚀 Iniciando reescritura de textos específicos para Eliou Masajes")
    print("=" * 70)
    
    improved_texts = {}
    
    for key, text in texts_to_improve.items():
        print(f"📝 Procesando: {key}")
        
        # Determinar tipo de contenido
        if 'hero' in key:
            content_type = "hero_section"
        elif 'service' in key:
            content_type = "service_description"
        elif 'about' in key:
            content_type = "about_section"
        elif 'cta' in key:
            content_type = "call_to_action"
        elif 'blog' in key:
            content_type = "blog_content"
        elif 'testimonial' in key:
            content_type = "testimonial"
        else:
            content_type = "general"
        
        improved = rewrite_text_for_eliou(text, content_type)
        improved_texts[key] = improved
        
        print(f"   Original: {text[:80]}...")
        print(f"   Mejorado: {improved[:80]}...")
        print()
        
        time.sleep(2)  # Rate limiting
    
    # Guardar resultados en archivo
    with open('textos_mejorados.txt', 'w', encoding='utf-8') as f:
        f.write("TEXTOS MEJORADOS PARA ELIOU MASAJES - PORTO ALEGRE\n")
        f.write("=" * 60 + "\n\n")
        
        for key, improved_text in improved_texts.items():
            f.write(f"{key.upper()}:\n")
            f.write(f"{improved_text}\n")
            f.write("-" * 40 + "\n\n")
    
    print("✅ Proceso completado!")
    print("📄 Textos guardados en: textos_mejorados.txt")
    print("🔧 Puedes copiar y pegar estos textos en el HTML")
    
    return improved_texts

if __name__ == "__main__":
    process_texts()