"""
Gerador de Estrutura de Pastas para Levantamentos Fotográficos
Aplicação desktop com interface gráfica moderna (CustomTkinter)

Princípios:
- Nada é criado automaticamente
- Tudo é selecionável
- A ordem de criação define a numeração
- O nome é livre
- A visualização é a verdade

───────────────────────────────────────────────────────────
Desenvolvido por: Thiago Nascimento Barbosa
Empresa: TM - Sempre Tecnologia
Data: Fevereiro 2026
───────────────────────────────────────────────────────────
"""

import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
import json

# ============================
# CONFIGURAÇÃO DO TEMA
# ============================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
import shutil # Import shutil for folder deletion

# ============================
# DADOS PRÉ-DEFINIDOS (ATUALIZADOS)
# ============================
AREAS_SUGERIDAS = [
    "Área externa",
    "Área interna",
    "Segundo piso",
    "Primeiro piso",
    "Cobertura"
]

AMBIENTES_SUGERIDOS = [
    "SAA (sala de autoatendimento)",
    "Atendimento",
    "Corredor de acesso",
    "Banheiro feminino",
    "Banheiro masculino",
    "Banheiro PNE",
    "Copa",
    "Cozinha",
    "Suporte",
    "CAIEX",
    "Tesouraria",
    "Sala de reunião",
    "Sala do gerente",
    "Depósito",
    "Arquivo",
    "Corredor de abastecimento",
    "Escadas",
    "Área restrita"
]

SERVICOS_SUGERIDOS = [
    "Pintura acrílica",
    "Pintura automotiva",
    "Pintura esmalte em porta",
    "Pintura esmalte metal",
    "Piso tátil inox",
    "Piso tátil",
    "Substituição de lâmpadas",
    "Substituição de ducha higiênica",
    "Substituição de torneira",
    "Substituição de fechadura",
    "Substituição de puxador",
    "Substituição de película e policarbonato",
    "Telhado",
    "Impermeabilização de calha",
    "SPDA",
    "Forro de fibra mineral",
    "Forro de gesso",
    "Manutenção em ponto elétrico",
    "Manutenção em ponto lógico",
    "Ar condicionado",
    "Pictograma",
    "Letreiro",
    "Limpeza de fachada"
]

SUBPASTAS_SUGERIDAS = [
    "Vista ampla",
    "Detalhes",
    "Antes",
    "Depois",
    "Descrição"
]


class GeradorEstruturaPastas(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuração da janela
        self.title("🏗️ Gerador de Estrutura de Pastas - TM")
        self.geometry("1300x850")
        self.minsize(1100, 700)
        
        # Estado da aplicação (Hierarquia: Area -> Itens (Ambiente ou Servico))
        self.pasta_destino = ctk.StringVar(value="")
        self.nome_levantamento = ctk.StringVar(value="")
        
        self.areas_selecionadas = []      # Lista ordenada de Áreas
        self.itens_por_area = {}         # {area: [lista de itens (ambientes ou servicos)]}
        self.servicos_por_ambiente = {}  # {(area, ambiente): [servicos]}
        self.itens_por_area = {}         # {area: [lista de itens (ambientes ou servicos)]}
        self.servicos_por_ambiente = {}  # {(area, ambiente): [servicos]}
        self.subpastas_por_item = {}      # {(area, amb/srv, srv_sub?): [subpastas]}
        self.detalhes_por_subitem = {}    # {(area, item, subitem): [detalhes]}
        self.vista_ampla_geral = {}      # {identificador: bool}
        
        # Rastreamento de itens personalizados
        self.custom_servicos = set()     # Nomes de serviços personalizados (para saber numerar 1.1)
        
        # Flag para evitar que atualizações de UI disparem eventos de toggle
        self.updating_ui = False
        
        # Seleções atuais para o fluxo de UI
        self.area_atual = None
        self.area_atual = None
        self.item_atual = None  # Pode ser Ambiente ou Serviço direto na Área
        self.subitem_atual = None # Serviço dentro de Ambiente (Nível 3)
        self.servico_atual = None
        
        # Construir interface
        self._criar_interface()
        
    def _criar_interface(self):
        """Monta toda a interface gráfica"""
        
        # ===== HEADER =====
        self.header = ctk.CTkFrame(self, height=80, fg_color="transparent")
        self.header.pack(fill="x", padx=20, pady=(20, 10))
        
        titulo = ctk.CTkLabel(
            self.header, 
            text="🏗️ Gerador de Estrutura de Pastas",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        titulo.pack(side="left")
        
        assinatura = ctk.CTkLabel(
            self.header,
            text="TM - Sempre Tecnologia",
            font=ctk.CTkFont(size=11),
            text_color="#666"
        )
        assinatura.pack(side="right", padx=10)
        
        # ===== BARRA DE CONFIGURAÇÃO =====
        self.config_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.config_bar.pack(fill="x", padx=20, pady=(0, 10))
        
        frame_nome = ctk.CTkFrame(self.config_bar, fg_color="transparent")
        frame_nome.pack(side="left")
        
        ctk.CTkLabel(frame_nome, text="📋 Levantamento:", font=ctk.CTkFont(size=13, weight="bold")).pack(side="left", padx=(0, 10))
        
        self.entry_nome_levantamento = ctk.CTkEntry(
            frame_nome,
            textvariable=self.nome_levantamento,
            width=350,
            placeholder_text="Ex: 01 - Arcos - Enviado"
        )
        self.entry_nome_levantamento.pack(side="left")
        self.entry_nome_levantamento.bind("<KeyRelease>", lambda e: self._atualizar_preview())
        
        frame_destino = ctk.CTkFrame(self.config_bar, fg_color="transparent")
        frame_destino.pack(side="right")
        
        self.entry_destino = ctk.CTkEntry(
            frame_destino, 
            textvariable=self.pasta_destino,
            width=300,
            placeholder_text="Pasta destino..."
        )
        self.entry_destino.pack(side="left", padx=(0, 10))
        
        ctk.CTkButton(
            frame_destino, 
            text="📁 Selecionar",
            width=100,
            command=self._selecionar_pasta
        ).pack(side="left")
        
        # ===== ÁREA PRINCIPAL =====
        self.main_area = ctk.CTkFrame(self, fg_color="transparent")
        self.main_area.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Painel esquerdo (seleções)
        self.painel_esquerdo = ctk.CTkScrollableFrame(self.main_area, width=550)
        self.painel_esquerdo.pack(side="left", fill="both", padx=(0, 10))
        
        # Painel direito (preview)
        self.painel_direito = ctk.CTkFrame(self.main_area)
        self.painel_direito.pack(side="right", fill="both", expand=True)
        
        # ===== COLUNAS DE SELEÇÃO =====
        self._criar_painel_areas()
        self._criar_painel_ambientes_servicos()
        self._criar_painel_subpastas()
        self._criar_painel_detalhes_nivel4()
        
        # ===== PREVIEW =====
        self._criar_painel_preview()
        
        # ===== FOOTER =====
        self.footer = ctk.CTkFrame(self, height=60, fg_color="transparent")
        self.footer.pack(fill="x", padx=20, pady=(10, 20))
        
        self.btn_gerar = ctk.CTkButton(
            self.footer,
            text="🔨 GERAR ESTRUTURA DE PASTAS",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=50,
            fg_color="#00875a",
            hover_color="#006644",
            command=self._gerar_estrutura
        )
        self.btn_gerar.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        self.btn_limpar = ctk.CTkButton(
            self.footer,
            text="🧹 LIMPAR SELEÇÃO",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=50,
            fg_color="#991b1b",
            hover_color="#7f1d1d",
            command=self._limpar_selecao
        )
        self.btn_limpar.pack(side="right", fill="x", expand=True)
        
    def _criar_painel_areas(self):
        """Cria o painel de seleção de Áreas (Nível 1)"""
        frame = ctk.CTkFrame(self.painel_esquerdo)
        frame.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkLabel(frame, text="🌎 1. SELECIONE A ÁREA", font=ctk.CTkFont(size=14, weight="bold")).pack(padx=10, pady=(10, 5), anchor="w")
        
        self.frame_areas_list = ctk.CTkFrame(frame, fg_color="transparent", height=100)
        self.frame_areas_list.pack(fill="x", padx=10, pady=5)
        
        self.checkboxes_areas = {}
        # Usar um grid para economizar espaço
        for i, area in enumerate(AREAS_SUGERIDAS):
            cb = ctk.CTkCheckBox(
                self.frame_areas_list,
                text=area,
                command=lambda a=area: self._toggle_area(a)
            )
            cb.grid(row=i//2, column=i%2, sticky="w", padx=5, pady=2)
            self.checkboxes_areas[area] = cb

    def _criar_painel_ambientes_servicos(self):
        """Cria o painel de Ambientes ou Serviços dentro da Área (Nível 2)"""
        self.frame_itens_container = ctk.CTkFrame(self.painel_esquerdo)
        self.frame_itens_container.pack(fill="x", padx=5, pady=5)
        
        header = ctk.CTkFrame(self.frame_itens_container, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=(10, 5))
        
        ctk.CTkLabel(header, text="📍 2. AMBIENTES / SERVIÇOS", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        
        self.label_area_temp = ctk.CTkLabel(header, text="", font=ctk.CTkFont(size=11), text_color="#00d4ff")
        self.label_area_temp.pack(side="right")

        # Vista ampla da ÁREA
        self.cb_va_area = ctk.CTkCheckBox(
            self.frame_itens_container,
            text="📷 Incluir 'Vista ampla' nesta ÁREA",
            command=self._toggle_va_area,
            fg_color="#00875a"
        )
        self.cb_va_area.pack(anchor="w", padx=15, pady=5)

        # Tabs para organizar Ambientes vs Serviços Sugeridos
        self.tab_itens = ctk.CTkTabview(self.frame_itens_container, height=250)
        self.tab_itens.pack(fill="x", padx=10, pady=5)
        
        self.tab_itens.add("Ambientes")
        self.tab_itens.add("Serviços")
        
        # Área de adição personalizada Nível 2
        frame_custom = ctk.CTkFrame(self.frame_itens_container, fg_color="transparent")
        frame_custom.pack(fill="x", padx=10, pady=5)
        
        self.entry_custom_n2 = ctk.CTkEntry(frame_custom, placeholder_text="Novo item...", width=150)
        self.entry_custom_n2.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        ctk.CTkButton(
            frame_custom, text="+", width=30, 
            command=self._adicionar_custom_nivel2
        ).pack(side="left")

        # Listas
        self.checkboxes_ambientes = {}
        self.scroll_amb = ctk.CTkScrollableFrame(self.tab_itens.tab("Ambientes"), height=200)
        self.scroll_amb.pack(fill="both", expand=True)
        for amb in AMBIENTES_SUGERIDOS:
            cb = ctk.CTkCheckBox(self.scroll_amb, text=amb, command=lambda a=amb: self._toggle_item(a))
            cb.pack(anchor="w", pady=2)
            self.checkboxes_ambientes[amb] = cb

        self.checkboxes_servicos = {}
        self.scroll_srv_n2 = ctk.CTkScrollableFrame(self.tab_itens.tab("Serviços"), height=200)
        self.scroll_srv_n2.pack(fill="both", expand=True)
        for srv in SERVICOS_SUGERIDOS:
            cb = ctk.CTkCheckBox(self.scroll_srv_n2, text=srv, command=lambda s=srv: self._toggle_item(s))
            cb.pack(anchor="w", pady=2)
            self.checkboxes_servicos[srv] = cb

    def _criar_painel_subpastas(self):
        """Cria o painel de Subpastas (Nível 3)"""
        self.frame_sub_container = ctk.CTkFrame(self.painel_esquerdo)
        self.frame_sub_container.pack(fill="x", padx=5, pady=5)
        
        header = ctk.CTkFrame(self.frame_sub_container, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=(10, 5))
        
        ctk.CTkLabel(header, text="📂 3. SERVIÇOS / SUBPASTAS (NÍVEL 3)", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        self.label_item_temp = ctk.CTkLabel(header, text="", font=ctk.CTkFont(size=11), text_color="#00d4ff")
        self.label_item_temp.pack(side="right")

        # Tabs para Subpastas Padrão vs Serviços (Filhos)
        self.tab_sub = ctk.CTkTabview(self.frame_sub_container, height=250)
        self.tab_sub.pack(fill="x", padx=10, pady=5)
        
        self.tab_sub.add("Padrão")
        self.tab_sub.add("Serviços")

        # Área de adição personalizada Nível 3
        frame_custom = ctk.CTkFrame(self.frame_sub_container, fg_color="transparent")
        frame_custom.pack(fill="x", padx=10, pady=5)
        
        self.entry_custom_n3 = ctk.CTkEntry(frame_custom, placeholder_text="Novo item...", width=150)
        self.entry_custom_n3.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        ctk.CTkButton(
            frame_custom, text="+", width=30, 
            command=self._adicionar_custom_nivel3
        ).pack(side="left")

        # Lista Padrão
        self.checkboxes_sub = {}
        self.scroll_sub_padrao = ctk.CTkScrollableFrame(self.tab_sub.tab("Padrão"), height=200)
        self.scroll_sub_padrao.pack(fill="both", expand=True)
        
        for sub in SUBPASTAS_SUGERIDAS:
            cb = ctk.CTkCheckBox(self.scroll_sub_padrao, text=sub, command=lambda s=sub: self._toggle_sub(s))
            cb.pack(anchor="w", pady=2)
            self.checkboxes_sub[sub] = cb

        # Lista Serviços (como filhos)
        self.scroll_sub_servicos = ctk.CTkScrollableFrame(self.tab_sub.tab("Serviços"), height=200)
        self.scroll_sub_servicos.pack(fill="both", expand=True)
        
        for srv in SERVICOS_SUGERIDOS:
            cb = ctk.CTkCheckBox(self.scroll_sub_servicos, text=srv, command=lambda s=srv: self._toggle_sub(s))
            cb.pack(anchor="w", pady=2)
            self.checkboxes_sub[srv] = cb

    def _criar_painel_detalhes_nivel4(self):
        """Cria o painel de Detalhes (Nível 4)"""
        self.frame_detalhes_container = ctk.CTkFrame(self.painel_esquerdo)
        self.frame_detalhes_container.pack(fill="x", padx=5, pady=5)
        
        header = ctk.CTkFrame(self.frame_detalhes_container, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=(10, 5))
        
        ctk.CTkLabel(header, text="🔍 4. DETALHES (NÍVEL 4)", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        self.label_subItem_temp = ctk.CTkLabel(header, text="", font=ctk.CTkFont(size=11), text_color="#00d4ff")
        self.label_subItem_temp.pack(side="right") # Vai mostrar qual Serviço Nível 3 está selecionado
        
        # Lista Única (Detalhes)
        self.checkboxes_detalhes = {}
        self.scroll_detalhes = ctk.CTkScrollableFrame(self.frame_detalhes_container, height=150)
        self.scroll_detalhes.pack(fill="both", expand=True, padx=10, pady=5)
        
        for det in SUBPASTAS_SUGERIDAS:
            cb = ctk.CTkCheckBox(self.scroll_detalhes, text=det, command=lambda d=det: self._toggle_nivel4(d))
            cb.pack(anchor="w", pady=2)
            self.checkboxes_detalhes[det] = cb

    def _criar_painel_preview(self):
        """Cria o painel de preview da estrutura"""
        header = ctk.CTkFrame(self.painel_direito, fg_color="transparent")
        header.pack(fill="x", padx=15, pady=(15, 5))
        
        ctk.CTkLabel(header, text="👁️ PREVIEW DA ESTRUTURA (ESTILO PASTAS.MD)", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        
        self.preview_text = ctk.CTkTextbox(
            self.painel_direito,
            font=ctk.CTkFont(family="Consolas", size=13),
            fg_color="#1a1a2e"
        )
        self.preview_text.pack(fill="both", expand=True, padx=15, pady=(5, 15))
        self.preview_text.configure(state="disabled")

    # ============================
    # LÓGICA DE EVENTOS
    # ============================

    def _selecionar_pasta(self):
        pasta = filedialog.askdirectory()
        if pasta: self.pasta_destino.set(pasta)

    def _toggle_area(self, area):
        if area in self.areas_selecionadas:
            self.areas_selecionadas.remove(area)
            if area in self.itens_por_area: del self.itens_por_area[area]
        else:
            self.areas_selecionadas.append(area)
            self.itens_por_area[area] = []
            self.area_atual = area
            self._atualizar_ui_itens()
        self._atualizar_preview()

    def _toggle_va_area(self):
        if not self.area_atual: return
        self.vista_ampla_geral[self.area_atual] = self.cb_va_area.get()
        self._atualizar_preview()

    def _toggle_item(self, item):
        if self.updating_ui:
            return
        if not self.area_atual:
            messagebox.showwarning("Atenção", "Selecione uma área primeiro!")
            return
        
        lista = self.itens_por_area[self.area_atual]
        if item in lista:
            lista.remove(item)
        else:
            # Lógica de Aviso para Área Interna + Serviço Nível 2
            eh_servico = item in SERVICOS_SUGERIDOS
            eh_area_interna = "interna" in self.area_atual.lower()
            
            if eh_area_interna and eh_servico:
                confirm = messagebox.askyesno(
                    "Atenção - Lógica de Pastas",
                    f"Você está adicionando '{item}' diretamente na raiz da '{self.area_atual}'.\n\n"
                    "Geralmente, em áreas internas, os serviços ficam dentro de um Ambiente (ex: SAA -> Pintura).\n\n"
                    "Deseja manter como item principal (Nível 2)?"
                )
                if not confirm:
                    return # O usuário cancelou, não marca o checkbox (mas como é command, o check visual já trocou?)
                    # O CustomTkinter CheckBox troca visualmente antes do command.
                    # Precisamos reverter visualmente se cancelou.
                    # Mas aqui é dificil acessar a instancia especifica do checkbox sem varrer self.checkboxes_servicos
                    # Vamos deixar o usuário desmarcar manualmente ou forçar refresh UI?
                    # Melhor: forçar refresh visual
                    # self.checkboxes_servicos[item].deselect() # Se conseguirmos acessar
            
            lista.append(item)
            self.item_atual = item
            self._atualizar_ui_sub()
        self._atualizar_preview()
        
        # Correção visual se cancelou (re-aplicar estado lógico)
        if self.area_atual:
             self._atualizar_ui_itens()

    def _toggle_sub(self, sub):
        if self.updating_ui:
            return
        if not self.area_atual or not self.item_atual:
            messagebox.showwarning("Atenção", "Selecione Área e Ambiente/Serviço!")
            return
        
        key = (self.area_atual, self.item_atual)
        if key not in self.subpastas_por_item: self.subpastas_por_item[key] = []
        
        if sub in self.subpastas_por_item[key]:
            self.subpastas_por_item[key].remove(sub)
        else:
            self.subpastas_por_item[key].append(sub)
            self.subitem_atual = sub # Define foco para Nível 4
            self._atualizar_ui_nivel4()
            
        self._atualizar_preview()

    def _toggle_nivel4(self, detalhe):
        if self.updating_ui: return
        
        if not self.area_atual or not self.item_atual or not self.subitem_atual:
             messagebox.showwarning("Atenção", "Selecione um Serviço/Subpasta no Nível 3 para adicionar detalhes!")
             return
             
        key = (self.area_atual, self.item_atual, self.subitem_atual)
        if key not in self.detalhes_por_subitem: self.detalhes_por_subitem[key] = []
        
        lista = self.detalhes_por_subitem[key]
        if detalhe in lista:
            lista.remove(detalhe)
        else:
            lista.append(detalhe)
            
        self._atualizar_preview()

    def _atualizar_ui_itens(self):
        if not self.area_atual: return
        self.updating_ui = True
        try:
            self.label_area_temp.configure(text=f"→ {self.area_atual}")
            self.cb_va_area.deselect()
            if self.vista_ampla_geral.get(self.area_atual): self.cb_va_area.select()
            
            selecionados = self.itens_por_area.get(self.area_atual, [])
            for name, cb in {**self.checkboxes_ambientes, **self.checkboxes_servicos}.items():
                if name in selecionados: cb.select()
                else: cb.deselect()
        finally:
            self.updating_ui = False

    def _atualizar_ui_sub(self):
        if not self.item_atual: return
        self.updating_ui = True
        try:
            self.label_item_temp.configure(text=f"→ {self.item_atual}")
            key = (self.area_atual, self.item_atual)
            selecionados = self.subpastas_por_item.get(key, [])
            for name, cb in self.checkboxes_sub.items():
                if name in selecionados: cb.select()
                else: cb.deselect()
        finally:
            self.updating_ui = False

    def _atualizar_ui_nivel4(self):
        if not self.subitem_atual: return
        self.updating_ui = True
        try:
             self.label_subItem_temp.configure(text=f"→ {self.subitem_atual}")
             key = (self.area_atual, self.item_atual, self.subitem_atual)
             selecionados = self.detalhes_por_subitem.get(key, [])
             
             for name, cb in self.checkboxes_detalhes.items():
                 if name in selecionados: cb.select()
                 else: cb.deselect()
        finally:
             self.updating_ui = False

    def _atualizar_preview(self):
        self.preview_text.configure(state="normal")
        self.preview_text.delete("1.0", "end")
        
        nome_raiz = self.nome_levantamento.get().strip() or "Levantamento"
        self.preview_text.insert("end", f"📁 {nome_raiz}\n")
        
        for area in self.areas_selecionadas:
            self.preview_text.insert("end", f"  - {area}\n")
            
            # Vista ampla da área
            if self.vista_ampla_geral.get(area):
                self.preview_text.insert("end", f"    - Vista ampla\n")
            
            itens = self.itens_por_area.get(area, [])
            for idx_item, item in enumerate(itens, 1):
                # Se o item for um ambiente (está na lista de ambientes sugeridos)
                if item in AMBIENTES_SUGERIDOS:
                    self.preview_text.insert("end", f"    {idx_item} - {item}\n")
                    
                    key = (area, item)
                    sub_selecionadas = self.subpastas_por_item.get(key, [])
                    # Se tiver subpastas, elas podem ser serviços (como no pastas.md)
                    for idx_sub, sub in enumerate(sub_selecionadas, 1):
                        # Se a subpasta é um serviço (standard ou custom)
                        eh_servico = (sub in SERVICOS_SUGERIDOS) or (sub in self.custom_servicos)
                        
                        if eh_servico:
                            self.preview_text.insert("end", f"      {idx_item}.{idx_sub} - {sub}\n")
                        else:
                            self.preview_text.insert("end", f"      - {sub}\n")
                        
                        # Nível 4 (Detalhes) para Ambientes
                        key_n4 = (area, item, sub)
                        detalhes = self.detalhes_por_subitem.get(key_n4, [])
                        for det in detalhes:
                             self.preview_text.insert("end", f"        - {det}\n")
                else:
                    # É um serviço direto na área
                    self.preview_text.insert("end", f"    {idx_item} - {item}\n")
                    key = (area, item)
                    for sub in self.subpastas_por_item.get(key, []):
                        self.preview_text.insert("end", f"      - {sub}\n")
                        # Nível 4 (Detalhes)
                        key_n4 = (area, item, sub)
                        detalhes = self.detalhes_por_subitem.get(key_n4, [])
                        for det in detalhes:
                             self.preview_text.insert("end", f"        - {det}\n")

        self.preview_text.configure(state="disabled")

    def _adicionar_custom_nivel2(self):
        nome = self.entry_custom_n2.get().strip()
        if not nome: return
        
        # Onde adicionar? Depende da aba ativa
        aba_ativa = self.tab_itens.get() # "Ambientes" ou "Serviços"
        
        if aba_ativa == "Ambientes":
            if nome in self.checkboxes_ambientes: return
            cb = ctk.CTkCheckBox(self.scroll_amb, text=nome, command=lambda a=nome: self._toggle_item(a))
            cb.pack(anchor="w", pady=2)
            self.checkboxes_ambientes[nome] = cb
            # Marcar automaticamente
            self._toggle_item(nome)
            
        else: # Serviços
            if nome in self.checkboxes_servicos: return
            cb = ctk.CTkCheckBox(self.scroll_srv_n2, text=nome, command=lambda s=nome: self._toggle_item(s))
            cb.pack(anchor="w", pady=2)
            self.checkboxes_servicos[nome] = cb
            self._toggle_item(nome)
            
        self.entry_custom_n2.delete(0, "end")

    def _adicionar_custom_nivel3(self):
        nome = self.entry_custom_n3.get().strip()
        if not nome: return
        
        aba_ativa = self.tab_sub.get() # "Padrão" ou "Serviços"
        
        if aba_ativa == "Padrão":
            target_scroll = self.scroll_sub_padrao
        else:
            target_scroll = self.scroll_sub_servicos
            self.custom_servicos.add(nome) # É um serviço
            
        if nome in self.checkboxes_sub: return
        
        cb = ctk.CTkCheckBox(target_scroll, text=nome, command=lambda s=nome: self._toggle_sub(s))
        cb.pack(anchor="w", pady=2)
        self.checkboxes_sub[nome] = cb
        self._toggle_sub(nome) # Marcar
        
        self.entry_custom_n3.delete(0, "end")

    def _gerar_estrutura(self):
        destino = self.pasta_destino.get()
        nome_raiz = self.nome_levantamento.get().strip()
        
        if not destino or not nome_raiz or not self.areas_selecionadas:
            messagebox.showwarning("Atenção", "Preencha todos os campos e selecione ao menos uma área!")
            return

        try:
            raiz = os.path.join(destino, nome_raiz)
            os.makedirs(raiz, exist_ok=True)
            count = 1
            
            for area in self.areas_selecionadas:
                path_area = os.path.join(raiz, f"- {area}")
                os.makedirs(path_area, exist_ok=True)
                count += 1
                
                if self.vista_ampla_geral.get(area):
                    os.makedirs(os.path.join(path_area, "- Vista ampla"), exist_ok=True)
                    count += 1
                
                itens = self.itens_por_area.get(area, [])
                for idx_item, item in enumerate(itens, 1):
                    # Nível Ambiente ou Serviço Direto
                    # Se for ambiente, usa número (1 - SAA)
                    # Se for serviço direto na área (ex: pintura externa), também usa número
                    # A lógica do pastas.md sugere que tudo no nível 2 tem número
                    nome_item = f"{idx_item} - {item}"
                    path_item = os.path.join(path_area, nome_item)
                    os.makedirs(path_item, exist_ok=True)
                    count += 1
                    
                    key = (area, item)
                    subs = self.subpastas_por_item.get(key, [])
                    for idx_sub, sub in enumerate(subs, 1):
                        # Lógica Atualizada para Nível 3 (Filho do item)
                        eh_servico = (sub in SERVICOS_SUGERIDOS) or (sub in self.custom_servicos)
                        
                        if eh_servico:
                             nome_sub = f"{idx_sub} - {sub}" # 1.1 simplificado para visualização, mas na pasta pode ser 1.1?
                             # Analisando o pastas.md: "1.1 - Pintura acrílica"
                             # Então precisamos do índice do pai.
                             nome_sub = f"{idx_item}.{idx_sub} - {sub}"
                        elif sub in SUBPASTAS_SUGERIDAS or sub == "Vista ampla":
                             nome_sub = f"- {sub}"
                        else:
                             nome_sub = f"- {sub}"
                        
                        path_sub = os.path.join(path_item, nome_sub)
                        os.makedirs(path_sub, exist_ok=True)
                        count += 1
                        
                        # NÍVEL 4: Detalhes dentro do Nível 3
                        key_n4 = (area, item, sub)
                        detalhes = self.detalhes_por_subitem.get(key_n4, [])
                        for det in detalhes:
                             path_det = os.path.join(path_sub, f"- {det}")
                             os.makedirs(path_det, exist_ok=True)
                             count += 1

            messagebox.showinfo("Sucesso", f"Estrutura criada com sucesso!\n{count} pastas geradas.")
            self._atualizar_preview()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar pastas: {str(e)}")

    def _limpar_selecao(self):
        confirm = messagebox.askyesno("Confirmar", "Deseja limpar todos os itens selecionados?")
        if not confirm: return
        
        # Resetar dados
        self.areas_selecionadas.clear()
        self.itens_por_area.clear()
        self.subpastas_por_item.clear()
        self.detalhes_por_subitem.clear()
        self.vista_ampla_geral.clear()
        
        self.area_atual = None
        self.item_atual = None
        self.subitem_atual = None
        
        # Resetar UI (Desmarcar tudo)
        for cb in self.checkboxes_areas.values(): cb.deselect()
        for cb in self.checkboxes_ambientes.values(): cb.deselect()
        for cb in self.checkboxes_servicos.values(): cb.deselect()
        for cb in self.checkboxes_sub.values(): cb.deselect()
        for cb in self.checkboxes_detalhes.values(): cb.deselect()
        self.cb_va_area.deselect()
        
        # Limpar Labels Temporários
        self.label_area_temp.configure(text="")
        self.label_item_temp.configure(text="")
        self.label_subItem_temp.configure(text="")

        self._atualizar_preview()
        messagebox.showinfo("Limpeza", "Todas as seleções foram removidas.")


if __name__ == "__main__":
    app = GeradorEstruturaPastas()
    app.mainloop()
