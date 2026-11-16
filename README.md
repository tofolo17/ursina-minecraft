# UrsinaMinecraft

> 🇧🇷 [Português](#o-que-você-encontrará-neste-repositório) · 🇺🇸 [English](#what-will-you-find-in-this-repository)

## O que você encontrará neste repositório?

Um clone simples do jogo Minecraft construído com a biblioteca Ursina, feito entre **maio e junho de 2021**. Neste
protótipo:
* Blocos podem ser adicionados e quebrados;
* O mapa é gerado proceduralmente a cada execução.

Para tal, li alguns capítulos do livro [The Nature of Code](https://natureofcode.com), de
[Daniel Shiffman](https://en.wikipedia.org/wiki/Daniel_Shiffman), e me aprofundei através de Jupyter Notebooks no
conceito de Perlin noise. Além disso, conheci o básico da Ursina através de sua própria
[documentação](https://www.ursinaengine.org/documentation.html).

### Estrutura

- **`Voxel/`** — o bloco: um `Button` da Ursina que cria um vizinho no clique esquerdo e se destrói no direito;
- **`model.py`** — primeiro teste: um chão plano de 8×8 blocos;
- **`Minecraft/`** — o protótipo final: altura de cada coluna vinda de um mapa de Perlin noise 2D (`Map/`);
- **`PyConda/`** — experimento alternativo com OpenSimplex, misturando ruídos de "montanhas" e "planícies";
- **`CodingTrain/`** — estudos de ruído: aleatório × Perlin em Pygame, Perlin 2D em p5.js e o notebook `graphs.ipynb`,
  que explica oitavas e interpolação com gráficos.

### Ferramentas

Python 3, Ursina, perlin-noise, OpenSimplex, Matplotlib, Pygame, Jupyter e p5.js.

### Como usar

```bash
git clone https://github.com/tofolo17/ursina-minecraft.git
cd ursina-minecraft
pip install -r requirements.txt
PYTHONPATH=. python Minecraft/main.py
```

Primeiro abre uma janela com o mapa de ruído gerado; feche-a para entrar no jogo. Os outros exemplos rodam do mesmo
jeito (`PYTHONPATH=. python model.py`, `PYTHONPATH=. python PyConda/main.py`).

| Ação             | Controle                |
|------------------|-------------------------|
| Andar / pular    | `W` `A` `S` `D` / espaço |
| Olhar            | mouse                   |
| Colocar bloco    | clique esquerdo         |
| Quebrar bloco    | clique direito          |

### Licença

[MIT](LICENSE)

---

## What will you find in this repository?

A simple Minecraft clone built with Ursina engine, made between **May and June 2021**. In this prototype:
* Blocks can be added and broken;
* The map is procedurally generated.

To do this, I had to read some chapters of the book [The Nature of Code](https://natureofcode.com), by
[Daniel Shiffman](https://en.wikipedia.org/wiki/Daniel_Shiffman), and go deeper through Perlin noise using Jupyter
Notebooks. In addition, I learned the basics of Ursina through its own
[documentation](https://www.ursinaengine.org/documentation.html).

### Structure

- **`Voxel/`** — the block: an Ursina `Button` that spawns a neighbor on left click and destroys itself on right click;
- **`model.py`** — first test: a flat 8×8 floor;
- **`Minecraft/`** — the final prototype: each column's height comes from a 2D Perlin noise map (`Map/`);
- **`PyConda/`** — an alternative experiment with OpenSimplex, blending "mountains" and "plains" noise;
- **`CodingTrain/`** — noise studies: random vs. Perlin in Pygame, 2D Perlin in p5.js and the `graphs.ipynb` notebook,
  which explains octaves and interpolation with plots.

### Tools

Python 3, Ursina, perlin-noise, OpenSimplex, Matplotlib, Pygame, Jupyter and p5.js.

### How to use

```bash
git clone https://github.com/tofolo17/ursina-minecraft.git
cd ursina-minecraft
pip install -r requirements.txt
PYTHONPATH=. python Minecraft/main.py
```

A window with the generated noise map opens first; close it to enter the game. The other examples run the same way
(`PYTHONPATH=. python model.py`, `PYTHONPATH=. python PyConda/main.py`).

| Action          | Control                 |
|-----------------|-------------------------|
| Walk / jump     | `W` `A` `S` `D` / space |
| Look around     | mouse                   |
| Place a block   | left click              |
| Break a block   | right click             |

### License

[MIT](LICENSE)
