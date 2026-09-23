<template>
  <div class="grafico">
    <header>
      <h2>
        {{ title }}
      </h2>
    </header>
    <Plotly :data="data" :layout="layout" :toImageButtonOptions="{format: 'png', scale: 3, filename:'sublineages', height: 651, width: 1546}" :display-mode-bar="true"></Plotly>
  </div>
</template>

<script>
import { Plotly } from "vue-plotly";
export default {
  props: {
    title: String,
    json: Array,
  },
  components: {
    Plotly,
  },
  data() {
    return {
      data: [
        {
          type: "heatmap",
          hoverongaps: false,
          opacity: 0.8,
          zmin: 0,
          zmax: 100,
          hovertemplate: "Sublinhagem: %{x}<br>UF: %{y}<br>%: %{z}<extra></extra>",
          colorscale: [
            [0, "#AED5A8"],
            [0.25, "#71BB76"],
            [0.50, "#11A856"],
            [0.75, "#00893B"],
            [1, "#005F2F"],
          ],
        },
      ],
      layout: {
        margin: {
          t: 0,
          l: 140,
          r: 0,
          b: 100,
        },
        height: 700,
        // yaxis: {
        //   autorange: "reversed",
        // },
      },
    };
  },

  created() {
    this.sort();
  },
  methods: {
    sort() {
      this.json = this.json.sort((a, b) => {
        let aState = a.state;
        let bState = b.state;
        return bState.localeCompare(aState);
      });

      (this.data[0].z = this.json.map((ocupation) => {
        return ocupation.copias;
      })),
        (this.data[0].x = this.json.map((ocupation) => {
          return ocupation.data;
        }));
      this.data[0].y = this.json.map((ocupation) => {
        return ocupation.state;
      });
    },
  },
};
</script>

<style></style>
