import os

BASE = r"H:\Diego obsidian\agencialocalweb\clients\ju-doceria-trindade\site-v2\src\pages"
WA = "https://wa.me/5562996358321?text=Oi%20Ju!%20Quero%20encomendar%20doces"

def slugify(s):
    return s.lower().replace(" ","-").replace("ã","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ç","c")

def write_page(path_dir, content):
    os.makedirs(path_dir, exist_ok=True)
    with open(os.path.join(path_dir, "index.astro"), "w", encoding="utf-8") as f:
        f.write(content)

# Template for inner pages (dark, minimal, GSAP-ready)
def inner_page(title, desc, h1, body_html, wa_text="doces"):
    wa_link = WA.replace("doces", wa_text.replace(" ","%20"))
    return f"""---
import MainLayout from '../../layouts/MainLayout.astro';
const WA_LINK = "{wa_link}";
---
<MainLayout title="{title} | Ju dOCERIA" description="{desc}">
  <section class="section" style="padding-top:8rem">
    <div class="container" style="max-width:800px">
      <span class="eyebrow reveal-up">Ju dOCERIA</span>
      <h1 class="reveal-up" style="margin-bottom:1.5rem">{h1}</h1>
      {body_html}
      <a href={{WA_LINK}} target="_blank" rel="noopener" class="btn btn-whatsapp reveal-up" style="margin-top:2.5rem;display:inline-flex">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.881 11.881 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        Encomendar pelo WhatsApp
      </a>
    </div>
  </section>
</MainLayout>
"""

count = 1  # homepage already done

# Service pages
services = [
    ("doces-caseiros", "Doces Caseiros em Trindade GO", "Doces artesanais em Trindade GO. Brigadeiros, beijinhos. WhatsApp.", "Doces Caseiros Artesanais", "Nossos doces sao feitos com receitas de familia e ingredientes selecionados. Brigadeiros, beijinhos, doces de fruta e mais.", ["Brigadeiro tradicional", "Brigadeiro gourmet", "Beijinho de coco", "Doce de leite", "Cajuzinho", "Trufas"]),
    ("bolos-artesanais", "Bolos Artesanais em Trindade GO", "Bolos caseiros em Trindade GO. WhatsApp.", "Bolos Artesanais", "Bolos fofinhos com sabor de vovo, receitas de geracao.", ["Chocolate", "Laranja", "Cenoura", "Coco", "Naked cake", "Formatura"]),
    ("doces-para-festas", "Doces para Festas em Trindade GO", "Doces para festas. Tabela de quantidades. WhatsApp.", "Doces para Festas", "Tabela de quantidades por evento. Aniversarios, casamentos, churrascos.", ["Aniversario", "Casamento", "Churrasco", "Baby shower", "Corporativo", "Quantidades"]),
    ("tortas-doces", "Tortas Doces em Trindade GO", "Tortas doces artesanais. WhatsApp.", "Tortas Doces", "Massa crocante, recheio generoso, receita da mamae.", ["Limao", "Chocolate", "Doce de leite", "Morango", "Holandesa", "Maca"]),
    ("brigadeiro-gourmet", "Brigadeiro Gourmet em Trindade GO", "Brigadeiro gourmet artesanal. WhatsApp.", "Brigadeiro Gourmet", "Chocolate nobre, receita da mamae, sabores variados.", ["Tradicional", "Ninho", "Pistache", "Cafe", "Maracuja", "Nutella"]),
    ("cestas-cafe-manha", "Cestas de Cafe da Manha em Trindade GO", "Cestas de cafe da manha. WhatsApp.", "Cestas de Cafe da Manha", "Presente perfeito para surpreender quem voce ama.", ["Classica", "Premium", "Aniversario", "Romantica", "Corporativa", "Surpresa"]),
    ("encomendas-de-doces", "Encomendas de Doces em Trindade GO", "Encomende doces. WhatsApp.", "Encomendas de Doces", "Facil, rapido, personalizado. Fale com a Ju.", ["WhatsApp direto", "3 dias para festas", "Trindade e regiao", "Pagamento na entrega", "Cardapio flexivel", "Prova antes"]),
]

for slug, title, desc, h1, intro, items in services:
    items_html = '<div class="grid-2 stagger-group" style="margin-top:2rem">' + "".join([f'<div class="card reveal-up" style="transform:rotate({(-1)**i * (0.3+i*0.2):.1f}deg)"><h3 style="color:var(--color-primary)">{it}</h3><p style="color:var(--color-text-muted);font-size:0.9rem">Feito com ingredientes selecionados</p></div>' for i, it in enumerate(items)]) + '</div>'
    body = f'<p class="reveal-up" style="color:var(--color-text-muted);font-size:1.1rem;line-height:1.7;margin-bottom:1rem">{intro}</p>{items_html}'
    write_page(f"{BASE}/servicos/{slug}", inner_page(title, desc, h1, body, slug.replace("-"," ")))
    count += 1

# City pages
cities = [("goiania","Goiania","GO"),("anapolis","Anapolis","GO"),("itumbiara","Itumbiara","GO")]
for slug, name, state in cities:
    body = f'<p class="reveal-up" style="color:var(--color-text-muted);font-size:1.1rem;line-height:1.7">A Ju dOCERIA entrega doces artesanais em {name}, {state}. Receitas de familia, ingredientes selecionados.</p><div class="grid-3 stagger-group" style="margin-top:2rem"><a href="/servicos/doces-caseiros/" class="card reveal-up" style="text-align:center"><h3>&#127856; Doces</h3></a><a href="/servicos/bolos-artesanais/" class="card reveal-up" style="text-align:center"><h3>&#127874; Bolos</h3></a><a href="/servicos/doces-para-festas/" class="card reveal-up" style="text-align:center"><h3>&#127880; Festas</h3></a></div>'
    write_page(f"{BASE}/cidades/{slug}", inner_page(f"Doces Caseiros em {name} {state}", f"Doces em {name}. WhatsApp.", f"Doces em {name}", body, f"doces em {name}"))
    count += 1

# Bairro pages
bairros = ["Centro","Vila Sao Jose","Setor Central","Jardim Americano","Residencial Alvorada","Setor Leste","Vila Boa Esperanca","Jardim Goias","Residencial Embaixador","Setor Sul","Vila Santa Cruz","Jardim Tropical","Setor Norte","Residencial Florenca","Vila Maria"]
for bairro in bairros:
    bslug = slugify(bairro)
    body = f'<p class="reveal-up" style="color:var(--color-text-muted);font-size:1.1rem;line-height:1.7">Doces artesanais no {bairro}, Trindade-GO. Receita da mamae, sabor de casa.</p><div class="grid-3 stagger-group" style="margin-top:2rem"><a href="/servicos/doces-caseiros/" class="card reveal-up" style="text-align:center"><h3>&#127856; Doces</h3></a><a href="/servicos/bolos-artesanais/" class="card reveal-up" style="text-align:center"><h3>&#127874; Bolos</h3></a><a href="/servicos/doces-para-festas/" class="card reveal-up" style="text-align:center"><h3>&#127880; Festas</h3></a></div>'
    write_page(f"{BASE}/trindade/{bslug}", inner_page(f"Doces no {bairro} - Trindade GO", f"Doces no {bairro}. WhatsApp.", f"Doces no {bairro}", body, f"doces no {bairro}"))
    count += 1

# Static pages
write_page(f"{BASE}/sobre", inner_page("Sobre a Ju dOCERIA", "Historia da Ju. Trindade GO.", "Nossa Historia", '<p class="quote-text reveal-up" style="margin-bottom:1.5rem">A Ju dOCERIA nasceu do amor pelos doces caseiros. Com as receitas da mamae, cada doce carrega tradicao de geracoes.</p><p class="reveal-up" style="color:var(--color-text-muted);line-height:1.8">Ju Cristina Resende comecou fazendo doces para a familia. Hoje atende Trindade, Goiania e toda a regiao com doces feitos no dia, com ingredientes selecionados.</p><p class="reveal-up" style="color:var(--color-text-muted);line-height:1.8;margin-top:1rem">Alem dos doces, a Ju oferece aulas de culinaria em Trindade GO. Aprenda a fazer brigadeiros, bolos e doces para festas.</p>'))

write_page(f"{BASE}/contato", inner_page("Contato - Ju dOCERIA", "WhatsApp (62) 99635-8321.", "Contato", '<p class="reveal-up" style="color:var(--color-text-muted);font-size:1.1rem;margin-bottom:2rem">Encomende pelo WhatsApp. Seg-Sab, 8h as 18h.</p><div class="grid-3 stagger-group"><a href="https://wa.me/5562996358321" target="_blank" class="card glow-border reveal-up" style="text-align:center"><span style="font-size:2rem">&#128241;</span><h3>WhatsApp</h3><p style="color:var(--color-text-muted)">(62) 99635-8321</p></a><a href="mailto:tomazcristina05@gmail.com" class="card glow-border reveal-up" style="text-align:center"><span style="font-size:2rem">&#128231;</span><h3>Email</h3><p style="color:var(--color-text-muted)">tomazcristina05@gmail.com</p></a><div class="card glow-border reveal-up" style="text-align:center"><span style="font-size:2rem">&#128205;</span><h3>Localizacao</h3><p style="color:var(--color-text-muted)">Trindade, GO</p></div></div>'))

write_page(f"{BASE}/faq", inner_page("Perguntas Frequentes", "FAQ sobre doces e encomendas.", "Perguntas Frequentes", '<div class="faq-list"><details class="faq-item reveal-up"><summary>Como encomendar?</summary><p>WhatsApp direto com a Ju. Seg-Sab 8h-18h.</p></details><details class="faq-item reveal-up"><summary>Prazo para encomendas?</summary><p>Festas: 3 dias. Pedidos menores: mesmo dia.</p></details><details class="faq-item reveal-up"><summary>Entregam em Goiania?</summary><p>Sim! Trindade, Goiania, Anapolis e Itumbiara.</p></details><details class="faq-item reveal-up"><summary>Doces feitos no dia?</summary><p>Sim, todos no dia da entrega.</p></details><details class="faq-item reveal-up"><summary>Aulas de culinaria?</summary><p>Presenciais em Trindade. Turmas pequenas.</p></details><details class="faq-item reveal-up"><summary>Pagamento?</summary><p>Dinheiro, PIX ou cartao na entrega.</p></details></div>'))

# Aulas
write_page(f"{BASE}/aulas", inner_page("Aulas de Culinaria em Trindade GO", "Aulas de culinaria. WhatsApp.", "Aulas com a Ju", '<p class="reveal-up" style="color:var(--color-text-muted);font-size:1.1rem;line-height:1.7;margin-bottom:2rem">Aprenda a fazer doces caseiros com receitas de familia. Aulas presenciais em Trindade GO.</p><div class="grid-2 stagger-group"><div class="card reveal-up"><h3 style="color:var(--color-primary)">&#127852; Brigadeiro Gourmet</h3><p style="color:var(--color-text-muted)">Tecnicas, sabores e decoracao.</p></div><div class="card reveal-up"><h3 style="color:var(--color-primary)">&#127874; Bolos Artesanais</h3><p style="color:var(--color-text-muted)">Massa, recheio e cobertura.</p></div><div class="card reveal-up"><h3 style="color:var(--color-primary)">&#127880; Doces para Festas</h3><p style="color:var(--color-text-muted)">Montagem e apresentacao.</p></div><div class="card reveal-up"><h3 style="color:var(--color-primary)">&#129472; Tortas Doces</h3><p style="color:var(--color-text-muted)">Massa crocante e recheios.</p></div></div>'))

# Index pages
write_page(f"{BASE}/trindade", f"""---
import MainLayout from '../layouts/MainLayout.astro';
---
<MainLayout title="Doces em Trindade GO | Ju dOCERIA" description="Doces em todos os bairros de Trindade.">
  <section class="section" style="padding-top:8rem"><div class="container">
    <span class="eyebrow reveal-up">Cobertura</span>
    <h1 class="reveal-up" style="margin-bottom:2rem">Doces em Trindade</h1>
    <div class="grid-4 stagger-group">
      {"".join([f'<a href="/trindade/{slugify(b)}/" class="card glow-border reveal-up" style="text-align:center"><span style="font-size:1.2rem">&#128205;</span><h3>{b}</h3></a>' for b in bairros])}
    </div>
  </div></section>
</MainLayout>""")

write_page(f"{BASE}/servicos", f"""---
import MainLayout from '../layouts/MainLayout.astro';
---
<MainLayout title="Cardapio | Ju dOCERIA" description="Cardapio completo.">
  <section class="section" style="padding-top:8rem"><div class="container">
    <span class="eyebrow reveal-up">Cardapio</span>
    <h1 class="reveal-up" style="margin-bottom:2rem">Nosso Cardapio</h1>
    <div class="grid-3 grid-stagger stagger-group">
      {"".join([f'<a href="/servicos/{s[0]}/" class="card service-card reveal-up" style="text-align:center"><span style="font-size:2.5rem">{s[4].split()[0]}</span><h3>{s[3]}</h3></a>' for s in services])}
    </div>
  </div></section>
</MainLayout>""")

write_page(f"{BASE}/cidades", """---
import MainLayout from '../layouts/MainLayout.astro';
---
<MainLayout title="Cidades Atendidas | Ju dOCERIA" description="Doces em Trindade, Goiania, Anapolis, Itumbiara.">
  <section class="section" style="padding-top:8rem"><div class="container">
    <span class="eyebrow reveal-up">Cidades</span>
    <h1 class="reveal-up" style="margin-bottom:2rem">Cidades Atendidas</h1>
    <div class="grid-2 stagger-group">
      <a href="/trindade/" class="card glow-border reveal-up" style="text-align:center"><h3>Trindade</h3></a>
      <a href="/cidades/goiania/" class="card glow-border reveal-up" style="text-align:center"><h3>Goiania</h3></a>
      <a href="/cidades/anapolis/" class="card glow-border reveal-up" style="text-align:center"><h3>Anapolis</h3></a>
      <a href="/cidades/itumbiara/" class="card glow-border reveal-up" style="text-align:center"><h3>Itumbiara</h3></a>
    </div>
  </div></section>
</MainLayout>""")

print(f"TOTAL PAGES: {count}")
