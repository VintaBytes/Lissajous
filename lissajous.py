import pygame
import math
import sys

# ------------------------------
# Constantes de color
# ------------------------------
COLOR_FONDO = (20, 20, 20)
COLOR_LINEA = (0, 255, 0)
COLOR_EJES = (80, 80, 80)
COLOR_TEXTO = (200, 200, 200)
COLOR_BOTON = (40, 40, 40)
COLOR_BORDE = (255, 255, 0) 
COLOR_TOOLTIP = (60, 60, 60)
FPS = 60
PASO_DELTA = math.pi / 32
animando = False  # Flag de animación

# ------------------------------
# Dimensiones
# ------------------------------
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

# ------------------------------
# Clase botón con tooltip
# ------------------------------
class Boton:
    def __init__(self, x, y, ancho, alto, texto, accion, tooltip=""):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.accion = accion
        self.tooltip = tooltip

    def dibujar(self, pantalla, fuente):
        pygame.draw.rect(pantalla, COLOR_BOTON, self.rect)
        pygame.draw.rect(pantalla, COLOR_BORDE, self.rect, 2)
        txt = fuente.render(self.texto, True, COLOR_TEXTO)
        pantalla.blit(txt, (self.rect.x + 5, self.rect.y + 5))

    def clickeado(self, pos):
        return self.rect.collidepoint(pos)

    def esta_hover(self, pos):
        return self.rect.collidepoint(pos)

# ------------------------------
# Funciones auxiliares
# ------------------------------
def dibujar_grilla(pantalla):
    espaciado = 50
    for x in range(0, ANCHO_VENTANA, espaciado):
        pygame.draw.line(pantalla, COLOR_EJES, (x, 0), (x, ALTO_VENTANA), 1)
    for y in range(0, ALTO_VENTANA, espaciado):
        pygame.draw.line(pantalla, COLOR_EJES, (0, y), (ANCHO_VENTANA, y), 1)

def generar_puntos(A, B, a, b, delta, centro_x, centro_y):
    puntos = []
    for t in range(0, 10000):
        t_real = t * 0.001
        x = A * math.sin(a * t_real + delta)
        y = B * math.sin(b * t_real)
        puntos.append((centro_x + int(x), centro_y + int(y)))
    return puntos

def mostrar_valores(pantalla, fuente, a, b, delta):
    texto = f"       {a:.2f}                    {b:.2f}              {delta:.2f} rad"
    superficie = fuente.render(texto, True, COLOR_TEXTO)
    pantalla.blit(superficie, (10, 10))

def mostrar_tooltip(pantalla, fuente, texto, pos):
    superficie = fuente.render(texto, True, COLOR_TEXTO)
    fondo = pygame.Surface((superficie.get_width() + 10, superficie.get_height() + 6))
    fondo.fill(COLOR_TOOLTIP)
    pantalla.blit(fondo, (pos[0] + 10, pos[1] + 10))
    pantalla.blit(superficie, (pos[0] + 15, pos[1] + 12))

# ------------------------------
# Inicialización
# ------------------------------
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Curvas de Lissajous Interactivas")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("consolas", 20)

# Valores iniciales
A = 250
B = 250
a = 3
b = 2
delta = math.pi / 2
centro_x = ANCHO_VENTANA // 2
centro_y = ALTO_VENTANA // 2

# ------------------------------
# Definición de botones
# ------------------------------
botones = []
base_y = 5
ancho_boton = 40
alto_boton = 30
espaciado = 40

def crear_botones():
    global botones
    botones = [
        Boton(600, 565, 80, 30, "Start", lambda: iniciar_animacion(), ""),
        Boton(700, 565, 80, 30, " Stop", lambda: detener_animacion(), ""),
        Boton(180, base_y, ancho_boton, alto_boton, "+a", lambda: incrementar('a'), "Incrementar a"),
        Boton(  0 + espaciado, base_y, ancho_boton, alto_boton, "-a", lambda: decrementar('a'), "Decrementar a"),
        Boton(460, base_y, ancho_boton, alto_boton, "+b", lambda: incrementar('b'), "Incrementar b"),
        Boton(280 + espaciado, base_y, ancho_boton, alto_boton, "-b", lambda: decrementar('b'), "Decrementar b"),
        Boton(720, base_y, ancho_boton, alto_boton, "+δ", lambda: incrementar('delta'), "Delta+"),
        Boton(505 + espaciado, base_y, ancho_boton, alto_boton, "-δ", lambda: decrementar('delta'), "Delta-"),
    ]

def incrementar(param):
    global a, b, delta
    if param == 'a' and a < 100:
        a += 1
    elif param == 'b' and b < 100:
        b += 1
    elif param == 'delta' and delta < 100:
        delta += PASO_DELTA

def decrementar(param):
    global a, b, delta
    if param == 'a' and a > 1:
        a -= 1
    elif param == 'b' and b > 1:
        b -= 1
    elif param == 'delta':
        delta -= PASO_DELTA

def iniciar_animacion():
    global animando
    animando = True

def detener_animacion():
    global animando
    animando = False

crear_botones()

# ------------------------------
# Bucle principal
# ------------------------------
corriendo = True
while corriendo:
    mouse_pos = pygame.mouse.get_pos()
    tooltip_texto = None

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
            elif evento.key == pygame.K_q:
                incrementar('a')
            elif evento.key == pygame.K_a:
                decrementar('a')
            elif evento.key == pygame.K_w:
                incrementar('b')
            elif evento.key == pygame.K_s:
                decrementar('b')
            elif evento.key == pygame.K_e:
                incrementar('delta')
            elif evento.key == pygame.K_d:
                decrementar('delta')
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                for boton in botones:
                    if boton.clickeado(evento.pos):
                        boton.accion()

    # Ver si el mouse está sobre algún botón
    for boton in botones:
        if boton.esta_hover(mouse_pos):
            tooltip_texto = boton.tooltip

    # Redibujar
    pantalla.fill(COLOR_FONDO)
    dibujar_grilla(pantalla)
    
    if animando:
        delta += PASO_DELTA / 4  # más suave
        if delta>99:
            delta = 0

    puntos = generar_puntos(A, B, a, b, delta, centro_x, centro_y)
    
    if len(puntos) > 1:
        pygame.draw.lines(pantalla, COLOR_LINEA, False, puntos, 2)
    mostrar_valores(pantalla, fuente, a, b, delta)

    # Dibujar botones
    for boton in botones:
        boton.dibujar(pantalla, fuente)

    # Mostrar tooltip si corresponde
    if tooltip_texto:
        mostrar_tooltip(pantalla, fuente, tooltip_texto, mouse_pos)

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()
