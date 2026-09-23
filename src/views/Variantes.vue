<template>
  <div class="app-content vacinacao">
    <div class="container">
      <h1 class="interna-titulo">Variantes</h1>
    </div>

    <div class="colunas">
      <div class="container">
        <div class="dadosv">
          <div class="cardsv">
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
        <div class="graficos">
          <Variantes title="Variantes no Brasil" :json="variantesData" />
        </div>
      </div>
    </div>
    <div class="container">
      <div class="tipo">
        <a href="#" class="alpha" @click.prevent="setarMapa('Alpha')">Alpha</a>
        <a href="#" class="beta" @click.prevent="setarMapa('Beta')">Beta</a>
        <a href="#" class="delta" @click.prevent="setarMapa('Delta')">Delta</a>
        <a href="#" class="gamma" @click.prevent="setarMapa('Gamma')">Gamma</a>
        <a href="#" class="omicron" @click.prevent="setarMapa('Omicron')">Omicron</a>
      </div>
    </div>
    
    <div id="r1" key="r1" v-if="tipo === 'Alpha'" class="">
      <div class="colunas">
        <div class="container">
          <div class="graficos">
            <Variantes title="Histórico de cópias da variante Alpha no Brasil" :json="variantesData" :tipo="tipo" />
          </div>
          <div class="mapa">
            <MapaVariantes ref="mapa" class="mapa" :tipo="tipo" />
          </div>
        </div>
      </div>
    </div>
    <div id="r2" key="r2" v-if="tipo === 'Beta'" class="">
      <div class="colunas">
        <div class="container">
          <div class="graficos">
            <Variantes title="Histórico de cópias da variante Beta no Brasil" :json="variantesData" :tipo="tipo" />
          </div>
          <div class="mapa">
            <MapaVariantes ref="mapa" class="mapa" :tipo="tipo" />
          </div>
        </div>
      </div>
    </div>
    <div id="r3" key="r3" v-if="tipo === 'Gamma'" class="">
      <div class="colunas">
        <div class="container">
          <div class="graficos">
            <Variantes title="Histórico de cópias da variante Gamma no Brasil" :json="variantesData" :tipo="tipo" />
          </div>
          <div class="mapa">
            <MapaVariantes ref="mapa" class="mapa" :tipo="tipo" />
          </div>
        </div>
      </div>
    </div>
    <div id="r4" key="r4" v-if="tipo === 'Delta'" class="">
      <div class="colunas">
        <div class="container">
          <div class="graficos">
            <Variantes title="Histórico de cópias da variante Delta no Brasil" :json="variantesData" :tipo="tipo" />
          </div>
          <div class="mapa">
            <MapaVariantes ref="mapa" class="mapa" :tipo="tipo" />
          </div>
        </div>
      </div>
    </div>
    <div id="r5" key="r5" v-if="tipo === 'Omicron'" class="">
      <div class="colunas">
        <div class="container">
          <div class="graficos">
            <Variantes title="Histórico de cópias da variante Omicron no Brasil" :json="variantesData" :tipo="tipo" />
          </div>
          <div class="mapa">
            <MapaVariantes ref="mapa" class="mapa" :tipo="tipo" />
          </div>
        </div>
      </div>
    </div>
    
    <div class="">
      <div class="container">
        <div class="graficos">
          <HeatmapSublinhagens
            ref="uti"
            title="Sublinhagens da Delta por estado"
            :json="SublinhagensDeltaDataJson"
          />
        </div>
      </div>
    </div>
    <div class="">
      <div class="container">
        <div class="graficos">
          <HeatmapSublinhagensOmicron
            ref="uti"
            title="Sublinhagens da Omicron por estado"
            :json="SublinhagensOmicronDataJson"
          />
        </div>
      </div>
    </div>
    <div class="colunas">
      <div class="container">
        <div class="graficos">
          <Tabela1
            title="Variantes de Preocupação (VOC)"
            :json="preocupacaoData"
          />
        </div>

        <div class="graficos">
          <Tabela1 title="Variantes de interesse (VOI)" :json="interesseData" />
        </div>
      </div>
    </div>
    <div class="footer">
      <p>Dados fornecidos pelo <i>Global Initiative on Sharing All Influenza Data</i> <img src="https://www.gisaid.org/fileadmin/gisaid/img/schild.png" alt="GISAID" width="60px" heigth="21px" />
      <p>Os dados são fornecidos pelo GISAID, os dados estão sujeitos aos <a href="https://www.gisaid.org/registration/terms-of-use/" target="_blank">Termos e Condições</a></p>
      <p v-for="update in Update" :key="update">
          {{update}}
      </p>
    </div>
  </div>
</template>
<script>
// @ is an alias to /src
import Tabela1 from "@/components/tabelas/tabela1.vue";
import Variantes from "@/components/graficos/variantes.vue";
import variantesData from "@/data/variantes/variantes_copias.json";
import preocupacaoData from "@/data/variantes/var_preocupacao.json";
import interesseData from "@/data/variantes/var_interesse.json";
import cards from "@/data/variantes/cards_variantes.json";
import MapaVariantes from "@/components/mapas/Brasil_variantes.vue";
import HeatmapSublinhagens from "@/components/graficos/heatmap-sublinhagens.vue";
import HeatmapSublinhagensOmicron from "@/components/graficos/heatmap-sublinhagens-omicron.vue";
import SublinhagensDeltaDataJson from "@/data/variantes/sublinhagens-delta.json";
import SublinhagensOmicronDataJson from "@/data/variantes/sublinhagens-omicron.json";
import Update from "@/data/variantes/variantes_update.json";


export default {
  name: "Home",
  metaInfo: {
    title: "Variantes",
    // titleTemplate: "%s | Ocupação de leitos",
  },
  mounted(){
    console.log({Update});
  },
  components: {
    Variantes,
    Tabela1,
    MapaVariantes,
    HeatmapSublinhagens,
    HeatmapSublinhagensOmicron,
    // CasosCovid,
    // Piramide,
  },
  data() {
    return {
      tipo:"Omicron",
      voc:true,
      variantesData,
      preocupacaoData,
      interesseData,
      cards,
      SublinhagensDeltaDataJson,
      SublinhagensOmicronDataJson,
      Update,
    };
  },
  computed: {
    listaCards: function () {
      return this.cards.filter(function (card) {
        return card.tipo;
      })
      
      // return this.cards.filter((card) => card.tipo == this.tipo);
    }
  },
 methods: {
    setarMapa(mapa) {
      this.voc = mapa === "Omicron";
      this.tipo = mapa;
      
    },
  },
};
</script>