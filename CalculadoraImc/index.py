import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Calculadora IMC', width=450, height=800)

# 1. Carregar a imagem na memória com o load_image
img_path = "IniciandoPython/IMC.png"
loaded_image = dpg.load_image(img_path)

if loaded_image is None: # Fallback caso o script seja rodado de dentro da própria pasta
    img_path = "IMC.png"
    loaded_image = dpg.load_image(img_path)

width, height, channels, data = loaded_image

# 2. Registrar a "textura" da imagem no DearPyGui
with dpg.texture_registry():
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="minha_imagem")

def calcular_imc():
    nome = dpg.get_value("nome")
    idade = dpg.get_value("idade")
    altura = dpg.get_value("altura")
    peso = dpg.get_value("peso")
    
    if not altura or altura <= 0:
        dpg.set_value("imc", "Altura inválida!")
        dpg.configure_item("imc", color=[255, 100, 100])
        return
        
    try:
        imc = peso / float(altura * altura)
        dpg.set_value("imc", f"IMC de {nome}: {imc:.2f}")
        dpg.configure_item("imc", color=[100, 255, 100])
    except Exception:
        dpg.set_value("imc", "Valores inválidos!")
        dpg.configure_item("imc", color=[255, 100, 100])

# Criando um tema global para aparência de APP
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        # Arredondar bordas dos inputs e botões
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
        # Background escuro agradável (Dark Mode)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (25, 25, 30, 255), category=dpg.mvThemeCat_Core)
        # Cores do botão
        dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 150, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (50, 180, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 100, 200, 255), category=dpg.mvThemeCat_Core)
        # Remove a borda padrão
        dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

# Estrutura do App na Janela Principal
with dpg.window(tag="main_window"):
    dpg.add_spacer(height=20)
    
    # Título centralizado
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=135)
        dpg.add_text("Calculadora de IMC", color=[0, 255, 255])
        
    dpg.add_spacer(height=30)
    
    # Campos de Entrada com larguras relativas
    dpg.add_text(" Nome:")
    dpg.add_input_text(tag="nome", width=-1)
    dpg.add_spacer(height=10)
    
    dpg.add_text(" Idade:")
    dpg.add_input_int(tag="idade", width=-1, step=0)
    dpg.add_spacer(height=10)
    
    dpg.add_text(" Altura (ex: 1.75):")
    dpg.add_input_float(tag="altura", width=-1, step=0.0)
    dpg.add_spacer(height=10)
    
    dpg.add_text(" Peso (kg):")
    dpg.add_input_float(tag="peso", width=-1, step=0.0)
    dpg.add_spacer(height=40)
    
    # Botão de cálculo
    dpg.add_button(label="CALCULAR IMC", callback=calcular_imc, height=50, width=-1)
    
    dpg.add_spacer(height=30)
    # Exibição do resultado (tentar centralizar via espaços)
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=140)
        dpg.add_text("Aguardando...", tag="imc", color=[200, 200, 200])
    
    dpg.add_spacer(height=30)
    
    # Imagem preenchendo de ponta a ponta e mantendo a proporção original
    img_width = 450
    img_height = int(height * (img_width / width)) if width > 0 else height
    dpg.add_image("minha_imagem", width=img_width, height=img_height)

dpg.setup_dearpygui()
dpg.show_viewport()
# Define a janela como primária - Isto remove as margens dela e preenche todo o Viewport!
dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()
dpg.destroy_context()
