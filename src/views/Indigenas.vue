<template>
  <div class="app-content vacinacao">
    <div class="container">
      <h1 class="interna-titulo">COVID-19 EM TERRAS INDÍGENAS</h1>
    </div>
    
    <div class="colunas_total">
      <div class="container">
        <div class="dadosi">
          <div class="cardsi">
            <div
              v-for="card in listaCards"
              :class="card.tipo"
              :key="card.id"
              class="card"
            >
              <h2>{{ card.nome }}</h2>
              <h4>{{ Number(card.valor).toLocaleString('pt-BR') }}</h4>
            </div>
          </div>
        </div>
      </div>
    </div>
        
    <div class="container">
      <div class="container mt-4">
        <TabelaIndigenasVacinas
          title="Tabela de doses aplicadas, proporção vacinal, tipo de dose e faixa etária por Distritos Sanitários Especiais Indígenas (DSEI)"
          :jsonIndigenasVac="dseisVacinas"
        />
      </div>
      <div class="container mt-4">
        <TabelaIndigenasCasos
          title="Tabela de casos, óbitos, semana epidemiológica por Distritos Sanitários Especiais Indígenas (DSEI)"
          :jsonIndigenasCasos="dseisCasos"
        />
      </div>
    </div>

    <div class="graficos">
      <div class="container">
        <header>
          <h2>
            PROPORÇÃO VACINAL, CASOS E ÓBITOS NOS DISTRITOS SANTÁRIOS ESPECIAIS INDÍGENAS (DSEIS)
          </h2>
        </header>
      </div>
    </div>
    
    <div class="colunas">
      <div class="container">
        <div class="vacinas">
          <div class="tipo">
            <a href="#" class="dose1" @click.prevent="setarMapaV('Dose1')">1ª Dose</a>
            <a href="#" class="dose2" @click.prevent="setarMapaV('Dose2')">2ª Dose</a>
            <a href="#" class="reforco" @click.prevent="setarMapaV('Reforco')">Reforço/Adicional</a>
          </div>
          <div id="v1" key="v1" v-if="tipoV === 'Dose1'" class="">
            <div class="mapa">
              <MapaDseiVacinas ref="mapa" class="mapa" :tipo="tipoV" />
            </div>
          </div>
          <div id="v2" key="v2" v-if="tipoV === 'Dose2'" class="">
            <div class="mapa">
              <MapaDseiVacinas ref="mapa" class="mapa" :tipo="tipoV" />
            </div>
          </div>
          <div id="v3" key="v3" v-if="tipoV === 'Reforco'" class="">
            <div class="mapa">
              <MapaDseiVacinas ref="mapa" class="mapa" :tipo="tipoV" />
            </div>
          </div>
        </div>
        <div class="covid">
          <div class="tipo">
            <a href="#" class="covid" @click.prevent="setarMapaC('Casos')">Casos</a>
            <a href="#" class="covid" @click.prevent="setarMapaC('Obitos')">Óbitos</a>
          </div>
          <div id="c1" key="c1" v-if="tipoC === 'Casos'" class="">
            <div class="mapa">
              <MapaDseiCasos ref="mapa" class="mapa" :tipo="tipoC" />
            </div>
          </div>
          <div id="c2" key="c2" v-if="tipoC === 'Obitos'" class="">
            <div class="mapa">
              <MapaDseiCasos ref="mapa" class="mapa" :tipo="tipoC" />
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="footer">
      <p>Dados são fornecidos pelas Secretarias Estaduais de Saúde (SES)</p>
      <p v-for="update in Update" :key="update">
          {{update}}
      </p>
    </div>
  </div>
</template>
<script>
import MapaDseiVacinas from "@/components/mapas/Dsei_Vacinas.vue";
import MapaDseiCasos from "@/components/mapas/Dsei_Casos.vue";
import TabelaIndigenasVacinas from "@/components/tabelas/tabela-indigena-vacina.vue";
import TabelaIndigenasCasos from "@/components/tabelas/tabela-indigena-covid.vue";
import dseisVacinas from "@/data/indigena/tabela_indigenas_vacinas.json";
import dseisCasos from "@/data/indigena/tablela_indigenas_obitos_casos.json";
import Update from "@/data/indigena/indigenas_update.json";
import cards from "@/data/indigena/cards_indigenas.json";

export default {
  name: "Indígenas",
  metaInfo: {
    title: "Indígenas",
    titleTemplate: "%s | COVID-19 em terras indígenas",
  },
  components: {
    TabelaIndigenasVacinas,
    TabelaIndigenasCasos,
    MapaDseiVacinas,
    MapaDseiCasos,
  },
  computed: {
    listaCards: function () {
      return this.cards.filter(function (card) {
        return card.tipo;
      })
      
      // return this.cards.filter((card) => card.tipo == this.tipo);
    }
  },
  data() {
    return {
      tipoV:"Dose1",
      tipoC:"Casos",
      vacina:true,
      casos:true,
      dseisVacinas,
      dseisCasos,
      Update,
      cards,
    };
  },
  methods: {
    setarMapaV(mapa) {
      this.vacina = mapa === "Dose1";
      this.tipoV = mapa;
    },
    setarMapaC(mapa) {
      this.casos = mapa === "Casos";
      this.tipoC = mapa;
    },
  },
};
</script>
