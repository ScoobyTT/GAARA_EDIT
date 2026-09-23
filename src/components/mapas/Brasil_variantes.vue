<template>
  <div>
    <l-map
      class="componente-mapa"
      v-if="tipo === 'Alpha'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="AlphaOptions"
    >
      <l-choropleth-layer
        :data="dadosPorEstado"
        titleKey="nome_var_estado"
        idKey="id_int_estado"
        :value="Alpha.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="brasilGeojson"
        :colorScale="Alpha.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="Alpha.tituloInfo"
            placeholder="Passe o mouse sobre a UF para visualizar os dados"
          />
          <l-reference-chart
            :title="Alpha.tituloReferencia"
            :colorScale="Alpha.colorScale"
            :min="props.min"
            :max="props.max"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>

   <l-map
      class="componente-mapa"
      v-if="tipo === 'Beta'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="BetaOptions"
    >
      <l-choropleth-layer
        :data="dadosPorEstado"
        titleKey="nome_var_estado"
        idKey="id_int_estado"
        :value="Beta.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="brasilGeojson"
        :colorScale="Beta.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="Beta.tituloInfo"
            placeholder="Passe o mouse sobre a UF para visualizar os dados"
          />
          <l-reference-chart
            :title="Beta.tituloReferencia"
            :colorScale="Beta.colorScale"
            :min="props.min"
            :max="props.max"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>
    
	<l-map
      class="componente-mapa"
      v-if="tipo === 'Gamma'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="GammaOptions"
    >
      <l-choropleth-layer
        :data="dadosPorEstado"
        titleKey="nome_var_estado"
        idKey="id_int_estado"
        :value="Gamma.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="brasilGeojson"
        :colorScale="Gamma.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="Gamma.tituloInfo"
            placeholder="Passe o mouse sobre a UF para visualizar os dados"
          />
          <l-reference-chart
            :title="Gamma.tituloReferencia"
            :colorScale="Gamma.colorScale"
            :min="props.min"
            :max="props.max"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>
    
    <l-map
      class="componente-mapa"
      v-if="tipo === 'Delta'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="DeltaOptions"
    >
      <l-choropleth-layer
        :data="dadosPorEstado"
        titleKey="nome_var_estado"
        idKey="id_int_estado"
        :value="Delta.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="brasilGeojson"
        :colorScale="Delta.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="Delta.tituloInfo"
            placeholder="Passe o mouse sobre a UF para visualizar os dados"
          />
          <l-reference-chart
            :title="Delta.tituloReferencia"
            :colorScale="Delta.colorScale"
            :min="props.min"
            :max="props.max"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>

   <l-map
      class="componente-mapa"
      v-if="tipo === 'Omicron'"
      :center="[-15.007034, -54.02578]"
      :zoom="zoom"
      style="height: 750px;"
      :options="OmicronOptions"
    >
      <l-choropleth-layer
        :data="dadosPorEstado"
        titleKey="nome_var_estado"
        idKey="id_int_estado"
        :value="Omicron.value"
        geojsonIdKey="GEOCODIGO"
        :geojson="brasilGeojson"
        :colorScale="Omicron.colorScale"
        :strokeWidth="1"
        :currentStrokeWidth="2"
        strokeColor="ccc"
        currentStrokeColor="333"
      >
        <template slot-scope="props">
          <l-info-control
            :item="props.currentItem"
            :unit="props.unit"
            :title="Omicron.tituloInfo"
            placeholder="Passe o mouse sobre a UF para visualizar os dados"
          />
          <l-reference-chart
            :title="Omicron.tituloReferencia"
            :colorScale="Omicron.colorScale"
            :min="props.min"
            :max="props.max"
            position="topright"
          />
        </template>
      </l-choropleth-layer>
    </l-map>

  </div>
</template>

<script>
import { InfoControl, ReferenceChart, ChoroplethLayer } from "vue-choropleth";
import brasilGeojson from "../../data/brasil_estados.json";
import { dadosPorEstado } from "../../data/variantes/dados-por-estado-variantes";
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
      dadosPorEstado,
      brasilGeojson,
      Alpha: {
        tituloInfo: "Copias de Alpha",
        tituloReferencia: "COPIAS DE ALPHA POR ESTADO",
        colorScale: ["FCF5EB", "EDC68B", "E5AB53", "DE9527", "B87A1C"],
        value: {
          key: "quantidade_int_alpha",
          metric: " casos",
        },
      },
      Beta: {
        tituloInfo: "Copias de Beta",
        tituloReferencia: "COPIAS DE BETA POR ESTADO",
        colorScale: ["9CC9E5", "51A0D1", "3288BD", "2D7CAC", "194560"],
        value: {
          key: "quantidade_int_beta",
          metric: " casos",
        },
      },
      Gamma: {
        tituloInfo: "Copias de Gamma",
        tituloReferencia: "COPIAS DE GAMMA POR ESTADO",
        colorScale: ["DFC5DF", "B475B3", "9F579E", "874A86", "693968"],
        value: {
          key: "quantidade_int_gamma",
          metric: " casos",
        },
      },
      Delta: {
        tituloInfo: "Copias de Delta",
        tituloReferencia: "COPIAS DE DELTA POR ESTADO",
        colorScale: ["C4D780", "9BB639", "7A8F2D","788D2C", "576620"],
        value: {
          key: "quantidade_int_delta",
          metric: " casos",
        },
      },
      Omicron: {
        tituloInfo: "Copias de Omicron",
        tituloReferencia: "COPIAS DE OMICRON POR ESTADO",
        colorScale: ["DFE4F0", "4D6AA9", "3D5486", "3C5384", "2C3D61"],
        value: {
          key: "quantidade_int_omicron",
          metric: " casos",
        },
      },
      AlphaOptions: {
        name: "AlphaMap",
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
      BetaOptions: {
        name: "BetaMap",
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
      GammaOptions: {
        name: "GammaMap",
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
      DeltaOptions: {
        name: "DeltaMap",
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
      OmicronOptions: {
        name: "OmicronMap",
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
  left: -50px;
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
  font-size: 1.6rem;
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
