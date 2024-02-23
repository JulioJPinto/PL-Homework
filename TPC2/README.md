# TPC1: 

### Data: 20/02/2024
### Autor: Júlio Pinto A100742

---

### Resumo

Neste exercício tinhamos como objetivo criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da [Cheat Sheet](https://www.markdownguide.org/cheat-sheet/).

De maneira a conseguir resolver este problema utilizei o módulo `re` para Regex em Python. Pode encontrar a solução no ficheiro `mdtohtml.py` onde utilizo a função `sub` para fazer algumas transformações.

Utilizando o ficheiro `test.md` obtive o seguinte resultado:

```html
> cat test.md | python3 mdtohtml.py

<h1>Heading 1</h1>

<h2>Heading 2</h2>

<h3>Heading 3</h3>

<h4>Heading 4</h4>

<h5>Heading 5</h5>

<h6>Heading 6</h6>

This is <b>bold</b> and <b>also bold</b>, and <i>italic</i> and <i>also italic</i>. This is <b><i>bold and italic</b></i> and so is this <b><i>bold and italic</b></i>

Unordered list:
<ul>
	<li>Item 1</li>
	<li>Item 2</li>
	<li>Item 3</li>
</ul>

Ordered list:
<ol>
	<li>First item</li>
	<li>Second item</li>
	<li>Third item</li>
</ol>

<a src="https://www.google.com">Link to Google</a>

<img src="https://via.placeholder.com/150" alt="Image"/>

```
