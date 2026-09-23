<template>
  <div>
    <l-map
      class="componente-mapa"
      v-if="tipo === 'Casos'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="CasosOptions"
    >
      <l-choropleth-layer
        :data="dadosPorDsei"
        titleKey="Dsei"
        idKey="id_int_dsei"
        :value="Casos.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="DseiGeojson"
        :colorScale="Casos.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="Casos.tituloInfo"
            placeholder="Passe o mouse sobre o DSEI para visualizar os dados"
          />
          <l-reference-chart
            :title="Casos.tituloReferencia"
            :colorScale="Casos.colorScale"
            :min="0"
            :max="props.max"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>
    <l-map
      class="componente-mapa"
      v-if="tipo === 'Obitos'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="ObitosOptions"
    >
      <l-choropleth-layer
        :data="dadosPorDsei"
        titleKey="Dsei"
        idKey="id_int_dsei"
        :value="Obitos.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="DseiGeojson"
        :colorScale="Obitos.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="Obitos.tituloInfo"
            placeholder="Passe o mouse sobre o DSEI para visualizar os dados"
          />
          <l-reference-chart
            :title="Obitos.tituloReferencia"
            :colorScale="Obitos.colorScale"
            :min="0"
            :max="props.max"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>
  </div>
</template>

<script>
import { ReferenceChart, InfoControl, ChoroplethLayer } from "vue-choropleth";
import DseiGeojson from "../../data/indigena/limite_dsei.json";
import { dadosPorDsei } from "../../data/indigena/dados-obitos-casos-por-dsei.js";
import { LMap } from "vue2-leaflet";

export default {
  name: "mapa",
  props: {
    tipo: String,
  },
  components: {
    LMap,
    "l-info-control": InfoControl,
    "l-reference-chart": ReferenceChart,
    "l-choropleth-layer": ChoroplethLayer,
  },
  data() {
    return {
      dadosPorDsei,
      DseiGeojson,
      Casos: {
        tituloInfo: "Casos de COVID-19",
        tituloReferencia: "CASOS DE COVID-19 POR DSEI",
        colorScale: ["74abe1", "468fd7", "1874CD", "135ca4", "0e457b"],
        value: {
          key: "casos",
          metric: " casos",
        },
      },
      Obitos: {
        tituloInfo: "Óbitos de COVID-19",
        tituloReferencia: "ÓBITOS DE COVID-19 POR DSEI",
        colorScale: ["ffaf85", "ff955c", "FF7B34", "cc6229", "99491f"],
        value: {
          key: "obitos",
          metric: " obitos",
        },
      },
      CasosOptions: {
        name: "CasosMap",
        attributionControl: false,
        inertia: true,
        doubleClickZoom: false,
        closePopupOnClick: false,
        dragging: false,
        zoomSnap: false,
        zoomDelta: false,
        trackResize: false,
        touchZoom: false,
        scrollWheelZoom: false,
        zoomControl: false,
      },
      ObitosOptions: {
        name: "ObitosMap",
        attributionControl: false,
        inertia: true,
        doubleClickZoom: false,
        closePopupOnClick: false,
        dragging: false,
        zoomSnap: false,
        zoomDelta: false,
        trackResize: false,
        touchZoom: false,
        scrollWheelZoom: false,
        zoomControl: false,
      },
      currentStrokeColor: "ddd",
      zoom: screen.width <= 760 ? 3.5 : 4.5,
    };
  },
  methods: {},
};
</script>

<style>
@import "../../../node_modules/leaflet/dist/leaflet.css";
.leaflet-container {
  background: #fff;
}
.leaflet-bottom {
  bottom: 30%;
  left: 10%;
}
.leaflet-top.leaflet-right {
  right: 32px;
}
.leaflet-top .info .gradient {
  width: 100%;
}
.leaflet-top .info {
  box-shadow: none;
}
.leaflet-bottom .info {
  box-shadow: none;
  background: transparent;
  position: absolute;
  left: 0;
  bottom: 0;
  width: 500px;
  right: 0;
  text-align: left;
  max-width: 300px;
  min-height: 80px;
}

.leaflet-bottom .info h4 {
  margin: 0 0 16px;
  color: #777;
  font-size: 1.8rem;
  text-transform: uppercase;
}
.leaflet-bottom .info b {
  font-size: 1.01rem;
}

.leaflet-top .info .gradient .domain-min,
.leaflet-top .info .gradient .domain-med,
.leaflet-top .info .gradient .domain-max {
  font-size: 16px;
  bottom: -4px;
  font-weight: bold;
}
</style>
