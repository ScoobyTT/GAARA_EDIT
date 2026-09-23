<template>
  <div class="home">
    <div class="topo container">
      <div class="dados">
        <div class="tipo">
          <a href="#" class="covid" @click.prevent="setarMapa('covid')"
            >COVID-19</a
          >
          <a href="#" class="srag" @click.prevent="setarMapa('srag')">SRAG</a>
          <div class="date-range">
            
          </div>
        </div>

        <div class="cards">
          <div
            v-for="card in cardsLista"
            :class="card.tipo"
            :key="card.id"
            class="card"
          >
            <h2>{{ card.nome }}</h2>
            <h4>{{ Number(card.valor).toLocaleString('pt-BR') }}</h4>
          </div>
        </div>
      </div>
      <div class="mapa">
        <MapaBrasil ref="mapa" class="mapa" :tipo="tipo" />
      </div>
    </div>

    <div class="colunas">
      <div class="container">
        <div class="graficos">
          <CasosCovid
            title="Casos de COVID-19 e hospitalizações por SRAG por SE* no Brasil"
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="BR"
          />
        </div>

        <div class="graficos">
          <Piramide
            title="Casos de Hospitalizados e Óbitos (SRAG) por Sexo e Faixa Etária"
            :hospitalizados="Hospitalizados"
          />
        </div>
      </div>
    </div>
    <div class="graficos por-regiao">
      <div class="container">
        <header>
          <h2>
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
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="PR"
            background="#fafafa"
            title="Paraná"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="SC"
            background="#fafafa"
            title="Santa Catarina"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="RS"
            background="#fafafa"
            title="Rio Grande do Sul"
          />
        </div>
        <div
          id="r2"
          key="r2"
          v-if="regiao === 'sudeste'"
          class="lista-graficos"
        >
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="SP"
            background="#fafafa"
            title="São Paulo"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="RJ"
            background="#fafafa"
            title="Rio de Janeiro"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="ES"
            background="#fafafa"
            title="Espírito Santo"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="MG"
            background="#fafafa"
            title="Minas Gerais"
          />
        </div>
        <div id="r3" key="r3" v-if="regiao === 'centro'" class="lista-graficos">
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="MS"
            background="#fafafa"
            title="Mato Grosso do Sul"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="MT"
            background="#fafafa"
            title="Mato Grosso"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="GO"
            background="#fafafa"
            title="Goiás"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="DF"
            background="#fafafa"
            title="Distrito Federal"
          />
        </div>
        <div id="r4" key="r4" v-if="regiao === 'norte'" class="lista-graficos">
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="RO"
            background="#fafafa"
            title="Rondônia"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            background="#fafafa"
            ufs="AC"
            title="Acre"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            background="#fafafa"
            ufs="AM"
            title="Amazonas"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            background="#fafafa"
            ufs="RR"
            title="Roraima"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            background="#fafafa"
            ufs="PA"
            title="Pará"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            background="#fafafa"
            ufs="AP"
            title="Amapá"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            background="#fafafa"
            ufs="TO"
            title="Tocantins"
          />
        </div>
        <div
          id="r5"
          key="r5"
          v-if="regiao === 'nordeste'"
          class="lista-graficos"
        >
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="MA"
            background="#fafafa"
            title="Maranhão"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="PI"
            background="#fafafa"
            title="Piauí"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="CE"
            background="#fafafa"
            title="Ceará"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="RN"
            background="#fafafa"
            title="Rio Grande do Norte"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="PB"
            background="#fafafa"
            title="Paraíba"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="PE"
            background="#fafafa"
            title="Pernambuco"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="AL"
            background="#fafafa"
            title="Alagoas"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="SE"
            background="#fafafa"
            title="Sergipe"
          />
          <CasosCovid
            :covid="weekCovidData"
            :nuti="weekSragNutiData"
            :uti="weekSragUtiData"
            ufs="BA"
            background="#fafafa"
            title="Bahia"
          />
        </div>
      </div>
    </div>
    <div class="footer">
      <p>Dados fornecidos pelo Ministerio da Saúde (MS)
      <p>Os dados de Vacina para COVID-19 e Hospitalizações por Srag estão disponíveis no <a href="https://opendatasus.saude.gov.br/" target="_blank">OpenDataSus</a></p>
      <p>Os dados de Casos e Óbitos pela COVID-19 estão disponíveis no <a href="https://covid.saude.gov.br/" target="_blank">Painel COVID</a></p>
      <p v-for="update in Update" :key="update">
          {{update}}
      </p>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import MapaBrasil from "@/components/mapas/Brasil.vue";
import CasosCovid from "@/components/graficos/casos-covid.vue";
import Piramide from "@/components/graficos/piramide-v2.vue";
import Hospitalizados from "@/data/home/age_gender_sars.json";
import weekCovidData from "@/data/home/week_covid.json";
import weekSragNutiData from "@/data/home/week_srag_NUTI_casos.json";
import weekSragUtiData from "@/data/home/week_srag_UTI_casos.json";
import Update from "@/data/home/home_update.json";
import { mapGetters } from "vuex";
export default {
  name: "Home",
  metaInfo: {
    title: "COVID-19 E SRAG",
    // titleTemplate: "%s | Ocupação de leitos",
  },
  components: {
    MapaBrasil,
    CasosCovid,
    Piramide,
  },
  computed: {
    ...mapGetters({
      cards: "home/getCards",
    }),
    cardsLista() {
      return this.cards.filter((card) => card.tipo == this.tipo);
    },
  },
  data() {
    return {
      tipo: "covid",
      regiao: "sul",
      covid: true,
      graficos: 6,
      Hospitalizados,
      weekCovidData,
      Update,
      weekSragNutiData,
      weekSragUtiData,
      rangeData: ["2021-10-07", "2021-11-25"],
      type: "total",
    };
  },
  async beforeMount() {
    await this.$store.dispatch("home/loadCards", {
      parametros: {
        start_date: this.rangeData[0],
        end_date: this.rangeData[1],
        type: this.type,
      },
    });

    await this.$store.dispatch("home/loadStates", {
      parametros: {
        start_date: this.rangeData[0],
        end_date: this.rangeData[1],
        type: this.type,
      },
    });
  },

  methods: {
    setarMapa(mapa) {
      this.covid = mapa === "covid";
      this.tipo = mapa;
    },
    setarRegiao(regiao) {
      this.regiao = regiao;
    },
    async selectedRange(range) {
      let start_date = range[0];
      let end_date = range[1];
      await this.$store.dispatch("home/loadCards", {
        parametros: {
          start_date: start_date,
          end_date: end_date,
          type: this.type,
        },
      });
    },
  },
};
</script>
