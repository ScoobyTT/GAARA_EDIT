import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// Cerrega os módulos da pasta sem precisar importar um por um.
// Uso do requireContext
const requireContext = require.context('./modulos', false, /.*\.js$/)

const modules = requireContext.keys()
  .map(arquivo =>
    [arquivo.replace(/(^.\/)|(\.js$)/g, ''), requireContext(arquivo)]
  )
  .reduce((modules, [name, module]) => {
    if (module.namespaced === undefined) {
      module.namespaced = true
    }

    return { ...modules, [name]: module }
  }, {})

export default new Vuex.Store({
  modules
})