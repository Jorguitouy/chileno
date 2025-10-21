#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para reescribir textos del sitio web Eliou Masajes usando Google Gemini AI
Optimiza contenidos para SEO y convierte textos genéricos en contenido específico para masajes
"""

import google.generativeai as genai
import re
import os
from bs4 import BeautifulSoup
import time
import json

# Configuración de la API de Google Gemini
GOOGLE_API_KEY = "AIzaSyD1dGRLMfot_aXriZKx-N8ciETqvNByI18"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('models/gemini-pro-latest')

class EliouTextRewriter:
    def __init__(self):
        self.prompts = {
            'hero_section': """
            Reescribe este texto para la sección hero de Eliou Masajes Terapéuticos en Porto Alegre, Brasil.
            
            CONTEXTO: Eliou es un masajista profesional especializado en:
            - Masajes terapéuticos y relajantes
            - Fisioterapia y rehabilitación
            - Acupuntura tradicional china
            - Tratamientos para dolor crónico
            - Masajes deportivos
            
            OBJETIVO: Crear un texto convincente, profesional y orientado a conversión
            UBICACIÓN: Porto Alegre, Rio Grande do Sul, Brasil
            TELÉFONO: +56941309260
            EMAIL: eliou.masajes@gmail.com
            
            INSTRUCCIONES:
            1. Mantén el tono profesional pero cálido
            2. Incluye beneficios específicos (alivio del dolor, relajación, bienestar)
            3. Menciona la experiencia y profesionalismo
            4. Incluye una llamada a la acción clara
            5. Máximo 150 palabras
            6. Optimizado para SEO local Porto Alegre
            
            TEXTO ORIGINAL:
            """,
            
            'services': """
            Reescribe esta descripción de servicio para Eliou Masajes Terapéuticos.
            
            CONTEXTO: Servicios profesionales de masajes y terapias corporales en Porto Alegre
            
            OBJETIVOS:
            1. Destacar beneficios específicos del servicio
            2. Usar terminología médica profesional pero comprensible
            3. Crear confianza y credibilidad
            4. Orientado a conversión
            5. SEO optimizado para Porto Alegre
            
            INSTRUCCIONES:
            - Máximo 80 palabras
            - Enfoque en resultados y beneficios
            - Menciona técnicas específicas cuando sea relevante
            - Tono profesional y tranquilizador
            
            TEXTO ORIGINAL:
            """,
            
            'testimonials': """
            Reescribe este testimonio para que sea más auténtico y específico para Eliou Masajes.
            
            CONTEXTO: Testimonios reales de pacientes de Porto Alegre que han recibido tratamientos
            
            OBJETIVOS:
            1. Testimonios creíbles y específicos
            2. Mencionar resultados concretos
            3. Incluir el problema inicial y la solución
            4. Emociones auténticas
            5. Nombres brasileños comunes
            
            INSTRUCCIONES:
            - Máximo 100 palabras
            - Incluir el problema específico tratado
            - Mencionar la mejora obtenida
            - Tono personal y agradecido
            - Que suene natural y brasileño
            
            TEXTO ORIGINAL:
            """,
            
            'blog_content': """
            Reescribe este contenido de blog para Eliou Masajes, orientado a educación y SEO.
            
            CONTEXTO: Blog educativo sobre masajes, fisioterapia y bienestar en Porto Alegre
            
            OBJETIVOS:
            1. Contenido educativo valioso
            2. Posicionamiento como experto
            3. SEO optimizado para Porto Alegre
            4. Generar interés en los servicios
            5. Compartible en redes sociales
            
            INSTRUCCIONES:
            - Títulos atractivos y descriptivos
            - Contenido informativo pero no demasiado técnico
            - Incluir call-to-action sutil hacia los servicios
            - Máximo 120 palabras para descripciones
            
            TEXTO ORIGINAL:
            """,
            
            'cta_sections': """
            Reescribe esta sección de llamada a la acción para maximizar conversiones.
            
            CONTEXTO: CTA para reservar citas en Eliou Masajes Porto Alegre
            
            OBJETIVOS:
            1. Crear urgencia sin presión
            2. Destacar beneficios únicos
            3. Reducir fricción para reservar
            4. Generar confianza
            5. Optimizar conversiones
            
            INSTRUCCIONES:
            - Verbos de acción potentes
            - Beneficios claros
            - Crear sentido de valor y oportunidad
            - Máximo 50 palabras
            - Tono motivacional pero profesional
            
            TEXTO ORIGINAL:
            """,
            
            'about_section': """
            Reescribe esta sección "Acerca de" para construir confianza y autoridad.
            
            CONTEXTO: Sección sobre Eliou como profesional en Porto Alegre
            
            OBJETIVOS:
            1. Establecer credibilidad y experiencia
            2. Crear conexión emocional
            3. Diferenciarse de la competencia
            4. Generar confianza
            5. Mostrar enfoque personalizado
            
            INSTRUCCIONES:
            - Enfoque en beneficios para el paciente
            - Mencionar experiencia y certificaciones
            - Tono personal pero profesional
            - Incluir filosofía de tratamiento
            - Máximo 200 palabras
            
            TEXTO ORIGINAL:
            """
        }
    
    def clean_text(self, text):
        """Limpia el texto de caracteres especiales y espacios extra"""
        text = re.sub(r'\s+', ' ', text)  # Múltiples espacios a uno
        text = text.strip()
        return text
    
    def detect_content_type(self, text, context=""):
        """Detecta el tipo de contenido basado en el texto y contexto"""
        text_lower = text.lower()
        context_lower = context.lower()
        
        if 'testimonio' in context_lower or 'cliente' in context_lower:
            return 'testimonials'
        elif 'hero' in context_lower or len(text) > 200:
            return 'hero_section'
        elif 'servicio' in context_lower or 'terapia' in context_lower:
            return 'services'
        elif 'blog' in context_lower or 'artículo' in context_lower:
            return 'blog_content'
        elif 'reservar' in text_lower or 'cita' in text_lower:
            return 'cta_sections'
        elif 'acerca' in context_lower or 'eliou' in text_lower:
            return 'about_section'
        else:
            return 'services'  # Default
    
    def rewrite_text(self, text, content_type='services', context=""):
        """Reescribe un texto usando Gemini AI"""
        if len(text.strip()) < 10:  # Textos muy cortos no se procesan
            return text
            
        prompt = self.prompts.get(content_type, self.prompts['services'])
        full_prompt = f"{prompt}\n\nCONTEXTO ADICIONAL: {context}\n\n{text}\n\nTEXTO REESCRITO:"
        
        try:
            response = model.generate_content(full_prompt)
            if response.text:
                rewritten = self.clean_text(response.text)
                print(f"✅ Reescrito ({content_type}): {text[:50]}... → {rewritten[:50]}...")
                return rewritten
            else:
                print(f"⚠️ Sin respuesta para: {text[:50]}...")
                return text
        except Exception as e:
            print(f"❌ Error reescribiendo: {str(e)}")
            return text
    
    def process_html_file(self, file_path):
        """Procesa un archivo HTML y reescribe los textos relevantes"""
        print(f"📄 Procesando archivo: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Contadores de cambios
        changes_made = 0
        
        # 1. Reescribir títulos H1, H2, H3
        for tag in soup.find_all(['h1', 'h2', 'h3', 'h5']):
            if tag.get_text().strip() and len(tag.get_text().strip()) > 5:
                original = tag.get_text().strip()
                content_type = self.detect_content_type(original, str(tag.parent))
                rewritten = self.rewrite_text(original, content_type, f"Título {tag.name}")
                if rewritten != original:
                    tag.string = rewritten
                    changes_made += 1
                time.sleep(2)  # Rate limiting
        
        # 2. Reescribir párrafos importantes
        for p in soup.find_all('p'):
            text = p.get_text().strip()
            if text and len(text) > 20 and len(text) < 500:  # Párrafos de tamaño medio
                content_type = self.detect_content_type(text, str(p.parent))
                rewritten = self.rewrite_text(text, content_type, "Párrafo de contenido")
                if rewritten != text:
                    p.string = rewritten
                    changes_made += 1
                time.sleep(2)  # Rate limiting
        
        # 3. Reescribir textos de botones y CTAs
        for button in soup.find_all(['a', 'button'], class_=re.compile('button|btn|cta')):
            text = button.get_text().strip()
            if text and len(text) > 5:
                rewritten = self.rewrite_text(text, 'cta_sections', "Botón CTA")
                if rewritten != text and len(rewritten) <= 30:  # Botones deben ser cortos
                    button.string = rewritten
                    changes_made += 1
                time.sleep(1)
        
        # 4. Actualizar meta descriptions
        meta_desc = soup.find('meta', {'name': 'description'})
        if meta_desc:
            original_desc = meta_desc.get('content', '')
            if original_desc:
                new_desc = self.rewrite_text(original_desc, 'hero_section', "Meta description")
                meta_desc['content'] = new_desc
                changes_made += 1
                time.sleep(2)
        
        # 5. Actualizar placeholders de formularios
        for input_field in soup.find_all('input', {'placeholder': True}):
            placeholder = input_field.get('placeholder')
            if placeholder and 'Email address' in placeholder:
                input_field['placeholder'] = 'Tu dirección de email'
                changes_made += 1
        
        # Guardar archivo modificado
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        
        print(f"✅ Archivo procesado. Cambios realizados: {changes_made}")
        return changes_made

def main():
    """Función principal del script"""
    print("🚀 Iniciando reescritura de textos con Google Gemini AI")
    print("=" * 60)
    
    rewriter = EliouTextRewriter()
    
    # Archivos a procesar
    files_to_process = [
        'index.html',
        'index-pt.html',
        'about-us.html',
        'contact.html',
        'service.html'
    ]
    
    total_changes = 0
    
    for file_name in files_to_process:
        if os.path.exists(file_name):
            try:
                changes = rewriter.process_html_file(file_name)
                total_changes += changes
                print(f"Procesado: {file_name} - {changes} cambios")
                time.sleep(3)  # Pausa entre archivos
            except Exception as e:
                print(f"❌ Error procesando {file_name}: {str(e)}")
        else:
            print(f"⚠️ Archivo no encontrado: {file_name}")
    
    print("=" * 60)
    print(f"🎉 Proceso completado!")
    print(f"📊 Total de cambios realizados: {total_changes}")
    print("🔧 Recuerda revisar los cambios y hacer commit a Git")

if __name__ == "__main__":
    main()