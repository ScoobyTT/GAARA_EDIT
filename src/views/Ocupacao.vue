<template>
  <div class="vacinacao">
    <div class="app-content container">
      <h1 class="interna-titulo">Ocupação de Leitos</h1>
    </div>

    <div class="colunas">
      <div class="container">
        <div class="graficos">
          <HeatmapOcupacao
            refs="uti"
            title="Taxa de Ocupação de UTIs por estado"
            :json="OcupacaoDataJson"
          />
        </div>
        <div class="graficos">
          <HeatmapOcupacao
            refs="clinicos"
            title="Taxa de Ocupação de leitos clínicos por estado"
            :json="OcupacaoDataJson"
          />
        </div>
      </div>
    </div>
    
    <div class="container">
      <div class="graficos">
        <header><h2> Taxa de Ocupação de leitos por estado nas últimas 12 semanas</h2></header>
        <div class="tipo">
          <a href="#" class="srag" @click.prevent="setarMapa('uti')">UTI</a>
          <a href="#" class="covid" @click.prevent="setarMapa('clinico')">CLÍNICO</a>
        </div>
      </div>
    </div>
    <div class="colunas6">
      <div class="container topo">
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="0" />
          </div>
        </div>
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="1" />
          </div>
        </div>
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="2" />
          </div>
        </div>
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="3" />
          </div>
        </div>
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="4" />
          </div>
        </div>
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="5" />
          </div>
        </div>
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="6" />
          </div>
        </div>
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="7" />
          </div>
        </div>
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="8" />
          </div>
        </div>
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="9" />
          </div>
        </div>
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="10" />
          </div>
        </div>
        <div class="graficos">
          <div class="mapa1">
            <MapaOcupacao ref="mapa" class="mapa1" :tipo="tipo" indice="11" />
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="container mt-4">
        <TabelaOcupacao
          title="Taxa de Ocupação de leitos de UTI por região e estados"
          :jsonOcupacao="OcupacaoDataJsonUti"
        />
      </div>

      <div class="container mt-4">
        <TabelaOcupacao
          title="Taxa de Ocupação de leitos clínicos por região e estados"
          :jsonOcupacao="OcupacaoDataJsonNuti"
        />
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
// @ is an alias to /src
import TabelaOcupacao from "@/components/tabelas/tabela-ocupacao-leitos.vue";
import OcupacaoDataJson from "@/data/ocupacao/ocupacao.json";
import OcupacaoDataJsonUti from "@/data/ocupacao/ocupacao_uti.json";
import OcupacaoDataJsonNuti from "@/data/ocupacao/ocupacao_clinico.json";
import HeatmapOcupacao from "@/components/graficos/heatmap-ocupacao.vue";
import MapaOcupacao from "@/components/mapas/Brasil_ocupacao.vue";
import Update from "@/data/ocupacao/ocupacao_update.json";

export default {
  name: "Ocupação",
  metaInfo: {
    title: "Ocupação",
    titleTemplate: "%s | Ocupação de leitos",
  },
  components: {
    TabelaOcupacao,
    HeatmapOcupacao,
    MapaOcupacao
  },
  data() {
    return {
      OcupacaoDataJson,
      OcupacaoDataJsonUti,
      OcupacaoDataJsonNuti,
      Update,
      regiao: "brasil",
      tipo: "uti",
      varia: true,
    };
  },
  methods: {
    setarMapa(mapa) {
      this.varia = mapa === "uti"
      this.tipo = mapa;
    },
    setarRegiao(regiao) {
      this.regiao = regiao;
    },
  },
};
</script>
