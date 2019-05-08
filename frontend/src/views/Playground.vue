<template>
    <div>
        <header class="color-wall">
            <h3>Playground</h3>
        </header>
        <b-container>
            <h4 class="mt-4">Selecciona el equipo local</h4>
            <team-selector @selected="selectLocalTeam"/>
            <div class="separator"></div>
            <h4 class="mt-4">Selecciona el equipo visitante</h4>
            <team-selector @selected="selectAwayTeam"/>
            <div class="separator"></div>
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
                <b-col cols="12" class="text-center mb-5">
                    <b-btn @click="predictMatch" v-show="showPredictButton" class="predict">Predecir</b-btn>
                </b-col>
            </b-row>
            <v-fixture
                class="mb-4"
                v-if="prediction !== null"
                :localName="prediction.homeTeam"
                :localLogo="prediction.homeLogo"
                :awayName="prediction.awayTeam"
                :awayLogo="prediction.awayLogo"
                :winner="prediction.matchResult"/>
        </b-container>
    </div>
</template>

<script>
import VFixture from '@/components/VFixture.vue';
import axios from 'axios';

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
            awayLogo: '',
            prediction: null
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
        },

        predictMatch() {
            const sendData = {
                home: this.localTeam,
                away: this.awayTeam
            }
            if (sendData.home === 'Brighton Hove Albion') {
                sendData.home = 'Brighton & Hove Albion';
            } else if (sendData.away === 'Brighton Hove Albion') {
                sendData.away = 'Brighton & Hove Albion';
            }
            axios.post('http://localhost:4000/predictOne', sendData)
            .then(({data}) => {
                if (data.homeTeam === 'Brighton & Hove Albion') {
                    data.homeLogo = 'BrightonHoveAlbion.png';
                } else if (data.awayTeam === 'Brighton & Hove Albion') {
                    data.awayLogo = 'BrightonHoveAlbion.png';
                }
                this.prediction = data;
            }).catch(err => {
                console.log(err);
            })
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

.separator {
    height: 2px;
    background-color: #38003c73;
    width: 70%;
    margin: 0 auto;
    margin-top: 1.5rem;
}
</style>
