#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para aplicar los textos mejorados por Google Gemini al sitio web de Eliou
"""

import re

def apply_improved_texts():
    """Aplica los textos mejorados al archivo HTML"""
    
    # Leer el archivo HTML actual
    with open('index.html', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Diccionario de reemplazos con los textos mejorados
    replacements = {
        # Hero section titles
        'Masajes Terapéuticos Profesionales en Porto Alegre': 'Recupera tu Equilibrio y Vive Sin Dolor en Porto Alegre',
        
        # CTA principal
        '🎯 Primera Consulta Gratuita para Nuevos Pacientes': '🎯 ¿Dolor, estrés o tensión? Descubre la raíz del problema',
        'Reserva tu evaluación inicial sin costo': 'Agenda tu Valoración Inicial Gratuita con nuestros especialistas en Porto Alegre',
        
        # Testimonial mejorado
        'Eliou es increíble. Llegué con dolor de espalda crónico después de años trabajando en oficina. Sus masajes terapéuticos no solo aliviaron mi dolor, sino que me enseñó ejercicios para prevenir futuras molestias. Altamente recomendado en Porto Alegre.': 
        'Después de años luchando con un dolor de espalda crónico, producto de mi trabajo en una oficina, encontrar a Eliou fue un punto de inflexión. Sus masajes terapéuticos no solo me brindaron un alivio inmediato y profundo, sino que me enseñó ejercicios específicos y pautas posturales. Para cualquier persona en Porto Alegre que busque una solución real y duradera, recomiendo sin dudarlo a Eliou Masajes Terapéuticos.',
        
        # Blog titles
        'Cómo Aliviar el Dolor de Espalda': '¿Dolor de Espalda en Porto Alegre? Descubre el Alivio Duradero',
        'Beneficios Científicos de los Masajes Terapéuticos': 'Masajes Terapéuticos en Porto Alegre: Ciencia y Bienestar',
        'Acupuntura: Medicina Tradicional China en Porto Alegre': 'Acupuntura Clínica en Porto Alegre: Alivio Natural del Dolor',
        'Fisioterapia Moderna: Técnicas Avanzadas de Rehabilitación': 'Fisioterapia Especializada en Porto Alegre: Tu Recuperación Total',
        
        # Footer improvements
        'Subscribe us': 'Recibe Consejos de Salud Directo a tu Email',
        'Email address': 'Tu dirección de email',
        
        # Services descriptions
        'Tratamientos especializados para alivio del dolor muscular, contracturas y tensiones. Técnicas de masaje sueco, deportivo y relajante para restaurar tu bienestar físico y mental en Porto Alegre.':
        'Libera tu cuerpo del dolor y el estrés con técnicas avanzadas de masaje terapéutico. Tratamos contracturas profundas, mejoramos la circulación y restauramos tu movilidad para que vuelvas a disfrutar de tus actividades sin limitaciones.',
        
        'Rehabilitación profesional para lesiones deportivas, problemas posturales y dolor crónico. Evaluaciones personalizadas y planes de tratamiento adaptados a tus necesidades específicas en Porto Alegre.':
        'Recupera tu movimiento y vive sin dolor con fisioterapia especializada. Tratamos lesiones deportivas, corregimos problemas posturales y fortalecemos tu cuerpo para prevenir futuras molestias con planes 100% personalizados.',
        
        'Medicina tradicional china para equilibrar la energía corporal, reducir el dolor crónico y mejorar la salud general. Sesiones personalizadas con técnicas milenarias aplicadas con estándares modernos.':
        'Descubre el poder de la Acupuntura Terapéutica para el alivio natural del dolor crónico. Equilibra tu energía vital, reduce el estrés y mejora tu bienestar general con técnicas milenarias aplicadas con los más altos estándares profesionales.'
    }
    
    # Aplicar reemplazos
    changes_made = 0
    for old_text, new_text in replacements.items():
        if old_text in content:
            content = content.replace(old_text, new_text)
            changes_made += 1
            print(f"✅ Reemplazado: {old_text[:50]}...")
    
    # Mejorar alt texts
    alt_replacements = {
        'dialia logo': 'Eliou Masajes Terapéuticos - Fisioterapia y Acupuntura en Porto Alegre',
        'author image': 'cliente satisfecho de Eliou Masajes',
        'blog image': 'artículo sobre masajes terapéuticos',
        'blog thumbnail': 'vista previa del artículo'
    }
    
    for old_alt, new_alt in alt_replacements.items():
        if old_alt in content:
            content = content.replace(old_alt, new_alt)
            changes_made += 1
            print(f"✅ Alt mejorado: {old_alt} → {new_alt}")
    
    # Guardar archivo modificado
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"\n🎉 Proceso completado! Se realizaron {changes_made} mejoras al sitio.")
    print("📄 El archivo index.html ha sido actualizado con los textos optimizados por IA")
    
    return changes_made

if __name__ == "__main__":
    print("🚀 Aplicando textos optimizados por Google Gemini AI")
    print("=" * 60)
    apply_improved_texts()
    print("=" * 60)
    print("🔧 Recuerda hacer commit de los cambios a Git")