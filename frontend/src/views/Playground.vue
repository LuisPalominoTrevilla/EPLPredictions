<template>
    <div>
        <header class="color-wall">
            <h3>Playground</h3>
        </header>
        <b-container>
            <h4 class="mt-4">Selecciona el equipo local</h4>
            <team-selector @selected="selectLocalTeam"/>
            <h4 class="mt-4">Selecciona el equipo visitante</h4>
            <team-selector @selected="selectAwayTeam"/>
            <b-row class="mt-5">
                <b-col class="text-center" v-if="localTeam !== null">
                    <h4>Equipo local seleccionado</h4>
                    <img class="team-logo" :src="getImgUrl(localLogo)" alt="">
                    <p>{{localTeam}}</p>
                </b-col>
                <b-col class="text-center" v-if="awayTeam !== null">
                    <h4>Equipo visitante seleccionado</h4>
                    <img class="team-logo" :src="getImgUrl(awayLogo)" alt="">
                    <p>{{awayTeam}}</p>
                </b-col>
                <b-col cols="12" class="text-center">
                    <b-btn v-show="showPredictButton" class="predict">Predecir</b-btn>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import VFixture from '@/components/VFixture.vue';

import TeamSelector from '@/components/TeamSelector.vue';

export default {
    components: {
        VFixture,
        TeamSelector
    },

    data() {
        return {
            localTeam: null,
            awayTeam: null,
            localLogo: '',
            awayLogo: ''
        };
    },

    computed: {
        showPredictButton() {
            return this.localTeam !== null && this.awayTeam !== null;
        }
    },

    methods: {
        getImgUrl(pic) {
            return require('@/assets/Logos/'+pic)
        },

        selectLocalTeam({ name, logo }) {
            this.localTeam = name;
            this.localLogo = logo;
        },

        selectAwayTeam({ name, logo }) {
            this.awayTeam = name;
            this.awayLogo = logo;
        }
    }
}
</script>

<style lang="scss" scoped>
.color-wall {
    background-color: #eaff04;
    height: 7rem;
    display: flex;
    align-items: center;

    h3 {
        color: #38003c;
        font-size: 2rem;
        font-weight: bold;
        margin-left: 2rem;
    }
}

.team-logo {
    width: 4rem;
    cursor: pointer;
}

h4 {
    color: #38003c;
    font-size: 1.5rem;
    margin-bottom: 2rem;
}

.predict,
.predict:focus,
.predict:active {
    background-color: #38003c !important;
    color: #ffffff !important;
    box-shadow: none !important;
}

.predict:hover {
    background-color: #520f57b0 !important;
    color: #ffffff !important;
    border-color: #520f57b0 !important;
    box-shadow: none !important;
}
</style>
