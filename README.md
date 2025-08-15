# Generador Interactivo de Curvas de Lissajous
<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>

Este proyecto es una aplicación interactiva desarrollada en **Python** utilizando la biblioteca **Pygame**. 

Permite visualizar y experimentar con curvas de Lissajous en tiempo real, ajustando sus parámetros principales desde una interfaz gráfica intuitiva.


## 📸 Captura de pantalla

<span><img src="https://github.com/VintaBytes/Lissajous/blob/main/imagen1.png?raw=true"  width="480px"/></span>

## Funcionalidades principales

- Representación dinámica de curvas de Lissajous.
- Control en tiempo real de los parámetros `a`, `b` y `delta`:
  - Por medio de botones (+ / -)
  - O mediante atajos de teclado (`Q/A`, `W/S`, `E/D`)
- Visualización clara con grilla de fondo.
- Animación suave del desfase `delta`, controlada por botones `Start` y `Stop`.
- Tooltips que explican cada botón al pasar el mouse por encima.

## Controles

| Acción                 | Tecla / Botón     |
|------------------------|------------------|
| Incrementar `a`        | `Q` o botón `+a` |
| Decrementar `a`        | `A` o botón `-a` |
| Incrementar `b`        | `W` o botón `+b` |
| Decrementar `b`        | `S` o botón `-b` |
| Incrementar `delta`    | `E` o botón `+δ` |
| Decrementar `delta`    | `D` o botón `-δ` |
| Iniciar animación      | Botón `Start`    |
| Detener animación      | Botón `Stop`     |
| Salir del programa     | `ESC`            |



$$ x(t) = A \cdot \sin(a t + \delta) $$
$$ y(t) = B \cdot \sin(b t) $$



Donde:
- `A` y `B` son las amplitudes,
- `a` y `b` son las frecuencias,
- `δ` (delta) es el desfase entre ambas señales.

Estas curvas se utilizan en física, electrónica (osciloscopios) y arte generativo, ya que visualmente resultan atractivas y revelan patrones de resonancia y armonía.

---

## Requisitos

- Python 3.8 o superior
- Biblioteca `pygame` instalada (`pip install pygame`)

---

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
