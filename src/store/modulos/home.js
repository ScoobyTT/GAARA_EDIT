import request from "../../api/home";

// Mock data
import cards from "../../data//home/cards.json";
import dadosPorEstado from "../../data/home/dados-por-estado";

export const state = {
    cards: cards,
    dadosPorEstado: dadosPorEstado
}

// getters
export const getters = {
    getCards: state => state.cards,
    getStates: state => state.dadosPorEstado
}

// mutations
export const mutations = {

    //TODO Separar o nome das actions pra evitar problemas futuros
    ["CARREGA_CARDS"](state, { cards }) {
        state.cards = cards
    },

    //TODO Separar o nome das actions pra evitar problemas futuros
    ["CARREGA_STATES"](state, { dadosPorEstado }) {
        state.dadosPorEstado = dadosPorEstado
    }
}

// actions
export const actions = {

    async loadCards({ commit }, { parametros }) {

        const { data } = await request.getCards(parametros)
        commit("CARREGA_CARDS", { cards: data })
    },

    async loadStates({ commit }, { parametros }) {

        const { data } = await request.getCards(parametros)
        commit("CARREGA_STATES", { dadosPorEstado: data })
    }
}