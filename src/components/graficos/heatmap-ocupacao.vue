<template>
  <div class="grafico">
    <header>
      <h2>
        {{ title }}
      </h2>
    </header>
    <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
  </div>
</template>

<script>
import { Plotly } from "vue-plotly";
export default {
  props: {
    title: String,
    refs: String,
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
          hovertemplate: "Data: %{x}<br>UF: %{y}<br>%: %{z}<extra></extra>",
          colorscale: [
            [0, "#c77560"],
            [0.2, "#dba788"],
            [0.4, "#efdbcb"],
            [0.6, "#b3d0c7"],
            [0.8, "#6fa194"],
            [1, "#2f7264"],
            
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
        return this.refs === "uti" ? ocupation.uti_beds : ocupation.clinical_beds;
      })),
      (this.data[0].x = this.json.map((ocupation) => {
          return ocupation.date;
        }));
      this.data[0].y = this.json.map((ocupation) => {
        return ocupation.state;
      });
    },
  },
};
</script>

<style></style>
