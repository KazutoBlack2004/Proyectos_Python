
#  pip install deep_translator  ||   pip install pyttsx3

from deep_translator import GoogleTranslator
import pyttsx3

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

def traducir_texto():
    print("\nBienvenido al Traductor Multilingüe")
    print("Idiomas soportados: español (es), inglés (en), francés (fr), alemán (de), italiano (it), etc.")
    
    try:
        # Solicitar idioma de origen y destino
        source_lang = input("Ingrese el idioma de origen (código, por ejemplo, 'es' para español): ").strip().lower()
        target_lang = input("Ingrese el idioma de destino (código, por ejemplo, 'en' para inglés): ").strip().lower()
        
        # Validar entrada
        if not source_lang or not target_lang:
            print("Los códigos de idioma no pueden estar vacíos. Intente nuevamente.")
            return traducir_texto()
        
        # Solicitar texto a traducir
        texto = input("Ingrese el texto que desea traducir: ").strip()
        if not texto:
            print("El texto no puede estar vacío. Intente nuevamente.")
            return traducir_texto()
        
        # Traducir el texto
        resultado = GoogleTranslator(source=source_lang, target=target_lang).translate(texto)
        print(f"\nTraducción ({source_lang} -> {target_lang}): {resultado}")
        
        # Convertir el texto traducido a voz
        engine.say(resultado)
        engine.runAndWait()  # Espera a que termine de hablar
    
    except Exception as e:
        print(f"\nOcurrió un error: {e}. Por favor, verifica los códigos de idioma y el texto ingresado.")
    
    # Opción para continuar o salir
    continuar = input("\n¿Desea traducir otro texto? (s/n): ").strip().lower()
    if continuar == 's':
        traducir_texto()
    else:
        print("¡Gracias por usar el Traductor Multilingüe! Hasta luego.")

# Ajustar la velocidad y el volumen antes de ejecutar
rate = engine.getProperty('rate')  # Obtiene la velocidad actual
engine.setProperty('rate', rate - 100)  # Disminuye la velocidad de lectura

volume = engine.getProperty('volume')  # Obtiene el volumen actual
engine.setProperty('volume', volume + 1.0)  # Aumenta el volumen un poco (max es 1.0)

# Ejecutar el traductor
traducir_texto()
