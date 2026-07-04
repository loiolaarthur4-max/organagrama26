import streamlit as st
import streamlit.components.v1 as components

st.title("Chaveamento Copa do Mundo 2026")

# Definindo o organograma em Mermaid
mermaid_code = """
graph LR
    A[Brasil] --> |Venceu| B(Quartas de Final)
    C[Japão] --> |Eliminado| B
    
    D[Alemanha] --> |Penaltis| E(Quartas de Final)
    F[Paraguai] --> |Venceu| E
    
    B --> G{Semifinal}
    E --> G
    
    subgraph Oitavas
    A
    C
    D
    F
    end
"""

# Renderizando o componente
components.html(
    f"""
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    <div class="mermaid">
        {mermaid_code}
    </div>
    """,
    height=500,
)

st.info("Dica: Você pode expandir o código acima para incluir todos os jogos das oitavas e quartas conforme a tabela que criamos.")
