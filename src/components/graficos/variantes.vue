<template>
  <div class="grafico">
    <header>
      <h2>
        {{ title }}
      </h2>
    </header>
    <Plotly :data="data" :layout="layout" :toImageButtonOptions="{format: 'png', scale: 3, filename:'variantes', height: 480, width: 845}" :display-mode-bar="true"></Plotly>
  </div>
</template>

<script>
import { Plotly } from "vue-plotly";

export default {
  props: {
    json: Object,
    title: String,
    tipo: String,
  },
  components: {
    Plotly,
  },
  data() {
    return {
      data: [],
      layout: {
        margin: {
          t: 40,
          l: 50,
          r: 50,
        },
        // title: {
        //   text: this.title,
        //   font: {
        //     size: 16,
        //   },
        // },
        bargap: 0.02,
        barmode: "stack",
        legend: {
          orientation: "h",
          yanchor: "bottom",
          y: -0.21,
          xanchor: "right",
          x: 1
        },
      },
    };
  },

  mounted() {
    let variantes = new Set(Object.values(this.json.Variante));
    let data = [];
    variantes.forEach((variante) => {
      if (typeof this.tipo !== "undefined") {
        if (this.tipo !== variante) {
          return false;
        }
      }

      // todas as chaves da variate
      let keys = Object.keys(this.json.Variante).filter(
        (chave) => this.json.Variante[chave] === variante
      );

      let eixoX = keys.map((key) => {
        return this.json.Data[key];
      });

      let eixoY = keys.map((key) => {
        return this.json["Nº de Cópias"][key];
      });

      let cores = keys.map((key) => {
        return this.json.VarianteCores[key];
      });

      let textos = keys.map((key) => {
        return this.json.Variante[key];
      });

      data.push({
        x: eixoX,
        y: eixoY,
        type: "bar",
        text: textos,
        name: variante,
        hovertemplate:
          "<b>Variante</b>: %{text}" +
          "<br><b>Data</b>: %{x}<br>" +
          "<br><b>Nº de Cópias</b>: %{y}<br>",
        marker: {
          color: cores,
        },
        showlegend: true,
      });
    });

    this.data = data;
  },

  methods: {},
};
</script>
