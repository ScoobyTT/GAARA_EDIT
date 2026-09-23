<template>
  <div class="grafico graficos">
    <header>
      <h2>
        {{ title }}
      </h2>
    </header>
    <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
    <!-- {{values}} -->
  </div>
</template>

<script>
import { Plotly } from "vue-plotly";

export default {
  props: {
    json: Object,
    title: String,
  },
  components: {
    Plotly,
  },

  data() {
    return {
      data: [
        {
          type: "table",
          header: {
            values: Object.keys(this.json),
            align: "center",
            line: { width: 1, color: "#fff" },
            fill: { color: "#61aac3" },
            font: { family: `"Oswald", sans-serif`, size: 14, color: "white" },
          },
          cells: {
            values: [],
            align: ["left", "center"],
            line: { color: "#fff", width: 1 },
            font: {
              family: `"Oswald", sans-serif`,
              size: 14,
              color: ["black"],
            },
            fill: { color: ["rgb(235, 240, 248)"] },
            height: 30,
          },
        },
      ],
      layout: {
        margin: {
          t: 30,
          l: 0,
          r: 0,
          b: 30,
        },
      },
    };
  },

  mounted() {
    let values = [];
    Object.keys(this.json).forEach((chave) => {
      let data = Object.keys(this.json[chave]).map((key) => {
        return this.json[chave][key];
      });
      values.push(data);
    });

    this.data[0].cells.values = values;
  },
};
</script>
