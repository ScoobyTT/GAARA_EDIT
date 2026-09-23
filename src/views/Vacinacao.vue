<template>
  <div class="app-content vacinacao">
    <div class="container">
      <h1 class="interna-titulo">Vacinação</h1>
    </div>

    <div class="container">
      <div class="graficos">
        <Vacinados
          title="% da População Vacinada por Estados"
          :json="dataVacinados"
        />
      </div>
    </div>
    <div class="container mt-4">
        <TabelaVacinados
          title="Tabela de Doses Aplicadas, Proporção Vacinal e Não Vacinados por Municípios e Faixa Etária"
          :jsonVacinadosMun="VacinadosDataJson"
        />
    </div>
    <div class="colunas">
      <div class="container">
        <div class="graficos">
          <Semana title="ÓBITOS POR SRAG E DOSES DE VACINA APLICADA POR SEMANA EPIDEMIOLÓGICA (SE)" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" uf="BR" />
        </div>

        <div class="graficos">
          <PiramideDoses
            title="Proporção de vacinação por faixa etária e sexo, segundo o tipo de dose, Brasil"
            :json="dataDoses"
          />
        </div>
      </div>
    </div>
    <div class="graficos por-regiao">
      <div class="container">
        <header>
          <h2 style="max-width: 100%">
            Hospitalizações por síndrome respiratória aguda grave (SRAG) em UTI
            e não UTI, por semana epidemiológica (SE)
          </h2>

          <div class="tipo">
            <a href="#" @click.prevent="setarRegiao('sul')">SUL</a>
            <a href="#" @click.prevent="setarRegiao('sudeste')">SUDESTE</a>
            <a href="#" @click.prevent="setarRegiao('centro')">CENTRO-OESTE</a>
            <a href="#" @click.prevent="setarRegiao('norte')">NORTE</a>
            <a href="#" @click.prevent="setarRegiao('nordeste')">NORDESTE</a>
          </div>
        </header>
        <div id="r1" key="r1" v-if="regiao === 'sul'" class="lista-graficos">
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Paraná" uf="PR" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Santa Catarina" uf="SC" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Rio Grande do Sul" uf="RS" />
        </div>
        <div id="r2" key="r2" v-if="regiao === 'sudeste'" class="lista-graficos">
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Espírito Santo" uf="ES" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Minas Gerais" uf="MG" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="São Paulo" uf="SP" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Rio de Janeiro" uf="RJ" />
        </div>
        <div id="r3" key="r3" v-if="regiao === 'centro'" class="lista-graficos">
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Mato Grosso do Sul" uf="MS" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Mato Grosso" uf="MT" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Goiás" uf="GO" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Distrito Federal" uf="DF" />
        </div>
        <div id="r4" key="r4" v-if="regiao === 'norte'" class="lista-graficos">
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Rondônia" uf="RO" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Acre" uf="AC" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Amazonas" uf="AM" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Roraima" uf="RR" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Pará" uf="PA" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Amapá" uf="AP" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Tocantins" uf="TO" />
        </div>
        <div id="r5" key="r5" v-if="regiao === 'nordeste'" class="lista-graficos">
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Maranhão" uf="MA" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Piauí" uf="PI" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Ceará" uf="CE" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Rio Grande do Norte" uf="RN" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Paraíba" uf="PB" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Pernambuco" uf="PE" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Alagoas" uf="AL" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Sergipe" uf="SE" />
          <Semana background="#fafafa" :obitosCovid="weekObitosCovid" :obitosNCovid="weekObitosNCovid" :dose1="weekDose1" :dose2="weekDose2" :dose3="weekDose3" :dose4="weekDose4" title="Bahia" uf="BA" />
        </div>
      </div>
    </div>
    <div class="footer">
      <p>Dados fornecidos pelo Ministerio da Saúde (MS)
      <p>Os dados de Vacina para COVID-19 e Hospitalizações por Srag estão disponíveis no <a href="https://opendatasus.saude.gov.br/" target="_blank">OpenDataSus</a></p>
      <p v-for="update in Update" :key="update">
          {{update}}
      </p>
    </div>
  </div>
</template>
<script>
import PiramideDoses from "@/components/graficos/piramide-doses.vue";
import Vacinados from "@/components/graficos/vacinados.vue";
import Semana from "@/components/graficos/semana-epidemiologica.vue";
import dataVacinados from "../data/vacinacao/vacinados_percent_uf.json";
import dataSemana from "../data/vacinacao/semana.json";
import dataDoses from "../data/vacinacao/age_gender_sars_vacina.json";
import TabelaVacinados from "@/components/tabelas/tabela_vacinados.vue";
import VacinadosDataJson from "@/data/vacinacao/tabela_vacina.json";
import Update from "@/data/vacinacao/vacinacao_update.json";
import weekObitosCovid from "@/data/vacinacao/week_obitos_especificados.json";
import weekObitosNCovid from "@/data/vacinacao/week_obitos_Nespecificados.json";
import weekDose1 from "@/data/vacinacao/week_vacina_1dose.json";
import weekDose2 from "@/data/vacinacao/week_vacina_completa.json";
import weekDose3 from "@/data/vacinacao/week_vacina_reforco.json";
import weekDose4 from "@/data/vacinacao/week_vacina_2reforco.json";


export default {
  name: "Vacinação",
  metaInfo: {
    title: "Vacinação",
    // titleTemplate: "%s | Ocupação de leitos",
  },
  components: {
    PiramideDoses,
    Semana,
    Vacinados,
    TabelaVacinados,
  },
  data() {
    return {
      regiao: "sul",
      dataVacinados,
      dataSemana,
      dataDoses,
      weekObitosCovid,
      weekObitosNCovid,
      weekDose1,
      weekDose2,
      weekDose3,
      weekDose4,
      VacinadosDataJson,
      Update,
    };
  },
  mounted() {
    // let doses = [];
    // let obtos = [];
    // Object.values(this.dose1["Total_Vac_1Dose"]).forEach((item, index) => {
    //   doses.push({
    //     week: this.dose2["SEM_NOT"][index],
    //     first: item,
    //     second: this.dose2["Total_Vac_2Dose"][index],
    //   });
    // });
    // Object.values(this.obitos_covid["TOTAL"]).forEach((item, index) => {
    //   obtos.push({
    //     week: this.obitos_naocovid["SEM_NOT"][index],
    //     covid: item,
    //     nocovid: this.obitos_naocovid["TOTAL"][index],
    //   });
    // });
    // console.clear();
    // Object.values(this.vac_pop_fem["CLASSE_ETARIA"]).forEach((item, index) => {
    //   doses.push({
    //     labels: item,
    //     male: {
    //       first: this.vac_pop_masc["DOSE_1"][index],
    //       second: this.vac_pop_masc["DOSE_2"][index],
    //       third: this.vac_pop_masc["DOSE_REFORCO"][index],
    //       population: this.vac_pop_masc["POPULACAO"][index],
    //     },
    //     female: {
    //       first: this.vac_pop_fem["DOSE_1"][index],
    //       second: this.vac_pop_fem["DOSE_2"][index],
    //       third: this.vac_pop_fem["DOSE_REFORCO"][index],
    //       population: this.vac_pop_fem["POPULACAO"][index],
    //     },
    //   });
    // });
    // console.log(doses);
  },
  methods: {
    setarMapa(mapa) {
      this.covid = mapa === "covid";
      this.tipo = mapa;
    },
    setarRegiao(regiao) {
      this.regiao = regiao;
    },
  },
};
</script>
