<template>
  <div class="grafico">
    <!-- <h2>{{ title }}</h2> -->
    <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
  </div>
</template>

<script>
import { Plotly } from "vue-plotly";

export default {
  props: {
    title: String,
    regiao: String,
    jsonTendencia: Array,
  },
  components: {
    Plotly,
  },
  data() {
    return {
      data: this.jsonTendencia
        .map((element) => {
          element.x = element.date_list;
          element.y = element.ocupation_list;
          element.name = element.state;
          element.showlegend = true;
          element.type = "scatter";
          element.hovertemplate = "<b>% de ocupação de UTI</b>: %{y}";
          return element;
        })
        .sort((a, b) => a.name.localeCompare(b.name)),
      layout: {
        height: 800,
        title: {
          text: this.title.toUpperCase(),
          font: {
            size: 18,
          },
          align: "left",
        },
        // barmode: "stack",
        legend: {
          orientation: "v",
        },
        yaxis: {
          range: [0, 100],
          zeroline: false,
        },
        xaxis: {
          zeroline: false,
        },
      },
    };
  },
  watch: {
    regiao() {
      if (this.regiao !== "brasil") {
        this.data = this.jsonTendencia
          .filter((tendencia) => tendencia.region.toLowerCase() === this.regiao)
          .map((tendencia) => {
            tendencia.x = tendencia.date_list;
            tendencia.y = tendencia.ocupation_list;
            tendencia.name = tendencia.state;
            tendencia.showlegend = true;
            tendencia.type = "scatter";
            tendencia.hovertemplate = "<b>% de ocupação de UTI</b>: %{y}";
            return tendencia;
          });
      } else {
        this.data = this.jsonTendencia
          .map((element) => {
            element.x = element.date_list;
            element.y = element.ocupation_list;
            element.name = element.state;
            element.showlegend = true;
            element.type = "scatter";
            element.hovertemplate = "<b>% de ocupação de UTI</b>: %{y}";
            return element;
          })
          .sort((a, b) => a.name.localeCompare(b.name));
      }
    },
  },
  methods: {},
};
</script>
